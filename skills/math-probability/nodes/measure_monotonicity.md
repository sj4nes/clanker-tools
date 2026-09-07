# measure_monotonicity

## Type
proposition

## Statement
For a measure mu: A subset B implies mu(A) <= mu(B); and mu is countably subadditive: mu(bigcup_n A_n) <= sum_n mu(A_n) for any (not necessarily disjoint) A_n.

## Symbols
- `mu` — a measure, type: F -> [0, inf]
- `(A_n)` — any countable family in F, type: N -> F

## Epistemic status
proposition

## Prerequisites (tsort edges into this node)
measure, series_convergence, set_algebra

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: monotonicity: B = A disjoint-union (B minus A), additivity, mu >= 0. Subadditivity: replace A_n by disjoint B_n subset A_n with the same union; sum mu(B_n) <= sum mu(A_n)
derives_from: measure
lean_status: core — validation/proof-checks.lean Prob.union_bound (the two-set case)

## Type / well-formedness check
monotonicity uses mu(B) = mu(A) + mu(B \ A) >= mu(A); subadditivity disjointifies B_n = A_n \ (A_1 cup ... cup A_{n-1}) then uses countable additivity + monotonicity.

## Specialization / boundary cases
- mu = P: P(A) <= P(B) and P(A) in [0,1]; Boole's inequality is the probability form of subadditivity
- equality in subadditivity iff the A_n are pairwise disjoint (mod null sets)

## Hypothesis-dropped counterexamples
- **nonnegativity_of_mu**: for a signed measure monotonicity fails: a set of negative measure can contain one of positive measure

## Common misuse
- expecting equality in the union bound (usually strict)
- using it for mu(A \ B) = mu(A) - mu(B) without mu(B) < inf and B subset A

## In the wild
- the union bound P(bad_1 or ... or bad_n) <= sum P(bad_i) is the single most-used step in randomized-algorithm analysis: bounding the failure probability of a hashing scheme, a randomized rounding, a sketch
- reliability engineering: a system fails if any component fails, so P(system failure) <= sum of component failure rates -- the standard conservative bound in an FMEA

## Related nodes (non-prerequisite)
- used_by: boole_inequality, borel_cantelli_first

## Sources
billingsley_probability_measure, folland_real_analysis
