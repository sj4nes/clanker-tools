# Scope — Release 0.1

Knowledge capsule: **linear (small-signal) acoustics in fluids**, built with
the [`physics-formula-tree`](../physics-formula-tree/SKILL.md) method. The
floor `physics-thermoacoustics` needs and currently lacks — see
`physics-formula-atlas/validation/duplicate-primitives.md`, which found
`small_amplitude` and `time_harmonic` re-declared as thermoacoustics roots
with no upstream capsule to discharge them against.

## Included

- SI units; `[M L T]` dimensional analysis (no new dimension — pressure,
  density, velocity are already typed in `physics-newtonian`).
- Continuum-fluid primitives: **mean density** `ρ₀`, **mean pressure** `P₀`,
  an inviscid, adiabatic, otherwise undisturbed equilibrium background.
- The **small-amplitude (linear) approximation**: acoustic perturbations
  `p', ρ', u` are small relative to the mean state, licensing the linearized
  continuity and momentum (Euler) equations.
- **Linearized continuity equation** and **linearized Euler's equation**
  (from `physics-newtonian`'s `F = ma` applied to a fluid element).
- The **adiabatic bulk modulus** and the **speed of sound**, both in the
  general thermodynamic form `c² = (∂P/∂ρ)_s` and the ideal-gas form
  `c = √(γRT/M)` (importing `physics-thermodynamics`'s `heat_capacity_ratio`,
  `gas_constant`, `ideal_gas_law`).
- The **linear acoustic wave equation** (1-D and 3-D), derived from
  continuity + Euler + the bulk-modulus constitutive relation.
- **Plane-wave solutions**; the **dispersion relation** `ω = ck`;
  wavelength/frequency/period relations.
- **Time-harmonic (single-frequency, steady-state) regime** and the
  **phasor / complex-amplitude convention**.
- **Acoustic impedance** (specific `z = p'/u`, characteristic `z₀ = ρ₀c`)
  and the **plane-wave pressure-velocity relation** `p' = ρ₀c u`.
- **Acoustic intensity** `I = ⟨p'u⟩`, **sound power**, the **inverse-square
  law** for a point source, and the **decibel (SPL) scale** with its
  reference pressure.
- **Superposition** and **interference** (constructive / destructive);
  **standing waves**; **normal modes** and resonance in a finite pipe
  (open–open, closed–closed, open–closed boundary conditions).
- **Normal-incidence reflection and transmission** at an impedance
  mismatch (reflection/transmission coefficients).
- The **Doppler effect** (moving source, moving observer, both — non-
  relativistic, source/observer speed `<< c`).

## Excluded (out of scope for 0.1)

- **Viscous and thermal dissipation** (boundary-layer absorption, Rott's
  `f_nu`/`f_kappa` functions, the short-stack results) — that is
  `physics-thermoacoustics`'s territory; this capsule stays inviscid so the
  two capsules don't duplicate content. `physics-thermoacoustics` gets to
  keep citing this capsule's `wave_equation`/`speed_of_sound` while adding
  its own thermoviscous corrections on top.
- **General fluid mechanics** (viscosity, laminar/turbulent flow, the
  Navier–Stokes equation, boundary layers) beyond the single inviscid-Euler
  step needed to derive the wave equation. A future
  `physics-fluid-mechanics` capsule is the natural home for `dynamic_viscosity`,
  `laminar_flow`, and `velocity_field` — three more roots
  `physics-formula-atlas`'s audit found capsule-local in
  `physics-thermoacoustics` that this release does **not** claim to
  discharge.
- **Nonlinear acoustics** (shock formation, finite-amplitude distortion,
  the Mach cone) — the small-amplitude assumption is exactly what rules
  these out; noted at every node that depends on it.
- **3-D scattering, diffraction, and room acoustics** (reverberation time,
  modal density in irregular enclosures) beyond the 1-D pipe resonance
  case needed for standing waves.
- **Electroacoustic transduction** (microphones, loudspeakers,
  piezoelectric transducers) and **psychoacoustics** (loudness, pitch
  perception, equal-loudness contours) — engineering/perceptual layers on
  top of this capsule, not developed here.
- **Underwater acoustics** and **atmospheric refraction/absorption**
  specifics (sonar equations, ocean sound-speed profiles) — a possible
  later specialization, not this release.

## Level and background

Upper-undergraduate, matching `physics-newtonian` and
`physics-thermodynamics`. Assumes both read. Like every existing
`physics-formula-tree` capsule, this one keeps its own self-contained
`nodes.tsv`/`tsort` graph (local primitives: `length`, `mass`, `time`,
`real_numbers`, `SI_units`, plus one genuinely new primitive,
`mean_density`, which — confirmed by checking — exists in **no** other
physics capsule). Real discharge against `physics-newtonian` and
`physics-thermodynamics` is added immediately after, in the same session,
by extending `physics-formula-atlas/edges/cross-capsule.plan` — so this
capsule's roots are never left undischarged the way
`physics-thermodynamics`'s and `physics-thermoacoustics`'s were before the
atlas existed.

## Foundational stance

No new foundational commitments. Classical (non-relativistic) continuum
mechanics; the small-amplitude linearization is the capsule's one
first-class regime assumption, flagged on every node that needs it.

## Proof / verification policy

- The wave-equation derivation (continuity + linearized Euler + bulk
  modulus, combined into one second-order PDE): worked algebraically in
  the node entry; a 1-D `bc` instance check confirms the dispersion
  relation `ω = ck` at concrete values.
- Speed of sound (ideal-gas form): `bc`-checked against the standard
  343 m/s figure for dry air at 20°C.
- Decibel scale, Doppler shift, standing-wave resonance frequencies:
  `bc` worked instances at textbook values.
- No Lean cores in this release — these are algebraic/calculus
  derivations and unit-checked numeric instances, not identities suited to
  a Mathlib-free kernel check (same proof-policy call `bayes-bridge` made
  for its conjugate-family derivations).
