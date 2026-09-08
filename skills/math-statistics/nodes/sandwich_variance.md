# sandwich_variance

## Type
proposition

## Statement
An M-estimator solving (1/n) sum psi(X_i; theta) = 0 has asymptotic covariance A(theta)^{-1} B(theta) A(theta)^{-T} with A = -E_theta[grad_theta psi(X; theta)] and B = E_theta[psi(X; theta) psi(X; theta)^T]; it reduces to I(theta)^{-1} when psi is the true score (information equality: A = B = I).

## Symbols
- `the 'bread' A^{-1}` — from the derivative of the estimating equation
- `the 'meat' B` — the variance of the estimating function
- `the estimated version` — A_hat = -(1/n) sum grad psi(X_i; theta_hat), B_hat = (1/n) sum psi psi^T at theta_hat -- the Huber-White / robust standard error

## Epistemic status
proposition  ·  regime: asymptotic

## Prerequisites (tsort edges into this node)
m_estimator, mle_asymptotic_normality

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: linearize the estimating equation: sqrt(n)(theta_hat - theta) = A^{-1} (1/sqrt n) sum psi(X_i; theta) + o_p(1); apply the CLT to the sum (covariance B)
derives_from: m_estimator
lean_status: core — the reduction A = B = I(theta) under the information equality is proof-checks.lean Stat.sandwich_reduces_when_info_equality

## Type / well-formedness check
A covariance formula, asymptotic. The reduction A^{-1} B A^{-1} -> I^{-1} needs the information equality (correct model). Under misspecification A != B and the sandwich is the only correct large-sample variance.

## Specialization / boundary cases
- OLS with heteroskedastic errors: the HC0-HC3 'robust' / 'Huber-White' standard errors are the sandwich with psi = x(y - x^T beta)
- GEE (longitudinal data): the sandwich gives valid SEs even if the working correlation is wrong
- a correctly specified GLM: sandwich SE approx model-based SE (they diverge => evidence of misspecification -- an informal specification test)

## Hypothesis-dropped counterexamples
- **finite_meat_and_bread**: if B = E[psi psi^T] is infinite (heavy-tailed influence) the sandwich variance is infinite and no sqrt(n) normal limit holds

## Common misuse
- using robust SEs to 'fix' a model whose POINT estimates are inconsistent -- the sandwich only fixes the variance, not the bias from a wrong mean model
- applying sandwich SEs at small n, where they are downward biased (hence the HC2/HC3 finite-sample corrections)

## Related nodes (non-prerequisite)
- uses: m_estimator, information_equality

## Sources
huber_robust_statistics, white_1982, stefanski_boos_2002
