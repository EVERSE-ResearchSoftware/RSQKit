#!/usr/bin/env bash
set -euo pipefail

# A Bash script that:
# - Takes one or more files as arguments.
# - Calls the Python script (format_sentences.py) on each.
# - Replaces the original file with the reformatted version (via a temporary file).
# - Leaves the file untouched if the Python script fails.

# Make the script executable: chmod +x reformat_files.sh
# Run it: ./reformat_files.sh file1.txt file2.txt file3.md
# Or run it on all .md files in a directory: ./reformat_files.sh ../../pages/*.md
# Each file will be replaced in place with the cleaned version.

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