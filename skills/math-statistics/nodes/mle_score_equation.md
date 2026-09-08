# mle_score_equation

## Type
proposition

## Statement
If the MLE theta_hat lies in the interior of Theta and ell is differentiable there, then it solves the score equation U(theta_hat) = 0.

## Symbols
- `U(theta_hat) = 0` — the first-order stationarity condition

## Epistemic status
proposition  ·  regime: exact

## Prerequisites (tsort edges into this node)
maximum_likelihood_estimator, score_function, true_parameter_interior

## Hypotheses
true_parameter_interior

## Proof provenance
technique: first-order condition for an interior maximum of a differentiable function
derives_from: ra_mean_value_theorem
lean_status: core — the 1-D statement (interior max => derivative zero) is proof-checks.lean Stat.interior_max_stationary via the MVT

## Type / well-formedness check
Fermat's stationarity condition, nothing more. It is NECESSARY, not sufficient -- a root of U can be a minimum or a saddle; and a boundary MLE need not be a root at all.

## Specialization / boundary cases
- Bernoulli: U(p) = (sum x_i)/p - (n - sum x_i)/(1-p) = 0  =>  p_hat = xbar
- exponential family: U(eta) = sum T(x_i) - n grad A(eta) = 0  =>  grad A(eta_hat) = Tbar  (moment matching)
- uniform(0, theta): U(theta) = -n/theta, never 0 -- the MLE max x_i is NOT found this way

## Hypothesis-dropped counterexamples
- **true_parameter_interior**: boundary MLE (uniform endpoint; a variance component estimated at 0; a probability estimated at exactly 0 or 1 in a small sample) -- U(theta_hat) != 0 and the score equation is the wrong tool
- **differentiability**: non-smooth log-likelihood (Laplace location -> sample median): U is a step function, 0 is 'crossed' not 'hit'

## Common misuse
- solving U(theta) = 0 and stopping -- must verify it is a maximum (check the Hessian is negative definite) and that no boundary point does better
- iterating Newton from a bad start into a saddle point

## Related nodes (non-prerequisite)
- required_by: mle_asymptotic_normality
- uses: score_function

## Sources
casella_berger_2e
