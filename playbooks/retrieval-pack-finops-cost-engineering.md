---
type: overview
title: "Retrieval Pack: FinOps and Cost Engineering"
summary: "Routing pack for cloud cost, AI cost, unit economics, billing-data, and cost-architecture questions. Routes to the FOCUS schema for cost definitions, the FinOps capability model for practice questions, unit economics for 'is this reasonable', and architecture pages for structural cost drivers."
tags: [meta, retrieval, finops, cloud-cost, ai-cost, unit-economics]
sources: []
created: 2026-08-19
updated: 2026-08-19
status: active
aliases: ["FinOps retrieval pack", "cloud cost pack", "cost engineering pack", "AI cost pack"]
related: ["[[question-router]]", "[[finops-capability-model]]", "[[focus-billing-schema]]", "[[unit-economics-cost-per-outcome]]", "[[retrieval-pack-ai-engineering]]", "[[coding-agent-data-system-playbook]]"]
confidence: high
domains: [finops, retrieval, governance]
source_kind: meta
authority_level: administrative
evidence_level: administrative
validation_status: validated
fidelity_status: not-applicable
index_eligible: true
retrieval_priority: critical
symbolic_role: retrieval-pack
evidence_lane: admin
requires_review: false
---

# Retrieval Pack: FinOps and Cost Engineering

## Summary

Use this pack for cloud cost, AI/token cost, billing data, unit economics, chargeback, commitment strategy, and cost-driven architecture questions. It separates the **standards layer** (what the data and the practice are defined to be) from the **practice layer** (how the books say to do it), because most cost questions are actually definition questions wearing a practice costume.

## Routing

| Question type | Start here | Escalate to |
|---|---|---|
| "What did this cost?" / billed vs amortized | [[focus-billing-schema]] | **focus-2026-v1-4-finops-open-cost-usage-spec** for exact column semantics |
| Cross-provider cost comparison, billing pipelines | [[focus-billing-schema]] | **jones-2023-ch2-data-contract-interface** · **schema-evolution-contracts** |
| "What should our practice be doing?" / maturity | [[finops-capability-model]] | **finops-2026-framework-domains-capabilities** |
| Commitments, reservations, rate strategy | [[finops-capability-model]] (Rate Optimization) | **storment-fuller-2020-cloud-finops** · **chung-2022-aws-finops-simplified** |
| Rightsizing, waste, scheduling | [[finops-capability-model]] (Usage Optimization) | **sanchez-garcia-2024-efficient-cloud-finops** |
| "Is this spend reasonable?" / KPIs | [[unit-economics-cost-per-outcome]] | **decision-oriented-measurement** · **proxy-metric-validity** |
| AI / token / agent cost | [[unit-economics-cost-per-outcome]] | **koenigstein-2026-ch11-agent-cost-efficiency** · [[test-time-compute-scaling]] |
| Model choice under a cost budget | [[test-time-compute-scaling]] | **snell-2024-scaling-test-time-compute** · **llm-selection-framework** |
| Data-platform cost structure | [[lakehouse-architecture]] | **armbrust-2021-lakehouse-architecture** · [[acid-table-storage-layer]] |
| Local project cost work | **project-finops-landing-context-manifest** | the live repo |

## Use Rules

- **Fix definitions before arguing about numbers.** Billed vs Effective Cost resolves most cross-team disagreements; do that first.
- **Separate rate from usage optimization.** They have different owners, different evidence and different ceilings. Blending them hides that a program has plateaued.
- **Never cite the FinOps Framework as causal evidence.** It is `evidence_level: administrative` — an industry consensus operating model. It says what a practice should contain, not that any capability produces savings.
- **Always name the denominator.** A cost figure without a unit is not an answer. If no meaningful denominator exists, say so rather than inventing one.
- **Price AI accuracy, don't assume it.** Reasoning models buy accuracy with tokens; the honest comparison is an accuracy-versus-tokens curve, not a per-call price.
- **Check spec recency.** FOCUS v1.4 was ratified 2026-06-04 and provider exports lag ratification. Verify a column exists in the actual export before relying on it.

## See Also

- **overview-finops-cost-engineering**
- [[question-router]]
- [[retrieval-pack-ai-engineering]]
