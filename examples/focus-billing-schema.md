---
type: concept
title: "FOCUS Billing Schema"
summary: "The vendor-neutral schema for technology billing data: four datasets and a normalized cost vocabulary — Billed, Effective, List and Contracted Cost — that removes per-provider normalization from FinOps work. Billed vs Effective is the distinction behind most 'our numbers don't match' disputes between finance and engineering."
tags: [finops, cloud-cost, standards, schema, billing, data-contracts, cost-allocation]
sources: []
created: 2026-08-19
updated: 2026-08-19
status: active
aliases: ["FOCUS schema", "billed vs effective cost", "amortized cost", "normalized billing data", "what is effective cost", "cross-cloud cost comparison", "charge category"]
related: ["[[finops-capability-model]]", "[[unit-economics-cost-per-outcome]]", "[[retrieval-pack-finops-cost-engineering]]"]
confidence: high
domains: [finops, data-engineering]
source_kind: synthesis
authority_level: synthetic
evidence_level: administrative
validation_status: reviewed
fidelity_status: source-checked
index_eligible: true
retrieval_priority: high
---

# FOCUS Billing Schema

## Summary

FOCUS defines a common schema for billing data across cloud, SaaS, data-centre and other technology providers (**focus-2026-v1-4-finops-open-cost-usage-spec**). Four datasets — **Cost and Usage**, **Billing Period**, **Contract Commitment**, **Invoice Detail** — plus a normalized cost vocabulary. Its purpose is to eliminate the **best-effort custom normalization scheme per provider** that every practitioner otherwise has to build before doing any allocation, chargeback, budgeting or forecasting.

## The Four Costs

This is the part worth memorizing, because the distinctions are where cost conversations go wrong.

- **Billed Cost** — what the invoice issuer charged in a given **billing period**. For usage charges it *excludes* any portion covered by a prepaid commitment; for purchase charges it *includes* whatever was invoiced this period.
- **Effective Cost** — what was actually consumed or recognized in a given **charge period**, including the amortized portion of prepayments and commitment drawdowns.
- **List Cost** — list unit price × pricing quantity. The undiscounted counterfactual.
- **Contracted Cost** — contracted unit price × pricing quantity. What the negotiated rate implies.

Billed and Effective diverge precisely when **covering charges are recorded separately from the charges they cover**. A three-year reservation bought in January shows as a large Billed Cost in January and near-zero afterwards, while Effective Cost spreads it across the periods that consumed it.

## Why It Matters

**It settles arguments.** Finance quotes Billed (it matches the invoice and the cash), engineering quotes Effective (it matches what the workload used). Both are right, they disagree by the amortization, and without shared definitions the disagreement is unresolvable. Naming both in one schema is what makes it a reconciliation instead of a fight.

**It makes cross-provider comparison meaningful.** Comparing an AWS bill to an Azure bill previously meant reconciling two proprietary schemas with different words for the same things. FOCUS is the shared denominator.

**Charge Class matters more than it looks.** It flags whether a row is a **correction to a previously closed billing period**. Any cost pipeline assuming closed periods are immutable is wrong, and this column is how you find out. Related: Charge Category (the highest-level classification of a charge), Charge Frequency, and Charge Period Start/End with an exclusive end bound.

**It is a data contract.** A versioned, published producer-consumer interface — exactly the artifact **jones-2023-ch2-data-contract-interface** argues for, and it deserves the same schema-evolution discipline (**schema-evolution-contracts**).

## Perspectives

A schema is not an implementation. Provider FOCUS exports vary in conformance and completeness, which is why the spec defines feature levels; v1.4 was ratified in June 2026 and tooling lags ratification.

FOCUS normalizes billing data only. It carries no notion of business value, workload attribution beyond what the provider tags, or unit-economics denominators — those live in the capability model ([[finops-capability-model]]), not the schema. Getting normalized cost data is the beginning of FinOps, not the end.

## Related Concepts

- [[finops-capability-model]] — the practice this schema serves
- [[unit-economics-cost-per-outcome]] — what you build on top of it
- **data-contract-boundary** · **source-of-truth**

## See Also

- **focus-2026-v1-4-finops-open-cost-usage-spec**
- [[retrieval-pack-finops-cost-engineering]]
