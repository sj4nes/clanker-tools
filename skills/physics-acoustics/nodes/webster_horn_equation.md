# webster_horn_equation

## Type
derived_formula

## Statement
For a duct whose cross-sectional area `S(x)` varies slowly along its axis
(slowly compared to the wavelength — the "quasi-1-D" approximation), the
plane-wave acoustic pressure obeys **`d/dx(S dp'/dx) + (omega/c)^2 S p' = 0`**
in the time-harmonic (frequency-domain) form. It reduces exactly to
`acoustic_wave_equation_1d`'s time-harmonic form when `S` is constant — a
horn is the wave equation with one extra term carrying the geometry.

## Symbols
- `S(x)`: cross-sectional area as a function of axial position, m²
- `p'(x)`: the (complex, time-harmonic) acoustic pressure amplitude, Pa
- `omega`: angular frequency, rad/s
- `c`: speed of sound, m/s

## Epistemic status
proved_theorem (a standard quasi-1-D reduction of the 3-D linear wave
equation to a duct with slowly-varying cross-section; not re-derived from
the 3-D equation symbolically in this capsule — stated as the accepted
generalization of `acoustic_wave_equation_1d`).

## Prerequisites (tsort edges into this node)
acoustic_wave_equation_1d, function, partial_derivative

## Hypotheses
`S(x)` varies slowly enough that the wavefronts stay approximately planar
across each cross-section (breaks down for a rapidly-flaring or very wide
horn, where genuinely 3-D higher-order modes appear); the same
small-amplitude, inviscid regime as the rest of the capsule.

## Proof provenance
technique: quasi-1-D reduction — integrate the 3-D linear wave equation
over a cross-section, treating `S(x)` as slowly varying so cross-sectional
averages of pressure and velocity make sense as 1-D fields.
derives_from: acoustic_wave_equation_1d (the `S=const` case), extended by
the varying-area term.
lean_status: not_attempted.

## Type / well-formedness check
Every term has units of Pa/m² after dividing through by `S` (pressure per
area, consistent with a force-balance-derived equation); `(omega/c)^2` has
units of 1/length², matching `d^2/dx^2`'s units acting on `p'`. Checked:
`validation/type-checks.md#webster_horn_equation`.

## Specialization / boundary cases
`S(x) = S0` (constant): the `S`-derivative term vanishes, leaving
`d^2p'/dx^2 + (omega/c)^2 p' = 0` — exactly the time-harmonic form of
`acoustic_wave_equation_1d`. `S(x) = S0 e^{2mx}` (exponential): solved in
closed form in `exponential_horn`.

## Hypothesis-dropped counterexamples
Drop "slowly varying": a duct with a sudden area change (a step, not a
smooth taper) needs the boundary-matching treatment this capsule's
`reflection_coefficient_normal_incidence` node already covers for a single
discontinuity — `webster_horn_equation` is specifically for the smooth-taper
regime, not a substitute for it.

## Common misuse
Applying the equation to a horn whose mouth is comparable to or larger
than the wavelength — the quasi-1-D (plane-wavefront) assumption breaks
down there, and genuine 3-D radiation effects (directivity, diffraction)
take over, outside this capsule's scope.

## Related nodes (non-prerequisite)
`acoustic_reciprocity_theorem`: the same linear operator underlying this
equation is what makes a horn's response reciprocal.

## Sources
[kinsler_frey] §9.1; [olson_acoustics] Ch. 3.
