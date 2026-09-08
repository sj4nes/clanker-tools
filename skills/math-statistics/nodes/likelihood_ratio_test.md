# likelihood_ratio_test

## Type
definition

## Statement
The (generalized) likelihood ratio test for H0: theta in Theta_0 rejects for small values of Lambda(x) = sup_{theta in Theta_0} L(theta; x) / sup_{theta in Theta} L(theta; x); equivalently for large -2 log Lambda.

## Symbols
- `Lambda in [0,1]` — how much the best null fit is beaten by the best overall fit
- `-2 log Lambda` — the deviance difference; its null distribution is asymptotically chi^2 (Wilks)

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
likelihood_function, maximum_likelihood_estimator, null_hypothesis

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
A general recipe (works for composite hypotheses and nuisance parameters). The exact null distribution of Lambda is problem-specific; the value of the test is that -2 log Lambda -> chi^2_r generically (wilks_theorem).

## Specialization / boundary cases
- N(mu, sigma^2), H0: mu = mu_0: -2 log Lambda is a monotone function of the t-statistic^2 -- the LRT IS the two-sided t-test
- H0: several regression coefficients are 0: -2 log Lambda ~ the F-test (exactly, under normal errors) or chi^2_q (asymptotically)
- multinomial goodness of fit: -2 log Lambda = 2 sum O_j log(O_j/E_j), the G-test, asymptotically chi^2 like Pearson's

## Hypothesis-dropped counterexamples
- **nested_models**: Lambda requires Theta_0 subset Theta (nested); comparing NON-nested models needs AIC / BIC / Vuong's test, not the LRT
- **regularity_for_the_chi2_limit**: if H0 is on the boundary of Theta (a variance component = 0) the chi^2_r calibration is wrong (mixture of chi^2's) -- true_parameter_interior again

## Common misuse
- using the chi^2 critical value for a boundary null (variance components, mixture number-of-components)
- applying the LRT to non-nested model selection
- trusting the chi^2 approximation at small n (the exact or bootstrap null distribution can differ substantially)

## In the wild
- the deviance and 'analysis of deviance' tables in every GLM package
- model comparison in phylogenetics, structural equation modeling, item response theory
- the profile-likelihood confidence interval is the LRT inverted (confidence_set_test_duality)

## Related nodes (non-prerequisite)
- uses: likelihood_function, maximum_likelihood_estimator
- required_by: wilks_theorem, pearson_chi_squared_gof
- special_case_of: 

## Sources
casella_berger_2e, lehmann_romano_tsh
