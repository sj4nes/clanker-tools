# james_stein

## Type
counterexample

## Statement
For X ~ N(theta, I_d) with d >= 3, the estimator theta_hat_JS = (1 - (d - 2)/||X||^2) X has strictly smaller total squared-error risk E||theta_hat - theta||^2 than the MLE theta_hat = X for EVERY theta. Hence X (the MLE, UMVUE, and minimax estimator) is inadmissible in dimension >= 3.

## Symbols
- `theta_hat_JS` — the James-Stein shrinkage estimator
- `(d - 2)/||X||^2` — the data-driven shrinkage factor -- shrinks X toward 0 (or toward any fixed point, or a subspace)
- `d` — the dimension; the effect is absent for d <= 2

## Epistemic status
counterexample  ·  regime: exact

## Prerequisites (tsort edges into this node)
admissibility, maximum_likelihood_estimator, mean_squared_error, prob_normal, risk_function

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: Stein's identity E[(X - theta) g(X)] = E[g'(X)] gives an unbiased estimate of the risk difference, which is negative for d >= 3
derives_from: mse_bias_variance_decomposition
lean_status: cited — CITED -- James-Stein 1961; Stein 1981 (SURE). The d=1 non-improvement and the risk-difference algebra are checked numerically in instance-checks.bc.

## Type / well-formedness check
A domination statement (a counterexample to admissibility of the MLE). Proof: Stein's unbiased risk estimate (SURE) gives E||theta_hat_JS - theta||^2 = d - E[(d-2)^2/||X||^2] < d. The (d-2) requires d >= 3 for the correction to help.

## Specialization / boundary cases
- d = 1, 2: no estimator dominates X -- shrinkage cannot uniformly help (the (d-2) factor is <= 0)
- the positive-part James-Stein max(0, 1 - (d-2)/||X||^2) X dominates the raw JS and is closer to admissible (still not admissible)
- shrinkage toward the grand mean, or toward a regression fit, works too -- the target is arbitrary

## Hypothesis-dropped counterexamples
- **d_at_least_3**: in d <= 2, X IS admissible -- the paradox is genuinely a high-dimensional phenomenon
- **the_loss_is_TOTAL_squared_error**: James-Stein improves the SUM of squared errors; a single coordinate's MSE can get WORSE. If you care about one coordinate, shrinkage can hurt you.

## Common misuse
- shrinking when you only care about one of the d parameters -- the improvement is in the aggregate, possibly at that coordinate's expense
- reading it as 'the MLE is bad' -- its total risk is d and JS's is only modestly less at most theta; the point is the EXISTENCE of uniform domination, overturning the sufficiency of unbiasedness/minimaxity

## In the wild
- empirical-Bayes shrinkage in genomics (limma / moderated t-statistics shrink thousands of gene-wise variances toward a common value), sports analytics (regress batting averages to the mean), and small-area estimation (Fay-Herriot) -- all are James-Stein in spirit
- the theoretical seed of ridge regression, LASSO, and every regularized high-dimensional estimator

## Related nodes (non-prerequisite)
- illustrated_by: prob_normal
- commonly_confused_with: admissibility
- historically_precedes: hastie_tibshirani_friedman_esl

## Sources
james_stein_1961, stein_1981, efron_large_scale_inference
