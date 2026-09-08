---
name: math-statistics
description: >-
  Mathematical statistics as a curated, dependency-ordered knowledge capsule —
  the theorem layer on top of math-probability, and the floor under a future
  statistics analysis-methodology skill and the bayes-bridge connector. The
  statistical model, the likelihood / score / Fisher information, and the
  REGULARITY CONDITIONS as first-class hypothesis nodes; exponential families
  (natural parameter, cumulant function, the moment identities, completeness);
  data reduction — sufficiency, the Neyman–Fisher factorization, minimal
  sufficiency, ancillarity, completeness, Basu's theorem; the optimality theory
  — bias–variance, MSE, consistency, the Cramér–Rao lower bound, Rao–Blackwell,
  Lehmann–Scheffé, CRLB attainment iff exponential family; methods — method of
  moments, MLE with its consistency and asymptotic normality (CITED), the score
  equation, invariance, M-estimators, the sandwich variance, Bayes estimators
  with conjugacy and Bernstein–von Mises; decision theory — loss, risk,
  admissibility, minimax, Bayes risk, the complete-class theorem, and JAMES–STEIN
  as the inadmissibility counterexample in dimension ≥ 3; the exact Gaussian core
  — χ², t, F CONSTRUCTED from the normal and gamma, the sample mean/variance,
  Xbar ⟂ S², (n−1)S²/σ² ~ χ²_{n−1}, the t-statistic, Cochran's theorem, ANOVA;
  interval estimation — confidence sets, pivots, the test/CI duality, the exact
  normal intervals, the Wald / delta-method intervals; hypothesis testing —
  size, power, Neyman–Pearson, monotone likelihood ratio, Karlin–Rubin, the LRT
  with Wilks' theorem (CITED), the Wald and score tests and their asymptotic
  equivalence, the p-value and its uniform-under-null property, Pearson's χ², and
  multiplicity (FWER, Bonferroni, Benjamini–Hochberg FDR); the nonparametric
  glue — the empirical CDF, Glivenko–Cantelli, the DKW inequality, the bootstrap
  with its consistency (CITED), the kernel density estimator with its
  bias–variance / n^{-4/5} rate; and the Gaussian linear model — OLS as
  projection, the normal equations, the hat matrix, Gauss–Markov, the exact
  coefficient t- and F-tests, R², Frisch–Waugh–Lovell. A 206-node acyclic graph
  (58 cited roots discharged into math-probability / math-real-analysis, plus a
  cited finite-dimensional linear-algebra bridge). Every inferential result is
  TAGGED by regime — exact | asymptotic | distribution_free | bayesian. Use when
  stating or checking a statistics result, when you need the minimum
  prerequisite chain for a theorem, when you must know which regularity
  condition a result needs and what breaks without it, or whether a guarantee is
  exact-finite-sample or only asymptotic. Built with, and maintained per, the
  math-theorem-tree method. Excludes computation (MCMC, EM), experimental design,
  causal inference, time series, and high-dimensional / post-selection inference.
version: 0.1.0
author: Simon Janes
tags: [mathematics, statistics, mathematical-statistics, inference, likelihood, sufficiency, cramer-rao, maximum-likelihood, hypothesis-testing, neyman-pearson, confidence-intervals, linear-regression, bootstrap, decision-theory, bayesian, dependencies, knowledge-capsule, lean]
---

# Mathematical Statistics — Release 0.1

A knowledge capsule built with the
[`math-theorem-tree`](../math-theorem-tree/SKILL.md) method: a **206-node
directed acyclic graph** from the statistical model to the classical
large-sample theory, the exact Gaussian core, and the Gaussian linear model,
linearized with `tsort` so every prerequisite precedes what uses it.

It is the statistical-inference analogue of the way
[`math-real-analysis`](../math-real-analysis/SKILL.md) sits on
[`math-number-systems`](../math-number-systems/SKILL.md): it sits on
[`math-probability`](../math-probability/SKILL.md) and takes every probabilistic
object and theorem — the CLT, the SLLN, Slutsky, the delta method, conditional
expectation, the distribution families, the inequalities — as a **cited root**.

Start with **[`README.md`](README.md)**, then **[`scope.md`](scope.md)** and
**[`conventions.md`](conventions.md)**.

## What this capsule is for

- **The prerequisite chain** for a statistics result — the minimal prerequisite
  set for each headline theorem is in
  [`indexes/prerequisite-paths.md`](indexes/prerequisite-paths.md).
