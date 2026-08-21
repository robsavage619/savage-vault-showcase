---
type: project-context-manifest
title: "{{title}}"
summary: "Agent-facing manifest for a local project. Tells coding agents what the project is, where it lives, what to read first, and which vault retrieval packs apply."
tags: [project, agent, context]
sources: []
created: "{{date:YYYY-MM-DD}}"
updated: "{{date:YYYY-MM-DD}}"
status: draft
aliases: []
related: ["[[agent-access-coding-corpus]]"]
confidence: medium
domains: [ai-engineering]
source_kind: meta
authority_level: administrative
evidence_level: administrative
validation_status: unreviewed
fidelity_status: not-applicable
index_eligible: false
retrieval_priority: high
symbolic_role: project-context
evidence_lane: admin
requires_review: true
project_path: ""
project_status: active
stack: []
agent_entry: ""
repo_kind: ""
---

# {{title}}

## Summary

What this project is, what it optimizes for, and what an agent must know before touching it.

## Project Path

`{{project_path}}`

## Read First

1. 
2. 
3. 

## Stack

- 

## Vault Context

- 

## Agent Rules

- Inspect live files before claims.
- Preserve existing project conventions.
- Run the smallest relevant validation before saying a change works.

## Open Questions

- 

## See Also

- **project-context-manifests**
- [[agent-access-coding-corpus]]
