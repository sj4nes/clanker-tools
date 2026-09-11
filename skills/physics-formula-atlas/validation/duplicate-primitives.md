# Discharge audit — every root in `physics-thermodynamics`, `physics-thermoacoustics`, and `physics-acoustics`

Every root (no in-capsule predecessor) in the two downstream capsules,
classified: **discharged** (a `cross-capsule.plan` edge was added),
**capsule-local** (no upstream equivalent exists — a genuine root, not a
gap), or **distinguished** (related to an upstream node but not the same
object — deliberately not edged).

## `physics-thermodynamics` roots (5 total)

| Root | Classification | Discharged by |
|---|---|---|
| `length` | discharged | `physics-newtonian:length` |
| `mass` | discharged | `physics-newtonian:mass` |
| `time` | discharged | `physics-newtonian:time` |
| `real_numbers` | discharged | `physics-newtonian:real_numbers` |
| `SI_units` | discharged | `physics-newtonian:SI_units` |

**100% discharged** — every root in `physics-thermodynamics` turned out to
be a duplicate of a `physics-newtonian` primitive. Nothing was
capsule-local here; that capsule's own genuine thermodynamic primitives
(`pressure`, `temperature` via `zeroth_law`, `gas_constant`, …) are all
already developed nodes with their own in-capsule prerequisite chains, not
undischarged roots.

## `physics-thermoacoustics` roots (25 total)

| Root | Classification | Discharged by / note |
|---|---|---|
| `real_numbers` | discharged | `physics-newtonian:real_numbers` |
| `SI_units` | discharged | `physics-newtonian:SI_units` |
| `time` | discharged | `physics-newtonian:time` |
| `ideal_gas` | discharged | `physics-thermodynamics:ideal_gas_law` |
| `gas_constant_specific` | discharged (unit conversion) | `physics-thermodynamics:gas_constant` — specific = molar / molar_mass |
| `specific_heat_cv` | discharged (unit conversion) | `physics-thermodynamics:heat_capacity_cv` — specific = molar / molar_mass |
| `specific_heat_cp` | discharged (unit conversion) | `physics-thermodynamics:heat_capacity_cp` — specific = molar / molar_mass |
| `first_law_thermodynamics` | discharged (pure duplicate) | `physics-thermodynamics:first_law_thermodynamics` — identical statement, restated from scratch |
| `mean_temperature` | discharged | `physics-thermodynamics:temperature` — the base state a perturbation is expanded around |
| `mean_pressure` | discharged | `physics-thermodynamics:pressure` — ditto |
| `mean_density` | **capsule-local** | `physics-thermodynamics` has no `density` node at all — genuine gap, not a discharge miss |
| `position` | **distinguished, not edged** | related to `physics-newtonian:length` (a dimension/primitive magnitude) but is a coordinate value along an axis, not the same object — edging them would misencode a type difference |
| `cross_sectional_uniformity` | capsule-local | a geometric assumption specific to the channel/pore model, no upstream analogue |
| `derivative` | capsule-local | a bare math primitive re-declared per capsule (see "Known limitation" below) |
| `dynamic_viscosity` | capsule-local | fluid-mechanics primitive, no `physics-newtonian` or `physics-thermodynamics` analogue (neither capsule covers viscous fluids) |
| `hydraulic_radius` | capsule-local | thermoacoustics-specific channel geometry |
| `integral` | capsule-local | see "Known limitation" |
| `laminar_flow` | capsule-local | fluid-mechanics assumption, no upstream analogue |
| `no_mean_flow` | capsule-local | thermoacoustics-specific modelling assumption |
| `rigid_isothermal_wall` | capsule-local | thermoacoustics-specific boundary-condition assumption |
| `small_amplitude` | discharged (added once `physics-acoustics` existed) | `physics-acoustics:small_amplitude` |
| `thermal_conductivity` | capsule-local | fluid/solid transport property, no upstream analogue |
| `time_harmonic` | discharged (added once `physics-acoustics` existed) | `physics-acoustics:time_harmonic` |
| `velocity_field` | capsule-local | fluid-mechanics primitive, no upstream analogue |
| `mean_temperature_gradient` | capsule-local | thermoacoustics-specific (an imposed gradient of the discharged `mean_temperature`, but the gradient itself has no thermodynamics-capsule analogue) |

**12 of 25 discharged** (10 against `physics-thermodynamics`, 2 —
`small_amplitude`, `time_harmonic` — against `physics-acoustics` once it
existed), **13 genuinely capsule-local or deliberately distinguished.**
The discharge rate is still lower than `physics-thermodynamics`'s because
`physics-thermoacoustics` sits at the intersection of thermodynamics *and*
fluid mechanics/acoustics — and
the remaining 13 are fluid-mechanics primitives (viscosity, laminar flow,
velocity fields) that no capsule in this stack develops — `physics-acoustics`
picked up the two wave-phenomena roots (`small_amplitude`, `time_harmonic`)
but stayed deliberately inviscid (see its `scope.md`'s exclusions), so it
could not discharge the fluid-mechanics roots too. That is a real scope
boundary — a future `physics-fluid-mechanics` capsule's job — not a missed
discharge; recorded here rather than silently absorbed.

## `physics-acoustics` roots (7 total)

Built after this atlas existed, so its `scope.md` committed to discharging
every root in the same session rather than leaving the duplication for a
later release.

| Root | Classification | Discharged by |
|---|---|---|
| `real_numbers` | discharged | `physics-newtonian:real_numbers` |
| `length` | discharged | `physics-newtonian:length` |
| `mass` | discharged | `physics-newtonian:mass` |
| `time` | discharged | `physics-newtonian:time` |
| `SI_units` | discharged | `physics-newtonian:SI_units` |
| `gas_constant` | discharged | `physics-thermodynamics:gas_constant` |
| `heat_capacity_ratio` | discharged | `physics-thermodynamics:heat_capacity_ratio` |

**100% discharged**, matching `physics-thermodynamics`'s rate once fixed.
Two further local copies (`newton_second_law`, `ideal_gas_law`) and two more
mean-state nodes (`mean_pressure`, `mean_temperature`) are not roots within
`physics-acoustics`'s own graph (each already has an in-capsule predecessor)
but are still pure duplicates of an upstream developed node, so
`cross-capsule.plan` edges them anyway — `prereq-path.py` walks predecessors
regardless of local-root status, so the printed path still shortens.
`mean_density` was checked again and confirmed capsule-local: no `density`
node exists anywhere in `physics-thermodynamics`, the same finding as
`physics-thermoacoustics`'s `mean_density`.

## Known limitation: bare math primitives

`derivative` and `integral` are independently re-declared as roots in
`physics-thermoacoustics`, and `physics-newtonian` has its own math-area
primitives (no `derivative`/`integral` node by that exact id, but
equivalent calculus prerequisites under different names — see that
capsule's "calculus prerequisites" edge block). A full discharge would need
either a shared `math-real-analysis` capsule (which exists in the `math-*`
stack — see `skills/math-real-analysis`) as the actual floor under *all*
physics capsules' calculus primitives, or at minimum a naming-convention
pass across the three physics capsules. Out of scope for this release —
flagged here as the next natural extension (a `physics-formula-atlas`
Release 0.2 candidate: discharge the physics stack's calculus primitives
against `math-real-analysis`, mirroring what the `math-*` capsules already
do for each other).
