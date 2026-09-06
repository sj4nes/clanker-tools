# covariance_bilinear

## Type
proposition

## Statement
Covariance is a symmetric, positive-semidefinite bilinear form on L^2(P): Cov(aX + bZ, Y) = a Cov(X, Y) + b Cov(Z, Y), Cov(X, Y) = Cov(Y, X), Cov(X, X) >= 0.

## Symbols
- `X, Y, Z` — random variables in L^2(P), type: L^2(P)
- `a, b` — constants, type: real

## Epistemic status
proposition

## Prerequisites (tsort edges into this node)
covariance, expectation_linearity, variance

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: expand the centered products and use expectation_linearity in each slot; symmetry is commutativity of the product; Cov(X,X) = Var(X) >= 0
derives_from: expectation_linearity
lean_status: core

## Type / well-formedness check
bilinearity is linearity of expectation applied in each argument after centering; constants have zero covariance with everything, so Cov(X + c, Y) = Cov(X, Y).

## Specialization / boundary cases
- Cov(sum a_i X_i, sum b_j Y_j) = sum_{i,j} a_i b_j Cov(X_i, Y_j) -- the general bilinear expansion behind variance_of_sum
- Cov(X, c) = 0 for constant c

## Hypothesis-dropped counterexamples
- **none_holds_on_all_of_L2**: bilinearity is unconditional on L^2(P); it is the inner-product structure (X, Y) |-> Cov(X, Y) on the quotient by constants

## Common misuse
- forgetting cross terms when expanding Cov of two sums
- treating Cov as an inner product without quotienting out constants (it is only PSD, not PD)

## Related nodes (non-prerequisite)
- gives: the L^2 geometry behind conditional_expectation_l2_projection
- used_by: variance_of_sum, correlation

## Sources
billingsley_probability_measure, durrett_pte
