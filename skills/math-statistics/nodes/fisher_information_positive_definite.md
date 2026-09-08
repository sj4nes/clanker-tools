# fisher_information_positive_definite

## Type
hypothesis

## Statement
I(theta_0) is finite and positive definite (positive and finite in the scalar case).

## Symbols
- `I(theta_0)` — the Fisher information at the truth
- `PD` — positive definite: x^T I x > 0 for all x != 0

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
fisher_information_matrix

## Hypotheses
(none — unconditional within scope)
## Well-definedness
Finiteness rules out heavy-tailed scores; positive-definiteness rules out a locally flat / non-identified direction.

## Type / well-formedness check
A nondegeneracy statement. PD => invertible => I(theta_0)^{-1} exists and is the MLE's asymptotic covariance. Uses linear_algebra_background for 'positive definite' and 'invertible'.

## Specialization / boundary cases
- any full-rank exponential family on the interior: I(eta) = Hess A(eta) is PD (A strictly convex)
- N(mu, sigma^2): I = diag(1/sigma^2, 1/(2 sigma^4)) PD for every sigma^2 > 0

## Hypothesis-dropped counterexamples
- **fisher_information_positive_definite**: the non-identified N(alpha + beta, 1): I = [[1,1],[1,1]] has eigenvalue 0 along (1, -1). The MLE is not consistent for (alpha, beta) and I^{-1} does not exist. This hypothesis is the local (2nd-order) counterpart of the global identifiability hypothesis.
- **singular in the limit**: a model at a parameter where a component's information -> 0 (e.g. a mixture weight at 0 or 1): near-singular I, unstable inversion, wide/unreliable intervals

## Common misuse
- inverting a singular or near-singular information matrix from collinear regressors and trusting the standard errors
- conflating this with global identifiability -- a model can be identified yet have singular information at one point (a 'non-regular' point)

## Related nodes (non-prerequisite)
- required_by: mle_asymptotic_normality, wilks_theorem
- commonly_confused_with: identifiability

## Sources
van_der_vaart_asymptotic, lehmann_casella_tpe
