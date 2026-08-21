---
type: overview
title: "Template Catalog"
summary: "Catalog of reusable Obsidian templates for the savage_vault maturity layer. Points humans and agents to source-summary, book-overview, research-finding, project-context-manifest, and weekly-corpus-review templates."
tags: [meta, templates, governance]
sources: []
created: 2026-08-08
updated: 2026-08-16
status: active
aliases: ["vault templates", "template catalog"]
related: ["[[metadata-schema]]", "[[corpus-governance]]"]
confidence: high
domains: [governance]
source_kind: meta
authority_level: administrative
evidence_level: administrative
validation_status: validated
fidelity_status: not-applicable
index_eligible: true
retrieval_priority: high
symbolic_role: schema
evidence_lane: admin
requires_review: false
---

# Template Catalog

## Summary

The vault uses a small template set for repeated note types. Templates live in `_templates/`, and Obsidian's core Templates plugin is configured to use that folder.

## Templates

| Template | Use |
|---|---|
| `_templates/source-summary.md` | New source notes backed by a paper, book chapter, web source, or raw file. |
| `_templates/book-overview.md` | Book hubs that point to chapter/source-summary notes. |
| `_templates/research-finding.md` | Rob's first-party empirical tests and experiments. |
| `_templates/project-context-manifest.md` | Agent-facing project cards for `~/Projects`. |
| `_templates/weekly-corpus-review.md` | Weekly health review of links, sources, Bases, review queue, and project context. |

## Rules

- Templates are scaffolds, not authority.
- New wiki pages still need complete frontmatter before promotion.
- Local raw source files must use quoted Obsidian wikilinks to the raw file.
- `project-context-manifest` pages should be reviewed against live project files before an agent uses them to edit code.

## See Also

- [[metadata-schema]]
- **project-context-manifests**
- **corpus-validation-report**
