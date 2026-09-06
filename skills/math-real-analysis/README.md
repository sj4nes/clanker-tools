# math-real-analysis

Real Analysis I as a **knowledge capsule** — the first artifact built with the
[`math-theorem-tree`](../math-theorem-tree/SKILL.md) method (itself the first
adaptation of [`physics-formula-tree`](../physics-formula-tree/SKILL.md) to a new
field), and its proof-of-method.

- Start: [`SKILL.md`](SKILL.md) · [`scope.md`](scope.md) · [`conventions.md`](conventions.md) · [`objects.md`](objects.md)
- Graph: [`nodes/nodes.tsv`](nodes/nodes.tsv) · [`edges/dependencies.plan`](edges/dependencies.plan) · [`edges/cycles.md`](edges/cycles.md) · [`edges/relations.tsv`](edges/relations.tsv)
- Results: [`results/`](results/) (15 headline YAMLs) · [`nodes/`](nodes/) (3 exemplar detail pages)
- Views: [`indexes/`](indexes/) — topic, hypothesis, status, counterexample, prerequisite-path, symbol, equivalent-definitions, common-misuse, generalization
- Verification: [`validation/consistency-audit.md`](validation/consistency-audit.md)

## Build

```sh
sh build/all.sh                        # everything
sh build/build-tree.sh                 # graph-check -> tsort -> views (109 nodes, 247 edges, acyclic)
lean validation/proof-checks.lean      # 12 kernel-checked algebraic cores
bc -q -l validation/instance-checks.bc  # specializations + hypothesis-dropped counterexamples
```

## Release 0.1 at a glance

109 nodes (36 definitions, 33 theorems, 24 propositions, 5 hypotheses, 4
primitives, 3 axioms, 1 structure, 1 principle, 1 notation convention, 1
identity), 247 prerequisite edges, acyclic. ℝ characterized by `lub_axiom`
(construction cited). Choice used only where the standard proof needs countable
choice, and edged to `countable_choice` so every use is visible.

## Method verification

Building this capsule exercised the `math-theorem-tree` method end-to-end. See
[`SKILL.md`](SKILL.md#method-verification-release-01) and the repo README
verification table.
