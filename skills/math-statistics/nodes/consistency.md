# consistency

## Type
definition

## Statement
A sequence of estimators theta_hat_n is (weakly) consistent for theta if theta_hat_n -> theta in P_theta-probability as n -> inf, for every theta; strongly consistent if the convergence is almost sure.

## Symbols
- `theta_hat_n` — the estimator based on a sample of size n
- `-> in probability` — the mode of convergence (prob_conv_p)

## Epistemic status
definition  ·  regime: asymptotic

## Prerequisites (tsort edges into this node)
estimator, iid_sample, prob_chebyshev_ineq, prob_conv_p

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: typically: a law of large numbers for the estimating equation plus continuity (or: Var -> 0 and bias -> 0, via Chebyshev)
derives_from: prob_wlln
lean_status: cited — the Chebyshev route (Var -> 0, bias -> 0 => consistency) is the finitary core in proof-checks.lean Stat.consistency_chebyshev

## Type / well-formedness check
An asymptotic (n -> inf) property; says nothing about any fixed n. 'For every theta' matters -- an estimator can be consistent at some theta and not others.

## Specialization / boundary cases
- Xbar is (strongly) consistent for the mean whenever E|X_1| < inf (SLLN)
- S^2 is consistent for sigma^2 when E X_1^4 < inf
- the sample maximum is consistent for theta in uniform(0, theta), at rate n

## Hypothesis-dropped counterexamples
- **finite_mean**: Xbar for iid Cauchy: NOT consistent for the median theta -- Xbar is again Cauchy(theta, 1) for every n and never concentrates. The sample median IS consistent.
- **for_every_theta**: an estimator hard-coded to return theta_0 is consistent AT theta_0 only; it is inconsistent everywhere else

## Common misuse
- treating consistency as a finite-sample guarantee -- it bounds nothing at the n you have
- confusing consistency (concentration at theta) with unbiasedness (correct mean); neither implies the other

## Related nodes (non-prerequisite)
- strengthened_by: asymptotic_normality_estimator
- required_by: mle_asymptotic_normality

## Sources
van_der_vaart_asymptotic, casella_berger_2e
