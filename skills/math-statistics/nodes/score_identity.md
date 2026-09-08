# score_identity

## Type
identity

## Statement
Under regularity, E_theta[U(theta)] = 0: the score has mean zero at the true parameter.

## Symbols
- `U(theta)` — the score at theta
- `E_theta` — expectation under P_theta (the SAME theta as in the score)

## Epistemic status
mathematical_identity  ·  regime: exact

## Prerequisites (tsort edges into this node)
interchange_derivative_integral, prob_expectation, score_function, support_independent_of_theta

## Hypotheses
interchange_derivative_integral, support_independent_of_theta

## Proof provenance
technique: differentiate the identity int f(x;theta) dx = 1 under the integral sign
derives_from: interchange_derivative_integral
lean_status: core — validation/proof-checks.lean Stat.score_mean_zero -- the algebra int (d log f) f = int df given int f = 1

## Type / well-formedness check
An identity in theta, not an approximation. Proof: 1 = int f(x; theta) dx; differentiate both sides; if d/dtheta passes inside, 0 = int (d/dtheta f) dx = int (d/dtheta log f) f dx = E_theta[U_1(theta)]. Sum over i for the full score.

## Specialization / boundary cases
- Bernoulli: E_p[(X - p)/(p(1-p))] = 0 since E[X] = p
- N(mu, sigma^2 known): E_mu[(X - mu)/sigma^2] = 0
- gives the moment condition behind method-of-moments and estimating-equation estimators

## Hypothesis-dropped counterexamples
- **support_independent_of_theta**: uniform(0, theta): the support {0 <= x <= theta} moves with theta, so d/dtheta int_0^theta theta^{-1} dx has a boundary term; E_theta[U(theta)] = -1/theta != 0. The score is biased and every downstream result (CRLB, information equality) fails.
- **interchange_derivative_integral**: a family where the tails are too heavy for the dominated-derivative condition: the swap of d/dtheta and int is invalid and E[U] can be nonzero

## Common misuse
- assuming E[score] = 0 for a MISSPECIFIED model -- then the score has mean zero only at the pseudo-true parameter, not the truth
- applying it at a boundary theta

## Related nodes (non-prerequisite)
- required_by: information_equality, cramer_rao_lower_bound
- generalizes_to: estimating_equation

## Sources
casella_berger_2e, van_der_vaart_asymptotic
