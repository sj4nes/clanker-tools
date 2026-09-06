# continuity_of_probability

## Type
proposition

## Statement
If A_n increases to A then P(A_n) -> P(A); if A_n decreases to A then P(A_n) -> P(A). (No finiteness caveat: P <= 1.)

## Symbols
- `(A_n)` — a monotone sequence of events, type: N -> F
- `A` — bigcup A_n or bigcap A_n, type: element of F

## Epistemic status
proposition

## Prerequisites (tsort edges into this node)
kolmogorov_axioms, measure_continuity, sequence_limit, set_algebra

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: measure_continuity with mu = P; from above via complements
derives_from: measure_continuity
lean_status: core

## Type / well-formedness check
the specialisation of measure_continuity to a finite (probability) measure; continuity from above needs no extra hypothesis because P(A_1) <= 1 < inf.

## Specialization / boundary cases
- A_n = { X <= x + 1/n } down { X <= x }: gives right-continuity of the CDF
- A_n = { |X_k - X| <= eps for all k <= n }: used to relate a.s. and in-probability convergence
- P(bigcup_{n} A_n) = lim_N P(bigcup_{n<=N} A_n)

## Hypothesis-dropped counterexamples
- **monotonicity_of_A_n**: for a non-monotone sequence only Fatou-type bounds hold: P(liminf A_n) <= liminf P(A_n) <= limsup P(A_n) <= P(limsup A_n)

## Common misuse
- applying to a non-monotone sequence
- confusing set convergence A_n -> A with numerical P(A_n) -> P(A) (the proposition is exactly the bridge)

## Related nodes (non-prerequisite)
- specializes: measure_continuity
- used_by: cdf_properties, borel_cantelli_first, borel_cantelli_second

## Sources
billingsley_probability_measure, durrett_pte
