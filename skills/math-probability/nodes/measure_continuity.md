# measure_continuity

## Type
proposition

## Statement
Continuity from below: A_n increasing to A implies mu(A_n) -> mu(A). Continuity from above: A_n decreasing to A with mu(A_1) < inf implies mu(A_n) -> mu(A).

## Symbols
- `(A_n)` — a monotone sequence of events, type: N -> F
- `A` — the limit set bigcup A_n or bigcap A_n, type: element of F

## Epistemic status
proposition

## Prerequisites (tsort edges into this node)
limsup_liminf, measure, sequence_limit, set_algebra

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: from below: write A_n \ A_{n-1} disjoint, mu(A) = sum = lim of partial sums = lim mu(A_n). From above: apply the from-below result to A_1 \ A_n up A_1 \ A
derives_from: measure
lean_status: cited — Billingsley Thm 10.2

## Type / well-formedness check
continuity from below telescopes A = disjoint-union of (A_n \ A_{n-1}) and applies countable additivity; continuity from above applies it to the complements and needs mu(A_1) < inf to subtract.

## Specialization / boundary cases
- mu = P: continuity_of_probability, no finiteness caveat needed (P <= 1)
- cdf right-continuity: F_X(x_n) -> F_X(x) for x_n decreasing to x, via { X <= x_n } down { X <= x }

## Hypothesis-dropped counterexamples
- **finite_measure_for_continuity_from_above**: Lebesgue measure, A_n = [n, inf): A_n down empty but lambda(A_n) = inf for all n, so lambda(A_n) does not converge to lambda(empty) = 0

## Common misuse
- dropping the mu(A_1) < inf hypothesis for continuity from above
- assuming continuity for a non-monotone sequence (use limsup/liminf and Fatou-type bounds)

## Related nodes (non-prerequisite)
- specializes_to: continuity_of_probability, cdf_properties

## Sources
billingsley_probability_measure, folland_real_analysis
