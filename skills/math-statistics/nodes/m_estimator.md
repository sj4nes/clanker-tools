# m_estimator

## Type
definition

## Statement
An M-estimator maximizes an empirical criterion theta_hat = argmax_theta (1/n) sum_i m(X_i; theta), or equivalently solves the estimating equation (1/n) sum_i psi(X_i; theta) = 0 with psi = grad_theta m; the MLE is the case m = log f.

## Symbols
- `m(x; theta)` — the per-observation criterion (log-density, negative loss, ...)
- `psi(x; theta) = grad_theta m` — the estimating function / influence-defining function

## Epistemic status
definition  ·  regime: asymptotic

## Prerequisites (tsort edges into this node)
maximum_likelihood_estimator, score_function

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: Z-estimator master theorem: consistency from a uniform LLN for the criterion, asymptotic normality from linearizing the estimating equation + CLT for (1/sqrt n) sum psi(X_i; theta_0)
derives_from: mle_asymptotic_normality
lean_status: cited

## Type / well-formedness check
Generalizes the MLE by decoupling the criterion from the true density. Under E_theta[psi(X; theta)] = 0 (the estimating equation is 'unbiased') the estimator is consistent for that theta; asymptotic normality with the SANDWICH covariance A^{-1} B A^{-T}, A = -E[grad psi], B = E[psi psi^T].

## Specialization / boundary cases
- Huber's robust location estimator: psi(x) = clip(x - theta, -c, c) -- bounded influence, resists outliers
- quantile regression: m(x; theta) = rho_tau(y - x^T theta), the check function -- estimates conditional quantiles
- quasi-likelihood / GEE: psi from a mean model only, no full distribution

## Hypothesis-dropped counterexamples
- **estimating_equation_unbiased**: if E_theta[psi(X; theta)] != 0 (a misspecified mean model, or Huber's psi under an asymmetric error) the M-estimator converges to the wrong value theta* -- the solution of E[psi(X; theta*)] = 0, not theta

## Common misuse
- reporting inverse-Hessian (naive) standard errors for an M-estimator that is not the MLE -- the sandwich B != A there and the naive SE is wrong
- assuming robustness of the estimator implies robustness of its standard error

## Related nodes (non-prerequisite)
- generalizes_from: maximum_likelihood_estimator, method_of_moments
- required_by: sandwich_variance

## Sources
huber_robust_statistics, van_der_vaart_asymptotic, stefanski_boos_2002
