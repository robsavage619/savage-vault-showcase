---
type: analysis
title: "Coding-Agent Context and Retrieval Playbook"
summary: "Operational context-engineering playbook for vault-backed coding agents. It tells agents how to route from the vault, distinguish source notes from extraction notes, select repo context, and avoid long-context sludge."
tags: [coding-agents, context-engineering, retrieval, rag]
sources: []
created: 2026-08-08
updated: 2026-08-08
status: active
aliases: ["agent context playbook", "coding agent retrieval playbook"]
related: ["[[retrieval-pack-ai-engineering]]"]
confidence: high
domains: [ai-engineering, rag, agents]
source_kind: synthesis
authority_level: synthetic
evidence_level: indirect
validation_status: validated
fidelity_status: source-checked
index_eligible: true
retrieval_priority: critical
approved_use: ["context-engineering", "agent-design", "vault-routing"]
prohibited_use: ["stuff-everything-into-context"]
---

# Coding-Agent Context and Retrieval Playbook

## Summary

Operational context-engineering playbook for vault-backed coding agents. It tells agents how to route from the vault, distinguish source notes from extraction notes, select repo context, and avoid long-context sludge.

## Retrieval Order

1. Read [[agent-access-coding-corpus]].
2. Read [[retrieval-pack-ai-engineering]].
3. For coding tasks, read the relevant book extraction/playbook notes before raw books.
4. In the target repo, search for existing patterns before editing.
5. Open only the files/symbols that affect the change.
6. Pull raw sources only when the wiki note is too thin or citation fidelity matters.

## Context Budget Rules

- Prefer one routing note, one playbook, and 2–4 source/extraction notes over a huge bundle.
- Keep repo context separate from vault context: source knowledge answers “what good looks like”; repo context answers “what this code already does.”
- Remove stale or irrelevant context when the task pivots.
- Treat retrieval packs and extraction notes as curated context; treat raw PDFs/EPUBs as fallback.

## Failure Modes

- **Wrong layer:** using general book advice when local repo convention already decides.
- **Context rot:** too many partially relevant notes drown the important invariant.
- **Derived-data confusion:** treating vector indexes, generated docs, or caches as sources of truth.
- **Tool-surface blur:** making a tool too broad or too chatty for the agent to use reliably.

## Source Grounding

- **huyen-2024-ch6-rag-agents** — RAG and tools are context-construction systems.
- **anthropic-2025-context-engineering-agents** — full token state matters.
- **mcp-2026-server-tools-resources-prompts** — tools/resources/prompts have different control semantics.
- **kleppmann-riccomini-2024-data-system-boundaries** — indexes and caches are derived data.

## See Also

- [[agent-access-coding-corpus]]
- [[coding-agent-validation-playbook]]
