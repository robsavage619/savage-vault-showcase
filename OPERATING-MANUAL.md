---
type: overview
title: "Wiki Operating Manual"
summary: "Schema and workflow document for the LLM that maintains this wiki. Defines directory structure, frontmatter conventions, page types, naming rules, and step-by-step workflows for ingest, query, and lint operations."
tags: [meta, schema]
sources: []
created: 2026-04-19
updated: 2026-08-09
status: active
---

# Wiki Operating Manual

You are the maintainer of this wiki. You read `raw/` but never write to it. You own `wiki/` entirely — create, update, and cross-link pages freely. This file defines every convention you need.

**Before any operation:** read this file in full, then read `START HERE.md`, `wiki/agent-entry.md`, and `wiki/question-router.md`. For coding-agent or software-engineering work, also read `wiki/coding-agent-operating-card.md` and `wiki/agent-access-coding-corpus.md` before answering or editing. For sports-business, sponsorship, brand, marketing, pricing, ranking, or product-experiment work, also read `wiki/sports-business-operating-card.md` before recommending strategy, metrics, valuation, or causal claims.

---

## 1. Vault Structure

```
raw/          Read-only. Source documents: articles, papers, PDFs, images,
              data files. Never modified by LLM. Filenames preserved as dropped.

START HERE.md Human and agent front door. Opens the core router, short index,
              validation report, coding-agent route, and sports-business route.

wiki/         LLM-generated knowledge pages. You own this entirely.
              All files: lowercase kebab-case .md

wiki/bases/    Obsidian Bases (.base files) — self-updating views over page
               frontmatter (by-type, recently-updated, review-queue). Embedded
               at the top of index.md. Render only in Obsidian; RAG readers skip
               them. Not wiki pages — no frontmatter required.

wiki/index.md  Master catalog. Updated on every ingest. Tier-1 RAG cache.
               Agents read this first; it contains inline summaries of every page.

wiki/log.md    Append-only operation record. One H2 entry per operation.
               Never edit past entries.

wiki/agent-entry.md  Orientation for external agents querying the wiki cold.
                     Keep up to date as the wiki grows.

wiki/question-router.md  Routing map for agents. Read before answering from the
                         corpus.

wiki/coding-agent-operating-card.md  Default behavior card for coding agents:
                                    classify work, retrieve the right playbook,
                                    inspect repo evidence, validate honestly.

wiki/agent-access-coding-corpus.md  Shared access guide for Claude Code, Codex,
                                    ChatGPT-style agents, and Obsidian REST
                                    clients using the coding-agent corpus.

wiki/sports-business-operating-card.md  Default behavior card for sports-business,
                                        sponsorship, brand, marketing, pricing,
                                        ranking, and experiment questions.

wiki/corpus-governance.md  Operating contract for maturity, review, and
                           decision-grade use.

wiki/corpus-validation-report.md  Latest health-check snapshot. It may contain
                                  known non-green items; do not claim full
                                  maturity unless this report supports it.

CLAUDE.md     This file. Update only when the user extends the schema.
```

`Welcome.md` at the vault root is an Obsidian default — ignore it.

---

## 2. Frontmatter Schema

Every wiki page requires this frontmatter. Obsidian Bases and Dataview compatible.

**Required fields:**

```yaml
---
type: source-summary | entity | concept | comparison | analysis | overview | book-overview | research-finding | project-context-manifest | corpus-review
title: "Human-readable title"
summary: "2–3 sentences. Self-contained. Answers: what is this page and what
          is the single most important thing it says. Written for an agent that
          may read only this field and nothing else."
tags: [tag1, tag2]          # lowercase, hyphenated; check tag registry in index.md first
sources: ["raw/filename.ext as a quoted Obsidian raw-file wikilink"] # quoted Obsidian links to raw/ source(s), or [] for synthesized
created: YYYY-MM-DD         # set once, never change
updated: YYYY-MM-DD         # set to today on every edit
status: draft | active | stale | needs-review
---
```

**Optional fields** (add when relevant):

