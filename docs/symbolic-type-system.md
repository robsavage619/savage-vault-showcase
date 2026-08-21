---
type: overview
title: "Symbolic Type System"
summary: "Machine-readable role system for corpus pages, claims, evidence, routers, rules, and validation reports. Gives agents a compact way to reason about what each page is allowed to do."
tags: [meta, symbolic, schema]
sources: []
created: 2026-08-08
updated: 2026-08-08
status: active
aliases: ["symbolic schema", "symbolic layer", "type system"]
related: ["[[metadata-schema]]", "[[symbolic-validation-rules]]", "[[corpus-governance]]", "[[corpus-agent-evaluation-suite]]"]
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

# Symbolic Type System

## Summary

This page defines symbolic roles for the vault. The fields are optional for legacy notes, but new operating, review, retrieval, and validation pages should use them when they need machine-checkable behavior. The type system helps agents distinguish sources, claims, routers, rules, and administrative reports.

## Symbolic Roles

| Role | Meaning |
|---|---|
| `router` | Directs retrieval or workflow selection |
| `rule` | Defines a constraint agents must apply inside the vault task |
| `schema` | Defines frontmatter or structure |
| `evidence` | Summarizes a source or source family |
| `claim` | Stores a claim requiring evidence and applicability limits |
| `retrieval-pack` | Curated reading order for a recurring question class |
| `validation-report` | Snapshot of corpus health |

## Claim Types

| Claim type | Standard |
|---|---|
| `descriptive` | Says what a source, concept, or system is |
| `causal` | Says X changes Y; needs stronger support |
| `predictive` | Forecasts future behavior or outcomes |
| `prescriptive` | Recommends action; requires high-stakes guard |
| `normative` | Encodes values or priorities |
| `methodological` | Defines how to measure, evaluate, or build something |

## Evidence Lanes

- `orientation`: safe for navigation and rough mental models.
- `working-synthesis`: safe for draft reasoning with caveats.
- `decision-grade`: reviewed enough for recommendation support.
- `admin`: controls the corpus but is not domain evidence.

## See Also

- [[symbolic-validation-rules]]
- [[metadata-schema]]
