# fisher_information_matrix

## Type
definition

## Statement
For a d-dimensional parameter, I(theta) = Cov_theta(grad log f(X_1; theta)) = E_theta[grad log f (grad log f)^T], a symmetric positive-semidefinite d x d matrix; = -E_theta[Hessian of log f] under regularity.

## Symbols
- `I(theta)` — the d x d Fisher information matrix, type: symmetric PSD matrix
- `grad log f` — the score vector, type: R^d
- `I(theta)^{-1}` — the asymptotic covariance of the MLE (when I is positive definite)

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
linear_algebra_background, prob_covariance, score_function

## Hypotheses
(none — unconditional within scope)
## Well-definedness
A covariance matrix, hence symmetric PSD; the matrix analogue of the scalar I(theta).

## Type / well-formedness check
Symmetric PSD by construction (a covariance matrix). Requires the vector score to exist (log_likelihood_smooth). Positive-DEFINITE is the separate hypothesis fisher_information_positive_definite. Uses linear_algebra_background for 'PSD', 'inverse', 'eigenvalues'.

## Specialization / boundary cases
- N(mu, sigma^2), theta = (mu, sigma^2): I = diag(1/sigma^2, 1/(2 sigma^4)) -- mu and sigma^2 are 'information-orthogonal'
- a full-rank exponential family: I(eta) = Hess A(eta), the Hessian of the cumulant function (always PD on the interior)
- block structure: a zero off-diagonal block means the blocks' MLEs are asymptotically independent

## Hypothesis-dropped counterexamples
- **fisher_information_positive_definite**: the non-identified model N(alpha + beta, 1): I(alpha, beta) = [[1,1],[1,1]], singular -- not invertible, so I^{-1} does not exist and MLE-normality fails along the ridge

## Common misuse
- inverting a near-singular information matrix (collinear covariates) and reporting the resulting huge, unstable standard errors as if reliable
- ignoring off-diagonal terms and treating each coordinate's information as 1 / I_jj instead of (I^{-1})_jj

## Related nodes (non-prerequisite)
- required_by: fisher_information_positive_definite, mle_asymptotic_normality
- specializes_from: fisher_information

## Sources
lehmann_casella_tpe, van_der_vaart_asymptotic