```yaml
aliases: ["alternate name", "abbreviation", "common search term"]
related: ["**concept-a**", "**concept-b**"]   # quoted wikilinks — visible to graph, backlinks, Bases file.hasLink(). Quoting is required in YAML flow lists.
confidence: high | medium | low     # for analysis/synthesis pages
supersedes: old-page-slug           # if this page replaces another
```

**Decision-grade fields** (new pages and reviewed legacy pages):

```yaml
domains: [ai-engineering, exercise-science, sleep-science, sabermetrics, quantitative-finance, career, decision-science]
source_kind: primary-study | review | book | benchmark | first-party-analysis | synthesis | reference | meta
authority_level: primary | secondary | tertiary | synthetic | administrative
evidence_level: direct | indirect | mechanistic | expert-opinion | anecdotal | administrative
validation_status: unreviewed | reviewed | validated | disputed | deprecated
fidelity_status: unreviewed | abstract-only | source-checked | quote-checked | full-text-checked | not-applicable
index_eligible: true | false
retrieval_priority: critical | high | normal | low | archive
approved_use: ["orientation", "draft-synthesis", "decision-support"]
prohibited_use: ["medical-advice", "financial-advice", "standalone-prescription"]
review_due: YYYY-MM-DD
```

Legacy pages missing these fields are `legacy-unreviewed` for decision-grade use.
They may be used for orientation and synthesis, but not as final authority for
health, training, investing, finance, or career prescriptions until reviewed.

**`summary` field rules:**
- Must be self-contained — no "as described above", no assumed context
- Must answer "what is this?" in the first sentence
- 2–3 sentences maximum; longer summaries belong in the `## Summary` section
- Written for machine triage: precise, specific, no filler

**`status` transitions:**
- `draft` → set on creation; page exists but cross-links incomplete
- `active` → promoted once cross-links are in place and summary is finalized
- `stale` → set during lint when content may be superseded
- `needs-review` → set during lint when contradictions or gaps found
- Operational surface: `wiki/bases/review-queue.base` auto-lists pages that are non-`active`, non-`high` confidence, or unedited for 180+ days — the standing queue lint works from.

---

## 3. Page Types

**`source-summary`**
One page per document in `raw/`. Sections: Overview · Key Claims · Data & Figures · Methodology (research) or Structure (other) · Limitations & Caveats · Seeds · See Also.
_Seeds_ = list of entity/concept pages this source touches or should touch, even if they don't exist yet. This drives the entity/concept update step during ingest.

**`entity`**
A specific named thing: person, organization, product, dataset, location, artifact.
Sections: Summary · Attributes · Timeline (mentions across sources, with citations) · Open Questions · See Also.
Filename: canonical name in kebab-case (`openai.md`, `attention-mechanism.md`).

**`concept`**
An abstract idea, technique, method, or domain area.
Sections: Summary · How It Works · Why It Matters · Perspectives (how different sources treat it; note disagreements) · Related Concepts · See Also.
Filename: concept name in kebab-case.

**`comparison`**
Structured side-by-side of 2+ entities or concepts. Created when a query or ingest reveals a meaningful distinction worth preserving.
Sections: Summary · Comparison Table · Synthesis · See Also.
Filename: `compare-X-vs-Y.md`.

**`analysis`**
Answer to a specific question, synthesized across multiple sources. Created when a query answer is good enough to file permanently.
Sections: Summary · Question (in bold) · Sources Consulted · Synthesis · Confidence Assessment · See Also.
Filename: question-slug (`why-does-X-happen.md`, `impact-of-X-on-Y.md`).

**`overview`**
Topic map for a major domain area. At most one per major topic. Create when 5+ entity/concept pages exist in an area.
Sections: Summary · Orientation · Key Pages · Open Questions · Suggested Reading Order · See Also.
Filename: `overview-<topic>.md`.

**`book-overview`**
Hub page for a multi-chapter book whose chapters are ingested as individual `source-summary` pages. One per book. Acts as the parent that links its chapter summaries.
Sections: Summary · Scope & Audience · Chapter Map (linked list of chapter pages) · Key Themes · Why This Book · Seeds · See Also.
Filename: `<author>-<year>-<short-title>.md` (e.g. `attia-2023-outlive.md`). Chapter pages use `<author>-<year>-ch<N>-<slug>.md` and set `parent:`/`chapter:` frontmatter pointing back to the hub.

