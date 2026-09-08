# method_of_moments

## Type
algorithm

## Statement
The method of moments estimates a d-dimensional theta by equating the first d population moments m_k(theta) = E_theta[X^k] to the sample moments mbar_k = (1/n) sum X_i^k and solving for theta.

## Symbols
- `m_k(theta) = E_theta[X^k]` — the k-th population (raw) moment as a function of theta
- `mbar_k = (1/n) sum X_i^k` — the k-th sample moment

## Epistemic status
constructive_result  ·  regime: asymptotic

## Prerequisites (tsort edges into this node)
iid_sample, parameter_space, prob_cauchy_no_mean, prob_chebyshev_ineq, prob_lotus, prob_moment

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: LLN: sample moments -> population moments; continuous mapping through the (assumed invertible) moment map gives consistency; CLT + delta method give asymptotic normality
derives_from: prob_wlln
lean_status: cited — the Chebyshev bound behind 'mbar_k -> m_k' is proof-checks.lean Stat.consistency_chebyshev

## Type / well-formedness check
A system of d equations in d unknowns. Consistency follows from the LLN (mbar_k -> m_k) plus continuity of the inverse moment map; asymptotic normality from the CLT + delta method. Generally NOT efficient.

## Specialization / boundary cases
- N(mu, sigma^2): m_1 = mu, m_2 = sigma^2 + mu^2 => mu_hat = Xbar, sigma^2_hat = (1/n) sum (X_i - Xbar)^2 (the /n version)
- Gamma(a, b): match mean a/b and variance a/b^2 => a_hat, b_hat in closed form (the MLE needs iteration)
- uniform(0, theta): m_1 = theta/2 => theta_hat = 2 Xbar -- which can be LESS than max X_i, an impossible estimate

## Hypothesis-dropped counterexamples
- **moments_exist**: Cauchy or t_2: no finite mean / variance, so mbar_1, mbar_2 do not converge and the method produces nonsense (prob_cauchy_no_mean). Estimate the median / IQR instead.
- **moment_map_invertible**: if two parameter values give the same first d moments the system is not solvable for theta

## Common misuse
- using MoM when the MLE is tractable -- MoM throws away efficiency for no reason in the exponential-family case
- reporting a MoM estimate that lies outside the parameter space (negative variance, 2 Xbar < max)

## In the wild
- the generalized method of moments (GMM, Hansen 1982) is the workhorse of econometrics -- it estimates from moment conditions E[psi(X; theta)] = 0 without a full likelihood
- quick starting values for iterative MLE / EM

## Related nodes (non-prerequisite)
- historically_precedes: maximum_likelihood_estimator
- generalizes_to: m_estimator

## Sources
casella_berger_2e, hansen_gmm_1982
