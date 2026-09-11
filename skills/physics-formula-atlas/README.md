# physics-formula-atlas

**Status: Release 0.1 built (2026-09-11).**

A `bridge`-archetype capsule connecting
[`physics-newtonian`](../physics-newtonian/SKILL.md),
[`physics-thermodynamics`](../physics-thermodynamics/SKILL.md), and
[`physics-thermoacoustics`](../physics-thermoacoustics/SKILL.md) with real
cross-capsule `requires` edges, plus a working tool
(`build/prereq-path.py`) to trace any formula's full prerequisite chain
back across capsule boundaries to its terminal primitives, axioms,
assumptions, and conventions.

Read [`SKILL.md`](SKILL.md) then [`scope.md`](scope.md).

## Quick start

```sh
sh build/all.sh
python3 build/prereq-path.py physics-thermoacoustics:specific_heat_cv
```

## Why

Three capsules each claimed another as "assumed background" in prose only.
A discharge audit (`validation/duplicate-primitives.md`) found real
duplication instead of real edges: `physics-thermodynamics`'s entire
5-primitive root set duplicates `physics-newtonian`; `physics-thermoacoustics`
re-declares six `physics-thermodynamics`-developed concepts (including the
literal first law of thermodynamics, restated from scratch) as its own
disconnected roots. This capsule adds the missing 15 edges and a tool to
actually use them.

## What's next

Release 0.2 candidate: extend to `chemistry-foundations` and
`chemistry-electrochemistry` (both already claim `physics-thermodynamics` as
background). A further extension flagged in the discharge audit: the bare
`derivative`/`integral` math primitives each physics capsule re-declares
independently could be discharged against `math-real-analysis`.
