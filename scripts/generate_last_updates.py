#!/usr/bin/env python3
"""Generate page modification dates from the repository's Git history."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = REPOSITORY_ROOT / "_data" / "last_updates.yml"


def git(*arguments: str) -> str:
    """Run Git in the repository root and return its standard output."""
    result = subprocess.run(
        ["git", *arguments],
        cwd=REPOSITORY_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def tracked_pages() -> list[str]:
    """Return tracked Markdown pages in stable path order."""
    output = git("ls-files", "--", "pages")
    return sorted(path for path in output.splitlines() if path.endswith(".md"))


def ensure_pages_are_committed() -> None:
    """Refuse to derive dates while the pages tree contains local changes."""
    if git("status", "--porcelain", "--untracked-files=all", "--", "pages"):
        raise RuntimeError(
            "There are uncommitted changes under pages/. Commit them before "
            "generating last-update dates."
        )


def last_update(path: str) -> str:
    """Return the most recent author date for a page, following renames."""
    return git("log", "-1", "--follow", "--format=%as", "--", path).strip()


def render() -> str:
    """Render the generated mapping as deterministic YAML."""
    lines = [
        "# Generated from Git history by scripts/generate_last_updates.py.",
        "# Do not edit manually.",
        "",
    ]

    for path in tracked_pages():
        date = last_update(path)
        if not date:
            raise RuntimeError(f"No Git history found for tracked page: {path}")
        lines.append(f"{json.dumps(path)}: {json.dumps(date)}")

    return "\n".join(lines) + "\n"


def main() -> int:
    try:
        ensure_pages_are_committed()
        generated = render()
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        temporary_path = OUTPUT_PATH.with_suffix(".yml.tmp")
        temporary_path.write_text(generated, encoding="utf-8")
        temporary_path.replace(OUTPUT_PATH)
    except (RuntimeError, subprocess.CalledProcessError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"Generated {OUTPUT_PATH.relative_to(REPOSITORY_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
