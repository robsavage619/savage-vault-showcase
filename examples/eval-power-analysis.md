---
type: concept
title: "Power Analysis for Evals"
summary: "Deciding before you build an eval whether it can detect the difference you care about. Most small hand-built domain evals cannot resolve anything under 10-15 points, which means they are run, reported, and used to justify decisions they never had the power to support."
tags: [evals, statistics, experimental-design, measurement, ai-engineering, decision-science]
sources: []
created: 2026-08-19
updated: 2026-08-19
status: active
aliases: ["eval power analysis", "how many eval questions do I need", "minimum detectable effect", "eval sample size", "is my eval big enough"]
related: ["[[eval-statistical-inference]]", "[[corpus-agent-evaluation-suite]]"]
confidence: high
domains: [evals, statistics, decision-science]
source_kind: synthesis
authority_level: synthetic
evidence_level: indirect
validation_status: reviewed
fidelity_status: source-checked
index_eligible: true
retrieval_priority: high
---

# Power Analysis for Evals

## Summary

Before building an eval, ask what difference would change your decision, and whether an eval of the size you are planning could detect it. **miller-2024-adding-error-bars-to-evals** makes this one of its five recommendations and supplies the sample-size formula. It is the recommendation most often skipped, and the one that would prevent the most wasted work.

## How It Works

Four quantities, one of which is usually left implicit and shouldn't be:

1. **The minimum difference worth acting on.** Not the difference you hope to see — the one that would change what you do. If a 2-point gain would not change the decision, do not design to detect 2 points.
2. **Question-level variance**, estimable from a pilot run or from the binomial approximation for pass/fail scoring.
3. **The sample size** — and, with resampling, the number of samples per question.
4. **Acceptable error rates**, conventionally 5% false positive and 20% false negative.

Fix any three and the fourth follows. The usual mode is fixing the difference you care about and solving for `n`.

The arithmetic is unforgiving. Detecting a 5-point difference between two models on pass/fail questions needs several hundred questions unpaired. Paired analysis reduces this materially — often the difference between feasible and not — which is why the paired-versus-unpaired choice in [[eval-statistical-inference]] belongs in the *planning* stage, not the analysis stage.

## Why It Matters

**The dominant failure is the underpowered domain eval.** Fifty hand-written questions, built with care, that cannot resolve anything smaller than a 15-point gap. It gets run, a 4-point difference appears, and a decision is made on it. The eval was never capable of answering the question, and nothing about its output says so.

**Power analysis is cheap and comes first.** The calculation takes minutes; building the eval takes days. Discovering after the fact that the instrument was too blunt is the expensive ordering.

**It reframes eval-building as a measurement investment.** How much evidence is worth buying is **value-of-information** and **hubbard-2010-ch7-value-of-information** territory — the question is not "is this eval good" but "does this eval reduce enough uncertainty to be worth building."

## Perspectives

Sometimes the honest answer is that the eval cannot be made big enough, and then the finding itself is useful: this decision cannot be made on this evidence, so make it on something else — a qualitative review, a staged rollout, an online experiment where `n` is not the constraint.

Power analysis assumes you can name the effect size you care about. When nobody can, that is the real gap, and it is a product question rather than a statistical one — see **decision-oriented-measurement**.

## Related Concepts

- [[eval-statistical-inference]] — the analysis-side companion
- **value-of-information** · **decision-oriented-measurement**
- **effect-size**

## See Also

- **miller-2024-adding-error-bars-to-evals**
- [[corpus-agent-evaluation-suite]] — a 75-case suite that should be power-checked before it is trusted
- **kohavi-tang-xu-2020-trustworthy-online-controlled-experiments**
