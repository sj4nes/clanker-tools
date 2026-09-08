# bayes_rule_minimizes_bayes_risk

## Type
theorem

## Statement
The rule that minimizes the posterior expected loss for each x, delta_pi(x) = argmin_a E[L(theta, a) | X = x], also minimizes the overall Bayes risk r(pi, delta); so the Bayes estimator is optimal against its prior.

## Symbols
- `the pointwise-vs-global equivalence` — minimize under the integral sign

## Epistemic status
proved_theorem  ·  regime: bayesian

## Prerequisites (tsort edges into this node)
bayes_risk, posterior_mean_rule, prob_tower_property

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: write the Bayes risk as an iterated expectation (tower property), then minimize the inner posterior expectation pointwise in x
derives_from: prob_tower_property
lean_status: core — validation/proof-checks.lean Stat.bayes_rule_pointwise -- if g(x, a) >= g(x, a*(x)) for every a then E_X[g(X, delta(X))] >= E_X[g(X, a*(X))]; the interchange of min and integral

## Type / well-formedness check
Proof: r(pi, delta) = E_X[ E_{theta|X}[ L(theta, delta(X)) ] ] (Fubini/tower). The inner expectation is minimized, for each x separately, by delta(x) = delta_pi(x); a rule minimizing every inner term minimizes the outer average.

## Specialization / boundary cases
- squared-error loss => delta_pi = posterior mean (posterior_mean_rule)
- absolute loss => posterior median; 0-1 loss => posterior mode
- the theorem is what licenses 'just compute the posterior and summarize it' as an optimal procedure

## Hypothesis-dropped counterexamples
- **inner_min_attained**: if argmin_a E[L(theta,a)|x] is empty (loss not lower-semicontinuous, or infinite everywhere) there is no Bayes rule -- e.g. squared loss with a Cauchy posterior

## Common misuse
- assuming the Bayes rule is also good in a frequentist sense for a fixed theta -- it is optimal ON AVERAGE against pi, and can be poor at a particular theta the prior disfavors
- forgetting the optimality is relative to the (subjective) prior

## Related nodes (non-prerequisite)
- required_by: bayes_estimator
- uses: bayes_risk, posterior_mean_rule

## Sources
berger_statistical_decision_theory, robert_bayesian_choice
