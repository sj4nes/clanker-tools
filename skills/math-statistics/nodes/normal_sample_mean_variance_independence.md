# normal_sample_mean_variance_independence

## Type
theorem

## Statement
If X_1, ..., X_n are iid N(mu, sigma^2), then Xbar and S^2 are independent (and Xbar ~ N(mu, sigma^2/n)). This characterizes the normal: independence of Xbar and S^2 for all n holds ONLY for normal data.

## Symbols
- `Xbar _||_ S^2` — full statistical independence, not merely zero correlation

## Epistemic status
proved_theorem  ·  regime: exact

## Prerequisites (tsort edges into this node)
basu_theorem, linear_algebra_background, prob_independence_factorization, prob_normal, sample_mean, sample_variance

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: orthogonal (Helmert) transformation of a spherical Gaussian: Xbar and the residual vector lie in orthogonal subspaces, hence are independent; S^2 is a function of the residual vector alone
derives_from: basu_theorem
lean_status: instance — the Basu route is one line given completeness+ancillarity; the Helmert-rotation route's key fact (orthogonal linear images of N(0, sigma^2 I) are independent) is proof-checks.lean Stat.gaussian_orthogonal_independent for a fixed small n via the covariance being zero + joint normality

## Type / well-formedness check
An independence conclusion, exact and finite-sample. Three routes: (a) Basu -- Xbar is complete sufficient for mu (sigma^2 known), S^2 is ancillary for mu, so independent; (b) the orthogonal transformation of (X_1,...,X_n) whose first coordinate is sqrt(n) Xbar and whose remaining n-1 are independent N(0, sigma^2), with S^2 a function of only the latter; (c) geometry: Xbar is the projection onto the 1-vector, the residual vector is orthogonal, and orthogonal components of a spherical Gaussian are independent.

## Specialization / boundary cases
- n = 2: Xbar = (X_1 + X_2)/2 and S^2 = (X_1 - X_2)^2/2 are functions of the orthogonal pair (X_1 + X_2, X_1 - X_2), which are independent for a bivariate spherical normal
- gives the numerator-denominator independence in the t-statistic sqrt(n)(Xbar - mu)/S
- and the independence of the ANOVA / regression 'model' and 'error' sums of squares

## Hypothesis-dropped counterexamples
- **normality**: exponential sample: Xbar and S^2 are POSITIVELY correlated (both driven up by a large observation). The one-sample t-statistic is then not exactly t-distributed and the t-test's level is off at small n. Independence of Xbar and S^2 for all n is a *characterization* of the normal (Geary 1936, Lukacs 1942).

## Common misuse
- assuming Xbar _||_ S^2 (hence an exact t distribution) for skewed data at small n
- using it to claim Xbar _||_ S^2 for sigma^2 unknown via Basu without noting S^2 is not ancillary for sigma^2 -- the independence still holds, but by the rotation argument, not that particular Basu application

## In the wild
- the foundation of every exact normal-theory procedure: the t-test, the chi^2 variance interval, the ANOVA F-test, the regression t- and F-tests
- the historical trigger for 'Student' (Gosset) 1908 -- small-sample brewing quality control at Guinness

## Related nodes (non-prerequisite)
- proof_route: basu_theorem
- required_by: scaled_sample_variance_chi_squared, t_statistic_distribution, ols_distribution_under_normal_errors

## Sources
casella_berger_2e, student_1908, lukacs_1942
