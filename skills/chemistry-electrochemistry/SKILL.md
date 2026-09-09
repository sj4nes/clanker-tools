---
name: chemistry-electrochemistry
description: >-
  Electrochemistry for making substances and storing energy, as a curated,
  dependency-ordered knowledge capsule — the Faraday charge/electron/mass
  bookkeeping (m = ItM/zF), current efficiency and specific energy consumption,
  electrochemical cells and the anode/cathode convention, standard reduction
  potentials and the SHE, E°_cell and ΔG = -zFE and ΔG° = -RT ln K, the Nernst
  equation, overpotential (activation/concentration/ohmic) and why real
  electrolysis costs more than E°, product selectivity (Cl2 vs O2), electrolyte
  transport (molar conductivity, mobility, transport number, Kohlrausch), seven
  named production processes (water electrolysis, chlor-alkali, chlorate,
  Hall-Heroult, copper refining, zinc electrowinning, reversible fuel cell), and
  redox flow batteries (energy-power decoupling, state of charge, the coulombic /
  voltage / energy efficiencies, crossover, capacity fade, all-vanadium). A
  110-node acyclic graph; every relation carries its symbols, SI units,
  [M L T Theta N I] dimensions, exactness label, assumptions as graph nodes, one
  special-case check, failure modes, and a source. Use when solving or checking
  an electrolysis / plating / electrowinning / battery-sizing problem, when you
  need the minimum prerequisite chain for a result, or when you must know which
  assumption a relation depends on. Built with the physics-formula-tree method;
  builds on chemistry-foundations. Butler-Volmer is stated, not derived;
  electrode microkinetics, the double layer, photo-electrochemistry, corrosion
  engineering, and non-flow battery chemistries are out of scope.
version: 0.1.0
author: Simon Janes
tags: [chemistry, electrochemistry, electrolysis, electrosynthesis, faraday, nernst, flow-battery, redox, knowledge-capsule]
---

# Electrochemistry — Release 0.1

A knowledge capsule built with the
[`physics-formula-tree`](../physics-formula-tree/SKILL.md) method: a 110-node
directed acyclic graph (256 edges) of electrical primitives, conventions,
first-class assumptions, half-reactions, cell relations, imported thermodynamic
bridges, and named production processes for **electrosynthesis and redox flow
batteries**, linearized with `tsort`. Use it as a trustworthy reference for the
bookkeeping of electrochemistry — not a course.

Builds on [`chemistry-foundations`](../chemistry-foundations/SKILL.md)
(Release 0.1) and [`physics-thermodynamics`](../physics-thermodynamics/SKILL.md)
via `bridge_imported` nodes. Intended, like `chemistry-foundations`, as a
verified substrate for a later **synthesis / process capsule** — electrosynthesis
is much of "how to make X from air, water, salt, and electricity".

## Scope

Covered / excluded / conventions: **read [`scope.md`](scope.md) and
[`conventions.md`](conventions.md) first.** Two applied aims shape the selection:
**making substances** (the Faraday bookkeeping, current efficiency, specific
energy, overpotential, product selectivity, named processes) and **flow
batteries** (energy–power decoupling, state of charge, the three efficiencies,
crossover, all-vanadium). Excluded: electrode microkinetics (Butler–Volmer
**stated, not derived**), the electrical double layer, semiconductor /
photo-electrochemistry, corrosion engineering (one boundary node), analytical
methods (CV, EIS), non-flow batteries (one contrast node), and fuel-cell
engineering (one node — "the electrolyser run backwards"). Dimensional basis is
`[M L T Θ N I]` — electric current `I` is added as a base dimension.

## How to use this capsule

1. **Find the relation** — [`indexes/formula-index.md`](indexes/formula-index.md)
   (by relation) or [`indexes/topic-index.md`](indexes/topic-index.md)
   (by sub-domain).
2. **Read its entry** — [`formulas/electrochemistry.md`](formulas/electrochemistry.md):
   every symbol, unit, `[M L T Θ N I]` dimension, exactness label, assumptions,
   one special-case check, failure modes, source.
