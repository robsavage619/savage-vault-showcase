---
type: concept
title: "Capability-Based Tool Policy"
summary: "Attaching provenance and permission metadata to every value an agent handles, then enforcing policy at the tool-call boundary. Where control-flow integrity stops untrusted data from choosing actions, capabilities stop trusted data from reaching unauthorized destinations — the exfiltration half of agent security."
tags: [ai-engineering, security, agents, access-control, information-flow-control, prompt-injection, mcp]
sources: []
created: 2026-08-19
updated: 2026-08-19
status: active
aliases: ["capabilities for agents", "provenance tracking agents", "tool call policy enforcement", "how do I stop an agent leaking data", "information flow control LLM", "data exfiltration defense"]
related: ["[[control-flow-integrity-for-agents]]", "[[agent-isolation-design-patterns]]"]
confidence: high
domains: [ai-engineering, security, agents]
source_kind: synthesis
authority_level: synthetic
evidence_level: indirect
validation_status: reviewed
fidelity_status: source-checked
index_eligible: true
retrieval_priority: high
---

# Capability-Based Tool Policy

## Summary

Every value an agent handles carries metadata — where it came from, what may be done with it — and that metadata is checked when a tool is invoked. The term comes from the software-security literature, where a **capability** is an unforgeable token conferring a specific permission on a specific object. **debenedetti-2025-camel-defeating-prompt-injections** adopts it to prevent **exfiltration of private data over unauthorized data flows**, and is explicit that "capability" here means the security concept, not the ML sense of how able a model is.

## How It Works

Three parts.

**Provenance on every value.** A string read from a private calendar is tagged as such; a string scraped from a web page carries a different tag. Tags propagate through operations, so anything derived from private data inherits its restrictions.

**Policies expressed over tags.** "Content tagged `private` may not be passed to a tool tagged `external-send`." "A URL originating from untrusted content may not be fetched with credentials attached."

**Enforcement at the tool-call boundary.** The check happens where the agent crosses from reasoning into acting — the only place where a bad decision becomes a real consequence, and therefore the correct chokepoint.

This is the **data-flow** half of agent security. [[control-flow-integrity-for-agents]] stops untrusted data from choosing *which* tool runs; capabilities stop legitimate data from reaching *the wrong destination*. Both are needed: an agent whose control flow is fixed can still be steered into emailing the right document to the wrong address.

## Why It Matters

**Exfiltration is the injection payload that matters most.** The classic attack does not need to hijack the agent's whole plan — it only needs one outbound channel and one sensitive value. An embedded image URL, a markdown link, a "helpful" summary sent to the wrong recipient. Capability policies close the channel rather than trying to detect the payload.

**It is implementable incrementally.** The full CaMeL interpreter is heavy, but the primitive is not: tag values with trust origin, and check the tag before any tool call with external side effects. Most of the protection comes from the first, crude version.

**MCP is the natural enforcement point for local work.** **mcp-2026-server-tools-resources-prompts** already places a permission surface at the tool boundary, which is exactly where this policy belongs — the mechanism exists, and the question is what policies get written on it.

## Perspectives

The honest limitation: **the guarantee is only as good as the policies.** "Provable security" means untrusted data provably cannot violate the stated policy, not that the policy is right. Writing correct policies is engineering work that scales with the tool surface, and the cost lands on whoever adds the next tool — a durable organizational problem, not a one-off.

Over-restrictive policies also break real tasks; CaMeL's 7-point utility cost on AgentDojo is what that looks like measured honestly. Security work reporting no utility cost is usually not measuring utility.

## Related Concepts

- [[control-flow-integrity-for-agents]] — the control-flow half
- [[agent-isolation-design-patterns]]
- **data-contract-boundary** — the same "check at the boundary" instinct in data systems

## See Also

- **debenedetti-2025-camel-defeating-prompt-injections**
- **owasp-2025-securing-agentic-applications**
- **mcp-2026-server-tools-resources-prompts**
