# inclusion_exclusion

## Type
theorem

## Statement
P(A_1 cup ... cup A_n) = sum P(A_i) - sum_{i<j} P(A_i cap A_j) + sum_{i<j<k} P(A_i cap A_j cap A_k) - ... + (-1)^{n+1} P(A_1 cap ... cap A_n).

## Symbols
- `A_i` — events, type: element of F
- `S` — a subset of {1..n}, type: index set

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
complement_rule, finite_additivity, set_algebra

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: induction on n using P(A cup B) = P(A) + P(B) - P(A cap B); or take expectations of the indicator identity 1_{bigcup A_i} = 1 - prod (1 - 1_{A_i})
derives_from: finite_additivity
lean_status: core — validation/proof-checks.lean Prob.incl_excl_2, Prob.incl_excl_3

## Type / well-formedness check
an alternating sum over all nonempty subsets S of the indices; the terms are probabilities of intersections, always well-defined.

## Specialization / boundary cases
- n = 2: P(A cup B) = P(A) + P(B) - P(A cap B)
- Bonferroni: truncating after k terms gives an upper bound (k odd) or lower bound (k even)
- derangements: P(no fixed point of a uniform random permutation) -> 1/e

## Hypothesis-dropped counterexamples
- **none_all_terms_needed**: dropping the higher-order terms gives only the Bonferroni one-sided bounds, not equality

## Common misuse
- forgetting the sign alternation
- using only the first two terms as if exact (that is the union bound / a Bonferroni bound)

## Related nodes (non-prerequisite)
- generalizes: finite_additivity
- special_case_of: the Mobius inversion formula on the subset lattice

## Sources
grimmett_stirzaker, durrett_pte
