---
type: project-context-manifest
title: "Redacted Project Manifest Example"
summary: "Synthetic example of a project manifest that tells agents what to inspect before advising on or editing a repository."
tags: [example, project-manifest, coding-agents]
sources: []
created: 2026-08-09
updated: 2026-08-09
status: active
aliases: ["example project manifest"]
related: ["[[operating-card-redacted]]"]
confidence: high
domains: [example-domain]
source_kind: meta
authority_level: administrative
evidence_level: administrative
validation_status: validated
fidelity_status: not-applicable
index_eligible: true
retrieval_priority: high
symbolic_role: project-manifest
evidence_lane: admin
requires_review: false
---

# Redacted Project Manifest Example

## Hard Stop

Do not modify code until the exact repository is named and live files have been inspected.

## Read First

- `README.md`
- agent instructions, if present
- package/config files
- source entry points
- tests and fixtures
- CI validation commands

## Validation

Report exactly what passed, what was not run, and what remains uncertain.

