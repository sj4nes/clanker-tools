---
name: physics-thermoacoustics
description: >-
  Linear thermoacoustics as a curated, dependency-ordered knowledge capsule —
  the coupling of acoustic oscillations and heat transport in thermoacoustic
  engines and refrigerators. Covers ideal-gas and thermodynamic prerequisites,
  transport properties, linear acoustics, thermal and viscous penetration
  depths, Rott's linear wave equation with the complex f-functions, the
  short-stack (Swift) results, the critical temperature gradient, and
  standing-wave vs traveling-wave (Stirling) device analysis with the Carnot
  limit. Use when reasoning about thermoacoustic device physics, when you need
  the prerequisite chain or regime of validity for a thermoacoustic relation, or
  when deciding between standing-wave and traveling-wave configurations. Built
  with, and maintained per, the physics-formula-tree method. Assumes the
  physics-newtonian capsule plus elementary thermodynamics.
version: 0.1.0
author: Simon Janes
tags: [physics, thermoacoustics, acoustics, thermodynamics, rott, stirling, engines, refrigerators]
---

# Linear Thermoacoustics — Release 0.1

A knowledge capsule built with the
[`physics-formula-tree`](../physics-formula-tree/SKILL.md) method: a 104-node
directed acyclic graph running from complex phasor calculus and the ideal-gas
law up to the Rott wave equation and the traveling-wave (thermoacoustic-Stirling)
engine. Scoped to track *the theory behind the most effective real devices* —
the Rott equations and their regenerator / traveling-wave limit — with Swift's
short-stack standing-wave analysis as the analytic on-ramp.

## Scope

Read [`scope.md`](scope.md) first. In brief: ideal-gas + thermodynamic +
transport prerequisites; linear acoustics of an ideal gas; thermal/viscous
penetration depths and the stack vs regenerator regimes; Rott's linearized
momentum, continuity, and wave equations with the complex `f_ν`, `f_κ`
functions and an imposed mean temperature gradient; energy conversion (total
energy flux, heat flux, critical temperature gradient, `Γ`, short-stack
results); devices (standing/traveling-wave engine and refrigerator, onset,
efficiency, COP, the Carnot limit). Excluded: nonlinear thermoacoustics,
streaming, time-domain analysis, DeltaEC numerics, pulse-tube network detail,
solid-side losses.

## How to use this capsule

1. **Find the relation** — [`indexes/formula-index.md`](indexes/formula-index.md)
   (by quantity) or [`indexes/topic-index.md`](indexes/topic-index.md).
2. **Read its entry** — [`formulas/thermoacoustics.md`](formulas/thermoacoustics.md):
   symbols, SI units, `[M L T Θ]` dimensions, exactness label, assumptions, one
   special-case check, failure modes, source.
3. **Check the regime.** Standing-wave vs traveling-wave phasing, stack vs
   regenerator (`r_h` vs `δ_κ`), short-stack vs full Rott, ideal gas, small
   amplitude — [`indexes/assumption-index.md`](indexes/assumption-index.md) lists
   which nodes each assumption governs.
4. **Need the background?**
   [`indexes/prerequisite-paths.md`](indexes/prerequisite-paths.md) gives the
   minimal chain for the core results;
   [`indexes/tsort-order.txt`](indexes/tsort-order.txt) is one full valid order.
5. **Conventions** (`[M L T Θ]` basis, `e^{+iωt}` phasors, `x` cold→hot, sign of
   `∇T_m`, primitive choices): [`conventions.md`](conventions.md).

## What the graph encodes about device effectiveness

- **Standing-wave devices** depend on `standing_wave_phasing` +
  `short_stack_approximation` + `boundary_layer_limit_f` — deliberately
  *imperfect* gas–wall thermal contact (`f_κ → 0`), which is intrinsically
  irreversible. Reachable efficiency ~10–20% (`~0.2–0.4 η_C`).
- **Traveling-wave (Stirling) devices** depend on `regenerator_regime`
  (`r_h ≪ δ_κ`, so `f_κ → 1`, near-reversible), `travelling_wave_phasing`,
  `ceperley_travelling_wave`, `acoustic_impedance_matching`, and `feedback_torus`.
  Backhaus & Swift (2000): `η ≈ 0.30 ≈ 0.40 η_C` — the effective-device branch.

The `critical_temperature_gradient` and `temperature_gradient_ratio` `Γ` nodes
are the standing-wave design handles; `Γ > 1` engine, `Γ < 1` refrigerator.

## What has been verified

Run `sh build/build-tree.sh`; see
[`validation/consistency-audit.md`](validation/consistency-audit.md).

- **Graph:** 104 nodes, 253 edges; `tsort` acyclic (BSD-safe check); every edge
  respected; no isolated nodes; five thermoacoustic coupling cycles avoided by
  documented edge-direction choices ([`edges/cycles.md`](edges/cycles.md)).
- **Dimensions:** 19 checks on the `[M L T Θ]` basis via `bc`
  ([`validation/dimensional-checks.bc`](validation/dimensional-checks.bc)) — all
  consistent, including the Rott momentum equation and the critical gradient.
- **Derivation algebra:** 13 kernel-checked instance identities via Lean
  ([`validation/derivation-checks.lean`](validation/derivation-checks.lean)) —
  Mayer/`γ`, the penetration-depth ratio, the Carnot relations, standing vs
  traveling acoustic-power phasing, the `Γ − 1` sign, and the Rott → free wave
  equation reduction. Not the physical premises.

## Limitations

This is a curated dependency graph, not a complete account of thermoacoustics.
A valid `tsort` order confirms only the encoded prerequisite constraints.
Dimensional consistency and the Lean instance checks do not establish physical
correctness. Ten nodes (the `f`-function closed forms, the full Rott continuity
and wave equations, the short-stack power/flux coefficients, the energy-flux
expressions) are carried at **`draft`** status — structure and dimensions
checked, exact coefficients pending line-by-line reconciliation with Swift 1988 /
Swift 2002 ch. 4. Every relation's validity remains conditional on its stated
regime, phasing, geometry, and source.

## Maintenance

Adding or changing a relation: follow
[`physics-formula-tree`](../physics-formula-tree/SKILL.md) steps 5–10 — search
first, add only direct prerequisite edges with an evidence comment in
[`edges/dependencies.plan`](edges/dependencies.plan), re-run `build/build-tree.sh`
and the `bc`/`lean` checks, regenerate the indexes, bump the release and
changelog. Promoting a `draft` node to `reviewed` requires the source-reconciled
formula plus its dimensional and (where algebraic) Lean check.
