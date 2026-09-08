# coefficient_t_test

## Type
proposition

## Statement
In the Gaussian linear model, (beta_hat_j - beta_j^0) / se(beta_hat_j) ~ t_{n-p} exactly, where se(beta_hat_j) = sigma_hat sqrt( ((X^T X)^{-1})_jj ); the test of H0: beta_j = 0 rejects when |t_j| > t_{n-p, 1-alpha/2}, and Xbar +- t_{n-p,1-alpha/2} se is an exact CI for beta_j.

## Symbols
- `se(beta_hat_j) = sigma_hat sqrt((X^T X)^{-1}_jj)` — the reported standard error
- `t_{n-p}` — n - p residual degrees of freedom

## Epistemic status
proposition  ·  regime: exact

## Prerequisites (tsort edges into this node)
ols_distribution_under_normal_errors, students_t_distribution, unbiased_error_variance_estimator

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: ols_distribution_under_normal_errors supplies numerator normality, denominator chi^2_{n-p}, and their independence; assemble t_{n-p}
derives_from: t_statistic_distribution
lean_status: core

## Type / well-formedness check
Exact under the Gaussian linear model. The numerator ~ N(0, sigma^2 (X^TX)^{-1}_jj) is independent of sigma_hat^2, and (n-p)sigma_hat^2/sigma^2 ~ chi^2_{n-p}, so the ratio is exactly t_{n-p} (assemble the t definition).

## Specialization / boundary cases
- the 't value' and 'Pr(>|t|)' columns of every regression summary table
- one predictor of interest, others as controls: t_j tests the PARTIAL effect (holding the other X fixed) -- Frisch-Waugh (partitioned_regression)
- as n - p grows, t_{n-p} -> N(0,1) and the t-test approaches the Wald z-test

## Hypothesis-dropped counterexamples
- **gaussian_errors**: with non-normal errors the exact t_{n-p} calibration is lost; for large n - p and bounded leverage it is asymptotically valid (t -> N(0,1) via the CLT for beta_hat)
- **homoskedasticity**: heteroskedastic errors make se(beta_hat_j) wrong -- use HC (White) robust SEs; the point estimate beta_hat_j stays unbiased
- **no_collinearity**: near-collinear predictors inflate ((X^TX)^{-1})_jj (the variance inflation factor), giving large SEs and unstable, individually-non-significant coefficients even when the group is jointly significant

## Common misuse
- reading a non-significant coefficient as 'no effect' when collinearity has inflated its SE (check the joint F-test and the VIFs)
- interpreting beta_hat_j in isolation when the other predictors would necessarily change with x_j
- multiple coefficient tests without multiplicity adjustment

## In the wild
- the near-universal way effects are judged 'significant' in observational research and covariate-adjusted experiments

## Related nodes (non-prerequisite)
- uses: ols_distribution_under_normal_errors, students_t_distribution, unbiased_error_variance_estimator
- special_case_of: overall_f_test

## Sources
seber_lee_linear_regression, weisberg_applied_linear_regression
