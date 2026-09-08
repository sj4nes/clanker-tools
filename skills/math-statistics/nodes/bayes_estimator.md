# bayes_estimator

## Type
definition

## Statement
Given a prior pi on Theta and a loss L(theta, a), the Bayes estimator is the decision rule delta_pi(x) = argmin_a E[ L(theta, a) | X = x ] = argmin_a int L(theta, a) pi(theta | x) dtheta: it minimizes the posterior expected loss for each observed x.

## Symbols
- `pi(theta)` — the prior density on Theta (a modeling input)
- `pi(theta | x) proportional to L(x; theta) pi(theta)` — the posterior
- `delta_pi` — the Bayes rule / Bayes estimator

## Epistemic status
definition  ·  regime: bayesian

## Prerequisites (tsort edges into this node)
loss_function, prob_conditional_distribution, risk_function

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: minimize the Bayes risk r(pi, delta) = E_X E_{theta|X}[L] by minimizing the inner (posterior) expectation for each x -- see bayes_rule_minimizes_bayes_risk
derives_from: bayes_rule_minimizes_bayes_risk
lean_status: core

## Type / well-formedness check
An argmin over actions of the posterior risk. Well-posed whenever the posterior exists (proper, or improper with a finite normalizer) and the posterior loss is finite. It is automatically a function of a sufficient statistic.

## Specialization / boundary cases
- squared-error loss: delta_pi(x) = posterior mean E[theta | x] (posterior_mean_rule)
- absolute-error loss: delta_pi(x) = a posterior median (posterior_median_rule)
- 0-1 loss on a discrete Theta: delta_pi(x) = the posterior mode (MAP estimate)

## Hypothesis-dropped counterexamples
- **proper_posterior**: an improper prior can yield an improper posterior (e.g. pi(sigma) = 1/sigma with n = 0, or the Bayes/Neyman-Scott hierarchical models) -- then no Bayes estimator exists and reported 'posterior summaries' are meaningless
- **finite_posterior_loss**: squared-error loss with a Cauchy posterior: E[theta | x] does not exist; use the posterior median

## Common misuse
- reporting a Bayes estimate without stating the prior -- the prior is part of the answer
- using a 'flat' prior on an unbounded parameter and assuming it is uninformative -- it is often improper and can be strongly informative after a nonlinear reparametrization

## In the wild
- Bayesian hierarchical shrinkage (small-area estimation, sports analytics, the 'James-Stein as empirical Bayes' story) -- the posterior mean pools information across units
- Kalman filtering is exact Bayesian estimation for the linear-Gaussian state-space model
- Thompson sampling for bandits draws from the posterior and acts greedily

## Related nodes (non-prerequisite)
- specializes_from: estimator, decision_rule
- required_by: posterior_mean_rule, posterior_median_rule, conjugate_prior, bernstein_von_mises

## Sources
berger_statistical_decision_theory, robert_bayesian_choice
