---
type: overview
title: "Claim Conflict Protocol"
summary: "Protocol for representing contradictions, uncertainty, and competing claims in the vault. Requires agents to preserve conflicts, cite both sides, and route disputed pages to review instead of silently resolving disagreements."
tags: [meta, governance, contradictions]
sources: []
created: 2026-08-08
updated: 2026-08-08
status: active
aliases: ["contradiction protocol", "claim conflict register", "conflict handling"]
related: ["[[corpus-governance]]", "[[source-fidelity-review-gate]]", "[[index-promotion-manifest]]", "[[symbolic-validation-rules]]"]
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

# Claim Conflict Protocol

## Summary

This protocol keeps disagreements visible. When two pages or sources conflict, agents must preserve both claims, mark the uncertainty, and route the affected pages to review. The correct behavior is not to average competing claims into a bland middle.

## Conflict Types

| Type | Example |
|---|---|
| empirical | studies report different effect sizes or directions |
| methodological | sources use incompatible definitions or measurement windows |
| applicability | claim holds for trained athletes but not novices |
| temporal | older source is superseded by newer evidence or rules |
| normative | sources optimize for different goals |

## Required Handling

When a conflict is found:

- Add a `## Contradictions & Debates` section to the relevant concept, analysis, or overview page.
- Cite both pages with wikilinks.
- Explain the likely reason for disagreement if known.
- Set `validation_status: disputed` or `status: needs-review`.
- Add `contradicted` to tags.
- Add the issue to **corpus-gap-register** or the claim-conflict Base.

## Answering Rule

Agents may answer from disputed material only if they name the dispute and avoid a single confident recommendation. For high-stakes domains, disputed evidence is orientation-only until reviewed.

## See Also

- [[source-fidelity-review-gate]]
- [[corpus-agent-judge-rubric]]
