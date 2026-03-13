#!/usr/bin/env bash
# resolve-answers.sh — Insert client answers from D4-Answers.json into G-files.
#
# Usage:
#   resolve-answers.sh <answers.json> <gap-directory>
#   resolve-answers.sh D4-Answers.json gap-analysis/
#   resolve-answers.sh D4-Answers.json gap-analysis/ -v   # verbose
#
# For each answered entry (answer != null):
#   - "N/A"  → finding status: "N/A", reason: "Not applicable (client)"
#   - "text" → finding status: "FOUND", evidence: "Client: <text>"
#   - null   → skipped (unanswered)
#
# After updating findings, recalculates counts for each modified G-file.
#
# Requirements: jq
#
# Error handling:
#   - Skips entries with null answers
#   - Skips domains with no matching G-file (warns to stderr)
#   - Exit 1 if no valid input or no answers to process

set -euo pipefail

verbose=false
answers_file=""
gap_dir=""

usage() {
    sed -n '2,/^$/{ s/^# \?//; p }' "$0"
    exit 0
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        -v) verbose=true; shift ;;
        -h|--help) usage ;;
        -*) echo "Unknown option: $1" >&2; exit 1 ;;
        *)
            if [[ -z "$answers_file" ]]; then
                answers_file="$1"
            elif [[ -z "$gap_dir" ]]; then
                gap_dir="$1"
            else
                echo "Error: Too many arguments." >&2; exit 1
            fi
            shift
            ;;
    esac
done

if [[ -z "$answers_file" || -z "$gap_dir" ]]; then
    echo "Error: Required arguments: <answers.json> <gap-directory>" >&2
    echo "Usage: resolve-answers.sh D4-Answers.json gap-analysis/" >&2
    exit 1
fi

if [[ ! -f "$answers_file" ]]; then
    echo "Error: Answers file not found: $answers_file" >&2
    exit 1
fi

if [[ ! -d "$gap_dir" ]]; then
    echo "Error: Gap directory not found: $gap_dir" >&2
    exit 1
fi

if ! command -v jq &>/dev/null; then
    echo "Error: jq is required but not found." >&2
    exit 1
fi

# Validate JSON
if ! jq empty "$answers_file" 2>/dev/null; then
    echo "Error: Invalid JSON in $answers_file" >&2
    exit 1
fi

# Count answered entries (non-null)
answered_count=$(jq '[.[] | select(.answer != null)] | length' "$answers_file")

if [[ "$answered_count" -eq 0 ]]; then
    echo "No answered entries found (all answers are null). Nothing to do." >&2
    exit 0
fi

$verbose && echo "Processing $answered_count answered entries..." >&2

# Get unique domains that have answers
domains=$(jq -r '[.[] | select(.answer != null) | .domain] | unique | .[]' "$answers_file")

domains_updated=0
findings_resolved=0

for domain in $domains; do
    # Find the matching G-file by domain field inside JSON
    gfile=""
    for candidate in "$gap_dir"/G*-*.json; do
        [[ ! -f "$candidate" ]] && continue
        # Skip question files
        [[ "$candidate" == *-questions.json ]] && continue
        file_domain=$(jq -r '.domain // empty' "$candidate" 2>/dev/null)
        if [[ "$file_domain" == "$domain" ]]; then
            gfile="$candidate"
            break
        fi
    done

    if [[ -z "$gfile" ]]; then
        echo "Warning: No G-file found for domain '$domain', skipping." >&2
        continue
    fi

    $verbose && echo "  Updating: $gfile (domain: $domain)" >&2

    # Extract answers for this domain
    domain_answers=$(jq --arg d "$domain" '[.[] | select(.domain == $d and .answer != null)]' "$answers_file")
    domain_answer_count=$(echo "$domain_answers" | jq 'length')

    # Apply each answer to the G-file
    tmpfile="${gfile}.tmp"
    cp "$gfile" "$tmpfile"

    for i in $(seq 0 $((domain_answer_count - 1))); do
        checkpoint=$(echo "$domain_answers" | jq -r ".[$i].checkpoint")
        answer=$(echo "$domain_answers" | jq -r ".[$i].answer")

        if [[ "$answer" == "N/A" ]]; then
            # Set status to N/A, add reason
            jq -c --arg cp "$checkpoint" \
                '.findings = [.findings[] | if .checkpoint == $cp then .status = "N/A" | .reason = "Not applicable (client)" | .evidence = null else . end]' \
                "$tmpfile" > "${tmpfile}.new" && mv "${tmpfile}.new" "$tmpfile"
        else
            # Set status to FOUND, add evidence
            jq -c --arg cp "$checkpoint" --arg ev "Client: $answer" \
                '.findings = [.findings[] | if .checkpoint == $cp then .status = "FOUND" | .evidence = $ev | .reason = null else . end]' \
                "$tmpfile" > "${tmpfile}.new" && mv "${tmpfile}.new" "$tmpfile"
        fi

        findings_resolved=$((findings_resolved + 1))
        if $verbose; then
            if [[ "$answer" == "N/A" ]]; then
                echo "    [N/A] $checkpoint" >&2
            else
                echo "    [FOUND] $checkpoint" >&2
            fi
        fi
    done

    # Recalculate counts
    jq -c --argjson resolved "$domain_answer_count" '
        .counts.found = ([.findings[] | select(.status == "FOUND")] | length) |
        .counts.partial = ([.findings[] | select(.status == "PARTIAL")] | length) |
        .counts.gap = ([.findings[] | select(.status == "GAP")] | length) |
        .counts.na = ([.findings[] | select(.status == "N/A")] | length) |
        .counts.critical_resolved = ([.findings[] | select(.status == "FOUND" and .priority == "CRITICAL")] | length) |
        .counts.questions_resolved = ((.counts.questions_resolved // 0) + $resolved)
    ' "$tmpfile" > "${tmpfile}.new" && mv "${tmpfile}.new" "$tmpfile"

    # Overwrite original (minified)
    jq -c '.' "$tmpfile" > "$gfile"
    rm -f "$tmpfile"

    domains_updated=$((domains_updated + 1))
    $verbose && echo "    $domain_answer_count findings resolved in $gfile" >&2
done

echo "$domains_updated domains updated, $findings_resolved findings resolved"
