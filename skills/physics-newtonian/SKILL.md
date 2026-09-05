---
name: physics-newtonian
description: >-
  Newtonian point-particle mechanics as a curated, dependency-ordered knowledge
  capsule — kinematics, Newton's three laws, work/energy and its conservation,
  momentum/impulse, simple harmonic motion, and Newtonian gravitation. Every
  formula carries its symbols, SI units, [M L T] dimensions, exactness label,
  assumptions (as first-class graph nodes), one limiting-case check, failure
  modes, and a source. Use when solving or checking a mechanics problem, when you
  need the minimum prerequisite chain for a mechanics formula, or when you must
  know whether a formula is valid in a given regime. Built with, and maintained
  per, the physics-formula-tree method.
version: 0.1.0
author: Simon Janes
tags: [physics, mechanics, newtonian, formulas, dependencies, knowledge-capsule]
---

# Newtonian Mechanics — Release 0.1

A knowledge capsule built with the
[`physics-formula-tree`](../physics-formula-tree/SKILL.md) method: a 58-node
directed acyclic graph of primitives, conventions, first-class assumptions,
laws, bridges, and canonical formulas, linearized with `tsort`. Use it as a
trustworthy mechanics reference, not a course.

## Scope

Covered / excluded / conventions / exactness policy: **read
[`scope.md`](scope.md) first.** In brief — SI units, single-variable calculus
prerequisites, 1-D/vector-consistent scalar mechanics through gravitation and
SHM. Excluded: rotation, relativity, EM, thermodynamics, fluids, Lagrangian
mechanics, non-inertial frames, numerics.

## How to use this capsule

1. **Find the formula** — [`indexes/formula-index.md`](indexes/formula-index.md)
   (by quantity) or [`indexes/topic-index.md`](indexes/topic-index.md).
2. **Read its entry** — [`formulas/newtonian.md`](formulas/newtonian.md): every
   symbol, unit, dimension, its exactness label, assumptions, one special-case
   check, failure modes, source.
3. **Check the regime before applying it.** If the problem violates a listed
   assumption, the formula is out of scope — see the "Failure" line and
   [`indexes/assumption-index.md`](indexes/assumption-index.md) (which formulas
   each assumption governs).
4. **Need the background?**
   [`indexes/prerequisite-paths.md`](indexes/prerequisite-paths.md) gives the
   minimal chain of prior concepts for the core formulas;
   [`indexes/tsort-order.txt`](indexes/tsort-order.txt) is one full valid order.
5. **Conventions** (signs, `g`, reference points, primitive choices):
   [`conventions.md`](conventions.md).

## What has been verified

Run `sh build/build-tree.sh` then see
[`validation/consistency-audit.md`](validation/consistency-audit.md):

- **Graph:** 58 nodes, 145 edges; `tsort` acyclic (BSD-safe stderr check); every
  edge respected by the order; no isolated nodes; four classic mechanics cycles
  (mass↔force, force↔acceleration, energy↔work, momentum↔force) avoided by
  documented edge-direction choices ([`edges/cycles.md`](edges/cycles.md)).
- **Dimensions:** 13 formulas checked component-wise on `[M L T]` via `bc`
  ([`validation/dimensional-checks.bc`](validation/dimensional-checks.bc)) — all
  consistent. Dimensional consistency is necessary, not sufficient.
- **Derivation algebra:** 5 kernel-checked instance identities via Lean
  ([`validation/derivation-checks.lean`](validation/derivation-checks.lean)) —
  the *algebra* of the kinematics elimination, work–energy theorem, elastic PE,
  SHM frequency, and pendulum reduction. Not the physical premises.

## Limitations

This is a curated dependency graph, not a complete account of mechanics. A valid
`tsort` order confirms only the encoded prerequisite constraints. Dimensional
consistency and the Lean instance checks do not establish physical correctness.
Every formula's validity remains conditional on its stated theory, regime,
convention, and source. Known structural gaps (per-node pages, YAML entries,
static friction, 2-D kinematics, orbital energy) are tracked in the consistency
audit for Release 0.2.

## Maintenance

Adding or changing a formula: follow
[`physics-formula-tree`](../physics-formula-tree/SKILL.md) steps 5–10 — search
first, add only direct prerequisite edges with an evidence comment in
[`edges/dependencies.plan`](edges/dependencies.plan), re-run `build/build-tree.sh`
and the `bc`/`lean` checks, regenerate the indexes, bump the release and
changelog.
