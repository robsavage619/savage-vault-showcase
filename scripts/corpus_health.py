"""Corpus health check for a savage-vault-style knowledge base.

Validates frontmatter, required fields, wikilink resolution, source-file
existence, and per-type page-size caps. Exits non-zero when problems are found.
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys
from collections import Counter

import yaml

REQUIRED = ("type", "title", "summary", "tags", "sources", "created", "updated", "status")
SIZE_CAPS = {"concept": 900, "entity": 900, "source-summary": 2500, "book-overview": 2500}
DEFAULT_CAP = 1500
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)
WIKILINK = re.compile(r"\[\[([^\]|#]+)\]\]")


def check(vault: str) -> int:
    """Run every check against `vault` and print a report.

    Returns the number of problems found.
    """
    wiki = os.path.join(vault, "wiki")
    files = sorted(glob.glob(os.path.join(wiki, "*.md")))
    if not files:
        print(f"no pages found under {wiki}", file=sys.stderr)
        return 1

    pages = {os.path.splitext(os.path.basename(f))[0] for f in files}
    problems: list[tuple[str, str]] = []
    types: Counter[str] = Counter()

    for path in files:
        slug = os.path.splitext(os.path.basename(path))[0]
        text = open(path, encoding="utf-8").read()

        match = FRONTMATTER.match(text)
        if not match:
            problems.append((slug, "no frontmatter"))
            continue
        try:
            meta = yaml.safe_load(match.group(1)) or {}
        except yaml.YAMLError as exc:
            problems.append((slug, f"YAML parse: {str(exc)[:80]}"))
            continue

        for field in REQUIRED:
            if field not in meta:
                problems.append((slug, f"missing {field}"))
            elif field != "sources" and not meta[field]:
                # sources may legitimately be an empty list on synthesized pages
                problems.append((slug, f"empty {field}"))

        page_type = str(meta.get("type", "unknown"))
        types[page_type] += 1

        for source in meta.get("sources") or []:
            if isinstance(source, str) and source.startswith("[[raw/"):
                target = os.path.join(vault, source[2:-2])
                if not os.path.exists(target):
                    problems.append((slug, f"missing source file {source[2:-2]}"))

        if not re.search(r"^## (See Also|Related|Seeds|Chapter Map)", text, re.M):
            problems.append((slug, "no cross-link section"))

        words = len(text.split())
        cap = SIZE_CAPS.get(page_type, DEFAULT_CAP)
        if words > cap:
            problems.append((slug, f"{words} words exceeds {cap} cap for {page_type}"))

        seeds = re.search(r"\n## Seeds\n(.*?)(?=\n## |\Z)", text, re.S)
        seed_text = seeds.group(1) if seeds else ""
        for link in set(WIKILINK.findall(text)):
            link = link.strip()
            if link.startswith("raw/") or link.endswith(".base") or link in pages:
                continue
            where = "Seeds" if link in seed_text else "body"
            problems.append((slug, f"unresolved wikilink ({where}): {link}"))

    print(f"pages: {len(files)}")
    print(f"types: {dict(types)}")
    print(f"problems: {len(problems)}")
    for slug, issue in problems[:40]:
        print(f"  {slug}: {issue}")
    if len(problems) > 40:
        print(f"  ... and {len(problems) - 40} more")
    return len(problems)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vault", help="path to the vault root (the directory containing wiki/)")
    args = parser.parse_args()
    return 1 if check(args.vault) else 0


if __name__ == "__main__":
    raise SystemExit(main())
