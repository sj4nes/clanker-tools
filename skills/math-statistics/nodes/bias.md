# bias

## Type
definition

## Statement
The bias of theta_hat is b(theta) = E_theta[theta_hat] - theta (for an estimand g(theta): E_theta[theta_hat] - g(theta)).

## Symbols
- `b(theta)` — the bias, type: real (or R^d) function of theta
- `E_theta[theta_hat]` — the mean of the estimator's sampling distribution under P_theta

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
estimator, prob_expectation

## Hypotheses
(none — unconditional within scope)
## Well-definedness
Defined wherever the estimator has a finite mean.

## Type / well-formedness check
A function of theta. Requires E_theta|theta_hat| < inf. Zero bias for all theta is 'unbiased'. Bias is not invariant under nonlinear reparametrization (an unbiased estimator of theta gives a biased estimator of theta^2).

## Specialization / boundary cases
- S^2 (with n-1) is unbiased for sigma^2; the n-divisor version has bias -sigma^2/n
- the MLE of sigma^2 in a normal model is biased low by a factor (n-1)/n
- the MLE is generally biased at finite n but its bias is O(1/n), vanishing in the limit

## Hypothesis-dropped counterexamples
- **finite_mean**: the MLE of the Cauchy scale from n=1 observation, or any estimator with heavy-tailed sampling distribution, may have no mean and hence no bias -- 'unbiased' is then not even a well-posed question

## Common misuse
- chasing zero bias at the cost of large variance -- MSE is what matters, and a little bias often buys a big variance reduction (shrinkage, ridge)
- assuming an unbiased estimator of theta yields an unbiased estimator of a nonlinear function of theta

## Related nodes (non-prerequisite)
- required_by: mse_bias_variance_decomposition, unbiased_estimator, cramer_rao_lower_bound

## Sources
casella_berger_2e
