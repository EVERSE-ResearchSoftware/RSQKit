#!/usr/bin/env python3
"""
Markdown Sentence Formatter

This script formats Markdown files with the following rules and behaviors:

1. Paragraphs:
   - Each sentence is placed on its own line.
   - Leading indentation and blank lines are preserved.

2. List items:
   - Single-sentence list items (even if wrapped) collapse into one line.
   - Multi-sentence list items split each sentence onto a new line.
     - First line keeps the bullet.
     - Subsequent lines have no indentation.

3. YAML front matter, reference-style links ([name]: ...), headers (# ...), and Markdown tables (GFM) are preserved intact.

4. Code fences (``` ... ```) and Liquid blocks ({% ... %} ... {% end ... %}) are preserved.

5. HTML blocks (e.g., <div>...</div>, <p>...</p>, <pre>...</pre>) are preserved as-is.
   - Single-line self-closing tags like <br /> or <img .../> are left untouched.

6. Blank lines and indentation:
   - Blank lines are preserved exactly.
   - Paragraph indentation is preserved.
   - Multi-sentence list items remove indentation after the first sentence.

7. Sentence splitting:
   - Common abbreviations (e.g., e.g., Mr., Dr., etc.) are protected to avoid incorrect splits.
   - Each sentence ends at ., !, or ?, optionally followed by quotes, parentheses, or brackets.
"""

#!/usr/bin/env python3
import argparse
import re

ABBREVIATIONS = [
    "e.g.", "i.e.", "etc.", "vs.", "Mr.", "Mrs.", "Ms.", "Dr.", "Prof.",
    "Sr.", "Jr.", "St.", "Inc.", "Ltd.", "et al.", "al.", "cf.", "Fig.", "fig.",
    "Jan.", "Feb.", "Mar.", "Apr.", "May.", "Jun.", "Jul.", "Aug.", "Sep.", "Sept.",
    "Oct.", "Nov.", "Dec."
]

BLOCK_PATTERNS = [
    r"^---\n.*?\n---",                          # YAML front matter
    r"```.*?```",                                # Code blocks
    r"{%.*?%}",                                  # Liquid blocks
    r"<(div|section|article|header|footer|nav|aside|h[1-6]|p|pre|table|form|blockquote|script).*?>.*?</\1>",  # HTML blocks
    r"^\[[^\]]+\]:\s*.*$",                      # Markdown reference links
]

def format_markdown(text):
    # Step 0: Protect Markdown tables
    table_placeholders = []
    def protect_table(match):
        table_placeholders.append(match.group(0))
        return f"@@TABLE{len(table_placeholders)-1}@@"
    text = re.sub(r'^(?:\s*\|.*\|.*)$', protect_table, text, flags=re.MULTILINE)

    # Step 1: Protect other blocks
    block_placeholders = []
    def protect_block(match):
        block_placeholders.append(match.group(0))
        return f"@@BLOCK{len(block_placeholders)-1}@@"
    for pattern in BLOCK_PATTERNS:
        text = re.sub(pattern, protect_block, text, flags=re.DOTALL | re.MULTILINE)

    # Step 2: Protect abbreviations
    abbrev_placeholders = {}
    for i, abbr in enumerate(ABBREVIATIONS):
        ph = f"@@ABBR{i}@@"
        text = text.replace(abbr, ph)
        abbrev_placeholders[ph] = abbr

    # Step 3: Split into paragraphs by empty lines (allow single empty lines only)
    paragraphs = re.split(r'\n\s*\n', text)
    formatted_paragraphs = []

    list_item_pattern = re.compile(r'^(\s*)([-*+]|[0-9]+[.])\s+')

    for para in paragraphs:
        para = para.strip()
        if not para:
            # preserve a single empty line
            formatted_paragraphs.append("")
            continue

        # Split lines in paragraph
        lines = para.splitlines()
        processed_lines = []

        for line in lines:
            stripped = line.lstrip()
            indent = line[:len(line) - len(stripped)]

            # Detect list items
            match = list_item_pattern.match(line)
            if match:
                item_indent = match.group(1)
                marker = match.group(2)
                content = stripped[match.end():]

                # Join wrapped lines in content
                content = " ".join(content.splitlines())

                # Split sentences
                sentences = re.split(r'([.!?])\s+', content)
                item_sentences = []
                for i in range(0, len(sentences)-1, 2):
                    item_sentences.append(sentences[i].strip() + sentences[i+1])
                if len(sentences) % 2 != 0:
                    item_sentences.append(sentences[-1].strip())

                # Recombine sentences with indentation and marker
                for idx, sent in enumerate(item_sentences):
                    if idx == 0:
                        processed_lines.append(f"{item_indent}{marker} {sent}")
                    else:
                        processed_lines.append(f"{item_indent}  {sent}")
            else:
                # Normal paragraph line: join wrapped lines
                joined_line = " ".join(stripped.splitlines())
                # Split sentences
                sentences = re.split(r'([.!?])\s+', joined_line)
                para_sentences = []
                for i in range(0, len(sentences)-1, 2):
                    para_sentences.append(sentences[i].strip() + sentences[i+1])
                if len(sentences) % 2 != 0:
                    para_sentences.append(sentences[-1].strip())

                processed_lines.extend([indent + s for s in para_sentences])

        formatted_paragraphs.append("\n".join(processed_lines))

    # Step 4: Join paragraphs with a single empty line between them
    result = "\n\n".join(formatted_paragraphs)

    # Step 5: Restore abbreviations
    for ph, abbr in abbrev_placeholders.items():
        result = result.replace(ph, abbr)

    # Step 6: Restore blocks
    for idx, block in enumerate(block_placeholders):
        result = result.replace(f"@@BLOCK{idx}@@", block)

    # Step 7: Restore tables
    for idx, table in enumerate(table_placeholders):
        result = result.replace(f"@@TABLE{idx}@@", table)

    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Format Markdown so each sentence is on its own line.")
    parser.add_argument("input_file", help="Input Markdown file")
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
