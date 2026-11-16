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


def check(vault: str) -> list[tuple[str, str]]:
    """Run every check against `vault` and print a report.

    Returns the problems found, as (slug, issue) pairs.
    """
    wiki = os.path.join(vault, "wiki")
    files = sorted(glob.glob(os.path.join(wiki, "*.md")))
    if not files:
        print(f"no pages found under {wiki}", file=sys.stderr)
        return [("", f"no pages found under {wiki}")]

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
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vault", help="path to the vault root (the directory containing wiki/)")
    parser.add_argument("--baseline", help="file of known problems, one 'slug: issue' per line; only problems not in it fail")
    parser.add_argument("--write-baseline", action="store_true", help="write the current problems to --baseline and exit 0")
    args = parser.parse_args()
    lines = sorted({f"{slug}: {issue}" for slug, issue in check(args.vault)})
    if not args.baseline:
        return 1 if lines else 0
    if args.write_baseline:
        with open(args.baseline, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        print(f"baseline: {len(lines)} known problems written to {args.baseline}")
        return 0
    def key(line: str) -> str:
        # a page already over its size cap stays one known problem as its word count moves
        return re.sub(r": \d+ words exceeds", ": N words exceeds", line)

    with open(args.baseline, encoding="utf-8") as fh:
        known = {key(line) for line in fh.read().splitlines()}
    new = [line for line in lines if key(line) not in known]
    print(f"new problems not in baseline: {len(new)}")
    for line in new:
        print(f"  {line}")
    return 1 if new else 0


if __name__ == "__main__":
    raise SystemExit(main())
