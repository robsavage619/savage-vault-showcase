---
type: concept
title: "Control-Flow Integrity for Agents"
summary: "Making prompt injection structurally impossible by ensuring untrusted data can never influence which actions an agent takes. Control flow is derived only from the trusted user query; untrusted content enters as values, never as instructions. The agent-security analogue of classical control-flow integrity against memory-corruption exploits."
tags: [ai-engineering, security, prompt-injection, agents, architecture, information-flow-control]
sources: []
created: 2026-08-19
updated: 2026-08-19
status: active
aliases: ["control flow integrity agents", "data cannot become control", "structural prompt injection defense", "why sanitizing input does not work", "trusted query compilation"]
related: ["[[capability-based-tool-policy]]", "[[agent-isolation-design-patterns]]"]
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

# Control-Flow Integrity for Agents

## Summary

The structural defense against prompt injection: ensure that **untrusted data can never determine which actions the agent takes.** Control flow is extracted from the **trusted** user query alone and fixed before untrusted content is ever read. Untrusted content then flows through that fixed structure as **values** — it can change what a step *contains*, never which steps *run*.

## How It Works

The parallel to conventional software security is exact, and it is the reason the approach works.

Memory-corruption exploits succeeded because data (a buffer) could become control (a return address). Two decades of input sanitization failed to stop them. **Control-flow integrity** succeeded by making the transition structurally impossible: the program's legal control-flow graph is fixed in advance and enforced at runtime, so corrupted data cannot redirect execution no matter what it contains.

Prompt injection is the same bug in a new substrate. An LLM's context is an undifferentiated token stream in which instructions and data are indistinguishable by construction, so retrieved content can become instruction. Filtering and defensive prompting are the sanitization era of this problem — they raise attacker cost and guarantee nothing.

**debenedetti-2025-camel-defeating-prompt-injections** applies the CFI move directly: compile the trusted query into an explicit program, execute it in a custom interpreter that tracks provenance, and let untrusted data occupy only value positions. **77% of AgentDojo tasks solved with provable security against 84% undefended.**

Several of the **beurer-kellner-2025-design-patterns-securing-llm-agents** patterns are weaker or stronger approximations of the same idea — action-selector removes feedback entirely, plan-then-execute fixes the plan before untrusted data arrives, code-then-execute makes the program explicit.

## Why It Matters

**It relocates the security boundary off the model.** If a defense depends on the model resisting the injection, the defense is only as good as the model's adversarial robustness — which, as the CaMeL authors note, remains unsolved after a decade of work in vision. Structural defenses do not care whether the model is fooled.

**The guarantee is precisely scoped, and the scope is the honest part.** Control-flow integrity protects control flow. It does **not** protect content: in plan-then-execute and code-then-execute, an injection in retrieved data can still alter the *text* of a message the agent sends. [[capability-based-tool-policy]] is the complementary mechanism that constrains where such content may go.

## Perspectives

The cost is generality, and it is unavoidable rather than an implementation defect. An agent that decides what to do based on what it reads is exactly the thing this forbids — and that is what most general-purpose agent designs are. The **beurer-kellner-2025-design-patterns-securing-llm-agents** authors accept the implication: general-purpose agents with tool access and untrusted input probably cannot be secured with current models.

Even without adopting a full interpreter, the cheap version is available to any agent: **tag every value with its trust origin and check that tag at tool-call time.**

## Related Concepts

- [[capability-based-tool-policy]] — constrains data flow where this constrains control flow
- [[agent-isolation-design-patterns]] — the pattern catalogue
- **system-boundary-and-side-effects**

## See Also

- **debenedetti-2025-camel-defeating-prompt-injections**
- **beurer-kellner-2025-design-patterns-securing-llm-agents**
- **owasp-2025-agentic-ai-threats-mitigations**
