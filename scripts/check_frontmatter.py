"""Validate that every published page in this repo parses and carries required fields.

The corpus health checker runs against a full vault; this runs against the pages
shipped here, so CI fails if an example or doc is committed malformed.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CHECKED_DIRS = ("reference", "playbooks", "examples", "templates")
REQUIRED = ("type", "title", "summary", "tags", "sources", "created", "updated", "status")
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)


def main() -> int:
    problems: list[str] = []
    checked = 0
    for directory in CHECKED_DIRS:
        for path in sorted((ROOT / directory).glob("*.md")):
            rel = path.relative_to(ROOT)
            checked += 1
            text = path.read_text(encoding="utf-8")
            match = FRONTMATTER.match(text)
            if not match:
                problems.append(f"{rel}: no frontmatter")
                continue
            try:
                meta = yaml.safe_load(match.group(1)) or {}
            except yaml.YAMLError as exc:
                problems.append(f"{rel}: YAML parse — {str(exc)[:80]}")
                continue
            if directory == "templates":
                continue  # templates carry unrendered {{date}} placeholders
            for field in REQUIRED:
                if field not in meta:
                    problems.append(f"{rel}: missing {field}")
                elif field != "sources" and not meta[field]:
                    problems.append(f"{rel}: empty {field}")

    pages = {p.stem for d in CHECKED_DIRS for p in (ROOT / d).glob("*.md")}
    for directory in CHECKED_DIRS:
        for path in sorted((ROOT / directory).glob("*.md")):
            for link in set(re.findall(r"\[\[([^\]|#]+)\]\]", path.read_text(encoding="utf-8"))):
                if link.strip() not in pages:
                    problems.append(f"{path.relative_to(ROOT)}: unresolved wikilink {link.strip()!r}")

    print(f"checked {checked} pages, {len(problems)} problem(s)")
    for problem in problems[:40]:
        print(f"  {problem}", file=sys.stderr)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