- **Which regularity condition a result needs** — the six regularity conditions
  (`support_independent_of_theta`, `interchange_derivative_integral`,
  `true_parameter_interior`, `fisher_information_positive_definite`,
  `log_likelihood_smooth`, `identifiability`) are first-class `hypothesis` nodes
  with a prerequisite edge into every theorem that uses them
  ([`indexes/hypothesis-index.md`](indexes/hypothesis-index.md)); each result's
  `counterexamples_when_dropped` says exactly what breaks without each one
  (uniform(0, θ) non-regularity, the Neyman–Scott inconsistency, the boundary
  χ² mixture, Hodges superefficiency, …).
- **Whether a guarantee is exact or asymptotic** — every inferential result YAML
  carries `regime: { exact | asymptotic | distribution_free | bayesian }`
  ([`indexes/regime-index.md`](indexes/regime-index.md)). Reading an
  `asymptotic` result as an `exact` finite-sample guarantee is the single most
  common misuse in applied statistics; the tag makes it graph-visible.
- **Which results rest on a cited theorem** versus a kernel-checked core —
  [`validation/proof-checks.md`](validation/proof-checks.md). 38 nodes have a
  genuine universal Lean core, 6 have a `decide` instance check, the rest are
  `cited` (the deep asymptotics — MLE normality, Wilks, Glivenko–Cantelli, the
  bootstrap, Bernstein–von Mises, LAN / Hájek / LAM — with named sources).
- **The acknowledged foundational gap** — there is no `math-linear-algebra`
  capsule; `linear_algebra_background` is one cited `bridge` node listing what
  the regression and quadratic-form results assume.

## Build

```sh
sh build/build-tree.sh   # graph-check + tsort (BSD-safe) + reverse deps
sh build/all.sh          # + index views + Lean proof cores + bc worksheets
```

Regenerate every node page and result YAML after editing a spec:

```sh
python3 build/gen-results.py     # from build/specs/spec_*.py; deps pulled from the graph
```

## Validation

- **Lean** ([`validation/proof-checks.lean`](validation/proof-checks.lean),
  Lean 4.33, no Mathlib, exit 0): 26 genuine universal cores — the score
  identity, the information equality, the centered-moment identity, the
  bias–variance / complete-the-square identity, the sample-variance `n−1`
  identity, 2-vector Cauchy–Schwarz for the CRLB, the Neyman–Pearson pointwise
  swap, the law-of-total-variance inequality for Rao–Blackwell, the
  factorization cancellation, Basu's independence step, the Bonferroni union
  bound, the Chebyshev consistency step, and more — plus 8 `decide` instance
  checks over one fixed 3×2 design (the hat matrix, Cochran orthogonality, the
  normal equations, the Gauss–Markov cross term, Frisch–Waugh).
- **bc** ([`validation/instance-checks.bc`](validation/instance-checks.bc),
  exit 0): the CRLB at Bernoulli / Poisson / normal-mean (attained) versus the
  normal variance (not attained); the `n−1` divisor by full n=3 enumeration;
  the `t` density → `1/√(2π)`; the Neyman–Pearson threshold and power for
  N(0,1) vs N(1,1); the Rao–Blackwell variance drop; OLS on a 3-point design;
  Wald-interval undercoverage for a binomial proportion; the Benjamini–Hochberg
  step-up versus Bonferroni.

## Downstream

- **`statistics`** (planned) — the analysis-methodology skill (sibling of
  `design-of-experiments`, `unknown-discovery`): the disciplined workflow for
  inference on data already collected. It will cite this capsule for the
  theorems and keep only the workflow plus a Monte Carlo verification harness.
- **`bayes-bridge`** (planned) — the Bayesian inferential apparatus as the
  connector between `math-probability`'s Bayes' theorem and this capsule's
  estimation and testing.
- **`design-of-experiments`** — the estimand / power / randomization-inference
  primitives it currently re-states have their theorem home here.

## Limitations

A curated graph, not a complete account of mathematical statistics. A valid
`tsort` order confirms only the encoded constraints. A type check and passing
`bc` instances are not a proof. `lean` verified only the small finitary cores
listed in `validation/proof-checks.md`; every deep asymptotic result is `cited`.
Finite-dimensional linear algebra is assumed, not built. Every result stays
conditional on its hypotheses, its regularity conditions, the foundational
stance, the conventions, and its source — and on the distinction, made explicit
by the `regime` tag, between an exact finite-sample guarantee and an asymptotic
one.
