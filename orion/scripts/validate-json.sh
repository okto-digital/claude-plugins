#!/usr/bin/env bash
# validate-json.sh — Validate JSON files using jq.
#
# Usage:
#   validate-json.sh <file> [<file>...]
#   validate-json.sh gap-analysis/G*-*.json
#   validate-json.sh -v D4-Gap-Analysis.json   # verbose
#
# Validates each file with jq. Reports pass/fail per file.
# On failure, shows the jq error message for diagnosis.
#
# Exit codes:
#   0 — all files valid JSON
#   1 — one or more files invalid
#   2 — no files to validate or missing jq
#
# Requirements: jq

set -euo pipefail

verbose=false
files=()

usage() {
    sed -n '2,/^$/{ s/^# \?//; p }' "$0"
    exit 0
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        -v) verbose=true; shift ;;
        -h|--help) usage ;;
        -*) echo "Unknown option: $1" >&2; exit 2 ;;
        *) files+=("$1"); shift ;;
    esac
done

if ! command -v jq &>/dev/null; then
    echo "Error: jq is required but not found." >&2
    exit 2
fi

if [[ ${#files[@]} -eq 0 ]]; then
    echo "Error: No files specified." >&2
    echo "Usage: validate-json.sh <file> [<file>...]" >&2
    exit 2
fi

passed=0
failed=0
failed_files=()

for file in "${files[@]}"; do
    if [[ ! -f "$file" ]]; then
        echo "SKIP $file (not found)" >&2
        continue
    fi

    # Check file is not empty
    if [[ ! -s "$file" ]]; then
        echo "FAIL $file (empty file)"
        failed=$((failed + 1))
        failed_files+=("$file")
        continue
    fi

    # Validate with jq, capture stderr for error details
    error_output=$(jq empty "$file" 2>&1)
    if [[ $? -eq 0 ]]; then
        $verbose && echo "PASS $file"
        passed=$((passed + 1))
    else
        echo "FAIL $file"
        # Show the jq error indented for readability
        echo "$error_output" | sed 's/^/     /'
        failed=$((failed + 1))
        failed_files+=("$file")
    fi
done

total=$((passed + failed))

if [[ $total -eq 0 ]]; then
    echo "No files found to validate." >&2
    exit 2
fi

# Summary
if [[ $failed -eq 0 ]]; then
    echo "$passed/$total JSON files valid"
    exit 0
else
    echo "$passed/$total valid, $failed/$total FAILED: ${failed_files[*]}"
    exit 1
fi
