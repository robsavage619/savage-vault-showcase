from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_PATH_PARTS = {
    "/raw/",
    "\\raw\\",
    "Vault/savage_vault/raw",
}

FORBIDDEN_PATTERNS = [
    re.compile(r"\[\[raw/", re.IGNORECASE),
    re.compile(r"Anna'?s?\s+Archive", re.IGNORECASE),
    re.compile(r"annas-archive", re.IGNORECASE),
    re.compile(r"/Users/robsavage/Vault/savage_vault/raw", re.IGNORECASE),
]

REQUIRED_FRONTMATTER = {
    "type",
    "title",
    "summary",
    "tags",
    "sources",
    "created",
    "updated",
    "status",
    "aliases",
    "related",
    "confidence",
}


def iter_text_files() -> list[Path]:
    ignored_parts = {".git", "__pycache__"}
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in ignored_parts for part in path.parts):
            continue
        if path.suffix.lower() in {".md", ".py", ".json", ".yml", ".yaml", ".gitignore"}:
            files.append(path)
    return files


def frontmatter(text: str) -> str | None:
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    return parts[1]


def validate_no_private_content(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    display = str(path.relative_to(ROOT))
    for forbidden in FORBIDDEN_PATH_PARTS:
        if forbidden in text:
            errors.append(f"{display}: contains forbidden path marker {forbidden!r}")
    for pattern in FORBIDDEN_PATTERNS:
        if pattern.search(text):
            errors.append(f"{display}: matches forbidden pattern {pattern.pattern!r}")
    return errors


def validate_markdown_frontmatter(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    if path.suffix.lower() != ".md" or path.name == "README.md":
        return errors
    fm = frontmatter(text)
    if fm is None:
        return errors
    keys = set()
    for line in fm.splitlines():
        if ":" in line and not line.startswith(" "):
            keys.add(line.split(":", 1)[0].strip())
    missing = sorted(REQUIRED_FRONTMATTER - keys)
    if missing:
        errors.append(f"{path.relative_to(ROOT)}: missing frontmatter keys {missing}")
    return errors


def main() -> int:
    errors: list[str] = []
    if (ROOT / "raw").exists():
        errors.append("raw/ directory must not exist in showcase repo")

    for path in iter_text_files():
        if path == Path(__file__).resolve():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        errors.extend(validate_no_private_content(path, text))
        errors.extend(validate_markdown_frontmatter(path, text))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("showcase validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
