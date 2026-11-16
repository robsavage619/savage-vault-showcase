"""Generate wiki/index.md, wiki/index-short.md and wiki/catalog.jsonl from page frontmatter.

A page's section is its `index_section`, else its `parent` page's section, else the default
for its `type`. index.md lists every page whose `index_eligible` is not false; index-short.md
lists pages whose `index_eligible` is true or that carry a `hook`. Text above the first
section, each section's intro, and the Live Views and Tag Registry sections are kept from the
current files; entries, Contents and Stats are regenerated.

    python scripts/build_index.py ~/Vault/savage_vault
    python scripts/build_index.py ~/Vault/savage_vault --check   # exit 1 on drift
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
GENERATED = {"index", "index-short", "log"}
UNSORTED = "Unsorted"
TYPE_SECTION = {
    "concept": "Concepts",
    "overview": "Overviews",
    "analysis": "Analyses",
    "comparison": "Comparisons",
    "entity": "Entities",
    "research-finding": "Research Findings",
    "project-context-manifest": "Local Project Manifests",
}
KEPT = ("Live Views (Bases)", "Tag Registry")
CATALOG_FIELDS = (
    "title",
    "type",
    "section",
    "summary",
    "hook",
    "updated",
    "status",
    "index_eligible",
    "parent",
    "domains",
    "tags",
    "doi",
    "sources",
    "fidelity_status",
    "validation_status",
    "retrieval_priority",
    "approved_use",
    "prohibited_use",
)


def load_pages(wiki: Path) -> dict[str, dict]:
    """Return slug -> frontmatter for every wiki page except the generated ones."""
    pages: dict[str, dict] = {}
    for path in sorted(wiki.glob("*.md")):
        if path.stem in GENERATED:
            continue
        match = FRONTMATTER.match(path.read_text(encoding="utf-8"))
        pages[path.stem] = (yaml.safe_load(match.group(1)) or {}) if match else {}
    return pages


def link_slug(value: object) -> str:
    return re.sub(r"[\[\]\"']", "", str(value or "")).split("|")[0].strip()


def one_line(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def section_of(
    slug: str, pages: dict[str, dict], seen: frozenset[str] = frozenset()
) -> str:
    meta = pages[slug]
    if meta.get("index_section"):
        return one_line(meta["index_section"])
    parent = link_slug(meta.get("parent"))
    if parent in pages and parent not in seen | {slug}:
        return section_of(parent, pages, seen | {slug})
    return TYPE_SECTION.get(str(meta.get("type")), UNSORTED)


def hook_of(meta: dict) -> str:
    """The page's `hook`, else the first sentence of its summary."""
    if meta.get("hook"):
        return one_line(meta["hook"])
    summary = one_line(meta.get("summary"))
    match = re.match(r"(.+?[.!?])(?:\s|$)", summary)
    return match.group(1) if match else summary


