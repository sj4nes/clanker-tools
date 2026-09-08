# posterior_median_rule

## Type
theorem

## Statement
Under absolute-error loss L(theta, a) = |theta - a|, the Bayes estimator is a posterior median: any m with P(theta <= m | x) >= 1/2 and P(theta >= m | x) >= 1/2.

## Symbols
- `m` — a posterior median (an interval of minimizers if the posterior has a flat spot at 1/2)

## Epistemic status
proved_theorem  ·  regime: bayesian

## Prerequisites (tsort edges into this node)
bayes_estimator

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: E[|theta - a|] has left-derivative P(theta <= a) - P(theta > a); it is <= 0 for a below the median and >= 0 above => minimized at the median
derives_from: posterior_mean_rule
lean_status: core — the sign-change-at-the-median argument; instance check in instance-checks.bc

## Type / well-formedness check
An argmin: d/da E[|theta - a| | x] = P(theta < a | x) - P(theta > a | x), which changes sign at the median. The median minimizes expected absolute deviation -- the L^1 analogue of the mean minimizing expected squared deviation.

## Specialization / boundary cases
- a symmetric unimodal posterior: median = mean = mode, all three rules agree
- a right-skewed posterior (variance, rate parameters): posterior median < posterior mean -- the median is the more stable point summary
- check loss (quantile) generalization: L_tau(theta, a) = (tau - 1{theta < a})(theta - a) gives the tau-th posterior quantile

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: the rule needs only that the posterior has a median (always true) and finite E|theta| for the risk to be finite -- weaker than the posterior-mean rule's requirement

## Common misuse
- reporting a posterior median but a 'mean +- SD' credible interval -- mixing loss functions

## Related nodes (non-prerequisite)
- special_case_of: bayes_estimator

## Sources
berger_statistical_decision_theory
