---
type: analysis
title: "Coding-Agent Data/ML Contracts Playbook"
summary: "Operational route for agents changing data pipelines, ML workflows, model-serving code, or analytics contracts. It combines data contracts, data-system boundaries, MLOps, validation, and production-readiness rules into a fast checklist."
tags: [coding-agents, data-engineering, mlops, production-ml]
sources: []
created: 2026-08-09
updated: 2026-08-09
status: active
aliases: ["data ML contracts playbook", "data pipeline and MLOps agent route"]
related: ["[[coding-agent-data-system-playbook]]", "[[coding-agent-production-readiness-playbook]]", "[[coding-agent-validation-playbook]]"]
confidence: high
domains: [software-engineering, data-engineering, ml-engineering]
source_kind: synthesis
authority_level: administrative
evidence_level: operational-synthesis
validation_status: validated
fidelity_status: source-checked
index_eligible: true
retrieval_priority: high
symbolic_role: playbook
evidence_lane: engineering
requires_review: false
approved_use: ["data-pipeline-change", "mlops-change", "model-serving-review", "coding-agent-guidance"]
prohibited_use: ["skipping-live-repo-inspection", "claiming-production-readiness-without-validation"]
---

# Coding-Agent Data/ML Contracts Playbook

## Summary

Operational route for agents changing data pipelines, ML workflows, model-serving code, or analytics contracts. Use this after [[coding-agent-operating-card]] when the work touches schemas, derived data, model artifacts, inference contracts, data quality, drift, or production ML.

## Read First

1. [[coding-agent-data-system-playbook]]
2. **jones-2023-coding-agent-extraction**
3. **jones-2023-ch2-data-contract-interface** if the task touches a producer/consumer data boundary.
4. **jones-2023-ch6-7-schema-contract-architecture** if the task touches schema, quality rules, or contract enforcement.
5. **jones-2023-ch9-10-contract-adoption-practice** if the task changes rollout, migration, or consumers.
6. **gift-deza-2021-coding-agent-extraction**
7. **gift-deza-2021-ch1-4-mlops-lifecycle-delivery** if the task touches training, CI/CD, containers, or deployment.
8. **gift-deza-2021-ch6-monitoring-logging-drift** if the task touches observability, data drift, model drift, or logs.
9. **gift-deza-2021-ch10-11-interoperability-cli-services** if the task touches model artifacts, CLIs, or serving APIs.
10. [[coding-agent-validation-playbook]]
11. [[coding-agent-production-readiness-playbook]] if the change affects runtime behavior or users.

## Agent Route

1. Identify the exact source of truth.
2. Classify every touched artifact: producer, contract, schema, transform, derived table, cache, model artifact, inference endpoint, report, or consumer.
3. Inspect live repo files before claims: README/agent docs, schemas/models, pipeline entry point, config, migrations, fixtures, validation commands, deployment/runtime code.
4. Determine the contract boundary: who produces the data/model behavior and who consumes it?
5. Capture current behavior when unprotected: counts, keys, nulls, units, ordering, schema, model artifact name/version, inference input/output, and current errors.
6. Make the smallest compatible change.
7. Validate both local correctness and boundary compatibility.
8. Report what passed, what was not run, and what remains uncertain.

## Required Questions

- What breaks if this input arrives late, duplicated, partial, malformed, or out of order?
- Is this file/table/model primary state or derived output?
- Is schema evolution backward compatible?
- Is the validation close enough to the producer boundary to fail early?
- How are freshness, provenance, and rebuilds represented?
- Can the model or pipeline be rerun safely?
- How would drift, bad data, or a bad model deployment become visible?
- Is there a rollback or recovery path?

## Hard Stops

- Unknown destructive data migration.
- Production data or model deployment without a credible rollback.
- Schema/interface change with unknown consumers.
- Silent data dropping, unit conversion, or key rewriting.
- No validation path for a behavior-changing data/ML edit.

## Output Bar

A decision-grade answer must say:

- target repo/path inspected;
- source-of-truth and derived artifacts identified;
- contract/schema/model boundary checked;
- validation run and result;
- remaining uncertainty.

## See Also

- **jones-2023-driving-data-quality-data-contracts**
- **gift-deza-2021-practical-mlops**
- **data-contract-boundary**
- **schema-evolution-contracts**
- **mlops-production-readiness**
- **model-drift-monitoring**
- **model-artifact-contract**
- **kleppmann-riccomini-2024-data-system-boundaries**
