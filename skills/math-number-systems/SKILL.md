---
name: math-number-systems
description: >-
  The number systems as a curated, dependency-ordered knowledge capsule:
  ℕ → ℤ → ℚ → ℝ, constructed and characterized. The Peano axioms and the
  recursion theorem; ℤ as (ℕ×ℕ)/∼ and ℚ as (ℤ×ℤ*)/∼ with explicit
  well-definedness; ℚ as an ordered field that is not complete; ℝ as the set of
  Dedekind cuts, with the least-upper-bound property proved as a THEOREM (not
  assumed); nth roots, uniqueness of ℝ, and the cardinality thread through
  Cantor's diagonal argument. A 100-node acyclic graph rooted at a single node,
  `set`. Use when you need the construction behind "ℝ is a complete ordered
  field", the prerequisite chain for a number-system fact, or to know exactly
  which axiom (Peano, choice) a result rests on. Built with, and maintained per,
  the math-theorem-tree method; discharges the primitives of math-real-analysis.
version: 0.1.0
author: Simon Janes
tags: [mathematics, foundations, number-systems, construction-of-reals, dependencies, knowledge-capsule, lean]
---

# The Number Systems — Release 0.1

A knowledge capsule built with the
[`math-theorem-tree`](../math-theorem-tree/SKILL.md) method: a **100-node
directed acyclic graph** — primitives, the Peano and choice axioms, the
algebraic-structure tower, the constructions of ℤ, ℚ, ℝ, and the cardinality
results — linearized with `tsort`. It is the capsule that **discharges what
[`math-real-analysis`](../math-real-analysis/SKILL.md) takes on faith**: there,
"ℝ is a complete ordered field" is an axiom; here it is a theorem with a
one-line proof (`sup S = ⋃ S`).

## Scope

**Read [`scope.md`](scope.md) first.** In brief: the Peano axioms as the floor
(ℕ's set model is cited); the recursion theorem and ℕ arithmetic; ℤ and ℚ as
quotient constructions with explicit well-definedness obligations; ℚ Archimedean,
dense, and **not order-complete**; ℝ via **Dedekind cuts** (canonical — the
Cauchy completion is recorded as an equivalent construction); the
**least-upper-bound property** proved; ℝ Archimedean, ℚ dense in ℝ, nth roots
exist, ℝ is unique up to isomorphism; countability of ℕ×ℕ, ℤ, ℚ, Cantor's
theorem and diagonal argument, ℝ uncountable. **Excluded:** the set-theoretic
construction of ℕ, formal logic/model theory, ℂ and beyond, everything
downstream in analysis (limits and calculus — that is `math-real-analysis`),
non-standard constructions of ℝ.

Foundational stance, all conventions, and the seven designed-out cycles:
[`conventions.md`](conventions.md). Type vocabulary and the
"does-it-respect-the-quotient" well-formedness rules: [`objects.md`](objects.md).
Symbol list: [`notation.md`](notation.md).

## How to use this capsule

1. **Find the result** — [`indexes/topic-index.md`](indexes/topic-index.md)
   (by system) or [`indexes/symbol-index.md`](indexes/symbol-index.md).
2. **Read its entry** — [`results/<id>.yaml`](results/) for the 15 headline
   results; the full registry is [`nodes/nodes.tsv`](nodes/nodes.tsv); exemplar
   detail pages in [`nodes/`](nodes/).
3. **Check what a result needs** —
   [`indexes/prerequisite-paths.md`](indexes/prerequisite-paths.md);
   [`indexes/hypothesis-index.md`](indexes/hypothesis-index.md) for everything
   resting on `peano_axioms`, on `countable_choice`, on `integral_domain`, ….
4. **Check what breaks without a hypothesis** —
   [`indexes/counterexample-index.md`](indexes/counterexample-index.md) and
   [`validation/specialization-cases.md`](validation/specialization-cases.md).

## The construction chain

```
set  ->  peano_axioms  ->  recursion_theorem  ->  N arithmetic
      ->  integer = (N x N)/~        (Grothendieck-style)
      ->  rational_number = (Z x Z*)/~   (field of fractions)
      ->  dedekind_cut  ->  real_number  ->  lub_property   <-- the payoff
      ->  nth_root_exists,  real_uniqueness
cardinality thread:  countable_set  ->  nat_pairing_bijection  ->
      rational_countable  |  cantor_diagonal_argument  ->  real_uncountable
```

Each quotient step carries an explicit **well-definedness** obligation
(`*_operations_well_defined`), and each system **embeds** in the next
(`nat_embeds_in_integer`, …) rather than being literally a subset.

## What "epistemic status" means here

`axiom` / `definition` / `mathematical_identity` / `proved_theorem` /
`proposition` / `constructive_result`. The constructions of ℤ, ℚ, ℝ and
`lub_property` are **`constructive_result`** — the objects are exhibited and no
choice is used. `countable_union_countable` is the one node with
`uses_choice: true` (countable choice). `lean_status` per YAML records what this
capsule's Lean file machine-checked (`core-arith` / `instance` / `cited` /
`none`), separate from the epistemic label.

