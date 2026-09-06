---
name: math-real-analysis
description: >-
  Real Analysis I as a curated, dependency-ordered knowledge capsule — the real
  line as a complete ordered field, sequences and series, the topology of the
  reals, limits and continuity, differentiation, Riemann integration, and
  uniform convergence. A 109-node acyclic graph: every definition, axiom,
  first-class hypothesis, and theorem carries its typed symbols, a
  well-formedness (type) check, an epistemic/proof status, its full hypothesis
  list, one specialization check, one hypothesis-dropped counterexample, a proof
  provenance with an explicit Lean status, and a source. Use when stating or
  checking a real-analysis result, when you need the minimum prerequisite chain
  for a theorem, or when you must know which hypothesis a result actually needs
  and what breaks without it. Built with, and maintained per, the
  math-theorem-tree method.
version: 0.1.0
author: Simon Janes
tags: [mathematics, real-analysis, calculus, theorems, dependencies, knowledge-capsule, lean]
---

# Real Analysis I — Release 0.1

A knowledge capsule built with the
[`math-theorem-tree`](../math-theorem-tree/SKILL.md) method: a **109-node
directed acyclic graph** of primitives, notation conventions, definitions,
axioms, first-class hypotheses, theorems, and one identity, linearized with
`tsort` so every prerequisite precedes what uses it. Use it as a trustworthy
real-analysis reference — not a course.

## Scope

**Read [`scope.md`](scope.md) first.** In brief: ℝ as a complete ordered field
(the least-upper-bound property is the completeness **axiom**; the construction
of ℝ is cited, not built); sequences, series, the topology of subsets of ℝ,
continuity, differentiation, Riemann (Darboux) integration on a compact
interval, and sequences/series of functions through power series. **Excluded:**
metric-space generality, ℝⁿ / multivariable, Lebesgue integration, complex
analysis, functional analysis, the construction of the number systems, numerical
analysis.

Foundational stance and every notation convention:
[`conventions.md`](conventions.md). Type vocabulary and well-formedness rules:
[`objects.md`](objects.md). Master symbol list: [`notation.md`](notation.md).

## How to use this capsule

1. **Find the result** — [`indexes/topic-index.md`](indexes/topic-index.md) (by
   area) or [`indexes/symbol-index.md`](indexes/symbol-index.md) (by notation).
2. **Read its entry** — [`results/<id>.yaml`](results/) for the 15 headline
   results (typed symbols, hypotheses, epistemic status, proof provenance,
   specializations, hypothesis-dropped counterexamples, sources); the full
   registry is [`nodes/nodes.tsv`](nodes/nodes.tsv) and exemplar detail pages
   are in [`nodes/`](nodes/).
3. **Check what a result needs** —
   [`indexes/prerequisite-paths.md`](indexes/prerequisite-paths.md) for the
   transitive prerequisite set of each headline theorem;
   [`indexes/hypothesis-index.md`](indexes/hypothesis-index.md) for everything
   that depends on `compactness`, `lub_axiom`, `countable_choice`, ….
4. **Check what breaks without a hypothesis** —
   [`indexes/counterexample-index.md`](indexes/counterexample-index.md) and
   [`validation/specialization-cases.md`](validation/specialization-cases.md).
5. **Avoid the standard traps** —
   [`indexes/common-misuse-index.md`](indexes/common-misuse-index.md).

## What "epistemic status" means here

Every result node carries one label (`nodes/nodes.tsv` `type` + the `status_label`
in its YAML): `axiom`, `definition`, `mathematical_identity`, `proved_theorem`,
`proposition`, or `nonconstructive_result` (its standard proof uses `lub_axiom`
non-constructively or uses `countable_choice`). A `proved_*` label rests on a
**cited, standard proof**; the separate `lean_status` field records what *this
capsule's* Lean file actually machine-checked (`core-arith` = a genuine `omega`
/ induction proof of the algebraic core; `instance` = a `decide` sample;
`none`). See [`validation/proof-checks.md`](validation/proof-checks.md).

## Build and verify

```sh
sh build/all.sh                       # graph-check -> tsort -> all views -> lean -> bc
sh build/build-tree.sh                # graph only: 109 nodes, 247 edges, acyclic
lean validation/proof-checks.lean     # 12 kernel-checked algebraic cores (exit 0)
bc -q -l validation/instance-checks.bc # specializations + hypothesis-dropped counterexamples
```

Full results: [`validation/consistency-audit.md`](validation/consistency-audit.md).

## Method verification (Release 0.1)

This capsule is the **proof-of-method for
[`math-theorem-tree`](../math-theorem-tree/SKILL.md)** — the first capsule built
with it, and the first time the `physics-formula-tree` meta method was carried
to a new field. Outcome:

| Stage | Tool | Result |
|---|---|---|
| graph + sort | BSD `tsort` | 109 nodes, 247 edges, **acyclic** (stderr-checked); every edge respected; 0 isolated nodes; 5 roots = the declared primitives + choice. Five would-be cycles designed out in advance ([`edges/cycles.md`](edges/cycles.md)). |
| type checks | this skill | 11 headline nodes, all **well_formed**; forced limit-point / boundedness / strict-monotonicity / nonempty-bounded-sup preconditions into the entries. |
| proof cores | Lean 4.33.1, **no Mathlib** | `lean validation/proof-checks.lean` exit 0. **Genuine universal** proofs (over ℤ/ℕ) of the triangle inequality, the squeeze pattern, the telescoping sum, and the geometric ratio bound (`omega` + induction); **instance** `decide` checks for the nonlinear identities (geometric partial sum, Taylor remainder, AM–GM, MVT endpoints). No analytic theorem is provable here — recorded per node. |
| instances / counterexamples | GNU `bc` 7.0.3 | clean run; the √2 recursion matches `sqrt(2)` to 40 places and fails in ℚ; `x^n` sup stays 1 on `[0,1]`, → 0 on `[0,0.9]`; alternating harmonic → `ln 2`; etc. One `bc` gotcha fixed: `n % 2` is scale-dependent — used a sign-flip variable instead. |
| symbol index | GNU `ptx` 9.x | discovery pass (4640 rotations) with `rg` confirmation; `ptx` errored on multi-file `-A -r` input (zero-length match) — fixed by feeding one cleaned concatenated stream. |

Fixes folded back into the method skill's `references/`: see the repo README
verification table.
