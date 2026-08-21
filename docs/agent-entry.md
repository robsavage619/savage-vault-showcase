---
type: overview
title: "Agent Entry Point"
summary: "Cold-start orientation for external agents querying this wiki. Read this page first, then wiki/index.md. Covers what this wiki contains, how to query it via REST API, recommended retrieval strategy, and how to interpret confidence and tags."
tags: [meta, agent]
sources: []
created: 2026-04-19
updated: 2026-08-19
status: active
aliases: []
related: ["[[question-router]]", "[[coding-agent-operating-card]]", "[[agent-access-coding-corpus]]", "[[template-catalog]]", "[[corpus-governance]]"]
confidence: high
domains: [governance, retrieval]
source_kind: meta
authority_level: administrative
evidence_level: administrative
validation_status: validated
fidelity_status: not-applicable
index_eligible: true
retrieval_priority: critical
symbolic_role: agent-entry
evidence_lane: admin
requires_review: false
---
# Agent Entry Point

Read this page before querying the wiki. It tells you what's here, how to find things, and how to interpret what you find. Then read [[question-router]] before answering.

## Summary

This is a persistent, LLM-maintained knowledge base stored as markdown files in an Obsidian vault. It is organized into four layers: immutable source documents in `raw/`, LLM-generated wiki pages in `wiki/`, live Obsidian Bases in `wiki/bases/`, and a maturity layer that governs routing, source fidelity, review, contradictions, and evaluation.

**Read order for agents:** [[question-router]] -> the matching retrieval pack or overview -> **index-short** -> **index** -> individual pages -> raw sources only when needed. For coding-agent or software-engineering work, read [[coding-agent-operating-card]] and [[agent-access-coding-corpus]] after [[question-router]] and before [[retrieval-pack-ai-engineering]]. For work inside `~/Projects`, also read **project-context-manifests** and the matching project manifest before editing. For health, training, investing, finance, or career recommendations, apply [[source-fidelity-review-gate]] before treating a page as decision-grade evidence.

**Domain:** This wiki spans several interconnected areas. The fastest way in is the domain **overview** pages (Maps of Content) — each links its key pages, a reading order, and open questions:
0. **Whole Corpus** (**overview-personal-knowledge-corpus**) — map of domains, operating layer, retrieval packs, and validation status
1. **RAG & Retrieval** (**overview-rag-retrieval**) — dense retrieval, ANN search, reranking, embedding models, RAG evaluation, hierarchical/adaptive/agentic retrieval
2. **Agentic LLMs & Tool Use** (**overview-agentic-llms**) — agent patterns, ReAct, Toolformer, Gorilla, CoALA, AutoGen, AgentBench; LLM app engineering; reasoning models and test-time compute; agent security ([[agent-isolation-design-patterns]])
3. **LLM Evaluation** — MT-Bench, Chatbot Arena, G-Eval, LLM-as-judge methods, and the statistical layer ([[eval-statistical-inference]], [[eval-power-analysis]])
4. **Exercise Science & Training** (**overview-exercise-science**) — hypertrophy, strength, periodization, sport nutrition
5. **Sleep Science** (**overview-sleep-science**) — architecture, circadian timing, CBT-I, wearable recovery
6. **Sabermetrics & Baseball Analytics** (**overview-sabermetrics**) — WAR and its inputs, analytics books, the trade-eval project
7. **Sports Business, Marketing Science & Experiments** (**sports-business-operating-card**, **retrieval-pack-sports-business-marketing**) — sponsorship, brand growth, pricing, marketing metrics, rankings, networks, and controlled experiments
8. **Quantitative Finance & Factor Investing** (**overview-quantitative-finance**) — factor investing, quant equity, active-management theory
9. **Job Market NLP, Labor Economics & Career** — skill extraction, ESCO taxonomy, automation risk, career theory
10. **Decision-making & Forecasting** — behavioral economics, judgment, superforecasting, sensitivity analysis
11. **FinOps, Cost Engineering & Data Platform** (**overview-finops-cost-engineering**, [[retrieval-pack-finops-cost-engineering]]) — the FOCUS billing schema, the FinOps capability model, unit economics, AI/token cost, and the lakehouse cost argument

The wiki is designed for high-accuracy retrieval: every page has a machine-readable frontmatter `summary` field, `wiki/index-short.md` gives one-line hooks, and `wiki/index.md` aggregates full summaries for much of the corpus. For most queries, the overviews plus the index are sufficient — you do not need to open individual pages unless you need full detail. `wiki/bases/` holds live Bases views that render in Obsidian.

