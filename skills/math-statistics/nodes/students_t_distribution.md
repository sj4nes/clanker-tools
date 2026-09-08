# students_t_distribution

## Type
construction

## Statement
Student's t distribution with k degrees of freedom is the law of T = Z / sqrt(V/k) where Z ~ N(0,1) is independent of V ~ chi^2_k. Symmetric, heavier-tailed than normal; E[T] = 0 for k > 1, Var(T) = k/(k-2) for k > 2.

## Symbols
- `k` — degrees of freedom
- `t_k` — the distribution; density proportional to (1 + t^2/k)^{-(k+1)/2}

## Epistemic status
constructive_result  ·  regime: exact

## Prerequisites (tsort edges into this node)
chi_squared_distribution, prob_independence_rv, prob_standard_normal

## Hypotheses
(none — unconditional within scope)
## Well-definedness
The ratio of a.s.-finite random variables with V > 0 a.s.; the density follows by a standard change of variables.

## Type / well-formedness check
A construction (ratio of independent N(0,1) and sqrt(chi^2_k / k)). Well-defined for k > 0. The independence of numerator and denominator is essential -- it is what Basu's theorem supplies for the one-sample t-statistic.

## Specialization / boundary cases
- k = 1: the standard Cauchy (no mean, no variance)
- k -> inf: t_k -> N(0,1) (V/k -> 1 by the LLN, then Slutsky)
- k = 2: E|T| < inf but Var = inf

## Hypothesis-dropped counterexamples
- **independence_Z_V**: if Z and V are dependent the ratio is not t-distributed -- the entire justification of the one-sample t-test rests on Xbar _||_ S^2 for a NORMAL sample (fails for non-normal data at small n)
- **V_is_chi_squared**: if V is a scaled chi^2 with the wrong df (correlated observations reducing the effective df) the nominal t_k reference is wrong and the test mis-calibrates

## Common misuse
- using t_k critical values for a small non-normal sample -- the numerator-denominator independence and the chi^2 denominator both fail; the t-test is only APPROXIMATELY valid via the CLT for large n
- forgetting Var(t_k) = k/(k-2) > 1 -- t intervals are wider than z intervals for a reason

## In the wild
- the one- and two-sample t-tests and the t confidence interval -- the most-used procedures in applied science
- regression coefficient t-tests (t_{n-p}); the t-copula in finance for tail dependence

## Related nodes (non-prerequisite)
- approximates: prob_standard_normal
- special_case_of: 
- required_by: t_statistic_distribution, coefficient_t_test

## Sources
casella_berger_2e, student_1908
