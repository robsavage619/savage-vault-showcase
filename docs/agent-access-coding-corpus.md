---
type: overview
title: "Agent Access: Coding Corpus"
summary: "Shared access guide for Claude Code, Codex, ChatGPT-style agents, and Obsidian REST clients using the coding-agent corpus. It defines the canonical read order, file/API access paths, and the source hierarchy agents should follow before answering or editing code."
tags: [meta, agent, coding-agents, retrieval]
sources: []
created: 2026-08-08
updated: 2026-08-09
status: active
aliases: ["coding corpus access", "Claude Code vault access", "ChatGPT vault access", "Codex vault access"]
related: ["[[agent-entry]]", "[[question-router]]", "[[coding-agent-operating-card]]", "[[retrieval-pack-ai-engineering]]", "[[coding-agent-review-checklist]]", "[[coding-agent-validation-playbook]]", "[[coding-agent-context-retrieval-playbook]]"]
confidence: high
domains: [ai-engineering, governance, retrieval]
source_kind: meta
authority_level: administrative
evidence_level: administrative
validation_status: validated
fidelity_status: not-applicable
index_eligible: true
retrieval_priority: critical
symbolic_role: agent-access-guide
evidence_lane: admin
requires_review: false
---

# Agent Access: Coding Corpus

## Summary

Shared access guide for Claude Code, Codex, ChatGPT-style agents, and Obsidian REST clients using the coding-agent corpus. It defines the canonical read order, file/API access paths, and the source hierarchy agents should follow before answering or editing code.

## Canonical Read Order

1. [[agent-entry]]
2. [[question-router]]
3. [[coding-agent-operating-card]]
4. [[retrieval-pack-ai-engineering]]
5. [[coding-agent-context-retrieval-playbook]]
6. One or more task-specific playbooks:
   - [[coding-agent-validation-playbook]]
   - [[coding-agent-safe-change-playbook]]
   - [[coding-agent-python-architecture-playbook]]
   - [[coding-agent-data-system-playbook]]
   - [[coding-agent-production-readiness-playbook]]
7. [[coding-agent-review-checklist]] before accepting a non-trivial answer or patch.
8. Task-specific source notes or extraction notes.
9. Raw PDF/EPUB sources only when page-level notes are insufficient.
10. For `~/Projects`, read **project-context-manifests** and the matching project manifest before editing.

## Claude Code Access

Claude Code should start from root `CLAUDE.md`, then this page through `wiki/agent-entry.md` and `wiki/question-router.md`. For coding-agent work, Claude should treat [[retrieval-pack-ai-engineering]] and the playbooks above as required context before making architecture, testing, refactoring, or production-readiness claims.

## ChatGPT / Codex Access

ChatGPT-style agents with filesystem access should read this vault directly:

- `~/Vault/savage_vault/START HERE.md`
- `~/Vault/savage_vault/wiki/agent-entry.md`
- `~/Vault/savage_vault/wiki/question-router.md`
- `~/Vault/savage_vault/wiki/coding-agent-operating-card.md`
- `~/Vault/savage_vault/wiki/agent-access-coding-corpus.md`
- `~/Vault/savage_vault/wiki/retrieval-pack-ai-engineering.md`
- `~/Vault/savage_vault/wiki/project-context-manifests.md`

If filesystem access is unavailable but Obsidian is running, use the REST API described in [[agent-entry]]. Do not hardcode the API key.

## Source Hierarchy

| Layer | Use |
|---|---|
| Playbooks | Action rules for agents |
| Section/chapter source notes | Source-grounded depth |
| Book extraction notes | Book-level operational summary |
| Book hubs | Navigation |
| Paper/source notes | Benchmarks and primary methods |
| Raw files | Fidelity checks and missing details |

## Access Test

An agent can access the coding corpus if it can answer:

- What is the canonical read order?
- Which operating card defines answer shape and hard stops?
- Which playbook governs safe changes?
- Which playbook governs validation?
- Which checklist reviews the answer or patch before acceptance?
- Which notes define Python architecture defaults?
- Which quoted raw-source wikilink backs a cited claim?
- Which project manifest applies before touching `~/Projects`?

## See Also

- [[retrieval-pack-ai-engineering]]
- [[coding-agent-operating-card]]
- [[coding-agent-review-checklist]]
- **corpus-validation-report**
