#!/usr/bin/env bash
set -euo pipefail

# Path to the Python script (adjust if needed)
PYTHON_SCRIPT="./format_sentences.py"

if [ $# -eq 0 ]; then
    echo "Usage: $0 file1 [file2 ...]"
    exit 1
fi

for file in "$@"; do
    if [ ! -f "$file" ]; then
        echo "Skipping: $file (not a file)"
        continue
    fi

    echo "Formatting: $file"
    tmpfile="$(mktemp)"

    if python3 "$PYTHON_SCRIPT" "$file" -o "$tmpfile"; then
        mv "$tmpfile" "$file"
    else
        echo "Error processing $file — leaving original unchanged."
        rm -f "$tmpfile"
    fi
done