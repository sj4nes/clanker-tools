# Scope — `physics-formula-atlas` Release 0.1

## What this is

A `bridge`-archetype capsule (same pattern as `bayes-bridge`, but with a
genuine one-directional hierarchy instead of a mutually-grounding pair — see
below) connecting three existing `physics-formula-tree` releases:

- [`physics-newtonian`](../physics-newtonian/SKILL.md) — mechanics, the
  floor.
- [`physics-thermodynamics`](../physics-thermodynamics/SKILL.md) —
  `scope.md` already states "Assumed background: algebra, logarithms,
  single-variable calculus" but not `physics-newtonian` explicitly, and
  shares 5 primitives with it verbatim (`length`, `mass`, `time`,
  `real_numbers`, `SI_units`) with no edge between the two capsules' copies.
- [`physics-thermoacoustics`](../physics-thermoacoustics/SKILL.md) —
  `scope.md` states "Assumed background: `physics-newtonian`" in prose, and
  independently re-declares as **roots** several nodes that
  `physics-thermodynamics` already **develops**: `first_law_thermodynamics`,
  `ideal_gas` (vs. thermo's `ideal_gas_law`), `gas_constant_specific` (vs.
  thermo's `gas_constant`), `specific_heat_cv`/`specific_heat_cp` (vs.
  thermo's `heat_capacity_cv`/`heat_capacity_cp`).

**Why this bridge is unlike `bayes-bridge`.** The math bridge connected two
capsules that are *mutually grounding* (each takes primitive what the other
develops) — a genuine circularity, resolved as prose metadata, never a real
edge. Here the relationship is a clean one-directional hierarchy:
Newtonian mechanics ⊂ thermodynamics' assumed background ⊂ thermoacoustics'
assumed background, with **no cycle back**. So this release adds **real
cross-capsule `requires` edges**, not prose-only discharge notes — that is
the entire point: a path-walking tool that crosses capsule boundaries needs
actual edges to walk.

## Included (Release 0.1)

1. **Cross-capsule edges** (`edges/cross-capsule.plan`, qualified
   `capsule:node_id` on both ends): every genuine duplicate-primitive pair
   (`physics-newtonian:length` → `physics-thermodynamics:length`, and the
   four more shared cross-domain primitives) and every genuine
   develops/re-primitives pair between `physics-thermodynamics` and
   `physics-thermoacoustics` (the `gas_constant`/`ideal_gas_law`/
   `heat_capacity_c{v,p}`/`first_law_thermodynamics` cluster, five edges).
   **Non-destructive**: this capsule does not edit the three source
   capsules' own `nodes.tsv`/`dependencies.plan` — exactly the precedent set
   by `bayes-bridge`'s `*_cited` bridge nodes, adapted here to real edges
   because (unlike `bayes-bridge`) there is no mutual-grounding hazard.
2. **A working cross-capsule path tool** (`build/prereq-path.py`): given a
   `capsule:node_id`, walks backward through the union of each capsule's own
   `edges/dependencies.edges` plus `edges/cross-capsule.edges`, across
   capsule boundaries wherever a cross-capsule edge fires, printing the full
   chain down to every root it bottoms out at (primitive / axiom /
   assumption / convention) — this is the "rapidly scan a formula's full
   path back to constants or dimensions" capability that motivated this
   release.
3. **A discharge audit** (`validation/duplicate-primitives.md`): every root
   in `physics-thermodynamics` and `physics-thermoacoustics` classified as
   *discharged* (an edge was added), *genuinely capsule-local* (no upstream
   equivalent exists — e.g. thermoacoustics' `mean_pressure`, `mean_density`,
   `mean_temperature`, which are perturbative quantities thermodynamics has
   no analogue of), or *deferred* (a real correspondence exists but needs a
   unit-conversion note before it can be a clean edge — see item 4).
4. **Unit-conversion notes where the discharge isn't a plain identity.**
   `gas_constant_specific = gas_constant / molar_mass` (specific vs. molar
   basis) and likewise for `specific_heat_c{v,p}` vs. `heat_capacity_c{v,p}`
   — the cross-capsule edge is still added (the concept *is* a genuine
   prerequisite), but the edge's evidence comment states the conversion
   factor explicitly rather than implying the two nodes are numerically
   identical.

## Excluded (out of scope for 0.1)

- **Chemistry capsules** (`chemistry-foundations`, `chemistry-electrochemistry`).
  Both already build on `physics-thermodynamics` in prose
  (`chemistry-foundations/scope.md` even names "bridge nodes from
  `physics-thermodynamics`") and would extend the atlas naturally, but
  adding them roughly doubles the capsule count and the discharge-audit
  work. A clean Release 0.2.
- **`physics-thermoacoustics`' `mean_pressure`/`mean_density`/
  `mean_temperature`/`velocity_field`/`hydraulic_radius`.** These are
  genuinely local to the perturbative acoustic setting — thermodynamics has
  no "mean" or spatially-varying analogue in scope. Left as capsule-local
  roots, recorded as such in the discharge audit (not silently dropped).
- **Re-deriving or re-proving anything.** Exactly like `bayes-bridge`, this
  capsule imports; it does not redevelop. No new Lean or `bc` proof
  obligations are created — the path tool is a graph-traversal utility, not
  a new theorem.
- **De-duplicating the source capsules.** `physics-thermoacoustics`'s
  `first_law_thermodynamics` node stays as its own (redundant) root in that
  capsule after this release — this capsule adds the missing edge to
  `physics-thermodynamics`'s version, it does not edit
  `physics-thermoacoustics` to remove its local copy. That cleanup, if
  wanted, is a change to `physics-thermoacoustics` itself, tracked
  separately in `BACKLOG.md`, not silently folded into this bridge.

## Foundational stance

No new foundational commitments — inherits all three capsules' stances
(classical Newtonian mechanics, the ideal-gas / equilibrium-thermodynamics
assumptions, the linear-acoustics small-amplitude regime). This capsule's
only claim is structural: which primitives are actually the same primitive
across capsule boundaries, and which developed node discharges which
downstream root.

## Verification policy

- Every cross-capsule edge passes the `tsort` skill's edge test *across* the
  boundary: "can I truthfully say the upstream node must be understood
  before the downstream root can be correctly stated" — applied the same way
  as any in-capsule edge.
- The combined graph (three capsules' native edges + `cross-capsule.edges`)
  must stay acyclic under `tsort`, stderr-checked (BSD-safe), confirming the
  one-directional-hierarchy claim in "What this is" is not just asserted but
  checked.
- `build/prereq-path.py` is verified against three worked traces (one per
  capsule, deepest available): a Newtonian result to its own primitives, a
  thermodynamics result crossing into Newtonian's `length`/`mass`/`time`,
  and a thermoacoustics result (ideally something built on the
  `first_law_thermodynamics` or `gas_constant_specific` cluster) crossing
  two capsule boundaries down to Newtonian's primitives.

## Scoping questions — resolved

- **`physics-thermoacoustics:position` vs. `physics-newtonian:length`:**
  **not** edged. `length` is a dimension/primitive magnitude; `position` is
  a coordinate value along an axis — related but not the same object, and
  identifying them would misencode a type difference. Recorded as a
  distinction, not a discharge, in `validation/duplicate-primitives.md`.
- **`mean_pressure` / `mean_temperature` / `mean_density`:** checked each
  against `physics-thermodynamics`'s actual node list.
  `physics-thermodynamics:pressure` (primitive) and
  `physics-thermodynamics:temperature` (developed) both exist, and the edge
  test passes cleanly — a time/space-averaged base state genuinely
  presupposes the underlying quantity — so these became real `requires`
  edges in `edges/cross-capsule.plan`, not a lighter `relates_to`.
  `mean_density` has **no** `physics-thermodynamics` analogue at all (that
  capsule has no `density` node) — stays a genuine capsule-local root,
  recorded as such in the audit.
