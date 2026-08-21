---
type: concept
title: "Replication vs Reproduction"
summary: "Reproduction re-derives a study's result from its own stated methodology; replication tests whether the finding survives a different, usually stricter, methodology. Conflating them makes contradictory-looking literatures — Chen & Zimmermann reproduce 98% of anomalies while Hou, Xue & Zhang find 65% fail replication, and both are correct."
tags: [research-methods, statistics, decision-science, quantitative-finance, evidence, validation]
sources: []
created: 2026-08-19
updated: 2026-08-19
status: active
aliases: ["reproduction vs replication", "is this study reproducible", "replication crisis definitions", "robustness vs reproduction", "why do replication studies disagree"]
related: ["[[claim-conflict-protocol]]", "[[source-fidelity-review-gate]]"]
confidence: high
domains: [research-methods, decision-science, statistics]
source_kind: synthesis
authority_level: synthetic
evidence_level: indirect
validation_status: reviewed
fidelity_status: source-checked
index_eligible: true
retrieval_priority: high
---

# Replication vs Reproduction

## Summary

Two different questions get asked with the same word, and the confusion produces literatures that appear to contradict each other when they do not.

- **Reproduction**: following the original paper's own stated methodology and data, do you get its number back? This tests arithmetic, code, and honesty.
- **Replication** (in the robustness sense): under a *different* and usually stricter methodology, does the finding survive? This tests whether the result was an artifact of the original's choices.

## How It Works

The asset-pricing case is the cleanest available illustration. **chen-2022-open-source-cross-sectional-asset-pricing** implements 319 predictors **following each original paper's own recipe** and finds **98% of the clearly-significant ones reproduce above `t = 1.96`**, with reproduced t-stats regressing on originals at slope 0.90, R² 0.83. **hou-2020-replicating-anomalies** re-runs 452 anomalies under **one imposed convention** — NYSE breakpoints and value-weighted returns — and finds **65% fail `|t| >= 1.96`**.

Both are right. The literature is arithmetically sound *and* heavily dependent on weighting choices that emphasize small illiquid stocks. The gap between 98% and 35% is a measurement of how much the published record leaned on microcaps.

## Why It Matters

**The two answer different decisions.** "Was this research conducted in good faith and is the code correct?" is a reproduction question. "Can I act on this?" is a replication question. Using a reproduction result to justify action is the most common misuse, and it is why "98% reproduce" gets quoted in contexts where it licenses nothing.

**Reproduction is a floor, not a finding.** Open data and code make reproduction cheap — see **raw-data-availability**. That is real progress in research infrastructure, and it says nothing about robustness.

**The choice of stricter methodology is itself contestable.** Hou-Xue-Zhang's NYSE-breakpoint convention is defensible for a tradable-capital question and is not neutral: it deliberately down-weights the segment where effects persist longest. A replication standard embeds a decision about what the result is *for*.

## Perspectives

The distinction generalizes well beyond any single field. Any model that reproduces perfectly on its original sample and fails to cross-validate on a new one is showing the same structure.

For vault practice, this maps onto the existing maturity vocabulary. `fidelity_status` is about whether the note faithfully represents the source — a reproduction-shaped question. `validation_status: disputed` is where replication disagreement belongs, per [[claim-conflict-protocol]].

## Related Concepts

- **out-of-sample-testing** · **selective-reporting** · **raw-data-availability**
- **post-publication-alpha-decay** — a third distinct reason a finding stops holding
- [[source-fidelity-review-gate]] — where this distinction is operationalized in the vault

## See Also

- **compare-anomaly-replication-vs-decay**
- **hou-2020-replicating-anomalies**
- **chen-2022-open-source-cross-sectional-asset-pricing**
- [[claim-conflict-protocol]]
