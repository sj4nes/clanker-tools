# decision_rule

## Type
definition

## Statement
A decision rule delta maps the data to an action: delta: X^n -> A. Estimators (A = Theta) and tests (A = {accept, reject}) are decision rules; a randomized rule maps data to a distribution over A.

## Symbols
- `A` — the action space
- `randomized delta` — outputs a probability distribution over actions (needed for exact-size tests on discrete data)

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
estimator, test_function

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
The abstract object the whole theory optimizes. Placed AFTER estimator and test_function in the graph because those concrete instances motivate it (see conventions.md -- this is tsort order, not teaching order).

## Specialization / boundary cases
- an estimator theta_hat(.) is a decision rule with A = Theta
- a test phi(.) in [0,1] is a randomized decision rule with A = {0,1}
- 'always report 5' and 'flip a coin' are (bad) decision rules

## Hypothesis-dropped counterexamples
- **measurable**: a non-measurable rule has no well-defined risk -- excluded

## Common misuse
- restricting attention to nonrandomized rules when an exact-size test on discrete data requires randomization
- conflating the rule (a function) with its output on one dataset

## Related nodes (non-prerequisite)
- specializes_from: estimator, test_function
- required_by: risk_function

## Sources
berger_statistical_decision_theory, lehmann_romano_tsh
