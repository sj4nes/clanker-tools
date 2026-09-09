# Electrochemistry — Release 0.1 (in progress)

A knowledge capsule built with the
[`physics-formula-tree`](../physics-formula-tree/SKILL.md) method: a directed
acyclic graph of electrical primitives, conventions, first-class assumptions,
half-reactions, cell relations, imported thermodynamic bridges, and named
production processes for **electrosynthesis and redox flow batteries**,
linearized with `tsort`. Use it as a trustworthy reference for the bookkeeping
of electrochemistry — not a course.

Builds on [`chemistry-foundations`](../chemistry-foundations/SKILL.md)
(Release 0.1): half-reactions, redox balancing, the mole, `K` / `Q` / the
reaction isotherm, and the ideal-gas law are imported as `bridge_imported`
nodes.

Intended, like `chemistry-foundations`, as the verified substrate for a later
**synthesis / process capsule** for the homesteading / self-sufficiency project
— electrosynthesis is "how to make X from air, water, salt, and electricity".

## Scope

**Read [`scope.md`](scope.md) first.** In brief — the Faraday charge/electron/mass
bridge, electrochemical cells, standard electrode potentials, `E°_cell` and
`ΔG = −zFE`, the Nernst equation, Faraday's laws of electrolysis with current
efficiency and specific energy, overpotential and product selectivity, named
production processes (water electrolysis, chlor-alkali, chlorate, Hall–Héroult,
electrorefining), and redox flow batteries (energy–power decoupling, state of
charge, the three efficiencies, crossover, all-vanadium).

**Excluded:** electrode microkinetics (Butler–Volmer stated not derived), the
electrical double layer, semiconductor / photoelectrochemistry, corrosion
engineering, analytical methods (CV, EIS), non-flow batteries in depth, and
fuel-cell engineering. See `scope.md`.

## Status

| stage | state |
|---|---|
| `scope.md` | **done** — scope signed off 2026-09-09 |
| `conventions.md` | done |
| node registry `nodes/nodes.tsv` | **110 nodes**, all `draft` |
| prerequisite graph | **255 edges, acyclic** (`tsort` clean, BSD-safe check), 0 isolated nodes; `edges/cycles.md`, `edges/relations.tsv` done |
| `formulas/electrochemistry.md` | not started |
| `sources/bibliography.md` | not started |
| `bc` dimensional checks | not started |
| `lean` identity checks | not started |
| discovery indexes | not started |
| `SKILL.md` | not started |
| tutorials | not started |

## Build

```sh
sh build/build-tree.sh   # graph-check + tsort + cycle check + order verification
```

## Reading order caveat

`indexes/tsort-order.txt` (once generated) is one valid prerequisite-respecting
linearization. Independent nodes fall in an arbitrary tie order — topological
order is not teaching order, historical order, or conceptual priority.