**Four standing guards** (from [[question-router]]), regardless of domain: a backtested financial signal is not evidence until it clears the four gates in **compare-anomaly-replication-vs-decay**; a benchmark delta without an interval is not a result ([[eval-statistical-inference]]); an agent with tool access over untrusted data needs a named isolation pattern ([[agent-isolation-design-patterns]]); a cost figure without a denominator is not an answer ([[unit-economics-cost-per-outcome]]).

**Maturity warning:** legacy notes are useful for routing and synthesis, but most do not yet carry `validation_status` or `fidelity_status`. Treat missing maturity fields as `legacy-unreviewed` for decision-grade use. Check **corpus-validation-report** and **corpus-gap-register** before claiming the corpus is fully healthy.

---

## How to Query This Wiki

### Option A — REST API (preferred for external agents)

The Obsidian Local REST API plugin (v3.6.1) serves the vault over **HTTPS on port 27124**.
All requests require an API key. Obsidian must be running on the host machine.

**Authentication:** `Authorization: Bearer <key>` header on every request.
Retrieve the key from `.obsidian/plugins/obsidian-local-rest-api/data.json` → `apiKey`.
**TLS:** Self-signed cert — pass `verify=False` or `--insecure` in your client.

```
# Read the master index (start here)
GET https://localhost:27124/vault/wiki/index.md
Authorization: Bearer <key>

# Read a specific page
GET https://localhost:27124/vault/wiki/{page-slug}.md
Authorization: Bearer <key>

# Full-text search across all vault files
POST https://localhost:27124/search/simple/?query=<search-term>
Authorization: Bearer <key>

# List all files in wiki/
GET https://localhost:27124/vault/wiki/
Authorization: Bearer <key>
```

**Python quickstart:**
```python
import requests
BASE, KEY = "https://localhost:27124", "<key>"
H = {"Authorization": f"Bearer {KEY}"}
index = requests.get(f"{BASE}/vault/wiki/index.md", headers=H, verify=False).text
```

### Option B — Direct file access

If you have filesystem access, read files directly:
- `START HERE.md` — vault front door
- `wiki/agent-entry.md` — agent orientation
- `wiki/question-router.md` — route the question before opening indexes or source notes
- `wiki/index-short.md` — fast candidate-page lookup
- `wiki/index.md` — full summary cache when the short index is insufficient
- `wiki/{slug}.md` — individual pages
- `raw/{filename}` — original source documents (read-only)

---

## Recommended Retrieval Strategy

**Tier 0 — Router + overviews + short index**
1. Read [[question-router]].
2. For coding-agent or software-engineering work, read [[coding-agent-operating-card]] and [[agent-access-coding-corpus]].
3. For an unfamiliar area, read **overview-personal-knowledge-corpus** or the relevant `overview-<domain>` page.
4. For common workflows, read the relevant retrieval pack:
   [[retrieval-pack-ai-engineering]] or one of the other domain retrieval packs.
5. For local project work, read **project-context-manifests** and the matching project manifest.
6. Read `wiki/index-short.md` — one-sentence hooks for candidate pages.
7. If the hook answers a low-stakes question: respond, done.

**Tier 1 — Full index (for queries needing richer context)**
3. Read the relevant *category section* of `wiki/index.md` — full 2–3 sentence summaries.
4. If the summaries answer the question: respond, done.

**Tier 2 — Page reads (for methodology, figures, or caveats)**
5. Read specific wiki pages identified in tier 0/1.
6. Check each page's `sources` frontmatter field for raw document paths.

**Tier 3 — Raw source documents and fidelity review**
7. Read raw documents only if the wiki page lacks the required detail or source fidelity matters.
8. Apply [[source-fidelity-review-gate]] for high-stakes or decision-grade claims.

**Tier 4 — Full-text search (discovery)**
9. Use the REST API search endpoint for topics not yet indexed.

---

## How to Interpret Frontmatter Fields

| Field | Interpretation |
|-------|----------------|
| `type` | Page category: `source-summary` `entity` `concept` `comparison` `analysis` `overview` `book-overview` `research-finding` |
| `summary` | 2–3 sentence self-contained description. Reliable for triage. |
| `confidence` | `high` = well-supported by multiple sources. `medium` = one source or inferred. `low` = contradicted, speculative, or needs review. Absent = not assessed. |
| `validation_status` | Review state for decision-grade use. Missing = legacy-unreviewed. |
| `fidelity_status` | Whether the source was checked. `abstract-only` and `unreviewed` require caution. |
| `index_eligible` | Whether the page is promoted to canonical retrieval. Missing = not proven eligible. |
| `retrieval_priority` | Which pages should be read early by agents. |
| `status` | `active` = cross-linked and complete. `draft` = recently ingested, not yet fully integrated. `stale` = may be superseded. `needs-review` = flagged during lint. |
| `sources` | Quoted Obsidian links to raw source documents. Empty `[]` for synthesized pages. |
| `updated` | Date the page was last modified. Use to assess freshness. |
| `contradicted` tag | Page contains information that conflicts with another source. See the `## Contradictions & Debates` section on that page. |

