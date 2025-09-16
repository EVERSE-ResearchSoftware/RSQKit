#!/usr/bin/env python3
import re
import argparse

def format_sentences(text: str) -> str:
    """
    Format text so each sentence appears on its own line, while preserving:
    - Front matter headers (YAML/front matter at the top of files),
    - Code blocks surrounded by triple backticks ``` ... ``` ,
    - Paragraph breaks (empty lines),
    - Leading tab characters at the start of lines,
    - List items starting with '*' or '-' optionally preceded by spaces or tabs,
    - Markdown inline named links starting with [name]:.

    Functionality:
    - Joins lines that are part of the same sentence outside preserved regions.
    - Splits text into sentences based on sentence-ending punctuation (., !, ?).
    - Lines inside code blocks, top matter, list items, or Markdown links are left untouched.
    - Leading tabs/spaces for indentation are preserved.
    """
    lines = text.splitlines()
    output_lines = []
    buffer = []
    buffer_indent = ""
    i = 0
    n = len(lines)

    # Check for top matter at the very beginning
    if n > 0 and lines[0].strip() == "---":
        output_lines.append(lines[0])
        i = 1
        while i < n:
            output_lines.append(lines[i])
            if lines[i].strip() == "---":
                i += 1
                break
            i += 1

    in_code_block = False

    while i < n:
        line = lines[i]
        leading_whitespace = re.match(r"^[ \t]*", line).group(0)
        stripped = line.strip()

        # Toggle code block flag
        if stripped.startswith("```"):
            if buffer:
                output_lines.append(buffer_indent + " ".join(buffer).strip())
                buffer = []
                buffer_indent = ""
            output_lines.append(line)
            in_code_block = not in_code_block
            i += 1
            continue

        # Inside code block: preserve as-is
        if in_code_block:
            output_lines.append(line)
            i += 1
            continue

        # Preserve empty lines
        if not stripped:
            if buffer:
                output_lines.append(buffer_indent + " ".join(buffer).strip())
                buffer = []
                buffer_indent = ""
            output_lines.append("")
            i += 1
            continue

        # Preserve list items starting with * or -
        if re.match(r"^[ \t]*[\*\-]\s+", line):
            if buffer:
                output_lines.append(buffer_indent + " ".join(buffer).strip())
                buffer = []
                buffer_indent = ""
            output_lines.append(line)
            i += 1
            continue

        # Preserve Markdown inline named links [name]:
        if re.match(r"^[ \t]*\[[^\]]+\]:", line):
            if buffer:
                output_lines.append(buffer_indent + " ".join(buffer).strip())
                buffer = []
                buffer_indent = ""
            output_lines.append(line)
            i += 1
            continue

        # If buffer is empty, store leading whitespace
        if not buffer:
            buffer_indent = leading_whitespace

        # Accumulate lines for sentence joining
        buffer.append(stripped)

        # Flush when line ends with sentence terminator
        if re.search(r"[.!?]['\"]?$", stripped):
            output_lines.append(buffer_indent + " ".join(buffer).strip())
            buffer = []
            buffer_indent = ""

        i += 1

    # Flush any remaining buffer
    if buffer:
        output_lines.append(buffer_indent + " ".join(buffer).strip())

    return "\n".join(output_lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Format text so each sentence is on a single line.")
    parser.add_argument("input_file", help="Input text file")
    parser.add_argument("-o", "--output_file", help="Output file (default: stdout)")
    args = parser.parse_args()

    with open(args.input_file, "r", encoding="utf-8") as f:
        text = f.read()

    formatted = format_sentences(text)

    if args.output_file:
        with open(args.output_file, "w", encoding="utf-8") as f:
            f.write(formatted)
    else:
        print(formatted)
