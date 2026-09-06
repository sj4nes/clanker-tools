# boole_inequality

## Type
theorem

## Statement
P(bigcup_n A_n) <= sum_n P(A_n) for any countable family of events (no disjointness).

## Symbols
- `(A_n)` — any countable family of events, type: N -> F

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
finite_additivity, kolmogorov_axioms, measure_monotonicity, series_convergence, set_algebra

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: disjointify and apply countable additivity: P(bigcup A_n) = P(bigcup B_n) = sum P(B_n) <= sum P(A_n)
derives_from: measure_monotonicity
lean_status: core — validation/proof-checks.lean Prob.union_bound (two-set case)

## Type / well-formedness check
the countable subadditivity of P; disjointify B_n = A_n minus (A_1 cup ... cup A_{n-1}), so B_n subset A_n, the B_n are disjoint with the same union, and countable additivity + monotonicity finish it.

## Specialization / boundary cases
- finitely many A_n: the finite union bound
- A_n with sum P(A_n) < 1: P(no A_n occurs) >= 1 - sum P(A_n) > 0 -- the probabilistic method's first-moment argument
- if sum P(A_n) < inf then P(A_n i.o.) = 0 (borel_cantelli_first)

## Hypothesis-dropped counterexamples
- **none_unconditional**: the bound holds for every countable family; it is tight iff the A_n are pairwise disjoint (mod null sets)

## Common misuse
- expecting near-equality when the A_n overlap a lot
- applying to an uncountable family

## Related nodes (non-prerequisite)
- generalizes: finite_additivity (as a bound)
- used_by: borel_cantelli_first, convergence_implications

## Sources
boucheron_lugosi_massart, durrett_pte
