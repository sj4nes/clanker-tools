# loss_function

## Type
definition

## Statement
A loss function L(theta, a) >= 0 gives the cost of taking action a when the true parameter is theta; L(theta, theta) is usually 0.

## Symbols
- `a` — an action / decision, type: element of the action space A (an estimate, or 'reject'/'accept')
- `L(theta, a)` — the loss, type: nonnegative real

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
parameter_space

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
A user-supplied function encoding the consequences of error. Squared error (theta - a)^2, absolute error |theta - a|, 0-1 loss 1{a != theta}, and the check (pinball) loss are the standard choices; the whole theory is relative to it.

## Specialization / boundary cases
- estimation: A = Theta, L = (theta - a)^2 or |theta - a|
- testing: A = {0, 1}, L(theta, a) = 1{a wrongly rejects/accepts} -- possibly weighted by how wrong
- asymmetric: newsvendor loss L(theta, a) = c_o (a - theta)_+ + c_u (theta - a)_+ for over/under-stocking

## Hypothesis-dropped counterexamples
- **loss_reflects_real_consequences**: using squared-error loss when the real cost is a step function (a dam either overtops or not) gives a Bayes rule optimizing the wrong thing

## Common misuse
- defaulting to squared-error loss without asking whether errors really cost the square of their size
- comparing procedures under one loss and deploying them where a different loss applies

## Related nodes (non-prerequisite)
- required_by: risk_function, bayes_estimator, posterior_mean_rule

## Sources
berger_statistical_decision_theory, lehmann_casella_tpe
