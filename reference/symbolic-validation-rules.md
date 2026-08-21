---
type: overview
title: "Symbolic Validation Rules"
summary: "Validation rules that agents should apply when using symbolic fields and decision-grade metadata. Converts the governance layer into checkable behavior for retrieval, review, and answer generation."
tags: [meta, symbolic, validation, agent]
sources: []
created: 2026-08-08
updated: 2026-08-08
status: active
aliases: ["symbolic rules", "validation rules", "agent validation rules"]
related: ["[[symbolic-type-system]]", "[[metadata-schema]]", "[[corpus-governance]]", "[[source-fidelity-review-gate]]", "[[claim-conflict-protocol]]"]
confidence: high
domains: [governance]
source_kind: meta
authority_level: administrative
evidence_level: administrative
validation_status: validated
fidelity_status: not-applicable
index_eligible: true
retrieval_priority: high
symbolic_role: rule
evidence_lane: admin
requires_review: false
---

# Symbolic Validation Rules

## Summary

These rules convert the maturity layer into agent behavior. Agents should apply them before treating a page as canonical evidence, especially in health, investing, career, finance, and training contexts. A rule failure does not delete the page; it changes how confidently the page may be used.

## Rules

| Rule | Failure response |
|---|---|
| High-stakes answer uses `legacy-unreviewed` evidence | State limitation and avoid prescriptive conclusion |
| `source-summary` has no source path or external-source note | Route to source-fidelity review |
| `fidelity_status: abstract-only` plus prescriptive language | Treat as orientation-only |
| `validation_status: disputed` | Name the dispute and cite both sides |
| Missing `summary`, `type`, `sources`, or `updated` | Do not promote to canonical retrieval |
| Broken wikilink in a required See Also section | Add to gap register before promotion |
| Stale fast-moving topic | Check updated date and prefer newer evidence |
| `prohibited_use` matches the user's requested action | Decline that use and offer safer framing |

## Answer Policy

When a rule fails, the agent can still help. The answer should be framed as "the vault suggests," "this source reports," or "for orientation," not as final instruction.

## See Also

- [[source-fidelity-review-gate]]
- [[corpus-agent-judge-rubric]]
