# finite_additivity

## Type
proposition

## Statement
For pairwise-disjoint A_1, ..., A_n in F, P(A_1 cup ... cup A_n) = P(A_1) + ... + P(A_n).

## Symbols
- `A_i` — pairwise disjoint events, type: element of F
- `n` — a fixed positive integer, type: natural number

## Epistemic status
proposition

## Prerequisites (tsort edges into this node)
kolmogorov_axioms, set_algebra

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: take the countably additive axiom on (A_1, ..., A_n, empty, empty, ...); the series has finitely many nonzero terms
derives_from: kolmogorov_axioms
lean_status: core — validation/proof-checks.lean Prob.incl_excl_2 (n=2)

## Type / well-formedness check
the finite case of countable additivity: pad the finite family with A_{n+1} = A_{n+2} = ... = empty and apply the countable axiom (the tail terms are 0).

## Specialization / boundary cases
- n = 2: P(A cup B) = P(A) + P(B) for disjoint A, B
- partition of Omega: sum_i P(B_i) = 1

## Hypothesis-dropped counterexamples
- **disjointness**: P(A cup B) = P(A) + P(B) - P(A cap B) in general; without disjointness the sum overcounts the overlap (inclusion_exclusion)

## Common misuse
- applying it to non-disjoint events
- extending to a countably infinite family (that is the axiom, not this proposition)

## In the wild
- the Bonferroni correction in multiple hypothesis testing: P(any of m tests falsely significant) <= sum of the per-test levels -- the finitely-additive union bound, used to set genome-wide significance at 5e-8 in GWAS

## Related nodes (non-prerequisite)
- special_case_of: kolmogorov_axioms
- generalizes_to: inclusion_exclusion

## Sources
billingsley_probability_measure, durrett_pte