**`research-finding`**
Rob's own original empirical test or experiment — not a synthesis of external sources but a first-party analysis run against vault data. Distinct from `analysis` (which answers a question by synthesizing existing pages).
Sections: Summary · Thesis Under Test · Rounds/Method (one H2 per analytical round) · Conclusions · Methodology References · Files · Status · See Also.
Filename: descriptive kebab slug, optionally namespaced (e.g. `trade-eval--<name>.md`).

**`project-context-manifest`**
Agent-facing card for one local project under `~/Projects`. Sections: Summary · Project Path · Read First · Stack · Vault Context · Agent Rules · Open Questions · See Also.
Filename: `project-<repo-name>-context-manifest.md`.

**`corpus-review`**
Weekly or ad-hoc vault maintenance note created from `_templates/weekly-corpus-review.md`. Sections: Summary · Checks · New / Changed Surfaces · Project Context · Gaps · Decisions · Next Actions.
Filename: `corpus-review-YYYY-MM-DD.md` or similar.

---

## 4. Page Structure Convention

Every page follows inverted pyramid — most important information first. This ensures
the first chunk is always informative when a RAG system splits the page.

**Mandatory section order:**
1. YAML frontmatter
2. `## Summary` — self-contained, ≤150 words. Must stand alone without the rest of the page.
3. Type-specific sections (from Section 3 above)
4. `## See Also` — Obsidian wikilinks to related pages. An equivalent final cross-link section satisfies this: concept pages may use `## Related Concepts`/`## Related Prescriptions`, and `book-overview` pages use `## Seeds` + `## Chapter Map`. Lint counts any of these as the required outgoing-link section; only a page with **no** cross-link section at all is a gap.

The `## Summary` body should mirror the frontmatter `summary` field but can be slightly longer. Both must be independently coherent.

---

## 5. Naming & Size

**Filenames:** lowercase, kebab-case, `.md`, no dates, no spaces or underscores.
- Entity: canonical name → `geoffrey-hinton.md`
- Concept: concept name → `reinforcement-learning.md`
- Source summary: stem of raw filename, kebab-cased → raw `Attention_Is_All_You_Need.pdf` → `wiki/attention-is-all-you-need.md`
- Comparison: `compare-<a>-vs-<b>.md`
- Analysis: question-slug, max 6 words
- Overview: `overview-<topic>.md`

**Page size:**
- Entity / concept leaf pages: target 300–600 words, hard cap 900 words
- Source-summaries of dense book chapters or research papers: target 900, soft 1,500, hard cap 2,500 words (their density is inherent; splitting a single chapter fragments it). Non-dense source-summaries stay at the 900 cap. A page over 2,500 that covers a whole book (not one chapter) should become a `book-overview` hub with per-chapter pages; a single dense chapter over cap should be trimmed, not fragmented.
- Comparison, analysis, and research-finding pages: up to 1,500 words
- If a page exceeds its hard cap: split into sub-pages and create a hub (`book-overview` for a book, `overview-<topic>` for a domain)

**Aliases:** Include common search terms, abbreviations, and synonyms an agent might search for — not just alternate proper names. Example for `attention-mechanism.md`:
```yaml
aliases: ["self-attention", "scaled dot-product attention", "multi-head attention", "transformer attention"]
```

---

## 6. Cross-Referencing Rules

- Use Obsidian wikilinks (double bracket, filename stem) for all internal page links. Obsidian resolves these natively.
- Every wiki page must have ≥1 outgoing Obsidian wikilink except the very first page created.
- Do not use bare markdown links `[text](path)` for internal pages — Obsidian wikilinks only.
- For external URLs: standard markdown `[text](url)`.
- Entity and concept pages must link to every source-summary page that mentions them.
- Source-summary pages must link to every entity and concept page in their Seeds list.
- **Bidirectional hygiene:** when you link page A → page B, add a mention of A in page B's body. Obsidian's backlinks panel catches these, but text should stand alone.

---

## 7. Contradiction Handling

When two sources make conflicting claims:

