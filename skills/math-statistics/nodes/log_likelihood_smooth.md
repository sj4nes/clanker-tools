# log_likelihood_smooth

## Type
hypothesis

## Statement
theta -> log f(x; theta) is three-times continuously differentiable in a neighbourhood of theta_0, with the third derivative dominated by a fixed integrable function uniformly in that neighbourhood.

## Symbols
- `C^3` — three continuous theta-derivatives
- `M(x)` — a fixed integrable envelope for the third derivative

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
log_likelihood

## Hypotheses
(none — unconditional within scope)
## Well-definedness
A regularity condition on the model.

## Type / well-formedness check
The classical (Cramer) smoothness package. C^2 gives the information equality; the dominated third derivative controls the Taylor remainder in the MLE expansion so the o_p(1) terms really are negligible.

## Specialization / boundary cases
- exponential families: log f = eta.T(x) - A(eta) + log h(x) is real-analytic in eta -- holds on the interior
- N, Gamma, Beta, Poisson in standard parametrizations: hold
- weaker 'differentiability in quadratic mean' (van der Vaart) replaces C^3 for the modern proof of mle_asymptotic_normality -- but C^3 is what the classical proof and this capsule use

## Hypothesis-dropped counterexamples
- **log_likelihood_smooth**: Laplace(theta) = (1/2) e^{-|x - theta|}: log f = -|x - theta| + const is not differentiable at x = theta. The MLE is the sample median; it IS sqrt(n)-asymptotically normal (variance 1), but via a different argument (the score is a sum of sign(X_i - theta), not a smooth function) -- the C^3 route does not apply.
- **uniform(0, theta)**: not differentiable in theta at all on the relevant set -- non-regular, rate n not sqrt(n)

## Common misuse
- applying the -d^2 ell(theta_hat) 'observed information' standard error to a non-smooth model (quantile regression, Laplace)
- assuming a neural-net / spline log-likelihood satisfies this near a boundary of the parameter region

## Related nodes (non-prerequisite)
- required_by: information_equality, mle_asymptotic_normality, wilks_theorem
- commonly_confused_with: support_independent_of_theta

## Sources
lehmann_casella_tpe, van_der_vaart_asymptotic
