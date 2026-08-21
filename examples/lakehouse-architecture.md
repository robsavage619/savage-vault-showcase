---
type: concept
title: "Lakehouse Architecture"
summary: "One governed storage tier in open formats serving both BI and ML, replacing the two-tier lake-plus-warehouse pattern. Targets data staleness from ETL lag, duplicated storage cost, lock-in, and the governance failure of BI and ML computing from different copies of the data."
tags: [data-engineering, architecture, lakehouse, data-warehouse, ml-engineering, cloud-cost, software-engineering]
sources: []
created: 2026-08-19
updated: 2026-08-19
status: active
aliases: ["lakehouse", "data lake vs warehouse", "two tier data architecture", "why is my BI data stale", "one copy of the data", "open direct access formats"]
related: ["[[acid-table-storage-layer]]", "[[finops-capability-model]]", "[[coding-agent-data-system-playbook]]"]
confidence: high
domains: [data-engineering, architecture, ml-engineering]
source_kind: synthesis
authority_level: synthetic
evidence_level: expert-opinion
validation_status: reviewed
fidelity_status: source-checked
index_eligible: true
retrieval_priority: normal
---

# Lakehouse Architecture

## Summary

A single storage tier in **open direct-access formats** (Parquet, ORC) with warehouse-grade transactions and performance layered on, serving BI and machine learning from the same governed copy. Proposed in **armbrust-2021-lakehouse-architecture** as the third generation of analytics platforms, and made technically possible by [[acid-table-storage-layer]].

## The Three Generations

**First — the data warehouse.** Schema-on-write, optimized for BI. Coupled compute and storage in an appliance, forcing enterprises to provision and pay for **peak** load and peak data volume. Could not store or query unstructured data at all.

**Second — the data lake.** Offload everything raw into cheap file-API storage in open formats. Fixes cost and unstructured data; loses transactions, reliability and governance. In practice organizations ran **both**, with ETL from lake to warehouse.

**Third — the lakehouse.** One tier, open formats, transactions on top.

## The Problem With Two Tiers

The duplication is the point, and each cost is separate.

**Staleness.** The warehouse is always behind the lake by one pipeline. Every "why doesn't this dashboard match" conversation starts here.

**Double storage cost**, plus the compute cost of the ETL that keeps the copies in sync.

**Divergence.** Data scientists read the lake tier directly because that is where the raw and unstructured data live; BI reads the warehouse. ML and BI are therefore computed from **different data**, and no amount of dashboard governance fixes it. This is a governance failure at least as much as a cost one — see **source-of-truth**.

**Lock-in.** Proprietary warehouse storage formats make exit expensive; open direct-access formats are the structural answer.

## Why It Matters

**Architecture is where the largest cost decisions get made and the hardest to reverse.** Paying for peak provisioned capacity, paying twice for storage, and paying for inter-tier ETL are all **Architecting & Workload Placement** decisions in [[finops-capability-model]] terms — the capability with the highest ceiling and the longest lead time.

**One governed copy is the durable win.** Cheaper is nice; having BI and ML agree is what changes how an organization argues about numbers.

**The pattern scales down.** Parquet on object storage plus a table format gives most of the benefit at any size, which is why DuckDB-plus-Parquet setups are lakehouses in miniature — the shape of a single-analyst analytics stack.

## Perspectives

The source is a vendor-authored position paper at an ideas venue, and its central prediction — that the warehouse architecture would **wither** — has not happened as stated. What happened instead is convergence: cloud warehouses adopted open table formats and external tables, lakehouses improved governance, and the categories blurred. The *arguments* proved more durable than the forecast.

TPC-DS competitiveness is a warehouse benchmark and a contested proxy for real workloads. Governance, fine-grained access control and high-concurrency BI remain the areas where warehouse products retain genuine advantages, and the original paper treats them lightly.

## Related Concepts

- [[acid-table-storage-layer]] — the enabling mechanism
- **source-of-truth** · **data-contract-boundary**
- [[finops-capability-model]] — where architecture sits as a cost capability

## See Also

- **armbrust-2021-lakehouse-architecture**
- **reis-housley-2022-fundamentals-data-engineering**
- [[coding-agent-data-system-playbook]]
