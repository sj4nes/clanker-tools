# minimax_rule

## Type
definition

## Statement
A rule delta* is minimax if it minimizes the worst-case risk: sup_theta R(theta, delta*) = inf_delta sup_theta R(theta, delta).

## Symbols
- `sup_theta R(theta, delta)` — the maximum risk of delta -- its worst case over Theta

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
risk_function

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
The rule with the best guarantee against an adversarial Nature. Often found as a Bayes rule against a 'least favorable' prior (the prior that makes the Bayes risk largest); minimax = Bayes vs least-favorable prior when a saddle point exists.

## Specialization / boundary cases
- N(theta, 1) known variance, Theta = R: Xbar is minimax (constant risk 1/n, and it is Bayes vs the flat improper prior limit)
- Bernoulli(p), Theta = [0,1], squared-error loss: the minimax estimator is (sum X_i + sqrt(n)/2) / (n + sqrt(n)) -- a Beta(sqrt(n)/2, sqrt(n)/2) Bayes rule, with constant risk
- bounded normal mean |theta| <= tau: the minimax rule is nonlinear and shrinks toward 0

## Hypothesis-dropped counterexamples
- **Theta_bounded_or_risk_controlled**: if Theta is unbounded and risk is unbounded, sup_theta R can be infinite for every rule and 'minimax' is degenerate -- restrict Theta or the loss

## Common misuse
- choosing minimax when the worst case is implausible -- it can be very conservative, paying everywhere to protect against a corner of Theta
- assuming the minimax rule has constant risk -- it need not, though many do

## Related nodes (non-prerequisite)
- uses: risk_function, bayes_risk
- commonly_confused_with: local_asymptotic_minimax

## Sources
berger_statistical_decision_theory, lehmann_casella_tpe
