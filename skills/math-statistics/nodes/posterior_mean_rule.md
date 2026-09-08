# posterior_mean_rule

## Type
theorem

## Statement
Under squared-error loss L(theta, a) = (theta - a)^2, the Bayes estimator is the posterior mean: delta_pi(x) = E[theta | X = x].

## Symbols
- `E[theta | x]` — the mean of the posterior distribution

## Epistemic status
proved_theorem  ·  regime: bayesian

## Prerequisites (tsort edges into this node)
bayes_estimator, loss_function, prob_conditional_expectation

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: E[(theta - a)^2 | x] = Var(theta | x) + (E[theta|x] - a)^2; the first term is free of a, the second is minimized (to 0) at a = E[theta | x]
derives_from: prob_conditional_expectation
lean_status: core — validation/proof-checks.lean Stat.posterior_mean_completes_square -- E[(t - a)^2] = E[(t - Et)^2] + (Et - a)^2, minimized at a = E t; identical to Stat.mse_decomp

## Type / well-formedness check
An argmin computed by completing the square: E[(theta - a)^2 | x] = Var(theta | x) + (E[theta | x] - a)^2, minimized at a = E[theta | x]. Same algebra as the bias-variance decomposition and the L^2-projection property of conditional expectation.

## Specialization / boundary cases
- Beta-Bernoulli: prior Beta(alpha, beta), data sum x_i = s in n trials => posterior Beta(alpha + s, beta + n - s), posterior mean (alpha + s)/(alpha + beta + n) -- a shrunk version of s/n toward the prior mean
- Normal-Normal: prior N(mu_0, tau^2), data Xbar with known sigma^2/n => posterior mean is a precision-weighted average of mu_0 and Xbar
- as n -> inf the posterior mean -> the MLE (Bernstein-von Mises)

## Hypothesis-dropped counterexamples
- **posterior_mean_exists**: heavy-tailed posterior (Cauchy prior + one observation): E[theta | x] is undefined; the posterior-median rule (absolute loss) still works
- **squared_loss_appropriate**: if over- and under-estimation have different costs (inventory, dosing) the posterior mean is the wrong summary -- use the rule for the actual asymmetric loss

## Common misuse
- reporting the posterior mean for a skewed posterior when the posterior median or mode better represents 'the estimate'
- forgetting that the posterior mean is a shrinkage estimator -- it is deliberately biased toward the prior

## Related nodes (non-prerequisite)
- special_case_of: bayes_estimator
- uses: prob_conditional_expectation
- commonly_confused_with: p_value

## Sources
berger_statistical_decision_theory, casella_berger_2e