def anchor(heading: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", heading.lower()).strip("-")


def split_blocks(text: str) -> tuple[str, list[tuple[str, str]]]:
    """Split markdown into the text before the first `## ` heading and (heading, body) blocks."""
    parts = re.split(r"^## (.+)\n", text, flags=re.MULTILINE)
    return parts[0], [(parts[i].strip(), parts[i + 1]) for i in range(1, len(parts), 2)]


def intro(body: str) -> str:
    """Body lines before the first list item, trailing blank lines dropped."""
    lines: list[str] = []
    for line in body.splitlines():
        if line.startswith("- "):
            break
        lines.append(line)
    return "\n".join(lines).rstrip()


def with_updated(head: str, date: str) -> str:
    return re.sub(
        r"^updated: .*$", f"updated: {date}", head, count=1, flags=re.MULTILINE
    )


def build(vault: Path) -> dict[Path, str]:
    """Render the three generated files from the vault's pages.

    Args:
        vault: The vault root, the directory that contains `wiki/`.

    Returns:
        Path -> full file text for index.md, index-short.md and catalog.jsonl.
    """
    wiki = vault / "wiki"
    pages = load_pages(wiki)
    sections = {slug: section_of(slug, pages) for slug in pages}
    newest = max(str(m.get("updated", "")) for m in pages.values())

    def listed(meta: dict) -> bool:
        return meta.get("index_eligible") is not False

    def order(slugs: list[str]) -> list[str]:
        return sorted(
            sorted(slugs), key=lambda s: str(pages[s].get("updated", "")), reverse=True
        )

    by_section: dict[str, list[str]] = {}
    for slug in pages:
        if listed(pages[slug]):
            by_section.setdefault(sections[slug], []).append(slug)

    head, blocks = split_blocks((wiki / "index.md").read_text(encoding="utf-8"))
    kept = {h: b.rstrip() for h, b in blocks if h in KEPT}
    contents_intro = next((intro(b) for h, b in blocks if h == "Contents"), "")
    known = [h for h, _ in blocks if h not in KEPT and h not in ("Contents", "Stats")]
    intros = {h: intro(b) for h, b in blocks if h in known}
    order_sections = [h for h in known if h in by_section] + sorted(
        s for s in by_section if s not in known
    )

    out: list[str] = [with_updated(head, newest).rstrip() + "\n"]
    toc = [f"- [{h}](#{anchor(h)})" for h in order_sections]
    out.append(
        "## Contents\n\n"
        + (contents_intro.strip() + "\n\n" if contents_intro.strip() else "")
        + "\n".join(toc)
        + "\n"
    )
    if "Live Views (Bases)" in kept:
        out.append("## Live Views (Bases)\n" + kept["Live Views (Bases)"] + "\n")
    for h in order_sections:
        entries = [
            f"- [[{s}]] `{pages[s].get('type')}` `updated: {pages[s].get('updated')}`\n  > {one_line(pages[s].get('summary'))}"
            for s in order(by_section[h])
        ]
        lead = intros.get(h, "").strip()
        out.append(
            f"## {h}\n\n"
            + (lead + "\n\n" if lead else "")
            + "\n\n".join(entries)
            + "\n"
        )
    if "Tag Registry" in kept:
        out.append("## Tag Registry\n" + kept["Tag Registry"] + "\n")
    types = Counter(str(m.get("type")) for m in pages.values())
    short = [
        s
        for s, m in pages.items()
        if m.get("index_eligible") is True or (m.get("hook") and listed(m))
    ]
    stats = [
        f"Generated from page frontmatter by `build_index.py`; newest page update {newest}.",
        "",
        f"- **Pages:** {len(pages)} (excluding index, index-short and log)",
        *[f"- **{t} pages:** {n}" for t, n in types.most_common()],
        f"- **Listed in index-short:** {len(short)}",
        f"- **Held out of the indexes (`index_eligible: false`):** {sum(not listed(m) for m in pages.values())}",
        f"- **Unsorted (no `index_section`, parent or type default):** {len(by_section.get(UNSORTED, []))}",
        f"- **Bases views:** {len(list((wiki / 'bases').glob('*.base')))}",
    ]
    out.append("## Stats\n\n" + "\n".join(stats) + "\n")
    index_md = "\n".join(out)

    s_head, s_blocks = split_blocks(
        (wiki / "index-short.md").read_text(encoding="utf-8")
    )
    s_contents_intro = next((intro(b) for h, b in s_blocks if h == "Contents"), "")
    short_by: dict[str, list[str]] = {}
    for slug in short:
        short_by.setdefault(sections[slug], []).append(slug)
    s_order = [h for h in order_sections if h in short_by]
    s_out = [with_updated(s_head, newest).rstrip() + "\n"]
    s_out.append(
        "## Contents\n\n"
        + (s_contents_intro.strip() + "\n\n" if s_contents_intro.strip() else "")
        + "\n".join(f"- [{h}](#{anchor(h)})" for h in s_order)
        + "\n"
    )
    for h in s_order:
        s_out.append(
            f"## {h}\n\n"
            + "\n".join(f"- [[{s}]] — {hook_of(pages[s])}" for s in order(short_by[h]))
            + "\n"
        )
    short_md = "\n".join(s_out)

    def plain(value: object) -> object:
        if isinstance(value, dt.date):
            return value.isoformat()
        if isinstance(value, list):
            return [plain(v) for v in value]
        return value

    rows = []
    for slug in sorted(pages):
        meta = pages[slug]
        row: dict[str, object] = {"slug": slug}
        for field in CATALOG_FIELDS:
            value = {
                "section": sections[slug],
                "hook": hook_of(meta),
                "parent": link_slug(meta.get("parent")) or None,
            }.get(field, meta.get(field))
            row[field] = (
                one_line(value) if field in ("summary", "title") else plain(value)
            )
        rows.append(json.dumps(row, ensure_ascii=False))
    catalog = "\n".join(rows) + "\n"

    return {
        wiki / "index.md": index_md,
        wiki / "index-short.md": short_md,
        wiki / "catalog.jsonl": catalog,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "vault",
        type=Path,
        help="path to the vault root (the directory containing wiki/)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="report files that differ from a fresh build and exit 1",
    )
    args = parser.parse_args()
    stale = []
    for path, text in build(args.vault.expanduser()).items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current == text:
            continue
        stale.append(path.name)
        if not args.check:
            path.write_text(text, encoding="utf-8")
    if args.check and stale:
        print(
            f"out of date: {', '.join(stale)}; run scripts/build_index.py",
            file=sys.stderr,
        )
        return 1
    print(
        f"{'checked' if args.check else 'wrote'}: {', '.join(stale) or 'nothing changed'}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