1. Do not silently pick one. Represent both.
2. Add `## Contradictions & Debates` section to the entity or concept page.
3. Format: name the claim, cite source A (`source-a` says X), cite source B (`source-b` says Y), add a note on which interpretation is better supported or why they may differ.
4. Set `confidence: low` or `confidence: medium` on that page's frontmatter.
5. Add tag `contradicted` to both the entity/concept page and both source-summary pages.
6. Annotate the log entry: `## [YYYY-MM-DD] ingest | Title [contradiction: entity-slug]`

For decision-grade use, also apply `wiki/claim-conflict-protocol.md` and set
`validation_status: disputed` until reviewed.

---

## 7b. Corpus Maturity Layer

The vault now uses an explicit maturity layer:

- `wiki/corpus-governance.md` — operating contract
- `wiki/metadata-schema.md` — extended frontmatter
- `wiki/index-promotion-manifest.md` — canonical retrieval eligibility
- `wiki/source-fidelity-review-gate.md` — evidence review procedure
- `wiki/question-router.md` — retrieval routing
- `wiki/corpus-gap-register.md` — known gaps, unresolved links, review backlog
- `wiki/corpus-validation-report.md` — latest health snapshot

`status: active` means the page is readable and integrated. It does not mean the
claims are source-fidelity reviewed. Use `validation_status` and
`fidelity_status` for that.

Reusable Obsidian templates live in `_templates/`; the core Templates plugin is
configured via `.obsidian/templates.json`. See `wiki/template-catalog.md`.

---

## 8. Agent Interface (REST API)

The Obsidian Local REST API plugin (v3.6.1) serves this vault over **HTTPS on port 27124**.
The insecure HTTP server (port 27123) is disabled. All requests require an API key header.

**Authentication:** Every request needs `Authorization: Bearer <key>`.
The key is in `.obsidian/plugins/obsidian-local-rest-api/data.json` → `apiKey` field.
Do not hardcode the key in wiki pages or commit it to git.

**TLS:** The cert is self-signed. Agents must either accept it (`--insecure` / `verify=False`)
or trust the cert at `~/.obsidian-local-rest-api.crt` if exported.

```
# Tier-1: read the master index
GET https://localhost:27124/vault/wiki/index.md
Authorization: Bearer <key>

# Read a specific page
GET https://localhost:27124/vault/wiki/{slug}.md
Authorization: Bearer <key>

# Full-text search
POST https://localhost:27124/search/simple/?query=<term>
Authorization: Bearer <key>

# List wiki pages
GET https://localhost:27124/vault/wiki/
Authorization: Bearer <key>
```

**Python snippet:**
```python
import requests
BASE = "https://localhost:27124"
HEADERS = {"Authorization": "Bearer <key>"}
index = requests.get(f"{BASE}/vault/wiki/index.md", headers=HEADERS, verify=False).text
```

Keep `wiki/agent-entry.md` up to date — it is the first page external agents read.
When the wiki's domain changes significantly, update the domain description in that page.

**Coding-agent access route:** for code, architecture, validation, data-system, or production-readiness questions, use
`CLAUDE.md -> START HERE.md -> wiki/agent-entry.md -> wiki/question-router.md -> wiki/coding-agent-operating-card.md -> wiki/agent-access-coding-corpus.md -> wiki/retrieval-pack-ai-engineering.md -> task-specific playbook -> source notes`.

**Sports-business access route:** for sponsorship, brand, pricing, ranking, marketing-metrics, or product-experiment questions, use
`CLAUDE.md -> START HERE.md -> wiki/agent-entry.md -> wiki/question-router.md -> wiki/sports-business-operating-card.md -> wiki/retrieval-pack-sports-business-marketing.md -> task-specific playbook -> extraction note -> source hub -> raw source when needed`.

---

## 9. Ingest Workflow

**Trigger:** user drops a file in `raw/` and says "ingest" or similar.

**Step 1 — Read and discuss.**
Read the source document. Before writing anything, state in chat: the source type, its central argument in one sentence, and 3–5 key takeaways. Ask if there are aspects to emphasize. Wait for "proceed" or direction.

**Step 2 — Create the source-summary page.**
File: `wiki/<kebab-cased-source-name>.md`. Sections per Section 3. Set `status: draft`.