## Build and verify

```sh
sh build/all.sh                       # graph -> tsort -> views -> lean -> bc
sh build/build-tree.sh                # 100 nodes, 274 edges, acyclic, 1 root (set)
lean validation/proof-checks.lean     # 10 kernel checks (exit 0), incl. Cantor's theorem
bc -q -l validation/instance-checks.bc # the constructions computed; Q's incompleteness exhibited
```

Full results: [`validation/consistency-audit.md`](validation/consistency-audit.md).

## Interactive tutorial

[`tutorial/building-the-number.md`](tutorial/building-the-number.md) — the path
to `√2` existing: `integer → rational_number → sqrt2_irrational →
rational_incomplete_lub → dedekind_cut → real_is_ordered_field → lub_property →
nth_root_exists`, with a runnable well-definedness check (and a broken-operation
counterexample) for each quotient. `upmd --ci --all` green.

## Method verification (Release 0.1)

Built with the `math-theorem-tree` method — the **second capsule** (after
`math-real-analysis`), and the one that closes the loop by discharging that
capsule's roots.

| Stage | Tool | Result |
|---|---|---|
| graph + sort | BSD `tsort` | 100 nodes, 274 edges, **acyclic** (stderr-checked); every edge respected; 0 isolated; **1 root, `set`** (+ 3 assumed axiom nodes). Seven would-be cycles designed out ([`edges/cycles.md`](edges/cycles.md)) — notably completeness ⟺ real-number, resolved *opposite* to `math-real-analysis`. |
| type checks | this skill | 14 headline nodes, all **well_formed**; forced the "relation is an equivalence first", "operation respects ∼", "output is a cut", and "dodge 0.999…" obligations into the entries. |
| proof cores | Lean 4.33.1, **no Mathlib** | `lean validation/proof-checks.lean` exit 0. **Genuine universal**: ℤ-relation transitivity + ℤ-addition/order well-definedness (`omega`), ℕ-addition commutativity from the recursive definition (induction), division-with-remainder (core lemmas), and **Cantor's diagonal theorem** (plain Lean). **Instance** `decide`: ℤ-multiplication `∼`, ℚ-transitivity, √2-irrationality (`q<50`), pairing injectivity (`8×8`). |
| instances | GNU `bc` 7.0.3 | clean run: the ℤ/ℚ quotient arithmetic computed; lowest terms via gcd; √2-irrationality (`q ≤ 2000`); ℚ's incompleteness as a decimal search; the Cantor pairing as a bijection; nth roots by bisection. **Fixes:** a `while` counter incremented outside its braces (infinite loop → `for`); `a % b` under `bc -l` is fractional (`scale = 20`) → `scale = 0` + `a - b*(a/b)` for the integer sections. |
| symbol index | GNU `ptx` 9.x | discovery pass (5013 rotations) + `rg` confirmation; single cleaned stream (the `-A -r` multi-file bug from `math-real-analysis` avoided). |
