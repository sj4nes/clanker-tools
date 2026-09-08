# estimator

## Type
definition

## Statement
An estimator of theta (or of a derived quantity g(theta)) is a statistic theta_hat = theta_hat(X_1,...,X_n) taking values in the parameter space (or the range of g), used as a guess for the unknown quantity.

## Symbols
- `theta_hat` — the estimator, type: statistic valued in Theta
- `theta_hat(x)` — the estimate, its realized value on data x
- `g(theta)` — an estimand -- a function of theta one may target instead of theta itself

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
parameter_space, statistic

## Hypotheses
(none — unconditional within scope)
## Well-definedness
Any statistic valued in the right space qualifies; quality is assessed by risk / bias / variance / consistency.

## Type / well-formedness check
An estimator is a function (a rule); an estimate is a number (its output). Its sampling distribution is induced by the law of X and depends on theta. No optimality is built in -- 'the constant 7' is an estimator.

## Specialization / boundary cases
- Xbar as an estimator of a population mean
- the MLE, the method-of-moments estimator, a Bayes posterior mean -- all estimators
- an estimator of g(theta) need not be g(theta_hat) (that can be biased -- Jensen)

## Hypothesis-dropped counterexamples
- **valued_in_the_parameter_space**: an 'estimator' of a variance that can return negative values (a naive ANOVA variance-component estimate) is ill-posed as a point in Theta = (0, inf); it must be truncated or the model rethought

## Common misuse
- reporting an estimate without a standard error or interval -- a point with no uncertainty statement
- choosing an estimator by its performance on the observed sample (that is overfitting the estimator to the data)

## Related nodes (non-prerequisite)
- specializes_from: statistic
- specializes_to: unbiased_estimator, maximum_likelihood_estimator, bayes_estimator

## Sources
casella_berger_2e
