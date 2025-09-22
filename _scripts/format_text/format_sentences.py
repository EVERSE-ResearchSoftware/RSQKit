#!/usr/bin/env python3
import re
import argparse
import sys

# Common abbreviations to protect (add more if needed)
ABBREVIATIONS = [
    "e.g.", "i.e.", "etc.", "vs.", "Mr.", "Mrs.", "Ms.", "Dr.", "Prof.",
    "Sr.", "Jr.", "St.", "Inc.", "Ltd.", "et al.", "al.", "cf.", "Fig.", "fig.",
    "Jan.", "Feb.", "Mar.", "Apr.", "May.", "Jun.", "Jul.", "Aug.", "Sep.", "Sept.",
    "Oct.", "Nov.", "Dec."
]
_PLACEHOLDER = "<<DOT>>"

def _protect_abbreviations(s: str) -> str:
    """Replace dots inside known abbreviations with a placeholder."""
    protected = s
    for abbr in ABBREVIATIONS:
        protected = re.sub(re.escape(abbr), abbr.replace(".", _PLACEHOLDER), protected)
    return protected

def _restore_placeholders(s: str) -> str:
    return s.replace(_PLACEHOLDER, ".")

def format_sentences(text: str) -> str:
    """
    Format text so that each sentence goes on its own line while preserving:
      - YAML front matter (--- ... --- at top),
      - Code blocks surrounded by triple backticks ``` ... ``` ,
      - Lists (*, -, or numbered lists),
      - Reference-style links ([name]: ...),
      - Markdown headers (# ...),
      - Indentation and blank lines.

    Functionality:
    - Joins lines that are part of the same sentence outside preserved regions.
    - Splits text into sentences based on sentence-ending punctuation (., !, ?).
    - Lines inside code blocks, front matter, list items, headers, or reference-style links are left untouched.
    - Leading tabs/spaces for indentation are preserved.
    """
    list_item_re   = re.compile(r"^[ \t]*(?:[\*\-]|\d+\.)\s+")
    ref_link_re    = re.compile(r"^[ \t]*\[[^\]]+\]:")
    header_re      = re.compile(r"^[ \t]*#+\s")
    code_fence_re  = re.compile(r"^[ \t]*```")
    sentence_pattern = re.compile(r'.*?[.!?]["\']?(?=\s|$)', flags=re.S)

    lines = text.splitlines()
    out_lines = []

    i = 0
    n = len(lines)

    # Preserve YAML front matter
    if n > 0 and lines[0].strip() == "---":
        out_lines.append(lines[0])
        i = 1
        while i < n:
            out_lines.append(lines[i])
            if lines[i].strip() == "---":
                i += 1
                break
            i += 1

    in_code_block = False
    buffer = ""
    buffer_indent = ""

    def _flush_buffer_as_sentences():
        nonlocal buffer, buffer_indent, out_lines
        if not buffer:
            return
        protected = _protect_abbreviations(buffer)
        matches = list(sentence_pattern.finditer(protected))
        if matches:
            last_end = 0
            for m in matches:
                raw_sent = protected[m.start():m.end()]
                sent = _restore_placeholders(raw_sent).strip()
                if sent:
                    out_lines.append(buffer_indent + sent)
                last_end = m.end()
            remainder_prot = protected[last_end:].strip()
            remainder = _restore_placeholders(remainder_prot).strip()
            if remainder:
                out_lines.append(buffer_indent + remainder)
        else:
            out_lines.append(buffer_indent + _restore_placeholders(buffer).strip())
        buffer = ""
        buffer_indent = ""

    while i < n:
        raw_line = lines[i]
        stripped = raw_line.strip()

        if code_fence_re.match(raw_line):
            if buffer:
                _flush_buffer_as_sentences()
            out_lines.append(raw_line)
            in_code_block = not in_code_block
            i += 1
            continue

        if in_code_block:
            out_lines.append(raw_line)
            i += 1
            continue

        if stripped == "":
            if buffer:
                _flush_buffer_as_sentences()
            out_lines.append("")
            i += 1
            continue

        if list_item_re.match(raw_line) or ref_link_re.match(raw_line) or header_re.match(raw_line):
            if buffer:
                _flush_buffer_as_sentences()
            out_lines.append(raw_line)
            i += 1
            continue

        leading_ws = re.match(r"^[ \t]*", raw_line).group(0)
        if buffer == "":
            buffer_indent = leading_ws
            buffer = stripped
        else:
            buffer += " " + stripped

        protected = _protect_abbreviations(buffer)
        matches = list(sentence_pattern.finditer(protected))
        if matches:
            last_end = 0
            for m in matches:
                raw_sent = protected[m.start():m.end()]
                sent = _restore_placeholders(raw_sent).strip()
                if sent:
                    out_lines.append(buffer_indent + sent)
                last_end = m.end()
            remainder_prot = protected[last_end:].strip()
            buffer = _restore_placeholders(remainder_prot)
            if not buffer:
                buffer_indent = ""
        i += 1

    if buffer:
        _flush_buffer_as_sentences()

    return "\n".join(out_lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Format text so each sentence is on its own line.")
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
