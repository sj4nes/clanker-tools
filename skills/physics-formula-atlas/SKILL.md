---
name: physics-formula-atlas
description: A bridge capsule connecting physics-newtonian, physics-thermodynamics, and physics-thermoacoustics with real cross-capsule requires edges (not prose-only discharge -- this hierarchy has no mutual-grounding cycle), plus a working prereq-path.py tool that walks any formula's full prerequisite chain backward across capsule boundaries down to its terminal primitives, axioms, assumptions, and conventions. Use when you need to trace a physics formula's complete dependency chain back to constants or dimensions, when adding a formula to physics-thermodynamics or physics-thermoacoustics and you need to know whether a "new" primitive is actually a duplicate of an already-developed node in an upstream capsule, or when auditing whether a capsule's assumed background is a real edge or just a prose claim. Built with the physics-formula-tree method's tsort/edge discipline, adapted across capsule boundaries.
---

# physics-formula-atlas

A `bridge`-archetype capsule connecting
[`physics-newtonian`](../physics-newtonian/SKILL.md),
[`physics-thermodynamics`](../physics-thermodynamics/SKILL.md), and
[`physics-thermoacoustics`](../physics-thermoacoustics/SKILL.md). Read
[`scope.md`](scope.md) first.

## Why this exists

Each of the three capsules' `scope.md` states an "assumed background" in
prose (`physics-thermoacoustics` names `physics-newtonian` explicitly). None
of that was a real edge. A discharge audit
(`validation/duplicate-primitives.md`) found the two downstream capsules
independently re-declaring primitives another capsule already develops:
`physics-thermodynamics`'s 5 roots (`length`, `mass`, `time`,
`real_numbers`, `SI_units`) are **100% duplicates** of `physics-newtonian`
primitives; `physics-thermoacoustics` re-primitives
`first_law_thermodynamics`, `ideal_gas`, `gas_constant_specific`,
`specific_heat_c{v,p}`, `mean_temperature`, `mean_pressure` instead of
citing the developed `physics-thermodynamics` nodes.

## What's here

- **`edges/cross-capsule.plan`** — 15 real cross-capsule `requires` edges,
  each with an evidence comment (including unit-conversion notes where the
  discharge isn't a plain identity: specific vs. molar heat capacity and
  gas constant). Unlike `bayes-bridge`, these are genuine `tsort` edges, not
  prose — this hierarchy (Newtonian ⊂ thermo ⊂ thermoacoustics) has no
  mutual-grounding cycle. **Non-destructive**: the three source capsules'
  own registries are untouched.
- **`build/prereq-path.py`** — given `capsule:node_id`, walks backward
  through the union of all three capsules' native edges plus the bridge
  edges, printing the full chain to every terminal root, crossing capsule
  boundaries wherever a bridge edge fires. This is the "rapidly scan a
  formula's path back to constants or dimensions" tool.
- **`validation/duplicate-primitives.md`** — every root in
  `physics-thermodynamics` (5/5 discharged) and `physics-thermoacoustics`
  (10/25 discharged, 15 genuinely capsule-local — mostly fluid-mechanics and
  acoustics primitives neither upstream capsule develops) classified.

## Use it

```sh
sh build/all.sh                                                    # graph-check + tsort + 3 worked traces
python3 build/prereq-path.py physics-thermoacoustics:specific_heat_cv   # full tree
python3 build/prereq-path.py physics-thermoacoustics:specific_heat_cv --roots-only
```

Worked example — `physics-thermoacoustics:specific_heat_cv` crosses two
capsule boundaries and bottoms out at exactly 5 `physics-newtonian`
primitives (`length`, `mass`, `time`, `real_numbers`, `SI_units`); before
this release the trace dead-ended at `physics-thermoacoustics`'s own
capsule-local root with no further path.

## Release 0.1 at a glance

15 cross-capsule edges; combined graph (3 capsules' native edges + the
bridge) = 239 nodes, 634 edges, `tsort`-clean (stderr-checked), acyclic.
Two scoping questions resolved (see `scope.md`): `position` vs. `length`
deliberately **not** edged (coordinate vs. dimension — a type difference);
`mean_temperature`/`mean_pressure` **are** real edges (the base state a
perturbation is expanded around genuinely presupposes the underlying
quantity), `mean_density` stays capsule-local (no `density` node exists
anywhere in `physics-thermodynamics`).

## Excluded / next steps

Chemistry capsules (`chemistry-foundations`, `chemistry-electrochemistry`)
deferred to Release 0.2 — both already claim `physics-thermodynamics` as
background in prose and would extend this atlas naturally.
`validation/duplicate-primitives.md`'s "Known limitation" section also
flags a further extension: discharging the physics stack's bare
`derivative`/`integral` math primitives against `math-real-analysis`,
mirroring what the `math-*` capsule stack already does internally.
