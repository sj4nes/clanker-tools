---
name: math-sets-functions-cardinality
description: >-
  Sets, functions, orders, and cardinality as a curated, dependency-ordered
  knowledge capsule — the layer below the number systems. The ZF(C) axioms; the
  algebra of sets and the PREIMAGE ALGEBRA that continuity and compactness
  proofs run on; equivalence relations and quotients; order theory with Zorn's
  lemma and the well-ordering theorem; a minimal ordinal spine; omega built from
  the Axiom of Infinity (discharging the Peano axioms); and cardinality through
  Cantor's theorem, Cantor-Schroeder-Bernstein, countable sets, the diagonal
  argument, the arithmetic of aleph_0 and 2^aleph_0, and a statement of the
  independence of CH. A 106-node acyclic graph rooted at a single node,
  propositional logic. Every result carries a well-formedness check, an
  epistemic status, its hypotheses, a specialization, a hypothesis-dropped
  counterexample, and a CHOICE GRADE (choice_free / needs_countable_choice /
  needs_full_AC). Use when you need the set-theoretic foundation a proof rests
  on, the prerequisite chain for a cardinality fact, or to know exactly which
  form of choice a result uses. Built with the math-theorem-tree method.
version: 0.1.0
author: Simon Janes
tags: [mathematics, foundations, set-theory, cardinality, axiom-of-choice, dependencies, knowledge-capsule, lean]
---

# Sets, Functions, and Cardinality — Release 0.1

A knowledge capsule built with the
[`math-theorem-tree`](../math-theorem-tree/SKILL.md) method: a **106-node
directed acyclic graph** — the logic floor, the ZF(C) axioms, set and function
algebra, equivalence relations and quotients, order theory, a minimal ordinal
spine, `ω` from the axioms, and the theory of cardinality — linearized with
`tsort`. It is the layer **below**
[`math-number-systems`](../math-number-systems/SKILL.md): every primitive that
capsule takes on faith (`set`, `function`, `quotient_set`, `axiom_of_choice`,
`peano_axioms`, …) is a node here.

## Scope

**Read [`scope.md`](scope.md) first.** In brief: propositional and predicate
logic as a cited **floor** (not developed — that is a future
`math-logic-and-proof`); the nine ZF axioms + Choice, with `countable_choice`
and `dependent_choice`; subset / power set / arbitrary union & intersection /
De Morgan / products; relations; equivalence relations, quotients, and
**well-definedness on a quotient**; injection / surjection / bijection, image
and preimage, the **preimage algebra**, one-sided inverses; partial / total /
well orders, bounds, **Zorn's lemma**, the **well-ordering theorem**;
`ordinal` / transfinite induction / transfinite recursion / order types;
**`ω` as the smallest inductive set**, and `peano_holds_in_omega`;
equinumerosity, **Cantor–Schröder–Bernstein** (choice-free), **Cantor's
theorem**, finite vs Dedekind-infinite, countable sets and their closure
properties, the **diagonal argument**, `|𝒫(ω)| = 2^ℵ₀ = |ℝ|`, the arithmetic of
infinite cardinals, the aleph hierarchy, Hartogs' number, the continuum, and a
**statement** (not a proof) of the independence of CH.

**Excluded:** the metatheory of logic; the independence proofs (`L`, forcing);
deep ordinal/cardinal theory (`V_α`, cofinality, large cardinals); the number
systems and everything downstream. Full detail, the foundational stance, and the
seven designed-out cycles: [`conventions.md`](conventions.md). The
"is-it-a-set / is-the-function-total / is-choice-used" well-formedness rules:
[`objects.md`](objects.md).

## How to use this capsule

1. **Find the result** — [`indexes/topic-index.md`](indexes/topic-index.md) or
   [`indexes/symbol-index.md`](indexes/symbol-index.md).
2. **Read its entry** — [`results/<id>.yaml`](results/) for the 15 headline
   nodes; full registry in [`nodes/nodes.tsv`](nodes/nodes.tsv); exemplar detail
   pages in [`nodes/`](nodes/).
