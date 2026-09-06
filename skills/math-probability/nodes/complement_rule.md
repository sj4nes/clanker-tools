# complement_rule

## Type
identity

## Statement
P(A^c) = 1 - P(A); consequently P(A) in [0,1], P(empty) = 0, and A subset B implies P(A) <= P(B) (with P(B \ A) = P(B) - P(A)).

## Symbols
- `A, B` — events, type: element of F

## Epistemic status
mathematical_identity

## Prerequisites (tsort edges into this node)
finite_additivity, kolmogorov_axioms

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: finite additivity on {A, A^c} plus P(Omega) = 1; monotonicity from B = A cup (B \ A) disjoint
derives_from: finite_additivity
lean_status: core — validation/proof-checks.lean Prob.union_bound / incl_excl_2

## Type / well-formedness check
A and A^c are disjoint with union Omega, so P(A) + P(A^c) = P(Omega) = 1 by finite additivity and normalization.

## Specialization / boundary cases
- A = Omega: P(empty) = 0
- A = B: P(B \ B) = 0

## Hypothesis-dropped counterexamples
- **P_a_probability_measure**: for a general (unnormalized) measure there is no '1 -' form; only mu(B \ A) = mu(B) - mu(A) with mu(A) < inf survives

## Common misuse
- writing P(A^c) = 1 - P(A) when conditioning: P(A^c | C) = 1 - P(A | C) is fine, but mixing conditioning events is not
- subtracting P(A) - P(B) without A superset B

## Related nodes (non-prerequisite)
- derives_from: finite_additivity
- used_by: conditional_probability, borel_cantelli_second

## Sources
billingsley_probability_measure, durrett_pte
