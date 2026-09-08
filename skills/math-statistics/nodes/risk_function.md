# risk_function

## Type
definition

## Statement
The risk of a decision rule delta at theta is R(theta, delta) = E_theta[ L(theta, delta(X)) ]: the expected loss over repeated sampling under P_theta.

## Symbols
- `delta` — a decision rule, type: map data -> action
- `R(., delta)` — the risk function, type: nonnegative function on Theta

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
decision_rule, loss_function, prob_expectation

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
A frequentist average (over the data) of the loss, for each fixed theta. Two rules are compared by their whole risk FUNCTIONS -- which usually cross, so there is no universally best rule (hence admissibility, minimax, Bayes as ways to break the tie).

## Specialization / boundary cases
- squared-error loss: R(theta, delta) = MSE(theta) = Var + bias^2
- 0-1 loss in testing: R(theta, delta) = P_theta(wrong decision) -- the error probability
- the constant rule delta = c has R(theta) = L(theta, c), typically 0 at theta = c and large elsewhere

## Hypothesis-dropped counterexamples
- **expectation_exists**: a rule whose loss has infinite expectation under some theta (an estimator with infinite MSE) has undefined risk there and cannot be compared by risk

## Common misuse
- summarizing a risk FUNCTION by a single number without saying how (max? average against which weight?) -- that choice IS the minimax-vs-Bayes decision
- comparing risks at the observed data's implied theta_hat rather than as functions

## Related nodes (non-prerequisite)
- required_by: admissibility, minimax_rule, bayes_risk, james_stein
- specializes_to: mean_squared_error, power_function

## Sources
berger_statistical_decision_theory
