#!/usr/bin/env python3
"""Validate that `quality_indicators` referenced in `pages/tasks/*.md`
exist in `_data/quality_indicators.yml` (matching `abbreviation`).

Exit codes:
 - 0: all indicators valid
 - 1: missing indicators found or errors
"""

import sys
import os
import re
import yaml
from glob import glob


FRONT_MATTER_RE = re.compile(r"^---\n(.*?\n)---\n", re.DOTALL)


def load_indicator_abbreviations(path="_data/quality_indicators.yml"):
    """Load and return a set of abbreviation identifiers from the
    quality indicators YAML file located at `path`.

    Each entry in the YAML file is expected to be a mapping containing an
    "abbreviation" key. Returns an empty set if the file is missing or if
    no valid abbreviations are found.
    """
    if not os.path.exists(path):
        print(f"Error: indicators file not found: {path}")
        return set()
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or []
    abbrevs = {item.get("abbreviation") for item in data if isinstance(item, dict) and item.get("abbreviation")}
    return set(abbrevs)


def extract_front_matter(filepath):
    """Extract YAML front matter from a Markdown file and return it as a dict.

    If the file has no front matter or parsing fails, an empty dict is
    returned. Parsing errors are printed as warnings.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    m = FRONT_MATTER_RE.match(content)
    if not m:
        return {}
    try:
        fm = yaml.safe_load(m.group(1)) or {}
        return fm if isinstance(fm, dict) else {}
    except Exception as e:
        print(f"Warning: failed to parse front matter in {filepath}: {e}")
        return {}


def find_task_pages(patterns=("pages/tasks/*.md",)):
    """Return a sorted list of task page file paths matching provided glob patterns.

    The default pattern scans `pages/tasks/*.md`.
    """
    files = []
    for p in patterns:
        files.extend(sorted(glob(p)))
    return files


def main():
    """validate that `quality_indicators` referenced in task pages exist in `_data/quality_indicators.yml`.

    Exits with code 0 when all references are valid, otherwise prints the
    missing identifiers and exits with code 1.
    """
    indicators = load_indicator_abbreviations()
    if not indicators:
        print("No indicators loaded — aborting")
        sys.exit(1)

    pages = find_task_pages()
    if not pages:
        print("No task pages found (pages/tasks/*.md)")
        sys.exit(0)

    missing = {}

    for page in pages:
        fm = extract_front_matter(page)
        qi = fm.get("quality_indicators")
        if qi is None:
            # treat missing key as empty
            continue
        # ensure it's a list
        if isinstance(qi, str):
            # YAML shorthand: single string — convert to list by splitting commas
            qi_list = [s.strip() for s in qi.split(",") if s.strip()]
        elif isinstance(qi, list):
            qi_list = qi
        else:
            qi_list = []

        for id_ in qi_list:
            if id_ == "":
                continue
            if id_ not in indicators:
                missing.setdefault(page, []).append(id_)

    if missing:
        print("Missing/unknown quality_indicator IDs found:")
        for page, ids in missing.items():
            print(f" - {page}: {', '.join(ids)}")
        print("\nEnsure these abbreviations exist in _data/quality_indicators.yml (field: 'abbreviation').")
        sys.exit(1)

    print("All quality_indicators referenced in pages/tasks are valid.")
    sys.exit(0)


if __name__ == "__main__":
    main()
