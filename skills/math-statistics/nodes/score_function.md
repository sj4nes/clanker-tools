# score_function

## Type
definition

## Statement
The score is U(theta) = d ell / d theta = sum_{i=1}^n d/dtheta log f(x_i; theta); in R^d it is the gradient of ell.

## Symbols
- `U(theta)` — the score, type: R^d-valued random function of theta (random through the data)
- `U_1(theta) = grad log f(X_1; theta)` — the single-observation score
- `U(theta) = sum_i U_i(theta)` — additivity over an iid sample

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
log_likelihood, ra_differentiability

## Hypotheses
(none — unconditional within scope)
## Well-definedness
Defined wherever ell is differentiable in theta. For an iid sample, U(theta) is a sum of n iid random vectors -- the structure the CLT needs.

## Type / well-formedness check
U(theta) in R^d for each theta; as a function of the data it is a random vector. Requires log f(x; .) differentiable in theta (part of log_likelihood_smooth). The MLE, when interior and smooth, is a root of U.

## Specialization / boundary cases
- Bernoulli: U(p) = (sum x_i)/p - (n - sum x_i)/(1 - p); setting U(p) = 0 gives p_hat = xbar
- N(mu, sigma^2 known): U(mu) = sum (x_i - mu)/sigma^2; root at mu_hat = xbar
- exponential family f = h exp(eta T - A): U(eta) = sum T(x_i) - n A'(eta) -- the score is 'observed minus expected sufficient statistic'

## Hypothesis-dropped counterexamples
- **log_likelihood_smooth**: uniform(0, theta): ell(theta) = -n log theta on theta >= max x_i, so U(theta) = -n/theta is never 0 -- the MLE is at the boundary theta_hat = max x_i and the score equation has no solution. Score-based asymptotics (Fisher information, mle_asymptotic_normality) do not apply.

## Common misuse
- solving U(theta) = 0 and declaring victory without checking it is a MAXIMUM and INTERIOR
- using the score identity / information equality when differentiation under the integral sign fails

## In the wild
- the score test uses U(theta_0) evaluated only under the null -- no need to fit the alternative
- score / estimating equations generalize to GLMs, GMM, and quasi-likelihood

## Related nodes (non-prerequisite)
- required_by: fisher_information, score_identity, mle_score_equation, score_test
- generalizes_to: estimating_equation

## Sources
casella_berger_2e, van_der_vaart_asymptotic
