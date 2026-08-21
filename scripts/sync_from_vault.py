"""Regenerate this repository's published pages from the private vault.

This repo republishes a hand-picked subset of vault pages with private-domain
content removed. Doing that by hand does not survive contact with an evolving
vault: the copies drift, and nothing distinguishes a deliberate redaction from a
stale file.

This script makes the transformation reproducible. `--check` reports drift
without writing, so CI or a pre-push hook can fail when the vault has moved on.

    python scripts/sync_from_vault.py --vault ~/Vault/savage_vault
    python scripts/sync_from_vault.py --vault ~/Vault/savage_vault --check
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

try:
    from scrub_rules import DROP_LINES, PRE_REWRITES, REWRITES
except ImportError:  # pragma: no cover - depends on an uncommitted local file
    print(
        "scripts/scrub_rules.py not found.\n"
        "The redaction rules name the private domains they remove, so they are not\n"
        "committed. Copy scripts/scrub_rules.example.py to scripts/scrub_rules.py and\n"
        "fill it in against your own vault.",
        file=sys.stderr,
    )
    raise SystemExit(2) from None

# Explicit allowlist. Nothing is published that is not named here — a denylist
# over ~1,400 pages leaked health and personal-medical cards on the first pass.
PUBLISHED: dict[str, tuple[str, ...]] = {
    "reference": (
        "metadata-schema", "corpus-governance", "source-fidelity-review-gate",
        "claim-conflict-protocol", "index-promotion-manifest",
        "corpus-weekly-review-protocol", "symbolic-type-system",
        "symbolic-validation-rules", "template-catalog", "question-router",
        "agent-entry", "agent-access-coding-corpus",
        "corpus-agent-evaluation-suite", "corpus-agent-judge-rubric",
    ),
    "playbooks": (
        "coding-agent-operating-card", "coding-agent-context-retrieval-playbook",
        "coding-agent-validation-playbook", "coding-agent-safe-change-playbook",
        "coding-agent-python-architecture-playbook", "coding-agent-data-system-playbook",
        "coding-agent-production-readiness-playbook", "coding-agent-data-ml-contracts-playbook",
        "coding-agent-review-checklist", "retrieval-pack-ai-engineering",
        "retrieval-pack-finops-cost-engineering",
    ),
    "examples": (
        "agent-isolation-design-patterns", "control-flow-integrity-for-agents",
        "capability-based-tool-policy", "eval-statistical-inference", "eval-power-analysis",
        "test-time-compute-scaling", "replication-vs-reproduction", "focus-billing-schema",
        "finops-capability-model", "unit-economics-cost-per-outcome",
        "lakehouse-architecture", "acid-table-storage-layer",
    ),
}


def transform(text: str, published: set[str]) -> str:
    """Transform one vault page into its published form.

    Order matters. `related:` is filtered first so line-dropping cannot delete
    the whole field, and the literal rewrites run last so they can match the
    bolded forms that link normalization produces.
    """

    def fix_related(match: re.Match[str]) -> str:
        items = re.findall(r'"\[\[([^\]]+)\]\]"', match.group(1))
        kept = ", ".join(f'"[[{i}]]"' for i in items if i in published)
        return f"related: [{kept}]"

    text = re.sub(r"^related: \[(.*)\]$", fix_related, text, flags=re.M)

    for old, new in PRE_REWRITES:
        text = text.replace(old, new)

    text = "\n".join(
        line for line in text.split("\n")
        if line.startswith("related:") or not any(m in line for m in DROP_LINES)
    )

    def fix_link(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        if target.endswith(".base") or target.startswith("raw/"):
            return f"`{target}`"
        return f"[[{target}]]" if target in published else f"**{target}**"

    text = re.sub(r"\[\[([^\]|#]+)\]\]", fix_link, text)

    for old, new in REWRITES:
        text = text.replace(old, new)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", required=True, help="path to the private vault root")
    parser.add_argument("--check", action="store_true", help="report drift, write nothing")
    args = parser.parse_args()

    wiki = Path(args.vault).expanduser() / "wiki"
    if not wiki.is_dir():
        print(f"no wiki/ directory under {args.vault}", file=sys.stderr)
        return 2

    published = {slug for slugs in PUBLISHED.values() for slug in slugs}
    drifted: list[str] = []
    written = missing = 0

    for subdir, slugs in PUBLISHED.items():
        for slug in slugs:
            source = wiki / f"{slug}.md"
            if not source.exists():
                print(f"  MISSING IN VAULT: {slug}", file=sys.stderr)
                missing += 1
                continue
            new_text = transform(source.read_text(encoding="utf-8"), published)
            target = ROOT / subdir / f"{slug}.md"
            old_text = target.read_text(encoding="utf-8") if target.exists() else ""
            if new_text == old_text:
                continue
            if args.check:
                diff = list(difflib.unified_diff(
                    old_text.split("\n"), new_text.split("\n"),
                    fromfile=f"published/{subdir}/{slug}.md",
                    tofile=f"vault/{slug}.md", lineterm="", n=0,
                ))
                changed = sum(1 for line in diff if line[:1] in "+-" and line[:3] not in ("+++", "---"))
                drifted.append(f"{subdir}/{slug}.md ({changed} lines)")
            else:
                target.write_text(new_text, encoding="utf-8")
                written += 1

    if args.check:
        if drifted or missing:
            print(f"DRIFT: {len(drifted)} page(s) differ from the vault", file=sys.stderr)
            for entry in drifted:
                print(f"  {entry}", file=sys.stderr)
            if missing:
                print(f"  {missing} allowlisted page(s) no longer exist in the vault", file=sys.stderr)
            print("\nRun without --check to regenerate, then re-run the leak guard.", file=sys.stderr)
            return 1
        print(f"in sync with the vault ({len(published)} pages)")
        return 0

    print(f"regenerated {written} page(s); {len(published) - written - missing} already current")
    if missing:
        print(f"{missing} allowlisted page(s) missing from the vault", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
