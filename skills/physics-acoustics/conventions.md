# Conventions

## Foundational stance

Classical (non-relativistic) continuum mechanics; no new foundational
commitments beyond `physics-newtonian` and `physics-thermodynamics`. The
small-amplitude linearization (`small_amplitude`) is this capsule's one
first-class regime assumption — every node whose statement depends on
dropping a quadratic term in the perturbation edges to it.

## Local copies of upstream nodes, discharged immediately

Unlike `physics-thermodynamics` and `physics-thermoacoustics` when they
were first built, this capsule's local roots (`real_numbers`, `length`,
`mass`, `time`, `SI_units`, `gas_constant`, `heat_capacity_ratio`) and two
further local copies that aren't roots but are still pure duplicates
(`newton_second_law`, `ideal_gas_law`) get a `physics-formula-atlas`
cross-capsule edge added in the same session — see
`physics-formula-atlas/edges/cross-capsule.plan` and
`physics-formula-atlas/validation/duplicate-primitives.md`. `mean_density`
is checked and confirmed to have no upstream analogue (no `density` node
exists anywhere in `physics-thermodynamics`) — a genuine capsule-local
primitive, not a discharge miss.

## Sign and notation conventions

- `p'`, `rho'` always denote the **perturbation** from the mean state
  (`p' = P - P0`, not the total pressure) — never silently dropped to `p`.
- `c` always denotes the speed of sound; `k` the wavenumber (`k = 2π/λ`,
  not `1/λ`); `omega` the angular frequency (`ω = 2πf`).
- Doppler formulas use `∓`/`±` inline in the primary_statement:
  `f' = f (c ± v_o)/(c ∓ v_s)` — `+` in the numerator and `-` in the
  denominator both mean "moving toward", so reading the sign requires
  checking which term it's attached to, not a fixed rule; each node's
  detail page spells out both cases explicitly rather than relying on the
  compact notation alone.
- Impedance is always the **specific** acoustic impedance unless stated
  otherwise (`z = p'/u`, units Pa·s/m); the **characteristic** impedance
  `z0 = ρ0 c` is the specific impedance's value for a plane traveling wave
  specifically, not a different physical quantity.

## Excluded content, restated

Viscosity, thermal dissipation, and general fluid mechanics are
deliberately out of scope (see `scope.md`) so this capsule and
`physics-thermoacoustics` don't duplicate content — this capsule supplies
the inviscid wave physics `physics-thermoacoustics` builds thermoviscous
corrections on top of, even though (as of this release) the citation only
runs through `physics-formula-atlas`, not a direct edge inside
`physics-thermoacoustics` itself (that capsule's own registry is untouched
by this release — see `physics-formula-atlas/scope.md`'s
"de-duplicating the source capsules" exclusion, which applies here too).
