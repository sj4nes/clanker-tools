# cf_properties

## Type
theorem

## Statement
phi_X is uniformly continuous with |phi_X| <= 1, phi_X(0) = 1, phi_{-X} = conjugate(phi_X). It determines the law (inversion formula). phi_{aX+b}(t) = e^{itb} phi_X(at). If E|X|^k < inf then phi_X is C^k with phi_X^{(k)}(0) = i^k E[X^k].

## Symbols
- `phi_X` — the characteristic function, type: R -> C
- `a, b` — constants, type: real

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
characteristic_function, distribution_pushforward, dominated_convergence_theorem

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: uniform continuity by DCT; the inversion formula by Fubini on the Dirichlet kernel; smoothness by differentiating under the integral (DCT) when the moment exists
derives_from: dominated_convergence_theorem
lean_status: cited — Billingsley Thm 26.2, 26.1; Durrett 3.3

## Type / well-formedness check
uniform continuity: |phi(t+h) - phi(t)| <= E|e^{ihX} - 1| -> 0 by DCT. Inversion: for a < b continuity points, P_X((a,b]) = lim_T (1/2 pi) integral_{-T}^{T} (e^{-ita} - e^{-itb})/(it) phi_X(t) dt.

## Specialization / boundary cases
- phi real-valued <=> P_X symmetric about 0
- phi integrable => P_X has a bounded continuous density f(x) = (1/2 pi) integral e^{-itx} phi(t) dt
- affine: standardizing X to (X - mu)/sigma multiplies the CF argument by sigma and adds a phase

## Hypothesis-dropped counterexamples
- **moment_for_smoothness**: Cauchy: phi(t) = e^{-|t|} is NOT differentiable at 0 -- consistent with E|X| = inf
- **continuity_points_for_inversion**: the inversion formula recovers P_X((a,b]) only at continuity points a, b of F_X

## Common misuse
- assuming phi determines a density (only if phi is integrable)
- reading non-smoothness of phi at 0 as pathology -- it just signals a heavy tail

## Related nodes (non-prerequisite)
- characterizes: the law
- requires: characteristic_function
- used_by: levy_continuity_theorem

## Sources
billingsley_probability_measure, durrett_pte