3. **Check the regime.** [`indexes/assumption-index.md`](indexes/assumption-index.md)
   — `dilute_ideal_solution` (every `E`/`Q`/`K`/`Λ_m`), the SHE zero, the
   `standard_state` convention, Butler–Volmer as a boundary node, and the
   embedded 298.15 K / ideal-gas / `α ≈ 0.5` assumptions.
4. **Need the background?**
   [`indexes/prerequisite-paths.md`](indexes/prerequisite-paths.md) gives the
   minimal chain for seven headline results (Faraday's law, specific energy,
   water electrolysis, chlor-alkali, the Nernst equation, the all-vanadium flow
   battery, round-trip efficiency);
   [`indexes/tsort-order.txt`](indexes/tsort-order.txt) is one full valid order.
5. **Symbols** (which nodes use `E°`, `η`, `z`, `F`, `Λ_m`, …):
   [`indexes/symbol-index.md`](indexes/symbol-index.md).
6. **Conventions** (reduction potentials, anode = oxidation, `E°_cell =
   E°_cathode − E°_anode`, `ΔG = −zFE`, overpotential adds work):
   [`conventions.md`](conventions.md); latent cycles pre-empted in
   [`edges/cycles.md`](edges/cycles.md).

## What has been verified

Run
`sh build/build-tree.sh && bc -q -l validation/dimensional-checks.bc && lean validation/derivation-checks.lean`
then see [`validation/consistency-audit.md`](validation/consistency-audit.md):

- **Graph:** 110 nodes, 256 edges; `tsort` acyclic (BSD-safe stderr check);
  every edge respected; no isolated nodes; six latent cycles pre-empted in
  modeling ([`edges/cycles.md`](edges/cycles.md)).
- **Dimensions:** 17 relations checked on the `[M L T Θ N I]` 6-tuple via `bc`
  ([`validation/dimensional-checks.bc`](validation/dimensional-checks.bc)) — all
  `0 0 0 0 0 0`. Dimensional consistency is necessary, not sufficient.
- **Arithmetic:** 29 kernel-`decide` instance checks via Lean
  ([`validation/derivation-checks.lean`](validation/derivation-checks.lean)) —
  the Faraday mass/volume bookkeeping, `E°_cell = E°_cathode − E°_anode`,
  `ΔG = −zFE`, `ln K = zFE°/RT`, the Nernst zero at `Q = K`, the `59.16/z` mV
  decade, the `118 mV` Tafel slope, the additive `V_cell`, and the flow-battery
  capacity and efficiency. Not the imported thermodynamics, not Butler–Volmer,
  not any tabulated value.

## Limitations

This is a curated dependency graph, not a complete account of electrochemistry.
A valid `tsort` order confirms only the encoded prerequisite constraints.
Dimensional consistency and the Lean instance checks do not establish
electrochemical correctness. Every relation stays conditional on its stated
model, regime, convention, and source; every `E`/`Q`/`K`/`Λ_m` additionally
assumes `dilute_ideal_solution` and 298.15 K. All 110 nodes are still
`status: draft`. `butler_volmer_equation` and the boundary nodes
(`corrosion_as_galvanic_cell`, `pourbaix_diagram`, `electrical_double_layer`,
`debye_huckel_onsager`) are named, not developed. Structural gaps (import the
electrical primitives, promote the embedded assumptions, per-node pages, YAML,
the review pass) are tracked in the consistency audit for Release 0.2.

## Maintenance

Adding or changing a relation: follow
[`physics-formula-tree`](../physics-formula-tree/SKILL.md) steps 5–10 — search
`nodes/ formulas/ indexes/` first, add only direct prerequisite edges with an
evidence comment in [`edges/dependencies.plan`](edges/dependencies.plan), re-run
`sh build/build-tree.sh` and the `bc` / `lean` checks, regenerate the indexes
(`build/gen-assumption-index.sh`; the symbol and curated indexes by hand), bump
the release and changelog.
