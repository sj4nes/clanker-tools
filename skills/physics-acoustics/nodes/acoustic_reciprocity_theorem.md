# acoustic_reciprocity_theorem

## Type
principle_law

## Statement
In any linear, passive (source-free apart from the two points in question)
acoustic system, the pressure at point B due to a point source at A equals
the pressure at A due to an equal source placed at B: `p_A(B) = p_B(A)`.
Equivalently — the roles of source and receiver may be interchanged without
changing the transfer function between them. This holds for the full 3-D
field, not just the 1-D case this capsule otherwise restricts to.

## Symbols
- `A, B`: two points in the acoustic medium
- `p_A(B)`: pressure perturbation measured at `B` when a source sits at `A`

## Epistemic status
proved_theorem (a structural consequence of the acoustic wave equation
being a linear, self-adjoint differential operator — the standard proof
uses Green's second identity, not reproduced in full here; this capsule
states the result and verifies one specialization).

## Prerequisites (tsort edges into this node)
acoustic_wave_equation_3d, superposition_principle

## Hypotheses
Linear (small-amplitude) regime; a time-invariant medium; no flow
(consistent with this capsule's inviscid, quiescent-background scope).
The theorem as stated needs no dissipation, though a lossy generalization
exists (out of scope here).

## Proof provenance
technique: Green's second identity applied to the (time-harmonic) Helmholtz
equation the 3-D wave equation reduces to — the wave operator is
self-adjoint, which is exactly what licenses swapping source and receiver.
derives_from: acoustic_wave_equation_3d, superposition_principle (linearity
is what makes "swap the roles" well-defined at all).
lean_status: not_attempted — the general proof is a PDE/functional-analysis
argument outside this capsule's `bc`-instance-check policy; the
specialization below is `bc`-verified instead.

## Type / well-formedness check
`p_A(B)` and `p_B(A)` are both pressure perturbations (Pa), well-typed and
directly comparable; the statement is an equality of two same-typed
quantities. Checked: `validation/type-checks.md#acoustic_reciprocity_theorem`
(informal — no new type-check worksheet entry needed beyond noting both
sides are pressures).

## Specialization / boundary cases
Specialized to one planar impedance boundary (`validation/instance-checks.md`):
the power transmission coefficient `tau = 1 - R^2` computed with air as the
"source side" equals `tau` computed with water as the "source side" —
`R` flips sign under the swap but `R^2` doesn't, so `tau` is exactly
symmetric. This is reciprocity's content on the one boundary case this
capsule already develops, not a full re-derivation of the 3-D theorem.

## Hypothesis-dropped counterexamples
Drop linearity (large-amplitude, nonlinear acoustics — out of this
capsule's scope entirely): reciprocity generally fails once the governing
equation is nonlinear, since superposition itself no longer holds.
Drop "no flow": a moving medium (wind) breaks source-receiver symmetry —
sound travels faster downwind than upwind between the same two points,
which is a real, well-known non-reciprocal effect outside this capsule's
quiescent-background scope.

## Common misuse
Concluding a horn or dish "sounds the same" as a speaker and as a
microphone — reciprocity guarantees the same *linear transfer function*
(gain and phase as a function of direction and frequency), not that a
device makes an equally good practical microphone and loudspeaker (power
handling, noise floor, and transduction efficiency differ independently of
reciprocity).

## Related nodes (non-prerequisite)
`webster_horn_equation` and `exponential_horn`: a horn is reciprocal by
this theorem, which is the physics-level reason horn megaphones and horn
"ear trumpets" are literally the same geometry.

## Sources
[kinsler_frey] §5.2, the Rayleigh–Helmholtz reciprocity theorem;
[pierce_acoustics] §4.9.
