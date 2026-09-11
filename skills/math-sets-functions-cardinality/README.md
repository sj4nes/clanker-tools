# math-sets-functions-cardinality

Sets, functions, orders, and cardinality as a **knowledge capsule** — built with
the [`math-theorem-tree`](../math-theorem-tree/SKILL.md) method, and the layer
**below** [`math-number-systems`](../math-number-systems/SKILL.md): every
primitive that capsule takes on faith (`set`, `function`, `quotient_set`,
`axiom_of_choice`, `peano_axioms`, `recursion_theorem`) is a node here, and
`peano_holds_in_omega` proves the Peano axioms from the Axiom of Infinity.

- Start: [`SKILL.md`](SKILL.md) · [`scope.md`](scope.md) · [`conventions.md`](conventions.md) · [`objects.md`](objects.md)
- Graph: [`nodes/nodes.tsv`](nodes/nodes.tsv) · [`edges/dependencies.plan`](edges/dependencies.plan) · [`edges/cycles.md`](edges/cycles.md) · [`edges/relations.tsv`](edges/relations.tsv)
- Results: [`results/`](results/) (15 headline YAMLs) · [`nodes/`](nodes/) (3 exemplar detail pages)
- Views: [`indexes/`](indexes/) — topic, hypothesis, status, counterexample, prerequisite-path, symbol
- Verification: [`validation/consistency-audit.md`](validation/consistency-audit.md)

## Build

```sh
sh build/all.sh                        # everything
sh build/build-tree.sh                 # 106 nodes, 263 edges, acyclic, 1 root (proposition_logic)
lean validation/proof-checks.lean      # 11 kernel checks: the preimage algebra (rfl!) + Cantor's diagonal
bc -q -l validation/instance-checks.bc  # the countability bijections and the diagonal argument, run
```

## Release 0.1 at a glance

106 nodes (52 definitions, 24 theorems, 12 axioms, 6 propositions, 3 principles,
3 primitives, 2 constructions, 2 structures, 1 regime, 1 convention), 263 edges,
acyclic, rooted at the single node `proposition_logic` (plus the 12 assumed
axiom nodes: 9 ZF + AC + DC + CC). **Every result carries a `choice_grade`**:
`choice_free` (CSB, Cantor's theorem, Hartogs, finite pigeonhole, the preimage
algebra), `needs_countable_choice` (countable unions), or `needs_full_AC` (Zorn,
well-ordering, comparability). `continuum_hypothesis` is `independent_of_ZFC`.

## Discharging math-number-systems' primitives

| number-systems primitive | discharged by |
|---|---|
| `set`, `function`, `relation`, `equivalence_relation`, `quotient_set`, `cartesian_product`, `well_defined_on_quotient` | nodes here |
| `peano_axioms` | **`peano_holds_in_omega`** (built from `axiom_infinity`) |
| `recursion_theorem` | **`recursion_theorem`** (proved from the `ω` model) |
| `axiom_of_choice`, `countable_choice` | nodes here (AC stays an axiom, correctly) |

It also supplies **`preimage_algebra`** — the node `math-real-analysis`'s
continuity and compactness proofs actually stand on.

## Release 0.2 — logic floor discharged

`proposition_logic`, `predicate_logic`, `quantifier_negation`,
`quantifier_order`, `proof_methods` were Release 0.1 primitives "cited to a
future `math-logic-and-proof`". That capsule now exists and develops them; see
[`edges/cross-capsule.md`](edges/cross-capsule.md) for the discharge table.
They stay `primitive` in this capsule's own `tsort` graph — the two capsules'
foundations are mutually grounding (this capsule assumes logic to state ZFC;
that capsule assumes naive set talk to state its semantics), so the discharge
is recorded as metadata, not a `tsort` edge, exactly as `math-logic-and-proof`
already documents from its side. `proposition_logic` and `predicate_logic`
promoted `active` → `reviewed`.
