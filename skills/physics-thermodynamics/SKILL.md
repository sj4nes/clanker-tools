---
name: physics-thermodynamics
description: >-
  Classical equilibrium thermodynamics as a curated, dependency-ordered
  knowledge capsule — the zeroth/first/second/third laws, the ideal-gas model,
  heat capacities and enthalpy, reversible adiabats, the Carnot results and the
  thermodynamic temperature scale, entropy and the entropy-increase principle,
  and the thermodynamic potentials with the Maxwell relations. Every formula
  carries its symbols, SI units, [M L T Θ N] dimensions, exactness label,
  first-class assumptions, the first-law sign convention it uses, one
  limiting-case check, failure modes, and a source. Use when solving or checking
  a thermodynamics problem, when you need the minimum prerequisite chain for a
  result, or when you must know which assumption (ideal gas, reversibility,
  closed system) a formula depends on and what breaks without it. Built with,
  and maintained per, the physics-formula-tree method. Excludes statistical
  mechanics, open systems and chemical potential, phase equilibria, and real-gas
  equations of state.
version: 0.1.0
author: Simon Janes
tags: [physics, thermodynamics, entropy, carnot, ideal-gas, first-law, second-law, formulas, dependencies, knowledge-capsule]
---

# Classical Thermodynamics — Release 0.1

A knowledge capsule built with the
[`physics-formula-tree`](../physics-formula-tree/SKILL.md) method: a 77-node
directed acyclic graph of primitives, conventions, first-class assumptions,
laws, bridges, and canonical formulas, linearized with `tsort`. Use it as a
trustworthy thermodynamics reference, not a course.

## Scope

Covered / excluded / conventions / exactness policy: **read
[`scope.md`](scope.md) first.** In brief — SI units, partial derivatives and
exact differentials as math prerequisites, macroscopic equilibrium
thermodynamics through the four laws, the Carnot results, entropy, and the
potentials. **Excluded:** statistical mechanics and any microscopic derivation,
open systems / chemical potential `μ` / mixtures, phase and chemical equilibrium
(so no Clausius–Clapeyron), real-gas equations of state, non-equilibrium
thermodynamics, radiation thermodynamics, thermoacoustics (its own capsule).

## Sign convention (load-bearing)

This release fixes the **first law as `dU = δQ − δW` with `δW = P dV`** — heat
added to the system and work done *by* the system are positive. The alternative
`dU = δQ + δW` is noted in [`conventions.md`](conventions.md) and not used.
Every formula here is written to this convention.

## How to use this capsule

1. **Find the result** — [`indexes/formula-index.md`](indexes/formula-index.md)
   (by quantity) or [`indexes/topic-index.md`](indexes/topic-index.md) (by area).
2. **Read its entry** —
   [`formulas/thermodynamics.md`](formulas/thermodynamics.md): every symbol,
   unit, dimension, exactness label, assumptions, one special-case check,
   failure modes, source.
3. **Check the regime before applying it.** If the problem violates a listed
   assumption (`ideal_gas`, `reversible`, `closed_system`, `quasistatic`), the
   formula is out of scope — see the "Failure" line and
   [`indexes/assumption-index.md`](indexes/assumption-index.md) (which formulas
   each assumption governs).
4. **Need the background?**
   [`indexes/prerequisite-paths.md`](indexes/prerequisite-paths.md) gives the
   minimal chain of prior concepts for the core results;
   [`indexes/tsort-order.txt`](indexes/tsort-order.txt) is one full valid order.
5. **Conventions** (signs, differentials, molar vs extensive, primitive
   choices, cycle resolutions): [`conventions.md`](conventions.md).

## What has been verified

Run `sh build/run.sh`:

- **Graph:** 77 nodes, 220 edges; `tsort` acyclic (BSD-safe stderr check); every
  edge respected by the order; no isolated nodes. Five would-be cycles
  (temperature↔zeroth-law, temperature↔absolute-scale, internal-energy↔first-law,
  heat↔first-law, entropy↔second-law) resolved by documented edge-direction
  choices ([`edges/cycles.md`](edges/cycles.md)).
- **Dimensions:** 10 relations checked component-wise on `[M L T Θ N]` via `bc`
  ([`validation/dimensional-checks.bc`](validation/dimensional-checks.bc)) — all
  consistent — plus 6 numeric special-case checks (Carnot `η = 0.5` at
  `T_c/T_h = 1/2`; diatomic `γ = 1.4`; Mayer `c_p − c_v ≈ R`; free-expansion
  `ΔS = R ln 2 > 0`; adiabatic `T₂/T₁ = 2^{−0.4}`). Dimensional consistency is
  necessary, not sufficient.
- **Derivation algebra:** 8 kernel-checked instance identities via Lean
  ([`validation/derivation-checks.lean`](validation/derivation-checks.lean)) —
  the *algebra* of Mayer's relation, the adiabatic exponent `γ − 1 = R/c_v`,
  Carnot efficiency from the heat ratio, `COP_hp = COP_ref + 1`, the
  `dH = T dS + V dP` reduction, the free-expansion `ΔU = 0`, and the ideal-gas
  entropy coefficient. Not the physical premises (the laws, the ideal-gas model,
  reversibility, the quoted `c_v` values).

## Limitations

This is a curated dependency graph, not a complete account of thermodynamics. A
valid `tsort` order confirms only the encoded prerequisite constraints.
Dimensional consistency and the Lean instance checks do not establish physical
correctness. Every formula's validity remains conditional on its stated theory,
regime, sign convention, and source. Derived-formula nodes are `status: draft`
pending per-node `bc`/`lean` cross-checks; structural nodes (primitives,
conventions, assumptions, laws) are `reviewed`. Known scope gaps for Release
0.2: open systems and `μ`, phase equilibria / Clausius–Clapeyron, real-gas
equations of state, per-node detail pages, an `upmd` tutorial.

## Maintenance

Adding or changing a formula: follow
[`physics-formula-tree`](../physics-formula-tree/SKILL.md) steps 5–10 — search
first (`rg` over `nodes/ formulas/ indexes/`), add only direct prerequisite
edges with an evidence comment in
[`edges/dependencies.plan`](edges/dependencies.plan), re-run `build/run.sh` and
the `bc`/`lean` checks, regenerate the indexes, bump the release and changelog.
Changing `work_sign_convention` or `extensive_intensive` is a broad semantic
change — revalidate every downstream formula's signs.
