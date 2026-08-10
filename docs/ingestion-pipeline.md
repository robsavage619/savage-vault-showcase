# Ingestion Pipeline

The private vault uses source-specific ingestion instead of one generic “summarize this file” pass.

## Ingestion layers

| Layer | Output |
|---|---|
| Raw source intake | private `raw/` file, excluded from showcase |
| Book or paper hub | source identity, scope, chapter/section map |
| Source-summary notes | reviewed extraction for agent use |
| Concept cards | reusable decision rules synthesized from sources |
| Retrieval-pack wiring | task routes that point agents at the right notes |
| Validation pass | metadata, links, raw-source references, and index checks |

## Depth policy

The system does not create chapter notes mechanically. It creates deeper notes where retrieval grain changes agent behavior.

Examples of high-value deep notes:

- a data-contract boundary note for pipeline changes
- a schema-evolution note for migrations and consumers
- an MLOps drift-monitoring note for model-serving work
- a positioning note for marketing strategy
- a sponsorship-evaluation note for claims about brand impact

Thin chapter summaries are avoided unless the chapter has a distinct decision role.

## Source maturity

Every mature note carries fields like:

- `validation_status`
- `fidelity_status`
- `retrieval_priority`
- `symbolic_role`
- `evidence_lane`
- `approved_use`
- `prohibited_use`

These fields tell agents how the note may be used.

## Public showcase boundary

The actual raw sources and source-derived summaries are not included here. The examples in `samples/` are synthetic and redacted to demonstrate structure only.

