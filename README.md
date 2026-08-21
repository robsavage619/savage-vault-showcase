# savage-vault-system

The operating system for a personal knowledge corpus that an LLM agent maintains and retrieves from — schema, governance, routing, and validation.

This repository contains **the system, not the corpus.** The corpus it governs is private: ~1,400 markdown pages covering AI engineering, software architecture, quantitative finance, sports analytics, and health science. What's published here is the machinery that keeps a corpus that size honest and retrievable — the part that's transferable.

## The problem

An LLM with a large personal knowledge base has two failure modes that get worse as the corpus grows.

**Retrieval gets slower and less accurate.** At 1,400 pages, "search the vault" means dumping a lot of irrelevant context. Semantic search alone doesn't fix it, because the model still has to decide what's authoritative.

**Editorial completeness gets confused with evidentiary quality.** A page can be well-written, cross-linked, and wrong — or right about a study whose abstract was read but whose methods weren't. Without a distinction between "this note exists and is integrated" and "this claim has been checked against its source," an agent will cite a half-read paper with the same confidence as a verified one.

This system addresses both.

## Design

### 1. A tiered retrieval ladder, not a search

Agents route before they read. The [question router](docs/question-router.md) maps a query type to a starting surface; a one-line-per-page short index answers most questions without opening a page at all.

```
router → retrieval pack → short index → full index → page → raw source
```

Each rung is opened only if the previous one was insufficient. Most queries stop at rung two. A [retrieval pack](playbooks/retrieval-pack-ai-engineering.md) is a curated routing document for one domain — reading order, task paths, and use rules that constrain how the evidence may be applied.

### 2. Evidence grading in frontmatter

Every page carries machine-readable maturity metadata, defined in the [metadata schema](docs/metadata-schema.md):

| Field | Answers |
|---|---|
| `source_kind` | primary study, review, book, benchmark, synthesis, reference |
| `authority_level` | primary, secondary, tertiary, synthetic, administrative |
| `evidence_level` | direct, indirect, mechanistic, expert-opinion, anecdotal |
| `validation_status` | unreviewed, reviewed, validated, **disputed**, deprecated |
| `fidelity_status` | abstract-only → source-checked → quote-checked → full-text-checked |
| `approved_use` / `prohibited_use` | what this page may and may not be cited for |

The key separation: **`status: active` means the page is integrated. It says nothing about whether the claims were verified.** That's `validation_status` and `fidelity_status`, and they move independently.

`fidelity_status: abstract-only` is the field that does the most work in practice. It marks a note written from an abstract the author never read past — legitimate for orientation, disqualifying for a prescription.

### 3. A gate for high-stakes claims

The [source fidelity review gate](docs/source-fidelity-review-gate.md) blocks decision-grade answers in domains where being wrong changes behavior. Pages that haven't cleared it can still be used for orientation and synthesis — they just can't be the final authority.

### 4. Contradictions are represented, not resolved

When two sources disagree, the [claim conflict protocol](docs/claim-conflict-protocol.md) requires both to be stated, both source notes tagged, and `validation_status: disputed` set on each. The system is explicitly designed **not** to silently pick a winner.

A worked example ships in [`examples/replication-vs-reproduction.md`](examples/replication-vs-reproduction.md): two studies of the same literature report 98% success and 65% failure. Both are correct — they asked different questions. The concept card exists so an agent retrieving either one finds the reconciliation rather than the headline.

### 5. Agents get behavior cards, not just documents

A [coding-agent operating card](playbooks/coding-agent-operating-card.md) tells an agent how to classify the work, which playbook to retrieve, what repo evidence to inspect before making claims, and how to validate honestly. Task-specific playbooks cover [safe changes](playbooks/coding-agent-safe-change-playbook.md), [validation](playbooks/coding-agent-validation-playbook.md), [data systems](playbooks/coding-agent-data-system-playbook.md), and [production readiness](playbooks/coding-agent-production-readiness-playbook.md).

The [review checklist](playbooks/coding-agent-review-checklist.md) is the acceptance gate.

### 6. Known gaps are tracked, not hidden

A [gap register](docs/corpus-governance.md) records what's unreviewed, unresolved, or unverified, and a validation report snapshots corpus health. **Neither is allowed to claim the corpus is healthier than it is** — a recent entry corrects an earlier one that understated an unresolved-link count by two orders of magnitude.

An [evaluation suite](docs/corpus-agent-evaluation-suite.md) and [judge rubric](docs/corpus-agent-judge-rubric.md) exist to test retrieval quality. The register openly records that the suite has never been run.

## Layout

```
OPERATING-MANUAL.md   the full conventions doc the maintaining agent reads first
CONTENT-BOUNDARY.md   what is and isn't published here, and how that's enforced
docs/                 schema, governance, routing, review gates, evaluation
playbooks/            operating cards, task playbooks, retrieval packs
examples/             representative concept cards showing the format
bases/                Obsidian Bases — live views over frontmatter
templates/            page templates for each type
schemas/              JSON Schema for page frontmatter
scripts/              corpus health check, leak guard, frontmatter check
```

## Health check

`scripts/corpus_health.py` validates frontmatter, required fields, unresolved wikilinks, missing source files, and page-size caps.

```bash
uv run --with pyyaml python scripts/corpus_health.py /path/to/vault
```

On the private corpus it currently reports, across 1,398 pages:

```
    0  frontmatter parse errors
    0  missing or empty required fields
    0  missing source files
  137  unresolved wikilinks in "Seeds" lines
   95  pages with no cross-link section
   48  pages over their per-type size cap
    2  genuinely broken body wikilinks
```

The schema layer is clean; the link hygiene is not. Those numbers are published rather than rounded off because a health check that only reports what passes isn't one — and the corpus governance documents here explicitly forbid claiming the corpus is healthier than it is.

## The boundary is a test, not a promise

The vault this system maintains contains health, financial, relationship, and employer material. Keeping it out of a public repository is not something a `.gitignore` can guarantee — git history is permanent, so an ignore rule added later leaves the files in every prior commit.

This repository therefore has an entirely separate history, and the boundary is enforced in CI. `scripts/leak_guard.py` fails the build on forbidden terms, on structural patterns that indicate vault content (`sources:` frontmatter pointing at raw files), and on credential shapes. It runs on every push.

Building it immediately caught four domain labels and one path that manual review had missed — which is the argument for having it.

See [CONTENT-BOUNDARY.md](CONTENT-BOUNDARY.md).

## What isn't here

The corpus itself — source summaries, book chapter notes, first-party research, and all personal material — stays private. Page summaries derived from copyrighted books are not published. This repository is deliberately a separate git history from the vault, so no corpus content exists in it at any commit.

## License

MIT. See [LICENSE](LICENSE).