---

## Tag Vocabulary

| Tag | Domain | Key pages |
|-----|--------|-----------|
| retrieval-augmented-generation | RAG | rag-for-knowledge-intensive-nlp, self-rag, hipporag |
| dense-retrieval | RAG | colbert-late-interaction, realm |
| agentic-rag | RAG/Agents | flare-active-retrieval, self-rag |
| language-agents | Agents | react, toolformer, cognitive-architectures |
| tool-use | Agents | toolformer, gorilla, autogen |
| multi-agent-systems | Agents | autogen, agentbench |
| llm-evaluation | Evaluation | llm-as-judge-mt-bench, g-eval, survey |
| llm-as-judge | Evaluation | llm-as-judge-mt-bench, g-eval, ragas |
| job-market-nlp | Job Market NLP | jobbert, skillspan, escoxlm-r |
| skill-extraction | Job Market NLP | skillspan, escoxlm-r |
| esco | Job Market NLP | escoxlm-r, jobbert |
| labor-economics | Labor Economics | frey-osborne, autor-levy-murnane, acemoglu-autor |
| automation | Labor Economics | frey-osborne, acemoglu-autor |
| career-development | Career | schein, newport, burnett-evans, bolles, tupper-ellis |
| deliberate-practice | Career | ericsson-1993, newport-2012 |
| career-theory | Career | holland-1985, schein-2021, newport-2012 |
| finops | FinOps / Cost | focus-2026-v1-4-finops-open-cost-usage-spec, finops-2026-framework-domains-capabilities, finops-capability-model |
| cloud-cost | FinOps / Cost | storment-fuller-2020-cloud-finops, focus-billing-schema, lakehouse-architecture |
| ai-cost | FinOps / Cost | unit-economics-cost-per-outcome, koenigstein-2026-ch11-agent-cost-efficiency, test-time-compute-scaling |
| unit-economics | FinOps / Cost | unit-economics-cost-per-outcome, finops-capability-model |
| lakehouse | Data Platform | armbrust-2020-delta-lake, armbrust-2021-lakehouse-architecture, acid-table-storage-layer |
| test-time-compute | AI Engineering | snell-2024-scaling-test-time-compute, muennighoff-2025-s1-simple-test-time-scaling, budget-forcing |
| reasoning | AI Engineering | deepseek-2025-r1-reasoning-rl, reinforcement-learning-verifiable-rewards, reasoning-distillation |
| reinforcement-learning | AI Engineering | deepseek-2025-r1-reasoning-rl, group-relative-policy-optimization |
| prompt-injection | Security / Agents | beurer-kellner-2025-design-patterns-securing-llm-agents, debenedetti-2025-camel-defeating-prompt-injections, agent-isolation-design-patterns |
| information-flow-control | Security / Agents | control-flow-integrity-for-agents, capability-based-tool-policy |
| alpha-decay | Quantitative Finance | mclean-2016-academic-research-destroy-predictability, post-publication-alpha-decay |
| replication | Quantitative Finance / Research Methods | hou-2020-replicating-anomalies, chen-2022-open-source-cross-sectional-asset-pricing, replication-vs-reproduction |
| transaction-costs | Quantitative Finance | novy-marx-2016-taxonomy-anomalies-trading-costs, net-of-cost-anomaly-capacity |
| experimental-design | Evals / Statistics | miller-2024-adding-error-bars-to-evals, eval-statistical-inference, eval-power-analysis |

_Check `wiki/index.md` tag registry for the full list with counts._

---

## What This Wiki Is Not

- Not a real-time data source. Information reflects ingested sources only.
- Not a search engine over `raw/`. The wiki is a synthesis; `raw/` is the archive.
- Not authoritative on topics with `confidence: low` or `status: needs-review` pages.
- Not fully source-fidelity reviewed across all legacy pages. Use **corpus-validation-report**.

---

## See Also

- **index** — master catalog of all wiki pages
- [[question-router]] — routing map for agents
- [[coding-agent-operating-card]] — compact default behavior card for coding agents
- [[agent-access-coding-corpus]] — canonical coding-agent access route for Claude Code, Codex, ChatGPT-style agents, and REST clients
- **project-context-manifests** — local project map for `~/Projects`
- [[corpus-governance]] — maturity and decision-grade use rules
- **corpus-validation-report** — current health snapshot
- **log** — chronological record of all operations
