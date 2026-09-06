---
name: math-probability
description: >-
  Probability theory as a curated, dependency-ordered knowledge capsule — the
  missing foundational floor under design-of-experiments, simulation, and
  unknown-discovery. The measure/σ-algebra entry (σ-algebra, generated and Borel
  σ-algebras, measure, the π–λ theorem; the abstract Lebesgue integral and
  MCT/DCT/Fatou/Fubini/Radon–Nikodym CITED, not built); Kolmogorov's axioms with
  countable additivity; the elementary consequences (inclusion–exclusion, the
  union bound, continuity of probability, both Borel–Cantelli lemmas);
  conditional probability and Bayes' theorem as a node; random variables, CDF,
  pmf/pdf, the probability integral transform, change of variables; expectation,
  LOTUS, linearity, variance/covariance/correlation, L^p and the moment ladder,
  MGF and characteristic function; independence of events / σ-algebras / random
  variables with the factorization theorem and the pairwise-≠-mutual and
  uncorrelated-≠-independent counterexamples; the distribution families
  (Bernoulli, binomial, geometric, Poisson with the law of rare events, uniform,
  exponential with memorylessness, gamma, beta, normal; Cauchy as the no-mean
  counterexample); the inequalities (Markov, Chebyshev, Chernoff, Jensen,
  Cauchy–Schwarz, Hölder, Hoeffding); the four MODES OF CONVERGENCE (almost
  sure, in probability, in L^p, in distribution) with every limit theorem TAGGED
  by the mode it delivers; the implication lattice, portmanteau, continuous
  mapping, Slutsky, the weak and strong laws of large numbers, Lévy's continuity
  theorem, the i.i.d. and Lindeberg central limit theorems, the delta method;
  and conditional expectation given a σ-algebra (existence CITED) with the tower
  property, the law of total variance, and the L^2-projection characterization.
  A 131-node acyclic graph rooted at eight primitives discharged into
  math-sets-functions-cardinality and math-real-analysis. Use when stating or
  checking a probability result, when you need the minimum prerequisite chain
  for a theorem, or when you must know which convergence mode a limit theorem
  actually delivers and which hypothesis breaks it. Built with, and maintained
  per, the math-theorem-tree method. Excludes the construction of the abstract
  integral, stochastic processes, and statistical inference.
version: 0.1.0
author: Simon Janes
tags: [mathematics, probability, measure-theory, random-variables, expectation, independence, limit-theorems, central-limit-theorem, conditional-expectation, dependencies, knowledge-capsule, lean]
---

# Probability Theory — Release 0.1

A knowledge capsule built with the
[`math-theorem-tree`](../math-theorem-tree/SKILL.md) method: a **131-node
directed acyclic graph** from the Kolmogorov axioms to the classical limit
theorems and conditional expectation, linearized with `tsort` so every
prerequisite precedes what uses it.

Start with **[`README.md`](README.md)**, then **[`scope.md`](scope.md)** and
**[`conventions.md`](conventions.md)**.

## What this capsule is for

- **The prerequisite chain** for a probability result — e.g. the CLT's minimal
  prerequisite set is in [`indexes/prerequisite-paths.md`](indexes/prerequisite-paths.md).
- **Which convergence mode** a limit theorem delivers (the per-result tag; see
  `conventions.md`) and **which hypothesis breaks it** (each result's
  `counterexamples_when_dropped`).
- **Which results rest on a cited analytic theorem** (the integral, MCT/DCT,
  Radon–Nikodym, Lévy continuity) versus a kernel-checked core —
  [`validation/proof-checks.md`](validation/proof-checks.md).
- **The foundational cut** that keeps the graph acyclic: independence is defined
  by factorization, not by conditioning ([`edges/cycles.md`](edges/cycles.md)).

## Build

```sh
sh build/build-tree.sh   # graph-check + tsort (BSD-safe) + reverse deps
sh build/all.sh          # + index views + lean proof cores + bc worksheets
```

## Downstream

`design-of-experiments` (power, estimands, randomization inference),
`simulation` (Monte Carlo, the probability integral transform, variance
reduction), and `unknown-discovery` (the forecast ledger, Brier calibration)
all currently re-state probability primitives; this capsule is the floor they
should `requires`-edge into.

## Limitations

A curated graph, not a complete account of probability. A valid `tsort` order
confirms only the encoded constraints. A type check and passing `bc` instances
are not a proof. `lean` verified only the small finitary cores listed in
`validation/proof-checks.md`; the CLT, SLLN, Lévy continuity, Radon–Nikodym,
MCT/DCT, and the existence of `E[X|G]` are `cited`. Every result stays
conditional on its hypotheses, the foundational stance, the conventions, and its
source.
