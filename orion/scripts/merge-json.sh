#!/usr/bin/env bash
# merge-json.sh — Merge multiple JSON files into a single keyed object.
#
# Usage:
#   merge-json.sh <file1.json> [file2.json ...] [-o output.json]
#   merge-json.sh research/*.json brief/*.json -o context.json
#   merge-json.sh *.json                          # prints to stdout
#
# Each file's content is wrapped under a key derived from the filename:
#   D1-Init.json        → "D1-Init"
#   R2-SERP.json        → "R2-SERP"
#   D2-Client-Intelligence.json → "D2-Client-Intelligence"
#
# Output:
#   {
#     "D1-Init": { ... },
#     "R1-SERP": { ... }
#   }
#
# Options:
#   -o FILE   Write output to FILE instead of stdout
#   -p        Pretty-print output (default: minified)
#   -v        Verbose: print files being merged to stderr
#   -h        Show this help
#
# Requirements: jq
#
# Error handling:
#   - Strips UTF-8 BOM if present
#   - Skips files that fail JSON parsing (warns to stderr)
#   - Exit 1 if no valid JSON files found

set -euo pipefail

output=""
pretty=false
verbose=false
files=()

usage() {
    sed -n '2,/^$/{ s/^# \?//; p }' "$0"
    exit 0
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        -o) output="$2"; shift 2 ;;
        -p) pretty=true; shift ;;
        -v) verbose=true; shift ;;
        -h|--help) usage ;;
        -*) echo "Unknown option: $1" >&2; exit 1 ;;
        *) files+=("$1"); shift ;;
    esac
done

if [[ ${#files[@]} -eq 0 ]]; then
    echo "Error: No input files specified." >&2
    echo "Usage: merge-json.sh <file1.json> [file2.json ...] [-o output.json]" >&2
    exit 1
fi

if ! command -v jq &>/dev/null; then
    echo "Error: jq is required but not found." >&2
    exit 1
fi

# Build merged object incrementally
merged="{}"
valid_count=0

for file in "${files[@]}"; do
    if [[ ! -f "$file" ]]; then
        echo "Warning: File not found, skipping: $file" >&2
        continue
    fi

    # Derive key from filename (strip path and .json extension)
    key=$(basename "$file" .json)

    # Read file, strip BOM if present
    content=$(sed '1s/^\xEF\xBB\xBF//' "$file")

    # Validate JSON
    if ! echo "$content" | jq empty 2>/dev/null; then
        echo "Warning: Invalid JSON, skipping: $file" >&2
        continue
    fi

    # Merge into result object
    merged=$(echo "$merged" | jq --arg key "$key" --argjson val "$content" '. + {($key): $val}')
    valid_count=$((valid_count + 1))

    if $verbose; then
        echo "  Merged: $file → \"$key\"" >&2
    fi
done

if [[ $valid_count -eq 0 ]]; then
    echo "Error: No valid JSON files found." >&2
    exit 1
fi

# Format output
if $pretty; then
    result=$(echo "$merged" | jq '.')
else
    result=$(echo "$merged" | jq -c '.')
fi

# Write output
if [[ -n "$output" ]]; then
    echo "$result" > "$output"
    if $verbose; then
        echo "  Output: $output ($valid_count files merged)" >&2
    fi
else
    echo "$result"
fi
