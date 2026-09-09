---
name: chemistry-foundations
description: >-
  Quantitative general chemistry (general chem I) as a curated,
  dependency-ordered knowledge capsule — the mole and atomic bookkeeping,
  formulas and percent composition, balancing equations, limiting reagent and
  yield, solution and gas stoichiometry, thermochemistry through Hess's law and
  formation enthalpies, chemical equilibrium (K, Q, Kp/Kc, ICE tables, the
  reaction isotherm), acid–base equilibria (Kw, pH, Ka, Ka·Kb=Kw,
  Henderson–Hasselbalch, buffers), and redox balancing. A 113-node acyclic
  graph: every relation carries its symbols, SI units, [M L T Θ N] dimensions
  (amount of substance first-class), exactness label, assumptions as graph
  nodes, one special-case check, failure modes, and a source. Use when solving
  or checking a stoichiometry / thermochemistry / equilibrium / acid–base /
  redox problem, when you need the minimum prerequisite chain for a result, or
  when you must know which assumption (dilute ideal solution, ideal gas,
  standard state) a formula depends on. Built with, and maintained per, the
  physics-formula-tree method. Excludes kinetics, electrochemistry, colligative
  properties, quantum/orbital bonding, and non-ideal solution theory.
version: 0.1.0
author: Simon Janes
tags: [chemistry, general-chemistry, stoichiometry, thermochemistry, equilibrium, acid-base, redox, formulas, dependencies, knowledge-capsule]
---

# Chemistry Foundations — Release 0.1

A knowledge capsule built with the
[`physics-formula-tree`](../physics-formula-tree/SKILL.md) method: a 113-node
directed acyclic graph (215 edges) of primitives, conventions, first-class
assumptions, definitions, conservation laws, imported thermodynamic bridges, and
canonical relations for **quantitative general chemistry**, linearized with
`tsort`. Use it as a trustworthy reference for the bookkeeping of chemistry —
not a course.

Intended as the verified substrate for a later, separate **synthesis / process
capsule** ("how to make X" keyed by product → route → feedstocks → unit
operations → hazards) for the homesteading / self-sufficiency project.

## Scope

Covered / excluded / conventions / exactness policy: **read
[`scope.md`](scope.md) and [`conventions.md`](conventions.md) first.** In brief
— SI units with the mole and amount of substance (`N`) as a base dimension;
atomic and mole bookkeeping; balancing, limiting reagent, yield; solutions and
gases; thermochemistry through Hess's law and formation enthalpies; equilibrium
`K`/`Q`/`Kp`/`Kc`/ICE; acid–base `Kw`/pH/`Ka`/buffers; redox **balancing** only.
Excluded: chemical kinetics, electrochemistry (cells, Nernst, Faraday),
colligative properties, all orbital / quantum bonding theory, nuclear and
organic chemistry, real-gas equations of state, and non-ideal solution theory
(every `K` / `Q` / pH node carries the `dilute_ideal_solution` assumption).
`ΔG = ΔH − TΔS`, `G = H − TS`, `ΔG° = −RT ln K`, and `PV = nRT` are **imported**
from [`physics-thermodynamics`](../physics-thermodynamics/SKILL.md), not derived
here.

## How to use this capsule

1. **Find the relation** — [`indexes/formula-index.md`](indexes/formula-index.md)
   (by relation) or [`indexes/topic-index.md`](indexes/topic-index.md) (by
   sub-domain).
2. **Read its entry** —
   [`formulas/chemistry-foundations.md`](formulas/chemistry-foundations.md):
   every symbol, unit, `[M L T Θ N]` dimension, exactness label, assumptions,
   one special-case check, failure modes, source.
3. **Check the regime before applying it.** If the problem violates a listed
   assumption, the relation is out of scope — see the "Failure" line and
   [`indexes/assumption-index.md`](indexes/assumption-index.md) (which nodes
   each assumption / convention governs, and the transitive reach of
   `dilute_ideal_solution`).
4. **Need the background?**
   [`indexes/prerequisite-paths.md`](indexes/prerequisite-paths.md) gives the
   minimal chain of prior concepts for seven headline results;
   [`indexes/tsort-order.txt`](indexes/tsort-order.txt) is one full valid order.
5. **Symbols** (which nodes use `K_a`, `ΔH`, `ν`, `χ`, …):
   [`indexes/symbol-index.md`](indexes/symbol-index.md).
6. **Conventions** (sign of `q`/`w`, standard state, the mole as primitive, the
   imported bridges, the excluded rate cycle):
   [`conventions.md`](conventions.md) and [`edges/cycles.md`](edges/cycles.md).

## What has been verified

Run
`sh build/build-tree.sh && bc -q -l validation/dimensional-checks.bc && lean validation/derivation-checks.lean`
then see [`validation/consistency-audit.md`](validation/consistency-audit.md):

- **Graph:** 113 nodes, 215 edges; `tsort` acyclic (BSD-safe stderr check);
  every edge respected by the order; no isolated nodes; six latent chemistry
  cycles (including `equilibrium ↔ rate`, resolved by excluding rate entirely)
  pre-empted in modeling ([`edges/cycles.md`](edges/cycles.md)).
- **Dimensions:** 18 relations checked component-wise on `[M L T Θ N]` via `bc`
  ([`validation/dimensional-checks.bc`](validation/dimensional-checks.bc)) — all
  consistent; the equilibrium constants, `Q`, `K_w`, `K_a`, pH argument, mole
  fraction and percent quantities are dimensionless by construction (each `[X]`
  is `c/c°`, each `P` is `P/P°`). Dimensional consistency is necessary, not
  sufficient.
- **Derivation algebra:** 23 kernel-`decide` instance identities via Lean
  ([`validation/derivation-checks.lean`](validation/derivation-checks.lean)) —
  the *arithmetic* of Hess's law, the formation-enthalpy sum, the Kp/Kc exponent
  bookkeeping, the reaction isotherm at `Q = K`, `Ka·Kb = Kw`,
  Henderson–Hasselbalch, `pH + pOH = pKw`, redox electron / charge balance,
  formal charge, and the integer formula multiplier. Not the chemistry: not that
  `H` is a state function, not the ideal-gas model, not the imported `ΔG`
  relations, not any tabulated value.

## Limitations

This is a curated dependency graph, not a complete account of chemistry. A valid
`tsort` order confirms only the encoded prerequisite constraints. Dimensional
consistency and the Lean instance checks do not establish chemical correctness.
Every relation's validity stays conditional on its stated model, regime,
convention, and source; every `K` / `Q` / pH result additionally assumes
`dilute_ideal_solution`, and every gas result assumes the ideal gas. All 113
nodes are still `status: draft`. Known structural gaps (promote `ideal_gas` to a
node, per-node pages, YAML entries, universal Lean proofs, the review pass) are
tracked in the consistency audit for Release 0.2.

## Maintenance

Adding or changing a relation: follow
[`physics-formula-tree`](../physics-formula-tree/SKILL.md) steps 5–10 — search
`nodes/ formulas/ indexes/` first, add only direct prerequisite edges with an
evidence comment in
[`edges/dependencies.plan`](edges/dependencies.plan), re-run
`sh build/build-tree.sh` and the `bc` / `lean` checks, regenerate the indexes
(`build/gen-assumption-index.sh`; the symbol and curated indexes by hand), bump
the release and changelog. Changing a convention node
(`heat_work_sign_convention`, `standard_state`) is a broad semantic change —
revalidate every downstream relation.
