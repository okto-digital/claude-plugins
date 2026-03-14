#!/usr/bin/env bash
# compile-answers.sh — Merge curated answers back into D4-Answers.json.
#
# Usage:
#   compile-answers.sh <project-dir>
#   compile-answers.sh /path/to/project
#   compile-answers.sh /path/to/project -v   # verbose
#
# Reads curated output files and populates D4-Answers.json:
#   1. DEDUCED entries (D4-Deductions.json) → auto-populated via answer_for_d4
#   2. CLIENT answers (D4-Questions-Client.json) → mapped via original_ids
#   3. AGENCY answers (D4-Questions-Agency.json) → mapped via original_ids
#
# Each curated file maps back to original question IDs via the original_ids field.
# Only entries with non-null selected/answer values are written.
#
# Output: D4-Answers.json compatible with resolve-answers.sh
#
# Requirements: jq
#
# Error handling:
#   - Skips missing curated files with warning
#   - Exit 1 if D4-Answers.json template is missing
#   - Exit 1 if jq is not available

set -euo pipefail

verbose=false
project_dir=""

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
            if [[ -z "$project_dir" ]]; then
                project_dir="$1"
            else
                echo "Error: Too many arguments." >&2; exit 1
            fi
            shift
            ;;
    esac
done

if [[ -z "$project_dir" ]]; then
    echo "Error: Required argument: <project-dir>" >&2
    echo "Usage: compile-answers.sh /path/to/project" >&2
    exit 1
fi

if ! command -v jq &>/dev/null; then
    echo "Error: jq is required but not found." >&2
    exit 1
fi

answers_file="$project_dir/D4-Answers.json"
deductions_file="$project_dir/D4-Deductions.json"
client_file="$project_dir/D4-Questions-Client.json"
agency_file="$project_dir/D4-Questions-Agency.json"

if [[ ! -f "$answers_file" ]]; then
    echo "Error: D4-Answers.json not found at $answers_file" >&2
    exit 1
fi

if ! jq empty "$answers_file" 2>/dev/null; then
    echo "Error: Invalid JSON in $answers_file" >&2
    exit 1
fi

tmpfile="${answers_file}.tmp"
cp "$answers_file" "$tmpfile"

total_populated=0

# --- 1. Deductions: auto-populate from answer_for_d4 ---
if [[ -f "$deductions_file" ]]; then
    if jq empty "$deductions_file" 2>/dev/null; then
        deduction_count=$(jq 'length' "$deductions_file")
        $verbose && echo "Processing $deduction_count deductions..." >&2

        # For each deduction, find its original question ID and set the answer
        for i in $(seq 0 $((deduction_count - 1))); do
            qid=$(jq -r ".[$i].id" "$deductions_file")
            answer=$(jq -r ".[$i].answer_for_d4" "$deductions_file")

            if [[ -n "$answer" && "$answer" != "null" ]]; then
                jq -c --arg qid "$qid" --arg ans "$answer" \
                    '[.[] | if .id == $qid then .answer = $ans else . end]' \
                    "$tmpfile" > "${tmpfile}.new" && mv "${tmpfile}.new" "$tmpfile"
                total_populated=$((total_populated + 1))
                $verbose && echo "  [DEDUCED] $qid" >&2
            fi
        done
    else
        echo "Warning: Invalid JSON in $deductions_file, skipping deductions." >&2
    fi
else
    $verbose && echo "No D4-Deductions.json found, skipping deductions." >&2
fi

# --- 2. Client answers: map via original_ids ---
if [[ -f "$client_file" ]]; then
    if jq empty "$client_file" 2>/dev/null; then
        # Only process entries with a non-null selected value
        answered_count=$(jq '[.[] | select(.selected != null and .selected != "")] | length' "$client_file")
        $verbose && echo "Processing $answered_count client answers..." >&2

        for i in $(seq 0 $(($(jq 'length' "$client_file") - 1))); do
            selected=$(jq -r ".[$i].selected // empty" "$client_file")
            [[ -z "$selected" ]] && continue

            # Get the answer text: freetext_response if "other", otherwise the selected option label
            if [[ "$selected" == "other" ]]; then
                answer=$(jq -r ".[$i].freetext_response // empty" "$client_file")
                [[ -z "$answer" ]] && continue
            elif [[ "$selected" == "na" ]]; then
                answer="N/A"
            else
                answer=$(jq -r --argjson idx "$i" --arg sel "$selected" '.[$idx].options[] | select(.id == $sel) | .label // empty' "$client_file" 2>/dev/null)
                [[ -z "$answer" ]] && continue
            fi

            # Map to all original question IDs
            original_ids=$(jq -r ".[$i].original_ids[]" "$client_file")
            for qid in $original_ids; do
                jq -c --arg qid "$qid" --arg ans "$answer" \
                    '[.[] | if .id == $qid then .answer = $ans else . end]' \
                    "$tmpfile" > "${tmpfile}.new" && mv "${tmpfile}.new" "$tmpfile"
                total_populated=$((total_populated + 1))
                $verbose && echo "  [CLIENT] $qid = $answer" >&2
            done
        done
    else
        echo "Warning: Invalid JSON in $client_file, skipping client answers." >&2
    fi
else
    $verbose && echo "No D4-Questions-Client.json found, skipping client answers." >&2
fi

# --- 3. Agency answers: map via original_ids ---
if [[ -f "$agency_file" ]]; then
    if jq empty "$agency_file" 2>/dev/null; then
        answered_count=$(jq '[.[] | select(.selected != null and .selected != "")] | length' "$agency_file")
        $verbose && echo "Processing $answered_count agency answers..." >&2

        for i in $(seq 0 $(($(jq 'length' "$agency_file") - 1))); do
            selected=$(jq -r ".[$i].selected // empty" "$agency_file")
            [[ -z "$selected" ]] && continue

            # For agency: use recommendation if selected matches, or option label
            if [[ "$selected" == "other" ]]; then
                answer=$(jq -r ".[$i].freetext_response // empty" "$agency_file" 2>/dev/null)
                [[ -z "$answer" ]] && answer=$(jq -r ".[$i].recommendation // empty" "$agency_file")
                [[ -z "$answer" ]] && continue
            else
                answer=$(jq -r --argjson idx "$i" --arg sel "$selected" '.[$idx].options[] | select(.id == $sel) | .label // empty' "$agency_file" 2>/dev/null)
                [[ -z "$answer" ]] && continue
            fi

            original_ids=$(jq -r ".[$i].original_ids[]" "$agency_file")
            for qid in $original_ids; do
                jq -c --arg qid "$qid" --arg ans "$answer" \
                    '[.[] | if .id == $qid then .answer = $ans else . end]' \
                    "$tmpfile" > "${tmpfile}.new" && mv "${tmpfile}.new" "$tmpfile"
                total_populated=$((total_populated + 1))
                $verbose && echo "  [AGENCY] $qid = $answer" >&2
            done
        done
    else
        echo "Warning: Invalid JSON in $agency_file, skipping agency answers." >&2
    fi
else
    $verbose && echo "No D4-Questions-Agency.json found, skipping agency answers." >&2
fi

# --- Write final output ---
jq -c '.' "$tmpfile" > "$answers_file"
rm -f "$tmpfile"

# --- Verification: count coverage ---
total_questions=$(jq 'length' "$answers_file")
total_answered=$(jq '[.[] | select(.answer != null)] | length' "$answers_file")
total_unanswered=$((total_questions - total_answered))

echo "$total_populated answers compiled into D4-Answers.json ($total_answered/$total_questions answered, $total_unanswered remaining)"
