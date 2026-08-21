---
type: analysis
title: "Coding-Agent Python Architecture Playbook"
summary: "Python architecture playbook for Rob's coding agents. It combines Rob's stack conventions with Cosmic Python, DDD, Effective Python, Robust Python, pytest, and TDD sources into a default architecture route for personal Python projects."
tags: [python, architecture, coding-agents, software-engineering]
sources: []
created: 2026-08-08
updated: 2026-08-08
status: active
aliases: ["agent Python architecture playbook", "Rob Python agent architecture"]
related: []
confidence: high
domains: [software-engineering, python]
source_kind: synthesis
authority_level: synthetic
evidence_level: indirect
validation_status: validated
fidelity_status: source-checked
index_eligible: true
retrieval_priority: critical
approved_use: ["python-architecture", "coding-agent-guidance"]
prohibited_use: ["overriding-local-repo-convention"]
---

# Coding-Agent Python Architecture Playbook

## Summary

Python architecture playbook for Rob's coding agents. It combines Rob's stack conventions with Cosmic Python, DDD, Effective Python, Robust Python, pytest, and TDD sources into a default architecture route for personal Python projects.

## Defaults

- Python 3.12.
- `src/<package>/` layout.
- `uv` for packages and commands.
- `ruff` for format/lint/isort.
- `pyright` basic mode.
- `from __future__ import annotations`.
- `X | None`, never `Optional[X]`.
- Google-style docstrings on public or complex functions.

## Architecture Route

1. Put business rules in domain/service code, not framework handlers.
2. Keep infrastructure behind repositories/adapters.
3. Use unit-of-work when a use case needs transaction consistency.
4. Use events/message bus only when workflow coupling justifies it.
5. Type public APIs and structural contracts.
6. Test domain rules with fast unit tests and adapters with integration tests.

## Source Grounding

- **percival-gregory-2020-ch1-3-domain-repository** — domain model and repository boundary.
- **percival-gregory-2020-ch6-13-uow-events-di** — UoW, events, DI.
- **evans-2003-coding-agent-extraction** — ubiquitous language and bounded contexts.
- **slatkin-2024-coding-agent-extraction** — Python idioms.
- **viafore-2022-coding-agent-extraction** — type-driven intent.
- **okken-2017-coding-agent-extraction** — pytest habits.

## See Also

- [[coding-agent-safe-change-playbook]]
- [[coding-agent-validation-playbook]]
