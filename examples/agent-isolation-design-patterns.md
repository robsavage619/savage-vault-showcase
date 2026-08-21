---
type: concept
title: "Agent Isolation Design Patterns"
summary: "Six composable architectures that limit what an agent can do after ingesting untrusted input: action-selector, plan-then-execute, LLM map-reduce, dual LLM, code-then-execute, and context-minimization. Each trades generality for injection resistance, and the right move is to pick the least general pattern that does the job."
tags: [ai-engineering, security, agents, architecture, design-patterns, prompt-injection, agent-design]
sources: []
created: 2026-08-19
updated: 2026-08-19
status: active
aliases: ["agent security patterns", "dual LLM", "plan then execute", "action selector", "context minimization", "LLM map reduce", "code then execute", "which agent architecture is safe"]
related: ["[[control-flow-integrity-for-agents]]", "[[capability-based-tool-policy]]", "[[coding-agent-safe-change-playbook]]"]
confidence: high
domains: [ai-engineering, security, agents, architecture]
source_kind: synthesis
authority_level: synthetic
evidence_level: indirect
validation_status: reviewed
fidelity_status: source-checked
index_eligible: true
retrieval_priority: critical
---

# Agent Isolation Design Patterns

## Summary

Six patterns from **beurer-kellner-2025-design-patterns-securing-llm-agents**, all serving one rule: **once an agent has ingested untrusted input, it must be structurally unable to trigger consequential actions.** They are ordered by generality, and the practical guidance is to choose the **least general pattern that still does the job**.

## The Patterns

| Pattern | Mechanism | Injection resistance |
|---|---|---|
| **Action-Selector** | Maps a request to predefined tool calls; **no feedback returns to the agent** | Complete — nothing untrusted ever re-enters context |
| **Plan-Then-Execute** | Plan is fixed **before** untrusted data is seen; feedback allowed | Control flow protected; content not |
| **LLM Map-Reduce** | Untrusted items processed by isolated sub-agents, outputs aggregated | Per-item blast radius bounded |
| **Dual LLM** | Privileged LLM never sees untrusted content; manipulates it **by reference only** | Strong; privileged context stays clean |
| **Code-Then-Execute** | Agent writes an explicit program calling tools and spawning unprivileged LLMs | Strong; the pattern **debenedetti-2025-camel-defeating-prompt-injections** implements |
| **Context-Minimization** | Removes content — **including the user's own prompt** — once it has served its purpose | Defends against injections in the user prompt |

## How to Choose

Ask what the agent must do *after* reading untrusted data.

If the answer is "nothing — just pick an action," **action-selector**. This covers far more real automations than people assume: routing, classification, triggering a fixed workflow. Most such systems get built as general agents by default and inherit an injection surface for no benefit.

If the agent must act on what it read but the *sequence* is knowable in advance, **plan-then-execute**. If untrusted items are independent, **map-reduce** bounds the damage per item.

If the agent must handle untrusted content in a privileged context, **dual LLM** — pass handles, not content. This is the single highest-leverage habit in the list and needs no new infrastructure.

**Context-minimization** is the most-missed, because most threat models stop at retrieved data and ignore the user's own prompt — a malicious user, or an ordinary one who pasted from an attacker's page.

The patterns **compose**. Code-then-execute generalizes plan-then-execute; dual LLM generalizes map-reduce.

## Why It Matters

**The concession behind the catalogue is the finding.** General-purpose agents with powerful tools and arbitrary untrusted data probably cannot be made reliably safe with current models. Every pattern here buys security by **explicitly limiting the agent's ability to perform arbitrary tasks**. If that trade is unacceptable for a use case, the honest conclusion is that the use case is currently unsafe — not that a better prompt will fix it.

These are distinct from general best practices — sandboxing, human confirmation on sensitive actions — which every agent should have regardless. Note that user confirmation is itself a weak control: tired reviewers approve unsafe actions.

## Related Concepts

- [[control-flow-integrity-for-agents]] · [[capability-based-tool-policy]] — the mechanisms underneath
- **anthropic-2024-building-effective-agents** · **llm-agent-patterns** — the capability-side vocabulary these constrain

## See Also

- **beurer-kellner-2025-design-patterns-securing-llm-agents**
- [[coding-agent-safe-change-playbook]]
- **owasp-2025-agentic-ai-threats-mitigations**