**Step 3 — Update or create entity/concept pages.**
Work through the Seeds list from the source-summary page:
- Page exists → add paragraph/bullet under relevant section, update `sources` field, update `updated` date
- Page doesn't exist → create it with the appropriate type template, `status: draft`
- One ingest typically touches 5–15 pages

**Step 4 — Update `wiki/index.md`.**
Add entry for the source-summary page. Update entries for materially changed entity/concept pages. Use the rich inline summary format (see Section 12). Update Stats block. Update tag registry if new tags were used.

**Step 4b — Update `wiki/index-short.md` and overviews.**
The tier-0 short index is read first by the query workflow (Section 10), so it must not lag `index.md`. Add a one-line hook under the matching domain section for each new page. Then, if an `overview-<domain>` page exists for this ingest's area, add the new page(s) to its Key Pages and bump its `updated`; if the ingest pushes a domain past 5+ pages with no overview, create one (Section 3). Bases (`wiki/bases/`) need no action — they auto-update from frontmatter. Reminder: every new page's `related:` field must use quoted wikilinks, never bare slugs.

**Step 5 — Update `wiki/agent-entry.md`.**
If the domain description needs updating (new topic area added), update it. Update the tag vocabulary table with any new tags.

**Step 6 — Append to `wiki/log.md`.**
`## [YYYY-MM-DD] ingest | <Title> [new-pages: N] [updated-pages: N]`

**Step 7 — Report.**
State in chat: pages created, pages updated, any contradictions found.

---

## 10. Query Workflow

**Trigger:** user asks a question about the knowledge base.

**Tier-0 — Router + short index (read first, always).**
Read `wiki/question-router.md`, then `wiki/index-short.md`. One-sentence hooks for every page. If the hooks answer the question and the stakes are low: respond with page-stem citations, done.

**Coding-agent route.**
For code, architecture, validation, data-system, or production-readiness questions, read `wiki/coding-agent-operating-card.md` and `wiki/agent-access-coding-corpus.md` before the short index. They route Claude Code, Codex, ChatGPT-style agents, and Obsidian REST clients through the same coding-agent corpus.

**Tier-1 — Full index scan.**
Read the relevant category section(s) of `wiki/index.md`. Full summaries. If summaries answer: respond, done.

**Tier-2 — Page reads.**
Read each relevant wiki page. Note `sources` field for tracing to raw documents. Read raw documents only if the wiki page lacks needed detail.

**Tier-3 — Synthesize.**
Answer in chat with inline citations. Be explicit about what is known (high confidence), inferred (medium), unknown, legacy-unreviewed, or source-fidelity reviewed.

**High-stakes gate.**
For health, training, investing, finance, medical, or career decisions, apply
`wiki/source-fidelity-review-gate.md` before making a recommendation. If the
evidence is abstract-only, disputed, stale, or legacy-unreviewed, say so.

**Filing decision.**
If the answer required synthesizing 3+ pages in a non-obvious way: create an `analysis` page. Single-page lookups do not need filing.

**If filing:**
- Create the analysis page
- Update `wiki/index.md` with the new entry
- Update `wiki/agent-entry.md` if this reveals a new domain area
- Append `## [YYYY-MM-DD] query | <question-slug> [filed]` to log

---

## 11. Lint Workflow

**Trigger:** user says "lint" or "health check."

**Step 1 — Read everything.**
Read `wiki/index.md` in full, then read every page listed in it.

**Step 2 — Check each issue type:**

| Issue | Detection | Action |
|-------|-----------|--------|
| Missing `summary` field | Frontmatter lacks `summary` | Flag; highest priority fix |
| Pages exceeding 900 words | Word count > 900 on leaf pages | Propose split |
| Orphan pages | Pages in wiki/ not in index.md | Add to index, or propose deletion |
| Broken index entries | index.md entries with no matching file | Flag as broken |
| Stale pages | `updated` date > 6 months behind newest ingest | Set `status: stale` |
| Missing cross-references | Entity/concept named in body but no Obsidian wikilink | Add the link |
| Undocumented contradictions | `contradicted` tag but no `## Contradictions` section | Add the section |
| Missing concept pages | Important concepts named in source-summaries but no page exists | List as gap |
| Missing maturity fields | Page lacks `validation_status`/`fidelity_status` | Treat as legacy-unreviewed; upgrade only during review |
| Unsupported prescription | Prescriptive language on abstract-only or unreviewed evidence | Route to source-fidelity review |
| Broken wikilinks | A wikilink has no page | Add to `corpus-gap-register.md` or resolve with a real page |

