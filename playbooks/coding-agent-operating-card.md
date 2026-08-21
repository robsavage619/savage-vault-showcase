---
type: overview
title: "Coding-Agent Operating Card"
summary: "Default operating card for coding agents using savage_vault. It gives Claude Code, Codex, ChatGPT-style agents, and REST clients a compact work-classification route, hard-stop rules, answer shape, and minimum good behavior before they edit or advise on code."
tags: [coding-agents, agent, software-engineering, retrieval]
sources: []
created: 2026-08-08
updated: 2026-08-08
status: active
aliases: ["coding agent operating card", "software agent operating card", "default coding agent card"]
related: ["[[agent-access-coding-corpus]]", "[[question-router]]", "[[retrieval-pack-ai-engineering]]", "[[coding-agent-review-checklist]]", "[[coding-agent-context-retrieval-playbook]]", "[[coding-agent-validation-playbook]]", "[[coding-agent-safe-change-playbook]]", "[[coding-agent-python-architecture-playbook]]", "[[coding-agent-data-system-playbook]]", "[[coding-agent-production-readiness-playbook]]"]
confidence: high
domains: [ai-engineering, software-engineering, governance]
source_kind: meta
authority_level: administrative
evidence_level: administrative
validation_status: validated
fidelity_status: not-applicable
index_eligible: true
retrieval_priority: critical
symbolic_role: operating-card
evidence_lane: admin
requires_review: false
---

# Coding-Agent Operating Card

## Summary

Default operating card for coding agents using savage_vault. It gives Claude Code, Codex, ChatGPT-style agents, and REST clients a compact work-classification route, hard-stop rules, answer shape, and minimum good behavior before they edit or advise on code.

## The Job

Help Rob build and maintain personal software with an expert-over-shoulder corpus. Do not try to sound broadly authoritative; retrieve the relevant vault route, inspect the actual repository, preserve existing conventions, and make uncertainty visible.

The default chain is:

```text
user request -> work type -> vault route -> repo evidence -> implementation choice -> validation -> handoff
```

If the agent jumps from “I know a pattern” to “change code” without reading the local repo and the relevant corpus route, the corpus has failed.

## Default Retrieval Route

1. [[agent-access-coding-corpus]]
2. [[retrieval-pack-ai-engineering]]
3. the matching playbook
4. task-specific source notes
5. repository files and tests
6. raw sources only when a claim needs fidelity checking

## First Question To Answer

Classify the work before answering:

| Work type | Must retrieve |
|---|---|
| Context/retrieval design | [[coding-agent-context-retrieval-playbook]], **huyen-2024-ch6-rag-agents** |
| Validation/evals/tests | [[coding-agent-validation-playbook]], **huyen-2024-ch3-evaluation-methodology**, **winters-2020-ch9-14-review-testing** |
| Existing-code change | [[coding-agent-safe-change-playbook]], **feathers-2004-ch2-4-feedback-seams**, **feathers-2004-ch13-characterization-tests** |
| Python architecture | [[coding-agent-python-architecture-playbook]], **percival-gregory-2020-ch1-3-domain-repository**, **percival-gregory-2020-ch6-13-uow-events-di** |
| Data pipeline, cache, vector store, analytics table, cost model | [[coding-agent-data-system-playbook]], **kleppmann-riccomini-2024-data-system-boundaries** |
| Service/runtime/tool production readiness | [[coding-agent-production-readiness-playbook]], **newman-2021-ch12-resiliency**, **huyen-2024-ch10-ai-architecture-feedback** |
| Benchmark or agent-performance claim | **jimenez-2023-swe-bench**, **openai-2024-swe-bench-verified**, **badertdinov-2025-swe-rebench** |

## Hard Stop Rules

Stop, ask, or downgrade to exploratory language when:

- the exact target repository path is unknown;
- the only supplied path is `~/Projects`; that is a root, not a repo target;
- the request implies changing code but tests/conventions have not been inspected;
- two local patterns conflict;
- the change touches auth, secrets, money, destructive file operations, production deployment, or external users without explicit scope;
- a benchmark claim is based on stale or non-validated tasks;
- a proposed architecture ignores Rob's Python stack or the repo's existing pattern;
- validation cannot be run and no honest alternative evidence exists;
- retrieved notes are unreviewed, disputed, or not source-fidelity checked for the claim being made.

## Answer Shape

For coding work, answer in this shape:

1. Work classification
2. Repository evidence inspected
3. Vault route used
4. Implementation path or design decision
5. Validation run or validation gap
6. Remaining risk
7. Next smallest action

## Minimum Good Behavior

A good coding agent should make Rob feel more capable by saying:

- what the software decision depends on;
- what the repo already does;
- what the vault suggests;
- what can safely be changed now;
- what must be tested;
- and what should wait for a clearer constraint or human review.

## See Also

- [[agent-access-coding-corpus]]
- [[coding-agent-review-checklist]]
- **coding-agent-corpus-usability-review**
