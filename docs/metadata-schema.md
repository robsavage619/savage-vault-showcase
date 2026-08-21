---
type: overview
title: "Metadata Schema"
summary: "Extended frontmatter schema for the savage_vault wiki. Preserves the existing required fields while adding maturity, evidence, retrieval, and review fields for decision-grade corpus behavior."
tags: [meta, schema, governance]
sources: []
created: 2026-08-08
updated: 2026-08-08
status: active
aliases: ["vault metadata", "frontmatter schema", "wiki schema"]
related: ["[[corpus-governance]]", "[[index-promotion-manifest]]", "[[source-fidelity-review-gate]]", "[[symbolic-type-system]]", "[[symbolic-validation-rules]]"]
confidence: high
domains: [governance]
source_kind: meta
authority_level: administrative
evidence_level: administrative
validation_status: validated
fidelity_status: not-applicable
index_eligible: true
retrieval_priority: critical
symbolic_role: schema
evidence_lane: admin
requires_review: false
---

# Metadata Schema

## Summary

This page extends the wiki frontmatter schema without breaking the existing vault. The original fields remain required for every wiki page; the new fields add evidence maturity, retrieval priority, index eligibility, and review semantics. Notes missing the new fields are legacy-unreviewed until a review pass upgrades them.

## Required Legacy Fields

Every page in `wiki/` still requires:

```yaml
type: source-summary | entity | concept | comparison | analysis | overview | book-overview | research-finding | project-context-manifest | corpus-review
title: "Human-readable title"
summary: "Self-contained 2-3 sentence summary."
tags: [tag]
sources: ["raw/<file>.pdf as a quoted Obsidian raw-file wikilink"]
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: draft | active | stale | needs-review
```

## Decision-Grade Fields

Add these when a page is created or materially reviewed:

```yaml
domains: [ai-engineering, exercise-science, sleep-science, sabermetrics, quantitative-finance, career, decision-science]
source_kind: primary-study | review | book | benchmark | first-party-analysis | synthesis | reference | meta
authority_level: primary | secondary | tertiary | synthetic | administrative
evidence_level: direct | indirect | mechanistic | expert-opinion | anecdotal | administrative
validation_status: unreviewed | reviewed | validated | disputed | deprecated
fidelity_status: unreviewed | abstract-only | source-checked | quote-checked | full-text-checked | not-applicable
index_eligible: true | false
retrieval_priority: critical | high | normal | low | archive
approved_use: ["orientation", "draft-synthesis", "decision-support"]
prohibited_use: ["medical-advice", "financial-advice", "standalone-prescription"]
review_due: YYYY-MM-DD
```

## Interpretive Rules

- `confidence` is a local judgment about the page's synthesis, not proof that source fidelity passed.
- `validation_status` is the review state that controls decision-grade use.
- `fidelity_status: abstract-only` must be obvious in the body when the full text was not checked.
- `index_eligible: false` means the page can exist in the graph but should not be treated as part of the canonical retrieval surface.
- Missing decision-grade fields imply `validation_status: unreviewed` and `index_eligible: false` for high-stakes use.
- `sources` should use quoted Obsidian links for local raw files so attachments remain clickable and visible to Obsidian's link graph.

## Symbolic Fields

Machine-checkable pages may also use:

```yaml
symbolic_role: router | rule | schema | evidence | claim | retrieval-pack | validation-report | project-context
claim_type: descriptive | causal | predictive | prescriptive | normative | methodological
evidence_lane: orientation | working-synthesis | decision-grade | admin
requires_review: true | false
review_owner_role: human | agent | domain-expert
applies_when: "Plain-language condition."
failure_mode: "What goes wrong if this is misused."
```

## Project Context Fields

`project-context-manifest` pages also use:

```yaml
project_path: "~/Projects/project-name"
project_status: active | reference | thin | stale
stack: [python, react]
agent_entry: "CLAUDE.md"
repo_kind: "short-kind"
```

These fields are routing hints only. Agents must still inspect the live project before making claims or edits.

## See Also

- [[corpus-governance]]
- [[source-fidelity-review-gate]]
- [[symbolic-validation-rules]]
