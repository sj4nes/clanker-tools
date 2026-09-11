# exponential_horn

## Type
derived_formula

## Statement
For a horn whose cross-sectional area grows exponentially along its axis,
`S(x) = S0 e^(2mx)` (flare constant `m`, units 1/length), a traveling-wave
ansatz `p'(x,t) = A e^(-mx) e^(i(omega t - kx))` solves `webster_horn_equation`
only when `k^2 = (omega/c)^2 - m^2`. For `omega > m c`, `k` is real and the
wave propagates (with the extra `e^(-mx)` geometric-spreading factor built
in). For `omega < m c`, `k` is imaginary — the disturbance decays
exponentially with distance instead of propagating. The **cutoff
frequency** is `f_c = m c / (2 pi)`: an exponential horn is a high-pass
filter.

## Symbols
- `S0`: the horn's throat area (at `x=0`), m²
- `m`: the flare constant, 1/m — controls how fast the horn widens
- `c`: speed of sound (imported, `speed_of_sound_general`/`_ideal_gas`)
- `f_c`: cutoff frequency, Hz

## Epistemic status
proved_theorem (a direct consequence of substituting the stated ansatz
into `webster_horn_equation` for this one cross-section profile; the
algebra is standard and not re-derived symbolically here beyond stating
the result).

## Prerequisites (tsort edges into this node)
webster_horn_equation, dispersion_relation

## Hypotheses
The exponential profile `S(x) = S0 e^(2mx)` specifically (other profiles —
conical, catenoidal — solve `webster_horn_equation` differently and are out
of scope); the same small-amplitude, time-harmonic regime as the rest of
this capsule.

## Proof provenance
technique: substitute the ansatz into `webster_horn_equation`
(`d/dx(S dp'/dx) + (omega/c)^2 S p' = 0`); for `S = S0 e^(2mx)`, the
`m`-dependence factors out cleanly, leaving the stated dispersion relation.
derives_from: webster_horn_equation.
lean_status: not_attempted.
bc_status: verified — `validation/instance-checks.md#exponential_horn`.

## Type / well-formedness check
`k^2 = (omega/c)^2 - m^2`: both terms have units of 1/length², so the
equation is dimensionally consistent; `k` real iff the right side is
non-negative, i.e. `omega >= mc`. Checked:
`validation/type-checks.md#exponential_horn`.

## Specialization / boundary cases
`m -> 0` (a straight, unflared duct, `S` constant): `f_c -> 0` — no cutoff,
recovering the ordinary `dispersion_relation` (`omega = ck`) for every
frequency, exactly the `S = const` case `webster_horn_equation` reduces to.

## Hypothesis-dropped counterexamples
A non-exponential flare (e.g. conical, `S(x) prop x^2`): the ansatz above
does not solve `webster_horn_equation` for that profile — conical horns
have no sharp cutoff in the same sense, a genuinely different solution
family, out of this capsule's scope.

## Common misuse
Treating the cutoff as a hard wall — below `f_c` the wave is evanescent
(decays exponentially with distance) rather than perfectly reflected; a
short horn still passes some sub-cutoff energy, just attenuated, not
zeroed.

## Related nodes (non-prerequisite)
`acoustic_reciprocity_theorem`: a horn's response is reciprocal, which is
the physics-level reason the same exponential-horn geometry works as
either a loudspeaker horn or a "horn microphone"/ear trumpet.

## Sources
[kinsler_frey] §9.1–9.3, the Webster horn equation and the exponential
horn's cutoff; [olson_acoustics] Ch. 3, horn loudspeaker design practice.
