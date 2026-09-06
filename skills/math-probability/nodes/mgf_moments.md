# mgf_moments

## Type
theorem

## Statement
If M_X is finite on a neighborhood of 0, then M_X is C^infinity there, X has moments of all orders, and M_X^{(k)}(0) = E[X^k]. Equivalently M_X(t) = sum_k E[X^k] t^k / k! near 0.

## Symbols
- `M_X` — the MGF, type: (-h, h) -> R
- `k` — a nonnegative integer, type: natural number

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
dominated_convergence_theorem, mgf, moment, series_convergence

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: DCT-justified differentiation under the integral sign, k times, then evaluate at t = 0
derives_from: dominated_convergence_theorem
lean_status: cited — Billingsley Thm 21.1; Durrett 3.3

## Type / well-formedness check
differentiate under the expectation: d^k/dt^k E[e^{tX}] = E[X^k e^{tX}], justified by DCT since finiteness on (-h, h) provides a dominating function e^{h'|X|} for |t| < h' < h.

## Specialization / boundary cases
- N(0,1): M(t) = e^{t^2/2}, M''(0) = 1 = E[Z^2], M^{(4)}(0) = 3 = E[Z^4]
- Exponential(1): M(t) = 1/(1-t), M^{(k)}(0) = k! = E[X^k]

## Hypothesis-dropped counterexamples
- **finiteness_of_M_X_near_0**: if M_X is finite only at 0, none of this holds -- a distribution can have all moments finite yet no MGF? no: all-moments-finite does not give an MGF (lognormal: every moment finite, MGF infinite, and the moment sequence does NOT determine the law)

## Common misuse
- computing moments from an MGF that is finite only at isolated points
- assuming the Taylor coefficients of any formal series 'M(t)' are moments without checking convergence

## Related nodes (non-prerequisite)
- requires: mgf
- computes: moment
- cf_analogue: phi_X^{(k)}(0) = i^k E[X^k] when E|X|^k < inf

## Sources
billingsley_probability_measure, durrett_pte
