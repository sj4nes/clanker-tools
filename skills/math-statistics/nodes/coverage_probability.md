# coverage_probability

## Type
definition

## Statement
The coverage probability of a confidence procedure C(.) at theta is beta_C(theta) = P_theta( theta in C(X) ); the procedure has confidence level 1 - alpha if inf_theta beta_C(theta) >= 1 - alpha.

## Symbols
- `beta_C(theta)` — coverage as a function of theta -- ideally flat at 1 - alpha

## Epistemic status
definition  ·  regime: exact

## Prerequisites (tsort edges into this node)
confidence_set

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
A function of theta, the CI analogue of a test's power function. 'Exact' procedures have beta_C(theta) = 1 - alpha for all theta; discrete data usually force beta_C(theta) > 1 - alpha somewhere (conservative) and it oscillates in theta.

## Specialization / boundary cases
- normal mean t-interval: beta_C(theta) = 1 - alpha exactly, for all (mu, sigma^2)
- binomial Clopper-Pearson: beta_C(p) >= 1 - alpha always, with sawtooth over-coverage
- binomial Wald: beta_C(p) oscillates and undershoots badly near the boundary

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: coverage is defined for any procedure; the content is whether inf_theta beta_C >= 1 - alpha

## Common misuse
- reporting the nominal level without checking actual coverage for discrete / small-sample / boundary problems
- averaging coverage over a prior and reporting that as 'the coverage' (that is a Bayesian, not frequentist, quantity)

## Related nodes (non-prerequisite)
- uses: confidence_set

## Sources
casella_berger_2e, brown_cai_dasgupta_2001
