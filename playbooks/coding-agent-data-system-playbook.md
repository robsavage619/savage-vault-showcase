---
type: analysis
title: "Coding-Agent Data-System Playbook"
summary: "Data-system playbook for coding agents working on Rob's FinOps, analytics, retrieval, and dashboard projects. It separates sources of truth from derived data, operational from analytical workloads, and local convenience from durable architecture."
tags: [data-engineering, distributed-systems, coding-agents, architecture]
sources: []
created: 2026-08-08
updated: 2026-08-19
status: active
aliases: ["agent data-system playbook", "coding agent data architecture"]
related: ["[[lakehouse-architecture]]", "[[acid-table-storage-layer]]"]
confidence: high
domains: [software-engineering, data-engineering]
source_kind: synthesis
authority_level: synthetic
evidence_level: indirect
validation_status: validated
fidelity_status: source-checked
index_eligible: true
retrieval_priority: high
approved_use: ["data-system-architecture", "coding-agent-guidance"]
prohibited_use: ["treating-derived-data-as-source-of-truth"]
---

# Coding-Agent Data-System Playbook

## Summary

Data-system playbook for coding agents working on Rob's FinOps, analytics, retrieval, and dashboard projects. It separates sources of truth from derived data, operational from analytical workloads, and local convenience from durable architecture.

## Checklist

- Identify the source of truth.
- Identify derived artifacts: caches, indexes, embeddings, materialized views, exports, reports.
- Document freshness, rebuild, and invalidation.
- Keep write paths and analytical read paths conceptually separate.
- Make schema/version boundaries explicit.
- Treat cloud services as cost and reliability dependencies.
- Validate with representative data, not only toy fixtures.

## Agent Rules

- Do not mutate generated/derived files as if they were primary state.
- If adding a cache/index, add a refresh or invalidation story.
- If adding a migration, include rollback or compatibility thinking.
- If touching cost data, preserve auditability and units.
- If touching embeddings/vector stores, preserve provenance back to source notes/raw files.

## Source Grounding

- **kleppmann-riccomini-2024-data-system-boundaries**
- **huyen-2024-ch6-rag-agents**
- **nygard-2007-coding-agent-extraction**

## See Also

- [[coding-agent-context-retrieval-playbook]]
- [[lakehouse-architecture]] — the one-governed-copy argument and its cost structure
- [[acid-table-storage-layer]] — transactions, time travel and metadata cost over object storage
