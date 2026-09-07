# math-number-systems

The construction chain ℕ → ℤ → ℚ → ℝ as a **knowledge capsule** — built with the
[`math-theorem-tree`](../math-theorem-tree/SKILL.md) method, and the capsule that
**discharges the primitive roots of
[`math-real-analysis`](../math-real-analysis/SKILL.md)**: there "ℝ is a complete
ordered field" is an axiom; here it is the theorem `lub_property`, proved
`sup S = ⋃ S`.

- Start: [`SKILL.md`](SKILL.md) · [`scope.md`](scope.md) · [`conventions.md`](conventions.md) · [`objects.md`](objects.md)
- Graph: [`nodes/nodes.tsv`](nodes/nodes.tsv) · [`edges/dependencies.plan`](edges/dependencies.plan) · [`edges/cycles.md`](edges/cycles.md) · [`edges/relations.tsv`](edges/relations.tsv)
- Results: [`results/`](results/) (15 headline YAMLs) · [`nodes/`](nodes/) (3 exemplar detail pages)
- Views: [`indexes/`](indexes/) — topic, hypothesis, status, counterexample, prerequisite-path, symbol
- Verification: [`validation/consistency-audit.md`](validation/consistency-audit.md)

## Build

```sh
sh build/all.sh                        # everything
sh build/build-tree.sh                 # 100 nodes, 274 edges, acyclic, 1 root (set)
lean validation/proof-checks.lean      # 10 kernel checks incl. Cantor's diagonal theorem
bc -q -l validation/instance-checks.bc  # the constructions computed; Q's incompleteness exhibited
```

## Interactive tutorial

[`tutorial/building-the-number.md`](tutorial/building-the-number.md) — "Building
the number that isn't there". Walks `integer → rational_number → sqrt2_irrational
→ rational_incomplete_lub → dedekind_cut → real_is_ordered_field → lub_property →
nth_root_exists` (the path to `√2` existing in `ℝ`), with a runnable
**well-definedness** check for each quotient construction (and a counterexample
where an operation on classes is *not* a function), the incompleteness of `ℚ`
exhibited, and the supremum of `{x² < 2}` computed as a union of cuts. Built with
[`theorem-tree-tutorial`](../theorem-tree-tutorial/SKILL.md); 23 blocks,
`upmd --ci --all` green.

## Release 0.1 at a glance

100 nodes (32 definitions, 26 theorems, 22 propositions, 9 structures, 5
constructions, 3 axioms, 2 principles, 1 primitive), 274 edges, acyclic, rooted
at the single node `set` (plus the assumed axiom nodes `peano_axioms`,
`axiom_of_choice`, `countable_choice`). ℝ built via Dedekind cuts;
`lub_property` proved, not assumed. `countable_union_countable` is the one node
that uses countable choice, and it is edged.

## Discharging math-real-analysis's roots

| analysis root | discharged by |
|---|---|
| `rational_field` | `rational_is_ordered_field` (ℚ constructed + proved) |
| `real_number` | `real_number` + `real_is_ordered_field` (cuts) |
| `lub_axiom` (an axiom there) | **`lub_property`** (a theorem here) |
| `natural_number` | refined to `peano_axioms` + `recursion_theorem` + ℕ arithmetic; set model still cited |
| `axiom_of_choice` | stays an axiom — correctly independent |
