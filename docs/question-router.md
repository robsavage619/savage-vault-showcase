---
type: overview
title: "Question Router"
summary: "Routing map for agents deciding where to start in the savage_vault wiki. Sends questions to overviews, retrieval packs, indexes, Bases, raw sources, or review gates depending on domain and risk."
tags: [meta, agent, retrieval]
sources: []
created: 2026-08-08
updated: 2026-08-19
status: active
aliases: ["vault router", "retrieval router", "question routing"]
related: ["[[agent-entry]]", "[[coding-agent-operating-card]]", "[[agent-access-coding-corpus]]", "[[corpus-governance]]", "[[retrieval-pack-ai-engineering]]", "[[retrieval-pack-finops-cost-engineering]]"]
confidence: high
domains: [governance, retrieval]
source_kind: meta
authority_level: administrative
evidence_level: administrative
validation_status: validated
fidelity_status: not-applicable
index_eligible: true
retrieval_priority: critical
symbolic_role: router
evidence_lane: admin
requires_review: false
---

# Question Router

## Summary

This router tells agents where to start before answering from the vault. It routes by domain, stakes, and evidence need: overviews for orientation, retrieval packs for common workflows, full pages for methods and caveats, raw sources for fidelity checks, and governance pages for validation decisions.

## Routing Table

| Query type | Start here | Escalate when |
|---|---|---|
| unknown domain | **overview-personal-knowledge-corpus** then **index-short** | the hook is too thin |
| AI engineering, RAG, agents | [[retrieval-pack-ai-engineering]] | implementation details or eval design needed |
| coding-agent, software-engineering, repo-change | [[coding-agent-operating-card]] then [[agent-access-coding-corpus]] then [[retrieval-pack-ai-engineering]] | implementation, validation, architecture, context-selection, or production-readiness judgment is needed |
| local project under `~/Projects` | **project-context-manifests** then the matching project manifest | exact target repo is unnamed; target repo has missing/stale README, no AGENTS/CLAUDE, or high-stakes domain behavior |
| training, hypertrophy, sleep, health | **retrieval-pack-health-training** | recommendation affects programming, injury, nutrition, or medical behavior |
| baseball, trades, sabermetrics | **retrieval-pack-baseball-trade-eval** | model feature, valuation, or causal claim is needed |
| sports business, sponsorship, brand, marketing, pricing, product experiments | **sports-business-operating-card** then **retrieval-pack-sports-business-marketing** | sponsorship valuation, causal impact, ranking, pricing, or metric-governance claim is needed |
| quant finance, investing | **retrieval-pack-quantitative-finance** | allocation or money decision is implied; any backtested signal needs the four gates in **compare-anomaly-replication-vs-decay** |
| FinOps, cloud cost, AI/token cost, unit economics, billing data | [[retrieval-pack-finops-cost-engineering]] | a cost figure is quoted without a denominator, or Billed vs Effective Cost is ambiguous |
| agent handling untrusted input, prompt injection, agent security | [[agent-isolation-design-patterns]] then [[retrieval-pack-ai-engineering]] | the agent has tool access **and** reads untrusted data — see **beurer-kellner-2025-design-patterns-securing-llm-agents** |
| eval design, benchmark comparison, "is this difference real" | [[eval-power-analysis]] before building, [[eval-statistical-inference]] before reporting | a decision rests on a benchmark delta |
| forecasting, behavioral decision-making | **retrieval-pack-decision-forecasting** | claim requires causal or probabilistic framing |
| career, job market, labor | **retrieval-pack-career** | rewrite, fit score, or life decision is implied |
| source trust, contradiction, validation | [[corpus-governance]] | decision-grade answer is requested |

## Retrieval Ladder

1. Read [[agent-entry]] and this router.
2. Read the matching overview or retrieval pack.
3. If touching a local project, read **project-context-manifests** and the matching manifest.
4. Read **index-short** for candidate pages.
5. Read the relevant section of **index**.
6. Open individual pages for caveats, methods, or source paths.
7. Use raw sources only for fidelity checks or missing details.
8. Apply [[source-fidelity-review-gate]] for high-stakes claims.

## Standing Guards

These apply regardless of domain route:

- **A backtested financial signal is not evidence until it clears four gates** — selection, robustness, decay, costs. **compare-anomaly-replication-vs-decay**.
- **A benchmark delta without an interval is not a result.** [[eval-statistical-inference]].
- **An agent with tool access over untrusted data needs a named isolation pattern**, or the honest answer is that the use case is unsafe. [[agent-isolation-design-patterns]].
- **A cost figure without a denominator is not an answer.** [[unit-economics-cost-per-outcome]].

## See Also

- [[corpus-governance]]
- [[corpus-agent-evaluation-suite]]
