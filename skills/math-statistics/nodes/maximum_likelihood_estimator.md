# maximum_likelihood_estimator

## Type
definition

## Statement
The maximum likelihood estimator is theta_hat = argmax_{theta in Theta} L(theta) = argmax_{theta in Theta} ell(theta): the parameter value that makes the observed data most probable under the model.

## Symbols
- `argmax` — the set of maximizers; theta_hat is any measurable selection when it is not unique
- `ell(theta) = sum_i log f(X_i; theta)` — the log-likelihood

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
likelihood_function, ra_compactness, ra_continuity

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: existence: extreme value theorem on a compact Theta (or coercivity of ell); computation: solve the score equation (interior, smooth case) or search
derives_from: ra_compactness
lean_status: cited

## Type / well-formedness check
Existence needs ell upper-semicontinuous and Theta compact (or ell -> -inf at the boundary) -- ra_compactness + ra_continuity. Uniqueness is separate (guaranteed if ell is strictly concave, e.g. a full-rank exponential family). The MLE is a function of any sufficient statistic.

## Specialization / boundary cases
- Bernoulli: p_hat = Xbar; Poisson: lambda_hat = Xbar; N(mu, sigma^2): mu_hat = Xbar, sigma^2_hat = (1/n) sum (X_i - Xbar)^2 (divisor n -- biased)
- uniform(0, theta): theta_hat = max X_i -- the argmax is at the boundary, the score equation has no root
- logistic regression: no closed form; Newton-Raphson / IRLS on the concave log-likelihood

## Hypothesis-dropped counterexamples
- **argmax_exists**: a two-component normal mixture with a free component variance: ell -> +inf as one component's variance -> 0 around a single data point -- the global MLE does not exist (only a consistent local maximizer does)
- **argmax_unique**: a periodic likelihood (circular / phase parameter) can have multiple equal maxima

## Common misuse
- reporting a local maximum from an optimizer as 'the MLE' without checking for higher modes
- using MLE standard errors (inverse observed information) for uniform(0, theta) or other non-regular models
- forgetting the divisor-n bias of the normal-variance MLE

## In the wild
- the default fitting method in essentially every statistical model and in much of machine learning (cross-entropy loss IS the negative log-likelihood of a categorical model)
- phylogenetics, population genetics, econometrics (structural models), item-response theory -- all MLE-based

## Related nodes (non-prerequisite)
- specializes_from: estimator
- special_case_of: m_estimator
- required_by: mle_score_equation, mle_consistency, likelihood_ratio_test

## Sources
casella_berger_2e, van_der_vaart_asymptotic