3. **Check what a result needs** —
   [`indexes/prerequisite-paths.md`](indexes/prerequisite-paths.md);
   [`indexes/hypothesis-index.md`](indexes/hypothesis-index.md) for everything
   resting on `axiom_of_choice`, on `countable_choice`, on `axiom_infinity`, ….
4. **Check the choice grade** — every result YAML has `choice_grade`:
   `choice_free`, `needs_countable_choice`, or `needs_full_AC`. CSB, Cantor's
   theorem, Hartogs, and the finite pigeonhole are flagged **choice-free**.
5. **Check what breaks** —
   [`indexes/counterexample-index.md`](indexes/counterexample-index.md) and
   [`validation/specialization-cases.md`](validation/specialization-cases.md).

## The spine

```
proposition_logic -> predicate_logic -> the 9 ZF axioms (+ AC, DC, CC)
   -> set algebra + PREIMAGE ALGEBRA        (f^-1 commutes with U, cap, complement)
   -> relations -> equivalence + quotients  (well_defined_on_quotient)
   -> functions (inj/surj/bij, image, one-sided inverses)
   -> orders -> zorn_lemma -> well_ordering_theorem
   -> ordinal spine (transfinite induction / recursion / order types)
   -> omega_construction -> peano_holds_in_omega -> recursion_theorem
   -> equinumerous -> cantor_schroeder_bernstein | cantor_theorem
   -> countable_set -> cantor_diagonal -> continuum -> continuum_hypothesis
```

## Build and verify

```sh
sh build/all.sh                       # graph -> tsort -> views -> lean -> bc
sh build/build-tree.sh                # 106 nodes, 263 edges, acyclic, 1 root
lean validation/proof-checks.lean     # 11 kernel checks: the preimage algebra + Cantor's diagonal, plain Lean
bc -q -l validation/instance-checks.bc # the countability bijections and the diagonal argument, run
```

Full results: [`validation/consistency-audit.md`](validation/consistency-audit.md).

## Method verification (Release 0.1)

Built with `math-theorem-tree` — the **third capsule** (after
`math-real-analysis` and `math-number-systems`), and the one that reaches the
foundational floor.

| Stage | Tool | Result |
|---|---|---|
| graph + sort | BSD `tsort` | 106 nodes, 263 edges, **acyclic** (stderr-checked); every edge respected; 0 isolated; **1 root, `proposition_logic`** (+ 12 assumed axiom nodes). Seven would-be cycles designed out ([`edges/cycles.md`](edges/cycles.md)) — AC⟺Zorn⟺well-ordering, ordinal⟺well-order, ℕ⟺set, and four more. |
| type checks | this skill | 14 headline nodes, all **well_formed**; forced the class-vs-set, total-function, `⋂`-nonempty, and — above all — the **choice-grade** obligations into the entries. |
| proof cores | Lean 4.33.1, **no Mathlib** | `lean validation/proof-checks.lean` exit 0. **Genuine universal** (sets as `X → Prop`): the **preimage algebra** (`rfl`!), the image laws, composition preserving inj/surj, classical quantifier negation, `[x]=[y] ⟺ x∼y`, and **Cantor's diagonal theorem** (2 lines, no Mathlib). **Instance** `decide`: pigeonhole `Fin 5 → Fin 4`. |
| instances | GNU `bc` 7.0.3 | clean run: the Cantor pairing as a bijection `ω×ω→ω` (+ inverse, `ℚ⁺`), `ℤ` countable by interleaving, the diagonal argument executed, `|𝒫(X)|=2^{\|X\|}`, Cantor's theorem worked with `D` exhibited, `ℵ₀+ℵ₀=ℵ₀`. Kept at `scale = 0` throughout (avoiding the `bc -l` fractional-`%` trap). |
| symbol index | GNU `ptx` 9.x | discovery pass (4972 rotations) + `rg` confirmation, single cleaned stream. |
