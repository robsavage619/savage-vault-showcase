"""Template for scripts/scrub_rules.py, which is intentionally not committed.

The real file names the private domains, project codenames, and personal
material that must not reach the public repository — which is precisely why
publishing it would defeat the purpose. Copy this file, rename it to
`scrub_rules.py`, and fill it in against your own vault.

Three phases, applied in this order by `sync_from_vault.transform`:

1. `PRE_REWRITES` — literal replacements on the raw page, before line dropping.
   Use these to neutralize a line in place that would otherwise be deleted
   wholesale (a `summary:` field mentioning a private template, for example).
2. `DROP_LINES` — any line containing one of these markers is removed, except
   frontmatter `related:` lines, which are filtered by allowlist instead.
3. `REWRITES` — literal replacements after link normalization, so they can match
   the `**bolded**` forms that unresolved wikilinks become.
"""

from __future__ import annotations

DROP_LINES = (
    "private-domain-operating-card",
    "| private-tag |",
)

PRE_REWRITES = (
    ("a summary line naming a private template", "a neutral summary line"),
)

REWRITES = (
    ("an absolute home path", "~"),
    ("**private-project-context-manifest**", "a representative project"),
)
