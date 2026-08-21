"""Fail the build if private corpus content reaches this public repository.

This repo publishes the *system* that maintains a personal knowledge vault, never
the vault. The vault contains health, financial, relationship, and employer
material that must not appear here. This script encodes that boundary as a test
so the guarantee survives future edits.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "__pycache__", ".venv"}

# Terms that must never appear. Word-boundary matched, case-insensitive.
FORBIDDEN = [
    # personal / relational
    "wife", "marriage", "divorce", "therapy", "therapist", "couples",
    "intimacy", "rejection sensitivity", "ADHD",
    # health
    "hypertrophy", "insomnia", "apoB", "whoop", "hevy",
    # finance / first-party research
    "CORTEX", "backtest run receipt", "signal register",
    # employer
    "Nike", "NSRL", "Swoosh",
    # private project names
    "padres", "xfriars", "savage-health", "sleeper-fantasy",
    # local environment
    "/Users/",
]

# Structural patterns that indicate vault content rather than system docs.
FORBIDDEN_PATTERNS = [
    re.compile(r"\[\[raw/", re.IGNORECASE),
    re.compile(r"^sources:\s*\[\s*\"\[\[raw/", re.IGNORECASE | re.MULTILINE),
    re.compile(r"anna'?s\s+archive", re.IGNORECASE),
    re.compile(r"\bgho_[A-Za-z0-9]{20,}", 0),        # GitHub token
    re.compile(r"\bsk-[A-Za-z0-9]{20,}", 0),          # API key
    re.compile(r"Bearer\s+(?!<key>)[A-Za-z0-9._-]{20,}", 0),
]


def scan() -> list[str]:
    """Return a list of human-readable violations, empty when the repo is clean."""
    violations: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or any(part in SKIP_DIRS for part in path.parts):
            continue
        # These files must name the forbidden patterns in order to enforce or
        # document them, so they are exempt from the pattern scan by design.
        if path.name in {"leak_guard.py", "corpus_health.py", "CONTENT-BOUNDARY.md"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        rel = path.relative_to(ROOT)
        for term in FORBIDDEN:
            pattern = re.escape(term)
            if not term.startswith("/"):
                pattern = rf"\b{pattern}\b"
            for match in re.finditer(pattern, text, re.IGNORECASE):
                line = text[: match.start()].count("\n") + 1
                violations.append(f"{rel}:{line}: forbidden term {term!r}")
        for pattern in FORBIDDEN_PATTERNS:
            for match in pattern.finditer(text):
                line = text[: match.start()].count("\n") + 1
                violations.append(f"{rel}:{line}: forbidden pattern {pattern.pattern!r}")
    return violations


def main() -> int:
    violations = scan()
    if violations:
        print(f"LEAK GUARD FAILED — {len(violations)} violation(s):", file=sys.stderr)
        for violation in violations[:50]:
            print(f"  {violation}", file=sys.stderr)
        if len(violations) > 50:
            print(f"  ... and {len(violations) - 50} more", file=sys.stderr)
        return 1
    print("leak guard: clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
