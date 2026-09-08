# power_function

## Type
definition

## Statement
The power function of a test phi is beta_phi(theta) = E_theta[phi(X)] for all theta in Theta; on Theta_1 it is the power (probability of correctly rejecting), on Theta_0 it is the Type I error rate.

## Symbols
- `beta_phi(theta)` — one function giving both the Type I profile (on Theta_0) and the power (on Theta_1)
- `power at a specific alternative theta_1` — beta_phi(theta_1) = 1 - P(Type II error at theta_1)

## Epistemic status
definition  ·  regime: exact

## Prerequisites (tsort edges into this node)
alternative_hypothesis, prob_expectation, test_function

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
A single function on all of Theta. An ideal test has beta_phi <= alpha on Theta_0 and beta_phi close to 1 on Theta_1. Power increases with n, with the effect size, and with alpha; it decreases with variance.

## Specialization / boundary cases
- one-sample z-test power at mu_1: Phi( sqrt(n)(mu_1 - mu_0)/sigma - z_{1-alpha} ) for a one-sided test
- sample-size formula: solve beta_phi(mu_1) = 1 - beta for n given a target alternative mu_1 and power 1 - beta
- the power of the LRT against local alternatives theta_0 + h/sqrt(n) tends to a noncentral chi^2 tail probability

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: the power function is defined for any test; the content is its shape

## Common misuse
- reporting 'observed power' computed at the estimated effect after a non-significant result -- it is a deterministic function of the p-value and adds nothing (Hoenig-Heisey 2001)
- designing a study with 50% power and treating a null result as informative

## In the wild
- prospective power / sample-size calculation is a regulatory requirement for clinical trials (ICH E9)
- the basis of 'minimum detectable effect' reporting in A/B testing platforms

## Related nodes (non-prerequisite)
- uses: test_function, alternative_hypothesis
- special_case_of: risk_function
- required_by: neyman_pearson_lemma, karlin_rubin_theorem

## Sources
lehmann_romano_tsh, cohen_power_analysis
