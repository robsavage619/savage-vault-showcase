---
type: overview
title: "Index Promotion Manifest"
summary: "Rules for deciding whether a page belongs in the canonical retrieval surface. Prevents legacy, draft, abstract-only, or high-stakes unreviewed notes from being treated as fully mature evidence."
tags: [meta, governance, retrieval]
sources: []
created: 2026-08-08
updated: 2026-08-08
status: active
aliases: ["index eligibility", "promotion manifest", "retrieval promotion"]
related: ["[[corpus-governance]]", "[[metadata-schema]]", "[[source-fidelity-review-gate]]", "[[question-router]]"]
confidence: high
domains: [governance, retrieval]
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

# Index Promotion Manifest

## Summary

This manifest defines when a page is eligible for canonical retrieval. It preserves the current index files as useful navigation artifacts while adding an explicit maturity gate for decision-grade answers. A page may be readable and linked while still being ineligible for final authority.

## Eligibility Levels

| Level | Meaning | Allowed use |
|---|---|---|
| `canonical` | Reviewed, source traceable, current, and cross-linked | Normal answers and decision support |
| `working` | Good summary but missing full validation | Draft synthesis and routing |
| `legacy-unreviewed` | Created before the maturity layer or missing decision-grade fields | Discovery and orientation |
| `quarantine` | Known conflict, stale source, or unsupported prescription | Do not use without human review |

## Promotion Criteria

A page is `canonical` when:

- `status: active`
- `validation_status: reviewed` or `validated`
- `fidelity_status` is suitable for the source type
- `sources:` is non-empty unless the page is a synthetic overview, analysis, governance page, or first-party finding
- `## Summary` exists and matches the frontmatter summary in substance
- all material internal links resolve, or unresolved future topics are written as plain text under a gap section
- high-stakes prescriptions have applicability limits and prohibited-use notes

## Demotion Criteria

Set `index_eligible: false` or route to review when:

- the page is abstract-only but makes strong practical recommendations
- claims conflict with another source and the contradiction is not documented
- source files are missing
- updated date is stale for fast-moving topics
- the note is a placeholder, empty stub, or seed list with no synthesis

## Current Standing

As of **corpus-validation-report**, most legacy pages are usable for routing and synthesis but have not been upgraded to the full decision-grade schema. The live Bases are the current way to see promotion candidates.

## See Also

- [[source-fidelity-review-gate]]
- [[claim-conflict-protocol]]
- **corpus-gap-register**
