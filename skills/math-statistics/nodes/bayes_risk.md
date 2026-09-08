# bayes_risk

## Type
definition

## Statement
The Bayes risk of a rule delta under a prior pi is r(pi, delta) = int R(theta, delta) pi(dtheta) = E_pi E_theta[ L(theta, delta(X)) ]: the risk averaged over theta with weight pi.

## Symbols
- `pi` — the prior (a probability measure on Theta, or an improper measure with finite r)
- `r(pi, delta)` — a single number -- so Bayes risk TOTALLY orders the rules (unlike the risk function)

## Epistemic status
definition  ·  regime: bayesian

## Prerequisites (tsort edges into this node)
risk_function

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
A scalar summary of the risk function against a weighting pi. Minimizing it is what makes the Bayes rule well-defined and unique (a.s.). Different priors give different orderings.

## Specialization / boundary cases
- r(pi, delta) = E_X[ posterior expected loss at X ] -- the two-way expectation can be taken in either order (Fubini)
- the minimizer over delta is delta_pi, the Bayes rule (posterior-loss minimizer)
- sup_pi inf_delta r(pi, delta) = the minimax risk when a saddle point exists (minimax theorem)

## Hypothesis-dropped counterexamples
- **prior_proper_or_r_finite**: an improper prior with infinite Bayes risk gives no minimizer; 'generalized Bayes' rules (formal posterior mean) may still be admissible but are not Bayes in this sense

## Common misuse
- comparing Bayes risks computed under different priors as if on the same scale
- reporting the Bayes risk as the actual error -- it is an average over a hypothetical prior draw of theta

## Related nodes (non-prerequisite)
- required_by: bayes_rule_minimizes_bayes_risk
- uses: risk_function

## Sources
berger_statistical_decision_theory
