---
type: concept
title: "Statistical Inference for Evals"
summary: "Evals are experiments, so eval differences need standard errors. Four techniques carry most of the value: CLT standard errors, clustered SEs when questions come in related groups, paired question-level comparison between models (a free variance reduction), and variance reduction by resampling answers."
tags: [evals, statistics, ai-engineering, experimental-design, measurement, decision-science, llm]
sources: []
created: 2026-08-19
updated: 2026-08-19
status: active
aliases: ["eval error bars", "eval standard errors", "is this benchmark difference real", "clustered standard errors evals", "paired eval comparison", "eval confidence intervals"]
related: ["[[eval-power-analysis]]", "[[corpus-agent-evaluation-suite]]", "[[coding-agent-validation-playbook]]"]
confidence: high
domains: [evals, statistics, ai-engineering, decision-science]
source_kind: synthesis
authority_level: synthetic
evidence_level: indirect
validation_status: reviewed
fidelity_status: source-checked
index_eligible: true
retrieval_priority: critical
---

# Statistical Inference for Evals

## Summary

An eval is an experiment on a sample of questions drawn from some larger population of questions you care about. That framing makes the whole apparatus of experimental statistics available, and **miller-2024-adding-error-bars-to-evals** is the reference implementation. Industry practice — bold the highest number, declare SOTA — is the practice of reporting a sample mean without a standard error.

## How It Works

**Standard errors from the CLT.** The baseline. Scoring 82% on 200 questions is an estimate with a standard error near 2.7 points, so an 82-vs-79 comparison is not a result.

**Clustered standard errors when questions come in groups.** Benchmarks routinely contain several questions about the same passage, image or scenario. Those are not independent observations, and treating them as `n` independent draws understates the standard error — sometimes badly. Domain evals built from a handful of source documents are the archetypal clustered case, and exactly where naive intervals mislead.

**Paired question-level comparison.** When two models answer the *same* questions, do inference on per-question differences rather than on the two summary statistics. Because model scores are positively correlated across questions, the paired variance is smaller than the unpaired one by a covariance term. Same data, same experiment, tighter interval — a **free** reduction in estimator variance, and the single cheapest upgrade available to most eval reporting.

**Variance reduction by resampling.** Sampling `K` answers per question and averaging reduces variance toward a stated limit; analyzing next-token probabilities where available does the same, though many API deployments do not expose logprobs.

## Why It Matters

The point of an eval is to support a decision — deploy this model, ship this prompt, keep this retrieval change. A decision made on a difference indistinguishable from noise is a coin flip with extra steps, and the industry's default reporting format actively conceals which case you are in.

The paper's audit makes the failure concrete: the confidence intervals in a major published model report were **too narrow in some cases and too wide in others**. Both directions, in careful hands.

## Perspectives

Statistical significance is not importance. A tightly measured 0.3-point difference can be real and irrelevant — pair with **effect-size** and with an explicit minimum difference worth acting on.

These methods address **sampling** noise only. They say nothing about contamination, construct validity, or whether the benchmark measures the thing you care about. A well-error-barred measurement of the wrong quantity is still wrong, and the confidence interval will look reassuring.

Online experimentation solved these problems years ago — **kohavi-tang-xu-2020-trustworthy-online-controlled-experiments** is the same discipline, and evals are rediscovering it.

## Related Concepts

- [[eval-power-analysis]] — the planning-side companion
- **effect-size** · **statistical-analysis**
- **llm-as-judge-mt-bench** — judge noise is an additional variance source these methods must accommodate

## See Also

- **miller-2024-adding-error-bars-to-evals**
- [[corpus-agent-evaluation-suite]]
- [[coding-agent-validation-playbook]]