**Step 3 — Report in chat.** Counts per issue type, specific files affected, suggested new sources for gaps.

**Step 4 — Do not auto-fix.** Present findings; apply only fixes the user confirms.

Exception: purely mechanical schema repairs that unblock parsing, such as quoting
URLs in YAML source lists, may be fixed during a maturity pass and logged.

**Step 5 — Append to log:** `## [YYYY-MM-DD] lint | wiki health check`

---

## 12. Index Format

Each entry uses the rich inline summary format:

```markdown
- page-slug `type` `updated: YYYY-MM-DD`
  > Summary text (identical to frontmatter summary field). Self-contained, 2–3 sentences.
```

- Categories are not fixed — add new ones as the wiki grows
- Within each category: ordered by `updated` descending (most recently touched first)
- The inline summary must match the page's frontmatter `summary` field exactly
- Do not add pages to the index until their `## Summary` section and frontmatter `summary` field exist

---

## 13. Log Format

Each entry is an H2 with this exact pattern:

```markdown
## [YYYY-MM-DD] <operation> | <title> [optional-annotations]
```

Valid operations: `ingest` `query` `lint` `edit` `delete` `schema-update`

- `ingest`: source title
- `query`: short question slug
- `lint`: always "wiki health check"
- `edit`: page slug edited
- `delete`: page slug deleted
- `schema-update`: description of change

Optional annotations: `[new-pages: N]` `[updated-pages: N]` `[contradiction: slug]` `[filed]`

Entries are append-only. Multi-line notes under an entry are allowed (bullets), but keep them brief. The log is a record, not documentation.

**Search:** `grep "^## \[" wiki/log.md` — returns all entries chronologically.

---

## 14. Schema Extension Guide

To evolve this schema without losing LLM consistency:

- **New page type:** add to Section 3 with description and filename pattern; add to Section 14 quick-reference card
- **New frontmatter field:** add to Section 2 table with type, valid values, required/optional
- **New workflow:** add a section following the numbered-step format of Sections 9–11
- **New lint check:** add a row to the table in Section 11
- Always update the `updated` date in this file's frontmatter
- Log it: `## [YYYY-MM-DD] schema-update | <description>`

---

## Quick-Reference Card

```
OPERATIONS
  ingest  → discuss → source-summary page → entity/concept pages → index → agent-entry → log
  query   → question-router → index-short → index.md → page reads → fidelity gate if high-stakes → synthesize
  lint    → read all → report schema/link/source/maturity issues → update validation report → log

PAGE TYPES
  source-summary  entity  concept  comparison  analysis  overview  book-overview  research-finding

SECTION ORDER (every page)
  frontmatter → ## Summary (≤150 words, self-contained) → type-specific sections → ## See Also

NAMING
  kebab-case-lowercase.md  |  compare-X-vs-Y.md  |  overview-topic.md

PAGE SIZE
  entity/concept: 300–600 target, 900 cap  |  chapter/paper source-summary: 900 target, 2,500 cap  |  analysis/comparison/research-finding: up to 1,500

FRONTMATTER (required)
  type  title  summary  tags  sources  created  updated  status

INDEX ENTRY FORMAT
  - page-slug `type` `updated: YYYY-MM-DD`
    > inline summary (= frontmatter summary field)

LOG ENTRY FORMAT
  ## [YYYY-MM-DD] <operation> | <title> [annotations]

AGENT INTERFACE (HTTPS, port 27124, Bearer token required)
  GET  https://localhost:27124/vault/wiki/index.md
  GET  https://localhost:27124/vault/wiki/{slug}.md
  POST https://localhost:27124/search/simple/?query=<term>

NEVER
  Write to raw/  |  Edit past log entries  |  Create pages without frontmatter summary  |  Auto-fix during lint
```
