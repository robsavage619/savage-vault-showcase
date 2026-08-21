---
type: overview
title: "Source Fidelity Review Gate"
summary: "Review procedure for upgrading vault notes from useful summaries to validated evidence. Defines what must be checked for raw files, abstracts, web-only sources, books, and synthesized pages before decision-grade use."
tags: [meta, governance, evidence, review]
sources: []
created: 2026-08-08
updated: 2026-08-08
status: active
aliases: ["fidelity gate", "source review gate", "evidence review"]
related: ["[[corpus-governance]]", "[[metadata-schema]]", "[[index-promotion-manifest]]", "[[claim-conflict-protocol]]"]
confidence: high
domains: [governance, evidence]
source_kind: meta
authority_level: administrative
evidence_level: administrative
validation_status: validated
fidelity_status: not-applicable
index_eligible: true
retrieval_priority: critical
symbolic_role: rule
evidence_lane: admin
requires_review: false
---

# Source Fidelity Review Gate

## Summary

This gate defines how a note becomes validated evidence. It is stricter than the old `confidence` field: the reviewer must check whether the page accurately represents its cited source, whether the source is strong enough for the claim, and whether limitations are visible. Abstract-only and web-only notes can be useful, but they cannot silently become decision-grade.

## Review Steps

1. Verify every `sources:` path exists, or record why the source is external.
2. Check that the frontmatter summary matches the page body.
3. Compare key claims against the source text, not memory.
4. Mark the evidence level and fidelity status.
5. Add limitations for population, sample size, measurement, domain, or time horizon.
6. Search nearby pages for contradictions.
7. Promote, demote, or send to [[claim-conflict-protocol]].

## Fidelity Status

| Status | Meaning |
|---|---|
| `unreviewed` | No fidelity check has been recorded |
| `abstract-only` | Summary is based on abstract, database snippet, or limited metadata |
| `source-checked` | Main source was opened and checked against the page |
| `quote-checked` | Specific quoted or numeric claims were checked |
| `full-text-checked` | Full source text was reviewed enough for high confidence |
| `not-applicable` | Administrative or synthetic page with no external source |

## High-Stakes Guard

If a page affects health, training, investing, finance, or career decisions, do not answer as if the claim is prescriptive unless the page is validated and limitations are clear. Otherwise, answer as evidence-informed orientation and say what would need review.

## See Also

- [[metadata-schema]]
- [[index-promotion-manifest]]
- [[corpus-agent-judge-rubric]]
