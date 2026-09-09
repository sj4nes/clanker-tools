# Chemistry Foundations — Release 0.1

A knowledge capsule built with the
[`physics-formula-tree`](../physics-formula-tree/SKILL.md) method: a directed
acyclic graph of primitives, conventions, first-class assumptions, definitions,
laws, imported bridges, and canonical relations for **quantitative general
chemistry**, linearized with `tsort`. Use it as a trustworthy reference for the
bookkeeping of chemistry — not a course.

Intended as the verified substrate for a later **synthesis / process capsule**
(“how to make X”) for the homesteading / self-sufficiency project.

## Scope

**Read [`scope.md`](scope.md) first.** In brief — atoms and the mole, formulas
and percent composition, balancing equations, limiting reagent and yield,
solution and gas stoichiometry, thermochemistry through Hess's law and formation
enthalpies, chemical equilibrium (`K`, `Q`, `Kp/Kc`, ICE tables, the reaction
isotherm), acid–base equilibria (`Kw`, pH, `Ka`, `Ka·Kb=Kw`,
Henderson–Hasselbalch, buffers), and redox **balancing**.

**Excluded:** all orbital / quantum bonding theory (VSEPR and Lewis structures
are kept only as qualitative feeder nodes), chemical **kinetics** (rate laws,
Arrhenius, mechanisms), **electrochemistry** (cells, Nernst, Faraday),
colligative properties, nuclear and organic chemistry, spectroscopy, and
non-ideal solution theory (every `K` / `Q` / pH node carries the
`dilute_ideal_solution` assumption). `ΔG = ΔH − TΔS` and `ΔG° = −RT ln K` are
**imported** from [`physics-thermodynamics`](../physics-thermodynamics/SKILL.md),
not derived here.

## Status

| stage | state |
|---|---|
| `scope.md`, `conventions.md` | done |
| node registry `nodes/nodes.tsv` | **113 nodes**, all `draft` |
| prerequisite graph | **215 edges, acyclic** (`tsort` clean, BSD-safe check), 0 isolated nodes |
| `edges/cycles.md`, `edges/relations.tsv` | done |
| concept/formula entries `formulas/chemistry-foundations.md` | **done** — one entry per node (113), domain-grouped, reconciled against the graph |
| `sources/bibliography.md` | done (BLM, Oxtoby, Zumdahl, Atkins, IUPAC, SI, CODATA, NIST-JANAF) |
| `bc` dimensional checks `validation/dimensional-checks.bc` | **done** — 18 exponent-tuple checks, all `0 0 0 0 0`; worked numbers spot-checked |
| `lean` identity checks `validation/derivation-checks.lean` | **done** — 25 kernel-`decide` instance checks (Hess, formation sum, Kp/Kc exponent, reaction isotherm, Ka·Kb=Kw, Henderson–Hasselbalch, pH+pOH, redox e⁻/charge balance, formal charge, k integer), `lean` exit 0 |
| per-formula YAML `formulas/<id>.yaml` | not used — this method's shipped capsules (physics-newtonian, physics-thermodynamics) consolidate into `formulas/<domain>.md`; same here |
| discovery indexes | **done** — `indexes/topic-index.md`, `formula-index.md`, `symbol-index.md`, `assumption-index.md`, `prerequisite-paths.md` (7 headline targets) |
| `validation/consistency-audit.md` | **done** — full run recorded |
| `SKILL.md` | **done** |

Release 0.1 is complete. Every node is still `status: draft`; the review pass,
promoting `ideal_gas` to a node, per-node pages, and YAML entries are Release
0.2 items (see `validation/consistency-audit.md`).

## Build

```sh
sh build/build-tree.sh                          # graph-check + tsort + cycle check + order verification
bc -q -l validation/dimensional-checks.bc       # 18 [M L T Θ N] checks, want 0 0 0 0 0
lean validation/derivation-checks.lean          # 23 kernel-decide instance checks, exit 0
sh build/gen-assumption-index.sh                # regenerate indexes/assumption-index.md
sh build/gen-symbol-index.sh                    # ptx discovery pass for the hand-curated symbol index
```

`build/build-tree.sh` regenerates `indexes/tsort-order.txt` and
`indexes/reverse-dependencies.txt`.

## Tutorials

Interactive walk-throughs built with the
[`formula-tree-tutorial`](../formula-tree-tutorial/SKILL.md) skill — plain
Markdown run under [`upmd`](https://upmd.dev), the reader executes every check.

| tutorial | target | run |
|---|---|---|
| [`tutorial/how-much-can-this-make.md`](tutorial/how-much-can-this-make.md) | `percent_yield` — grams → moles → limiting reagent → theoretical vs actual yield | `upmd skills/chemistry-foundations/tutorial/how-much-can-this-make.md` |
| [`tutorial/reaction-enthalpy-from-formation.md`](tutorial/reaction-enthalpy-from-formation.md) | `enthalpy_from_formation_enthalpies` — combustion ΔH from a table, no calorimeter | `upmd skills/chemistry-foundations/tutorial/reaction-enthalpy-from-formation.md` |
| [`tutorial/balancing-a-redox-equation.md`](tutorial/balancing-a-redox-equation.md) | `balancing_redox_half_reactions` — oxidation numbers, half-reactions, electron balance (MnO₄⁻/Fe²⁺) | `upmd skills/chemistry-foundations/tutorial/balancing-a-redox-equation.md` |

Block counts: `how-much-can-this-make.md` 13, `reaction-enthalpy-from-formation.md`
11, `balancing-a-redox-equation.md` 8 (5 `awk` checks, 2 `lean` beats, capstone).
All `upmd --ci --all` green. Four more cuts staged in
`indexes/prerequisite-paths.md` (`ice_table`, `henderson_hasselbalch`,
`reaction_isotherm`, `gas_stoichiometry`).

## Reading order caveat

`indexes/tsort-order.txt` is one valid prerequisite-respecting linearization.
Independent nodes fall in an arbitrary tie order — do not read adjacency as
"comes right before". Topological order is not teaching order, historical order,
or conceptual priority.
