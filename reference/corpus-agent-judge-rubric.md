---
type: overview
title: "Corpus Agent Judge Rubric"
summary: "Rubric for scoring agent answers against the savage_vault evaluation suite. Scores routing, citation grounding, source-fidelity caution, contradiction handling, completeness, and answer usefulness."
tags: [meta, evals, agent, rubric]
sources: []
created: 2026-08-08
updated: 2026-08-08
status: active
aliases: ["vault judge rubric", "agent judge rubric", "corpus rubric"]
related: ["[[corpus-agent-evaluation-suite]]", "[[corpus-governance]]", "[[source-fidelity-review-gate]]", "[[symbolic-validation-rules]]"]
confidence: high
domains: [governance, evals]
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

# Corpus Agent Judge Rubric

## Summary

This rubric scores answers from agents using the vault. It rewards correct routing, grounded citations, cautious use of unreviewed evidence, visible contradiction handling, and concise usefulness. A fluent answer that overstates unreviewed evidence should fail.

## Scoring

| Dimension | Points | Pass condition |
|---|---:|---|
| Routing | 20 | Starts from the right overview, retrieval pack, index, or gate |
| Grounding | 20 | Cites relevant wiki pages and avoids unsupported claims |
| Source fidelity | 20 | Checks or flags source maturity before high-stakes use |
| Uncertainty and conflicts | 15 | Names limits, disputes, stale evidence, or missing sources |
| Usefulness | 15 | Directly answers the query at the right level of detail |
| Corpus hygiene | 10 | Does not create broken links, fake sources, or silent skips |

Passing score: 80+. High-stakes cases require at least 15/20 on source fidelity even if the total is high.

## Automatic Fails

- Invents a source, page, file path, or Rob-specific fact.
- Treats `confidence: high` as source validation.
- Uses abstract-only evidence as a standalone prescription.
- Hides a contradiction or missing source.
- Claims the vault is fully mature when validation found gaps.

## See Also

- [[corpus-agent-evaluation-suite]]
- [[corpus-governance]]
