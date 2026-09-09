# Electrochemistry — Release 0.1

A knowledge capsule built with the
[`physics-formula-tree`](../physics-formula-tree/SKILL.md) method: a 110-node
directed acyclic graph (256 edges) of electrical primitives, conventions,
first-class assumptions, half-reactions, cell relations, imported thermodynamic
bridges, and named production processes for **electrosynthesis and redox flow
batteries**, linearized with `tsort`. Use it as a trustworthy reference for the
bookkeeping of electrochemistry — not a course.

Builds on [`chemistry-foundations`](../chemistry-foundations/SKILL.md): half-
reactions, redox balancing, the mole, `K` / `Q` / the reaction isotherm, and the
ideal-gas law are imported as `bridge_imported` nodes; `gibbs_free_energy` and
`entropy` come from [`physics-thermodynamics`](../physics-thermodynamics/SKILL.md).

Intended, like `chemistry-foundations`, as the verified substrate for a later
**synthesis / process capsule** for the homesteading / self-sufficiency project.

## Scope

**Read [`scope.md`](scope.md) first.** In brief — `Q = zFn` and `m = ItM/(zF)`,
current efficiency and specific energy; cells and the anode/cathode convention;
standard reduction potentials + SHE; `E°_cell` and `ΔG = −zFE` and
`ΔG° = −RT ln K`; the Nernst equation; overpotential and why real electrolysis
costs more than `E°`; product selectivity (Cl₂ vs O₂); electrolyte transport;
seven named production processes; redox flow batteries.

**Excluded:** electrode microkinetics (Butler–Volmer stated not derived), the
electrical double layer, semiconductor / photo-electrochemistry, corrosion
engineering (one boundary node), analytical methods (CV, EIS), non-flow
batteries (one contrast node), fuel-cell engineering. See `scope.md`.

## Status

| stage | state |
|---|---|
| `scope.md` | **done** — scope signed off 2026-09-09 |
| `conventions.md` | **done** |
| node registry `nodes/nodes.tsv` | **110 nodes**, all `draft` |
| prerequisite graph | **256 edges, acyclic** (`tsort` clean, BSD-safe check), 0 isolated nodes; `edges/cycles.md`, `edges/relations.tsv` done |
| concept/formula entries `formulas/electrochemistry.md` | **done** — one entry per node (110), domain-grouped, reconciled against the graph |
| `sources/bibliography.md` | **done** (BLM, Atkins, Bard & Faulkner, Newman, Pletcher & Walsh, Skyllas-Kazacos, IUPAC, SI, CODATA) |
| `bc` dimensional checks `validation/dimensional-checks.bc` | **done** — 17 checks on the `[M L T Θ N I]` 6-tuple, all `0 0 0 0 0 0` |
| `lean` identity checks `validation/derivation-checks.lean` | **done** — 29 kernel-`decide` instance checks, `lean` exit 0 |
| discovery indexes | **done** — `indexes/topic-index.md`, `formula-index.md`, `symbol-index.md`, `assumption-index.md`, `prerequisite-paths.md` (7 headline targets) |
| `validation/consistency-audit.md` | **done** — full run recorded |
| `SKILL.md` | **done** |
| tutorials | **3 shipped** — see below |

Release 0.1 core is complete. All 110 nodes are still `status: draft`; importing
the electrical primitives from a future `physics-circuits` capsule, promoting the
embedded assumptions to nodes, per-node pages, and the review pass are Release
0.2 items (see `validation/consistency-audit.md`).

## Build

```sh
sh build/build-tree.sh                          # graph-check + tsort + cycle check + order verification
bc -q -l validation/dimensional-checks.bc       # 17 [M L T Θ N I] checks, want 0 0 0 0 0 0
lean validation/derivation-checks.lean          # 29 kernel-decide instance checks, exit 0
sh build/gen-assumption-index.sh                # regenerate indexes/assumption-index.md
sh build/gen-symbol-index.sh                    # ptx discovery pass for the hand-curated symbol index
```

## Tutorials

Interactive walk-throughs built with the
[`formula-tree-tutorial`](../formula-tree-tutorial/SKILL.md) skill — plain
Markdown run under [`upmd`](https://upmd.dev), the reader executes every check.
**Read [`tutorial/README.md`](tutorial/README.md) for the order.**

| # | tutorial | target — one line |
|---|---|---|
| 1 | [`per-amp-hour`](tutorial/per-amp-hour.md) | `faradays_law_electrolysis` — `Q = It`, `z`, `m = ItM/(zF)`, gas volume, current efficiency; capstone sizes a hydrogen electrolyser (~26.6 kA·h/kg H₂) |
| 2 | [`kwh-per-kilogram`](tutorial/kwh-per-kilogram.md) | `specific_energy_consumption` — `E°_cell`, `ΔG = −zFE`, overpotential + IR, `V_cell`, `E_spec = zF V_cell/(M η_F)`; capstone: H₂ ~54 kWh/kg vs Al ~13 kWh/kg |
| 3 | [`chlorine-not-oxygen`](tutorial/chlorine-not-oxygen.md) | `chlor_alkali_process` — competing anode reactions, the effective potential `E° + η`, why the `0.5 V` oxygen overpotential makes Cl₂ win; capstone: a 15 kA cell line, ~19 kg/h Cl₂ at ~2.4 kWh/kg |

`upmd --ci --all` green (11 / 11 / 9 blocks). More cuts staged in
`indexes/prerequisite-paths.md` (`water_electrolysis`, `nernst_equation`,
`all_vanadium_flow_battery`, `energy_efficiency`).

## Reading order caveat

`indexes/tsort-order.txt` is one valid prerequisite-respecting linearization.
Independent nodes fall in an arbitrary tie order — topological order is not
teaching order, historical order, or conceptual priority.
