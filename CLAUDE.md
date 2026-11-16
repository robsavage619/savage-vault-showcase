# savage-vault-system

Rob's global conventions (`~/.claude/CLAUDE.md`) apply; this file is the project overlay.

This repo publishes the system that maintains a personal Obsidian knowledge vault: the operating manual, metadata schema, governance and routing docs, agent playbooks, Bases definitions, page templates, twelve example concept cards on public technical subjects, and two checkers. It does not publish the vault. Its git history is separate from the vault's, so no vault content exists at any commit. Treat it as public.

## Commands

Run 2026-11-15, local Python 3.14.4 (CI uses 3.12):

- `python3 scripts/leak_guard.py` -> `leak guard: clean`, exit 0.
- `python3 scripts/check_frontmatter.py` -> not run to completion: needs PyYAML, which is not installed here (`ModuleNotFoundError: yaml`). CI runs it after `pip install pyyaml`. Result unverified locally.

CI (`.github/workflows/validate.yml`) runs both on every push and pull request.

## Layout

- `OPERATING-MANUAL.md`: schema and workflow doc for the maintaining agent.
- `CONTENT-BOUNDARY.md`: what is and is not published; read before adding files.
- `reference/`, `docs/`: governance, metadata schema, architecture explainers.
- `playbooks/`: coding-agent playbooks and retrieval packs.
- `bases/`, `templates/`, `schemas/`: Obsidian Bases, page templates, schemas.
- `examples/`, `samples/`: public example pages and samples.
- `scripts/`: `leak_guard.py`, `check_frontmatter.py`, `corpus_health.py`, `build_index.py`, `sync_from_vault.py`.
- `scripts/scrub_rules.py` is gitignored (local rules); never commit it. `scrub_rules.example.py` is the tracked template.

## Content boundary

From `CONTENT-BOUNDARY.md`. The repo publishes the system, not the vault.

- Included: operating manual; metadata schema, governance contract, review gates, contradiction protocol; routing (question router, agent entry, retrieval packs); agent behavior cards and playbooks; Bases definitions and templates; twelve example cards on public technical subjects; the corpus health checker and leak guard.
- Excluded: `raw/` (every PDF, EPUB, paper, book); source summaries and chapter notes from copyrighted works; first-party research (factor models, signal registers, backtest receipts); health, financial, relationship, family, career, and employer material; local project context manifests and absolute filesystem paths; any full or partial vault export.
- The boundary is structural: a `.gitignore` rule would not help because git history is permanent, so this repo has its own history.
- Enforcement: `scripts/leak_guard.py` fails on forbidden terms (personal, health, financial, employer, private project names), vault-shaped patterns (wikilinks and `sources:` frontmatter pointing into the vault's raw-sources folder; the exact patterns are in the script, and quoting them in a tracked file, this one included, fails the check), and credential shapes (GitHub tokens, API keys, bearer tokens). Never weaken or bypass it.
- Do not paste vault notes, paths, or terms into any file here, including this one.

## Git

Conventional commits. Commit to main. Ask before pushing — this repo is public.
