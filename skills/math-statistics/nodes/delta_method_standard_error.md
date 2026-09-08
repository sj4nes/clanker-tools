# delta_method_standard_error

## Type
proposition

## Statement
If sqrt(n)(theta_hat - theta) -> N(0, v(theta)) and g is differentiable at theta with g'(theta) != 0, then sqrt(n)(g(theta_hat) - g(theta)) -> N(0, g'(theta)^2 v(theta)); so se(g(theta_hat)) = |g'(theta_hat)| se(theta_hat), giving an asymptotic interval for g(theta).

## Symbols
- `g'(theta)` — the derivative (gradient, then g'(theta)^T V g'(theta) in the vector case)
- `the linearization` — g(theta_hat) approx g(theta) + g'(theta)(theta_hat - theta)

## Epistemic status
proposition  ·  regime: asymptotic

## Prerequisites (tsort edges into this node)
prob_continuous_mapping, prob_delta_method, ra_differentiability, wald_interval

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: first-order Taylor of g at theta_hat, then Slutsky (the remainder is o_p(1/sqrt n))
derives_from: prob_delta_method
lean_status: cited

## Type / well-formedness check
A first-order (Taylor) propagation of uncertainty. Asymptotic. Fails when g'(theta) = 0 (then the limit is a scaled chi^2_1, the 'second-order delta method') or g is not differentiable.

## Specialization / boundary cases
- odds ratio from log-odds: se(OR) = OR . se(log OR) -- but the CI is better built on the log scale and exponentiated
- se of p_hat(1 - p_hat) is |1 - 2 p_hat| se(p_hat) -- ZERO at p_hat = 1/2, where the first-order method fails and Var(p_hat(1-p_hat)) = O(1/n^2)
- se of a ratio Xbar/Ybar (Ybar bounded away from 0): the classic ratio-estimator variance formula

## Hypothesis-dropped counterexamples
- **g_prime_nonzero**: g(theta) = theta^2 at theta = 0: g'(0) = 0, so the first-order delta method gives se = 0. The truth is n theta_hat^2 -> sigma^2 chi^2_1 -- a completely different (one-sided, non-normal) limit.
- **g_differentiable**: g(theta) = |theta| at 0, or a max/min functional -- not differentiable, delta method inapplicable

## Common misuse
- applying it where g'(theta_hat) is near 0 and reporting an absurdly small SE
- building a symmetric CI for a bounded quantity (a probability, a correlation) on the natural scale rather than a variance-stabilizing scale (logit, Fisher z)

## In the wild
- the universal 'error propagation' formula in physics and chemistry lab courses
- standard errors for predicted probabilities, marginal effects, EC50s, and elasticities in applied econometrics/biostatistics

## Related nodes (non-prerequisite)
- uses: wald_interval, ra_differentiability
- special_case_of: prob_delta_method

## Sources
van_der_vaart_asymptotic, casella_berger_2e
