---
type: analysis
title: "Coding-Agent Validation Playbook"
summary: "Operational validation playbook for vault-backed coding agents. It synthesizes AI eval methodology, SWE-bench-style task quality, Google testing/review practice, pytest/TDD guidance, and delivery metrics into a concrete route for proving a code change."
tags: [coding-agents, evals, testing, software-engineering]
sources: []
created: 2026-08-08
updated: 2026-08-08
status: active
aliases: ["agent validation playbook", "coding agent eval route"]
related: []
confidence: high
domains: [ai-engineering, evals, software-engineering]
source_kind: synthesis
authority_level: synthetic
evidence_level: indirect
validation_status: validated
fidelity_status: source-checked
index_eligible: true
retrieval_priority: critical
approved_use: ["coding-agent-validation", "eval-design", "agent-handoff"]
prohibited_use: ["benchmark-only-claim"]
---

# Coding-Agent Validation Playbook

## Summary

Operational validation playbook for vault-backed coding agents. It synthesizes AI eval methodology, SWE-bench-style task quality, Google testing/review practice, pytest/TDD guidance, and delivery metrics into a concrete route for proving a code change.

## Validation Ladder

1. **Define the claim.** What exactly should be true after the change?
2. **Locate the risk.** Retrieval miss, wrong file, bad patch, brittle test, tool failure, stale source, latency/cost, or unsafe side effect?
3. **Choose the narrowest credible check.** Unit test, characterization test, integration test, UI/e2e test, static analysis, or manual inspection.
4. **Run local gates.** In Rob's Python repos, prefer `ruff`, `pyright`, and targeted tests through the repo's existing `uv` workflow.
5. **Escalate only when needed.** Full suite, browser test, raw source check, or human review when the change crosses boundaries.
6. **Report honestly.** State what passed, what was not run, and what remains uncertain.

## Agent Rubric

| Dimension | Good | Bad |
|---|---|---|
| Task fit | Tests answer the user’s requested behavior | Tests only prove implementation details |
| Patch safety | Small, reversible, scoped | Broad rewrite without need |
| Evidence | Links to source notes or repo checks | Vibe-based confidence |
| Failure visibility | Errors surfaced | Skipped/degraded silently |
| Delivery | Fast feedback before broad checks | Full-suite cargo cult or no checks |

## Source Grounding

- **huyen-2024-ch3-evaluation-methodology** — evals should target likely failure modes.
- **openai-2024-swe-bench-verified** — task quality and human validation matter.
- **winters-2020-ch9-14-review-testing** — review and test design are long-term maintainability tools.
- **okken-2017-coding-agent-extraction** — pytest mechanics.
- **percival-2025-coding-agent-extraction** — outside-in loops.
- **forsgren-humble-kim-2018-coding-agent-extraction** — speed and stability must both count.

## See Also

- [[corpus-agent-evaluation-suite]]
- [[agent-access-coding-corpus]]
