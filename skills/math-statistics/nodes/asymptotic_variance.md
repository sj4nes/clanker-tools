# asymptotic_variance

## Type
definition

## Statement
The asymptotic variance of an asymptotically normal estimator is the covariance Sigma(theta) in its limit law sqrt(n)(theta_hat_n - theta) -> N(0, Sigma(theta)); the estimator's approximate variance at finite n is Sigma(theta)/n.

## Symbols
- `Sigma(theta)/n` — the finite-n variance approximation used for standard errors

## Epistemic status
definition  ·  regime: asymptotic

## Prerequisites (tsort edges into this node)
asymptotic_normality_estimator

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
Defined only for sqrt(n)-asymptotically-normal estimators. It is NOT in general the limit of n Var(theta_hat_n) (that can differ or be infinite); it is the variance of the limiting law.

## Specialization / boundary cases
- MLE: Sigma = I(theta)^{-1}
- sample median of iid f: Sigma = 1 / (4 f(m)^2) where m is the population median
- delta method: AVar(g(theta_hat)) = g'(theta)^T Sigma g'(theta)

## Hypothesis-dropped counterexamples
- **limit_of_scaled_variance**: an estimator can be asymptotically N(0, Sigma) yet have Var(theta_hat_n) = inf for every n (a small-probability heavy tail that vanishes in the limit) -- report the asymptotic variance, not the (infinite) exact one

## Common misuse
- reporting Sigma(theta_hat)/n as if exact -- it is a large-n approximation
- plugging a very rough theta_hat into a steep Sigma(theta) and trusting the SE

## Related nodes (non-prerequisite)
- required_by: relative_efficiency, asymptotic_efficiency

## Sources
van_der_vaart_asymptotic
