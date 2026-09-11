# physics-thermodynamics

Classical equilibrium thermodynamics as a **knowledge capsule**, built with the
[`physics-formula-tree`](../physics-formula-tree/SKILL.md) method.

- Start: [`SKILL.md`](SKILL.md) · [`scope.md`](scope.md) · [`conventions.md`](conventions.md)
- Graph: [`nodes/nodes.tsv`](nodes/nodes.tsv) · [`edges/dependencies.plan`](edges/dependencies.plan) · [`edges/cycles.md`](edges/cycles.md)
- Formulas: [`formulas/thermodynamics.md`](formulas/thermodynamics.md)
- Views: [`indexes/`](indexes/) — formula / topic / assumption indexes, tsort order, prerequisite paths
- Sources: [`sources/bibliography.md`](sources/bibliography.md)

## Build

```sh
sh build/run.sh                              # graph-check -> tsort -> views -> bc -> lean
```

Individually:

```sh
sh build/build-tree.sh                       # graph-check -> tsort -> reverse deps
sh build/gen-topic-index.sh                  # topic index (registry-derived)
sh build/gen-assumption-index.sh             # assumption -> governed formulas
sh build/gen-prereq-paths.sh                 # minimal prerequisite paths for the core results
bc -q -l validation/dimensional-checks.bc    # [M L T Theta N] consistency, 10 relations + 6 numeric
lean validation/derivation-checks.lean       # 8 kernel-checked algebra instances
```

## Tutorials

An `upmd`-executable tutorial, built with the `formula-tree-tutorial`
skill, verified with `upmd --ci --all` (every block exits 0) and a
standalone capstone + mid-chain run:

- [`tutorial/why-heat-engines-have-a-ceiling.md`](tutorial/why-heat-engines-have-a-ceiling.md)
  — `zeroth_law` → `carnot_efficiency` (trimmed from the full 42-node
  prerequisite path to the physically load-bearing steps); capstone
  computes the Carnot ceiling for a real coal-fired steam plant
  (`Th≈838K, Tc≈298K` → ~64%) and contrasts it with real plants' 35–40%.

## Method verification (Release 0.1)

Building this capsule exercised the `physics-formula-tree` method on a 77-node
graph spanning the four laws.

| Stage | Tool | Result |
|---|---|---|
| graph + sort | BSD `tsort` | 77 nodes, 220 edges, **acyclic** (stderr-checked); every edge respected; 0 isolated. Five conceptual cycles (temperature↔zeroth-law, temperature↔absolute-scale, U↔first-law, heat↔first-law, entropy↔second-law) designed out in advance — see [`edges/cycles.md`](edges/cycles.md). |
| dimensional | GNU `bc` 7.0.3 | 10/10 relations consistent on the `[M L T Θ N]` basis; 6/6 numeric special cases (Carnot `η=0.5`, diatomic `γ=1.4`, Mayer `c_p−c_v≈R`, free-expansion `ΔS=R ln2>0`, adiabatic `T₂/T₁=2^−0.4`). Five-tuple lowercase-exponent trick from the method's `bc` guidance; a void-return print artifact suppressed with an assignment sink. |
| derivations | Lean 4.33.1, **no Mathlib** | 8/8 `Int` instance checks pass — Mayer, `γ−1=R/c_v`, Carnot `η` from the heat ratio, `COP_hp=COP_ref+1`, `dH=T dS+V dP`, free-expansion `ΔU=0`, ideal-gas entropy coefficient. Instance checks only (no `ring` without Mathlib); the physical premises are **not** verified. |

Structural nodes are `reviewed`; the 15 derived-formula nodes are `draft`
pending per-node `bc`/`lean` cross-checks (Release 0.2, with open systems / `μ`,
phase equilibria, real-gas EoS, per-node pages, and an `upmd` tutorial).

## Limitations

A curated dependency graph, not a complete account of thermodynamics. A valid
`tsort` order confirms only the encoded prerequisite constraints; dimensional
consistency and the Lean instance checks are not physical correctness. Every
formula's validity stays conditional on its theory, regime, sign convention
(`dU = δQ − δW` here), and source.
