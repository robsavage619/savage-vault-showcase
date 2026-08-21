---
type: overview
title: "Corpus Governance"
summary: "Operating contract for the savage_vault wiki as a personal knowledge corpus. Defines maturity levels, decision-grade use, review gates, and the difference between active notes and validated evidence."
tags: [meta, governance, agent]
sources: []
created: 2026-08-08
updated: 2026-08-08
status: active
aliases: ["vault governance", "personal corpus governance", "corpus operating contract"]
related: ["[[metadata-schema]]", "[[index-promotion-manifest]]", "[[source-fidelity-review-gate]]", "[[question-router]]", "[[claim-conflict-protocol]]"]
confidence: high
domains: [governance]
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

# Corpus Governance

## Summary

This page is the operating contract for the savage_vault wiki as a personal knowledge corpus. It separates editorial completeness from evidentiary maturity, so agents can use the vault for orientation without treating every legacy note as decision-grade truth. The goal is research-lab-style behavior: explicit routing, source fidelity, contradiction handling, index eligibility, evaluation cases, and validation reports.

## Maturity Contract

`status: active` means a page is readable, cross-linked, and complete enough to appear in normal navigation. It does not mean the page has passed source-fidelity review.

Decision-grade use requires the page or claim to satisfy all of these:

- Frontmatter includes `validation_status: validated` or `reviewed`.
- Source-backed claims point to `sources:` or explain why the page is synthetic.
- High-stakes health, investing, career, and financial claims include caveats, applicability limits, and enough provenance for a human to inspect.
- Contradictions are routed through [[claim-conflict-protocol]].
- The page is eligible under [[index-promotion-manifest]].

Legacy notes missing the newer maturity fields are treated as `legacy-unreviewed`. They may be used for discovery, orientation, search routing, and draft synthesis, but not as final authority for high-stakes prescriptions.

## Review Lanes

| Lane | Use | Minimum standard |
|---|---|---|
| `orientation` | Finding concepts, sources, and likely pages | Required frontmatter and readable summary |
| `working-synthesis` | Draft answers and exploratory synthesis | Sources checked at page level; uncertainty stated |
| `decision-grade` | Recommendations that change training, money, career, or health behavior | Validated source fidelity, limitations, and contradiction check |
| `admin` | Schema, routers, Bases, evals, validation reports | Internally coherent and linked from entry points |

## High-Stakes Rule

The vault can inform decisions, but it is not a medical, legal, or financial authority. For training, nutrition, sleep, investing, and career choices, agents must say when evidence is incomplete, population-specific, stale, or outside the user's context.

## Operating Pages

- [[question-router]] decides what to read first.
- [[metadata-schema]] defines current and legacy frontmatter.
- [[index-promotion-manifest]] controls index eligibility.
- [[source-fidelity-review-gate]] defines how claims become validated.
- [[claim-conflict-protocol]] handles contradictory claims.
- [[symbolic-type-system]] and [[symbolic-validation-rules]] define machine-checkable roles.
- [[corpus-agent-evaluation-suite]] and [[corpus-agent-judge-rubric]] define agent performance checks.
- **corpus-validation-report** records the latest health check.

## See Also

- [[agent-entry]]
- **index**
- **index-short**
