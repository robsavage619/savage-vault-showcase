---
type: analysis
title: "Coding-Agent Review Checklist"
summary: "Review checklist for accepting an agent's code change, architecture proposal, eval design, data-model change, or production-readiness claim. It catches the software equivalent of polished-but-thin work: missing repo evidence, hidden uncertainty, weak validation, pattern drift, and unsupported benchmark claims."
tags: [coding-agents, review, validation, software-engineering]
sources: []
created: 2026-08-08
updated: 2026-08-08
status: active
aliases: ["coding agent checklist", "agent code review checklist", "software agent review checklist"]
related: ["[[coding-agent-operating-card]]", "[[coding-agent-validation-playbook]]", "[[coding-agent-safe-change-playbook]]", "[[coding-agent-python-architecture-playbook]]", "[[coding-agent-data-system-playbook]]", "[[coding-agent-production-readiness-playbook]]"]
confidence: high
domains: [ai-engineering, software-engineering, evals]
source_kind: synthesis
authority_level: synthetic
evidence_level: indirect
validation_status: validated
fidelity_status: source-checked
index_eligible: true
retrieval_priority: critical
approved_use: ["agent-review", "code-review", "eval-review", "handoff-review"]
prohibited_use: ["substitute-for-repo-validation"]
---

# Coding-Agent Review Checklist

## Summary

Review checklist for accepting an agent's code change, architecture proposal, eval design, data-model change, or production-readiness claim. It catches the software equivalent of polished-but-thin work: missing repo evidence, hidden uncertainty, weak validation, pattern drift, and unsupported benchmark claims.

## Review Setup

- [ ] The agent classified the work type.
- [ ] The agent named the vault route or playbook it used.
- [ ] The target repo/path was inspected, not assumed.
- [ ] Existing conventions were identified before proposing a pattern.
- [ ] Conflicting local patterns were surfaced instead of blended.
- [ ] The agent named what would make the answer blocked, exploratory, or decision-grade.

## Repo Evidence

- [ ] Relevant files, tests, configs, and docs were read.
- [ ] Existing package, lint, type, and test commands were discovered from the repo.
- [ ] Rob's defaults were applied only where the repo did not already define a stronger convention.
- [ ] No invented file, symbol, flag, tool, or API was recommended without verification.
- [ ] Dirty-worktree or user-owned changes were preserved.

## Architecture And Data

- [ ] Domain logic, infrastructure, UI, and orchestration concerns are not collapsed into one opaque object.
- [ ] Data sources of truth, derived data, caches, indexes, and exports are separated.
- [ ] Public API/types preserve important domain distinctions instead of generic records.
- [ ] Transaction, idempotency, retry, and failure behavior are explicit where relevant.
- [ ] Any architectural tradeoff names what is gained, what is lost, and when to revisit it.

## Validation

- [ ] The validation target matches the user-visible behavior or risk.
- [ ] Unit, characterization, integration, e2e, static, or manual checks were chosen deliberately.
- [ ] `ruff`, `pyright`, targeted tests, or repo-native gates were run when applicable.
- [ ] Skipped checks are listed with a reason.
- [ ] The agent does not claim “done” if validation quietly degraded.
- [ ] Benchmarks are not treated as proof of production behavior.

## Agent And Tool Features

- [ ] Tool descriptions, schemas, and outputs are designed for model comprehension, not just human APIs.
- [ ] Context sources are ranked by usefulness and cost.
- [ ] Retrieved notes are cited by role: playbook, section note, extraction note, paper, or raw source.
- [ ] The agent separates retrieval failure, tool failure, patch failure, and validation failure.
- [ ] Memory, logs, traces, and eval examples do not leak secrets or private data.

## Production Readiness

- [ ] User-visible errors, retries, timeouts, observability, and rollback are considered.
- [ ] External calls have failure modes and rate/cost boundaries.
- [ ] Background jobs, caches, derived data, and scheduled work have rebuild or repair paths.
- [ ] Deployments, migrations, or destructive operations are explicitly scoped.
- [ ] The handoff states what changed, what passed, what did not run, and what remains risky.

## Blockers

Block the answer or mark it `needs_review` if:

- the agent cannot identify the target repo or files;
- a code change has no credible validation path;
- the answer depends on a missing source, hidden environment, secret, or external system;
- the agent is about to overwrite user work or run a destructive command without clear scope;
- a claim about agent performance relies only on benchmark headlines;
- the proposed design conflicts with local conventions and Rob has not chosen which pattern wins.

## See Also

- [[coding-agent-operating-card]]
- [[coding-agent-validation-playbook]]
- [[coding-agent-safe-change-playbook]]
