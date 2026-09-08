# math-logic-and-proof

Logic and proof as a **knowledge capsule** — built with the
[`math-theorem-tree`](../math-theorem-tree/SKILL.md) method, and the **deepest
floor** under
[`math-sets-functions-cardinality`](../math-sets-functions-cardinality/SKILL.md)
→ [`math-number-systems`](../math-number-systems/SKILL.md) →
[`math-real-analysis`](../math-real-analysis/SKILL.md). It develops the five
primitives that `math-sets-functions-cardinality` cites but does not build:
`proposition_logic`, `predicate_logic`, `quantifier_negation`,
`quantifier_order`, `proof_methods`.

- Start: [`SKILL.md`](SKILL.md) · [`scope.md`](scope.md) · [`conventions.md`](conventions.md) · [`objects.md`](objects.md) · [`notation.md`](notation.md)
- Graph: [`nodes/nodes.tsv`](nodes/nodes.tsv) · [`edges/dependencies.plan`](edges/dependencies.plan) · [`edges/cycles.md`](edges/cycles.md) · [`edges/relations.tsv`](edges/relations.tsv) · [`edges/cross-capsule.md`](edges/cross-capsule.md)
- Views: [`indexes/`](indexes/) — tsort order, hypothesis, status, constructive-grade, counterexample, prerequisite-paths, reverse-deps, [`symbol-index.md`](indexes/symbol-index.md)
- Verification: [`validation/`](validation/) — Lean proof-checks, `bc` instance-checks, type-checks

## Build

```sh
sh build/all.sh                        # graph -> tsort -> views -> lean -> bc -> yaml check
sh build/build-tree.sh                 # 130 nodes, 312 edges, acyclic, 7 roots
lean validation/proof-checks.lean      # exit 0, no sorry: soundness + deduction theorem (propext only)
bc -q -l validation/instance-checks.bc # truth tables, NAND completeness, forall-exists vs exists-forall
```

## Release 0.1 at a glance

**130 nodes** (57 definitions, 21 theorems, 13 logical identities, 8
metatheorems, 6 primitives, 5 proved lemmas, 3 constructions, 3 examples, 2
axioms, 5 propositions, 1 each of algorithm / corollary / diagnostic /
hypothesis / notation_convention / proved_theorem / regime), **312 edges**,
acyclic, **7 roots**: `symbol`, `string`, `finite_sequence`,
`inductive_definition`, `metatheoretic_induction` (the finitary five),
`first_order_logic_with_equality` (axiom root), `decidability` (boundary-block
informal primitive), plus `naive_collection` (primitive here, discharged from
above by the set capsule).

**Every logical law and proof method carries a `constructive_grade`:**
`intuitionistic` (Lean without `Classical`), `needs_LEM`, `needs_DNE`, or
`needs_full_classical`. E.g. `¬∃x φ ⟺ ∀x ¬φ` is `intuitionistic`;
`¬∀x φ ⟺ ∃x ¬φ` is `needs_LEM`; proof by contradiction is `needs_DNE`; Gödel
completeness is `needs_full_classical`.

## The syntax ↔ collections loop

The foundations are genuinely circular: model theory needs "sets", set theory
needs logic. This capsule keeps the **syntactic/proof-theoretic subgraph
self-contained** (no `naive_collection` edge) and tags every **semantic** node
`metatheory: naive_collections`. The loop is recorded in
[`edges/cross-capsule.md`](edges/cross-capsule.md) as a bidirectional `grounds`
relation — and linearised in neither capsule's `tsort` graph.

## Status

**Release 0.1 — fully built and self-checking.** All 130 registry rows are
`reviewed` (122) or `active` (8: the 6 syntax primitives + 2 first-order-logic
axiom nodes); every node page is step-7 audited by `build/audit-pages.py`.
Complete: foundational docs; 130-node registry; acyclic evidence-backed dependency graph; **21 headline result YAMLs**;
**a detail page for every one of the 130 nodes** (`nodes/*.md`) — each with
typed symbols, a well-formedness check, its constructive grade and Lean status,
specialization / boundary cases, hypothesis-dropped counterexamples, common
misuse, related nodes, and sources; every page's stated prerequisites are
machine-checked against the graph edges;
**`validation/proof-checks.lean`** (Lean 4.33, no
Mathlib, exit 0, no `sorry` — `soundness_prop` and `deduction_theorem` genuine
universal proofs on `propext` alone, the equivalence-catalogue constructive
split, `induction_equivalence`; the Henkin/completeness/compactness/LS layer and
every boundary node are `cited`, tracked in
[`validation/proof-checks.md`](validation/proof-checks.md));
**`validation/instance-checks.bc`**; and the generated
[`indexes/`](indexes/) (status, **constructive-grade**, counterexample,
hypothesis, prerequisite-paths). `sh build/all.sh` runs the lot; every result
YAML's `dependencies` list is machine-checked against the graph edges.
