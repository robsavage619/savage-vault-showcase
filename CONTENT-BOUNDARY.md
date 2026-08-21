# Content Boundary

This repository publishes the **system** that maintains a personal knowledge vault. It does not publish the vault.

## Why the boundary is structural, not a `.gitignore`

The vault's own git history contains private material — relationship notes, health data, first-party financial research, personal project context. Adding an ignore rule to that repository would not help, because git history is permanent: the files exist in every prior commit.

So this repository has **an entirely separate git history**. No corpus content exists here at any commit, and none ever did.

## Included

- The operating manual the maintaining agent reads first
- Metadata schema, governance contract, review gates, contradiction protocol
- Routing: question router, agent entry point, retrieval packs
- Agent behavior cards and task playbooks
- Obsidian Bases definitions and page templates
- Twelve example concept cards, all on public technical subjects
- A corpus health checker and a leak guard

## Excluded

- `raw/` — every PDF, EPUB, paper, and book
- Source summaries and chapter notes derived from copyrighted works
- First-party research: factor models, signal registers, backtest receipts
- Health, financial, relationship, family, career, and employer material
- Local project context manifests and absolute filesystem paths
- Any full or partial vault export

## Enforcement

`scripts/leak_guard.py` fails the build on forbidden terms — personal, health, financial, employer, and private project names — plus structural patterns that indicate vault content (`[[raw/` links, `sources:` frontmatter pointing at raw files) and credential shapes (GitHub tokens, API keys, bearer tokens).

It runs on every push and pull request via `.github/workflows/validate.yml`. The guarantee is therefore a test, not a promise, and it survives edits made after this file was written.

Example pages are additionally checked for frontmatter validity and unresolved wikilinks by `scripts/check_frontmatter.py`.
