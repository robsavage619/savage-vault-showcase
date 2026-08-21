---
type: overview
title: "Corpus Weekly Review Protocol"
summary: "Weekly maintenance protocol for savage_vault. Converts community weekly-review practice into concrete checks for source links, Bases, review queues, project manifests, stale claims, and agent retrieval surfaces."
tags: [meta, review, governance, maintenance]
sources: []
created: 2026-08-08
updated: 2026-08-08
status: active
aliases: ["weekly corpus review", "vault weekly review", "corpus review protocol"]
related: ["[[template-catalog]]", "[[source-fidelity-review-gate]]"]
confidence: high
domains: [governance]
source_kind: meta
authority_level: administrative
evidence_level: administrative
validation_status: validated
fidelity_status: not-applicable
index_eligible: true
retrieval_priority: high
symbolic_role: validation-report
evidence_lane: admin
requires_review: false
---

# Corpus Weekly Review Protocol

## Summary

Run this once a week, or after a large ingest. The goal is not polish; it is keeping the corpus useful, source-grounded, and easy for agents to navigate.

## Review Loop

1. Create a note from `_templates/weekly-corpus-review.md`.
2. Check frontmatter parse, missing raw source links, unresolved wiki links, active raw duplicate hashes, and Base YAML.
3. Open **corpus-gap-register** and close or update any items that changed.
4. Open **project-context-manifests** and review any project touched that week.
5. Open [[retrieval-pack-ai-engineering]] and confirm new coding-agent material has a task path, not just a long list entry.
6. Update **corpus-validation-report** only when checks have actually been run.
7. Append the result to **log**.

## Review Heuristics

- Prefer better routes over more notes.
- Promote a note only when it has sources, links, and a clear use.
- Do not bulk-stamp legacy notes as validated.
- If a note affects health, training, investing, career, or code changes, apply [[source-fidelity-review-gate]] or the coding-agent review checklist.

## See Also

- [[template-catalog]]
- **corpus-validation-report**
- **project-context-manifests**
