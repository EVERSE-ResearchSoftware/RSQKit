#!/usr/bin/env python3
"""
Markdown Sentence Formatter

This script formats Markdown files with the following rules and behaviors:

1. Paragraphs:
   - Each sentence is placed on its own line.
   - Leading indentation and blank lines are preserved.

2. List items:
   - Single-sentence list items (even if wrapped across multiple lines) are collapsed into a single line:
        - Example:
            - This is a wrapped single sentence.
   - Multi-sentence list items are split so each sentence appears on its own line:
        - Only the first line keeps the bullet/number.
        - Subsequent lines have no indentation.
        - Example:
            - First sentence.
            Second sentence.
            Third sentence.

3. Reference-style links ([name]: ...):
   - Preserved exactly as-is.

4. Markdown headers (# ...):
   - Preserved exactly as-is.

5. Markdown pipe tables (GFM):
   - Entire table blocks, including header and divider row, are preserved intact.

6. Code blocks (``` ... ```):
   - Fenced code blocks are preserved entirely, including all inner lines.

7. Liquid blocks ({% ... %} ... {% end... %}):
   - Multi-line Liquid blocks are preserved entirely.
   - Inline Liquid tags (e.g., {{ ... }}) are preserved within sentences.

8. Blank lines and indentation:
   - Blank lines are preserved exactly.
   - Paragraph indentation is preserved.
   - Multi-sentence list items remove indentation after the first sentence.

9. Sentence splitting:
   - Common abbreviations (e.g., e.g., Mr., Dr., etc.) are protected to avoid incorrect splits.
   - Each sentence ends at ., !, or ?, optionally followed by quotes, parentheses, or brackets.
"""

import re
import argparse
import sys
import tempfile
import os
import shutil

# Abbreviations to protect while splitting sentences
ABBREVIATIONS = [
    "e.g.", "i.e.", "etc.", "vs.", "Mr.", "Mrs.", "Ms.", "Dr.", "Prof.",
    "Sr.", "Jr.", "St.", "Inc.", "Ltd.", "et al.", "al.", "cf.", "Fig.", "fig.",
    "Jan.", "Feb.", "Mar.", "Apr.", "May.", "Jun.", "Jul.", "Aug.", "Sep.", "Sept.",
    "Oct.", "Nov.", "Dec."
]
_PLACEHOLDER = "<<DOT>>"

def _protect_abbreviations(text: str) -> str:
    for abbr in ABBREVIATIONS:
        text = text.replace(abbr, abbr.replace(".", _PLACEHOLDER))
    return text

def _restore_placeholders(text: str) -> str:
    return text.replace(_PLACEHOLDER, ".")

def split_sentences(text: str) -> list[str]:
    """Split a paragraph into sentences, protecting abbreviations."""
    protected = _protect_abbreviations(text)
    # Non-greedy split at punctuation
    pattern = re.compile(r'.*?[.!?]["\')\]]*(?=\s|$)', re.S)
    matches = pattern.findall(protected)
    sentences = [_restore_placeholders(m.strip()) for m in matches if m.strip()]
    return sentences

def format_markdown(text: str) -> str:
    lines = text.splitlines()
    out = []
    i = 0
    n = len(lines)

    # Regex patterns
    list_item_re = re.compile(r"^[ \t]*(?:[-*]|\d+\.)\s+")
    ref_link_re = re.compile(r"^[ \t]*\[[^\]]+\]:")
    header_re = re.compile(r"^[ \t]*#+\s")
    code_fence_re = re.compile(r"^[ \t]*```")
    table_divider_re = re.compile(r'^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$')
    liquid_start_re = re.compile(r'^[ \t]*{%-?\s*(for|if|case|unless|raw|capture|comment|tablerow|paginate|schema|section)\b.*-?%}', re.I)
    liquid_end_re = re.compile(r'^[ \t]*{%-?\s*end(for|if|case|unless|raw|capture|comment|tablerow|paginate|schema|section)\b.*-?%}', re.I)
    liquid_single_re = re.compile(r'^[ \t]*{%-?.*?-?%}[ \t]*$')

    in_code = False
    in_liquid = False
    buffer = ""
    buffer_indent = ""

    def flush_buffer():
        nonlocal buffer, buffer_indent, out
        if not buffer:
            return
        sentences = split_sentences(buffer)
        for idx, s in enumerate(sentences):
            if buffer_indent and idx == 0:
                out.append(buffer_indent + s)
            else:
                out.append(s)
        buffer = ""
        buffer_indent = ""

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # YAML front matter
        if i == 0 and stripped == "---":
            out.append(line)
            i += 1
            while i < n:
                out.append(lines[i])
                if lines[i].strip() == "---":
                    i += 1
                    break
                i += 1
            continue

        # Code fences
        if code_fence_re.match(line):
            flush_buffer()
            out.append(line)
            in_code = not in_code
            i += 1
            continue
        if in_code:
            out.append(line)
            i += 1
            continue

        # Liquid blocks
        if in_liquid:
            out.append(line)
            if liquid_end_re.match(line):
                in_liquid = False
            i += 1
            continue
        if liquid_start_re.match(line):
            flush_buffer()
            out.append(line)
            in_liquid = True
            i += 1
            continue
        if liquid_single_re.match(line):
            flush_buffer()
            out.append(line)
            i += 1
            continue

        # Blank lines
        if stripped == "":
            flush_buffer()
            out.append("")
            i += 1
            continue

        # Tables
        if "|" in line and (i + 1) < n and table_divider_re.match(lines[i + 1]):
            flush_buffer()
            while i < n and ("|" in lines[i] or lines[i].strip() == ""):
                out.append(lines[i])
                i += 1
            continue

        # Headers and reference links
        if header_re.match(line) or ref_link_re.match(line):
            flush_buffer()
            out.append(line)
            i += 1
            continue

        # List items
        if list_item_re.match(line):
            flush_buffer()
            # Accumulate list item
            list_indent_match = re.match(r"^([ \t]*)([-*]|\d+\.)\s+", line)
            list_indent = list_indent_match.group(1) + list_indent_match.group(2) + " "
            buffer = line.strip()[len(list_indent_match.group(0)):]  # text without bullet
            buffer_indent = list_indent
            i += 1
            # Collect wrapped lines
            while i < n:
                next_line = lines[i]
                if next_line.strip() == "":
                    break
                # stop if next line starts a new list item
                if list_item_re.match(next_line):
                    break
                buffer += " " + next_line.strip()
                i += 1
            # Split into sentences
            sentences = split_sentences(buffer)
            if len(sentences) == 1:
                out.append(buffer_indent + sentences[0])
            else:
                # multi-sentence: first line keeps bullet, rest without indentation
                out.append(buffer_indent + sentences[0])
                out.extend(sentences[1:])
            buffer = ""
            buffer_indent = ""
            continue

        # Paragraph lines
        leading_ws = re.match(r"^[ \t]*", line).group(0)
        if not buffer:
            buffer_indent = leading_ws
            buffer = stripped
        else:
            buffer += " " + stripped
        i += 1

    flush_buffer()
    return "\n".join(out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Format text so each sentence is on its own line.")
    parser.add_argument("input_file", help="Input text file")
    parser.add_argument("-o", "--output_file", help="Output file (default: stdout)")
    args = parser.parse_args()

    with open(args.input_file, "r", encoding="utf-8") as f:
        text = f.read()

    formatted = format_markdown(text)

    if args.output_file:
        with open(args.output_file, "w", encoding="utf-8") as f:
            f.write(formatted)
    else:
        print(formatted)