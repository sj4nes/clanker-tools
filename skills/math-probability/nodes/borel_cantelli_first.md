# borel_cantelli_first

## Type
theorem

## Statement
If sum_n P(A_n) < inf, then P(A_n infinitely often) = 0; i.e. almost surely only finitely many A_n occur.

## Symbols
- `(A_n)` — any sequence of events (no independence), type: N -> F
- `limsup A_n` — the i.o. event, type: element of F

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
boole_inequality, continuity_of_probability, limsup_liminf, series_convergence

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: monotonicity into the N-th tail union, then Boole, then let N -> inf using that the series tail vanishes
derives_from: boole_inequality
lean_status: core — validation/proof-checks.lean Prob.union_bound is the Boole step

## Type / well-formedness check
no independence needed. P(limsup A_n) = P(bigcap_N bigcup_{n>=N} A_n) <= P(bigcup_{n>=N} A_n) <= sum_{n>=N} P(A_n) -> 0 as N -> inf (tail of a convergent series).

## Specialization / boundary cases
- A_n = { |X_n - X| > eps }: sum P < inf gives X_n -> X a.s. -- the standard route from a rate to a.s. convergence
- A_n = { X_n / n > 1 + eps } with sum P < inf: proves a.s. bounds like the SLLN's a.s. o(n) growth

## Hypothesis-dropped counterexamples
- **none_unconditional_direction**: the converse needs independence (borel_cantelli_second); without it sum P(A_n) = inf gives no lower bound -- take A_n all equal to a fixed A with 0 < P(A) < 1: sum diverges but P(A i.o.) = P(A) < 1

## Common misuse
- thinking it needs independence (it does not)
- concluding P(A_n i.o.) > 0 from sum P(A_n) = inf without independence

## Related nodes (non-prerequisite)
- dual_of: borel_cantelli_second
- used_by: strong_law_large_numbers, convergence_implications

## Sources
billingsley_probability_measure, durrett_pte
