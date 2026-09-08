# bootstrap

## Type
algorithm

## Statement
The (nonparametric) bootstrap approximates the sampling distribution of a statistic T_n = T(X_1,...,X_n) by the distribution of T_n* = T(X_1*, ..., X_n*), where X_1*, ..., X_n* are drawn iid from the empirical distribution P_hat_n (i.e. resampled with replacement from the data); this is estimated by Monte Carlo over B resamples.

## Symbols
- `T_n*` — the statistic recomputed on a resample
- `B` — the number of Monte Carlo resamples (500-10000 typically)
- `the plug-in idea` — replace the unknown P by P_hat_n in 'the sampling distribution of T under P'

## Epistemic status
constructive_result  ·  regime: distribution_free

## Prerequisites (tsort edges into this node)
empirical_cdf, plug_in_estimator

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: bootstrap_consistency (below): for Hadamard-differentiable T, the conditional law of sqrt(n)(T_n* - T_n) converges to the same limit as sqrt(n)(T_n - theta)
derives_from: bootstrap_consistency
lean_status: cited

## Type / well-formedness check
A resampling algorithm. Two error sources: the statistical approximation (P_hat_n for P) and the Monte Carlo approximation (B < inf). It works when T is a smooth functional of P (Hadamard-differentiable); it FAILS for non-smooth functionals (the max, a parameter on a boundary) and for statistics whose limit law depends on unknown nuisance parameters.

## Specialization / boundary cases
- bootstrap SE: the sample standard deviation of the B values T_n*
- percentile CI: the alpha/2 and 1 - alpha/2 empirical quantiles of the T_n* -- simple but first-order; BCa and bootstrap-t are second-order accurate
- the parametric bootstrap resamples from F(.; theta_hat) instead of P_hat_n -- useful when a model is trusted

## Hypothesis-dropped counterexamples
- **smooth_functional**: the maximum of a uniform(0, theta) sample: the bootstrap distribution of n(theta_hat - theta_hat*) does NOT converge to the true Exponential limit -- P(X_(n)* = X_(n)) -> 1 - 1/e, an atom that should not be there. The m-out-of-n bootstrap or subsampling fixes it.
- **limit_free_of_nuisance**: bootstrapping a non-studentized statistic when the limit variance is unknown gives poor coverage -- bootstrap the STUDENTIZED (pivotal) statistic (bootstrap-t)

## Common misuse
- percentile bootstrap CIs for a skewed statistic at small n (undercover) -- use BCa or bootstrap-t
- bootstrapping time-series or clustered data by resampling individual observations (destroys the dependence) -- use the block / cluster bootstrap
- too few resamples B for a tail quantile (B = 200 for a 95% CI endpoint is marginal)

## In the wild
- standard errors and CIs for statistics with no closed-form variance: medians, ratios, correlations, indirect effects in mediation analysis, complex survey estimators
- random forests and bagging ARE the bootstrap applied to prediction; out-of-bag error is a bootstrap cross-validation

## Related nodes (non-prerequisite)
- uses: plug_in_estimator, empirical_cdf
- required_by: bootstrap_consistency
- historically_precedes: 

## Sources
efron_1979, efron_tibshirani_bootstrap, davison_hinkley_bootstrap
