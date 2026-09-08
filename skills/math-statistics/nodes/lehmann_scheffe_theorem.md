# lehmann_scheffe_theorem

## Type
theorem

## Statement
If T is a complete sufficient statistic for theta and phi(T) is an unbiased estimator of g(theta), then phi(T) is the unique (a.s.) UMVUE of g(theta).

## Symbols
- `phi(T)` — any unbiased estimator that is a function of the complete sufficient statistic

## Epistemic status
proved_theorem  ·  regime: exact

## Prerequisites (tsort edges into this node)
completeness_statistic, rao_blackwell_theorem, umvue

## Hypotheses
completeness_statistic, sufficiency, unbiased_estimator

## Proof provenance
technique: any unbiased theta_tilde: Rao-Blackwell to E[theta_tilde | T], an unbiased function of T; completeness => it equals phi(T) a.s.; so phi(T) dominates every unbiased estimator
derives_from: rao_blackwell_theorem
lean_status: cited — the completeness step (difference of two unbiased functions of T is unbiased-of-zero, hence 0) is proof-checks.lean Stat.basu_step reused

## Type / well-formedness check
Combines Rao-Blackwell (improvement by conditioning on T) with completeness (there is at most one unbiased function of T, since the difference of two would be an unbiased estimator of 0). Gives both existence and uniqueness of the UMVUE.

## Specialization / boundary cases
- N(mu, sigma^2): (Xbar, S^2) complete sufficient => Xbar is the unique UMVUE of mu, S^2 of sigma^2
- uniform(0, theta): X_(n) complete sufficient => (n+1)/n X_(n) is the unique UMVUE of theta
- two routes to the UMVUE: (a) guess an unbiased function of T; (b) Rao-Blackwell any unbiased estimator onto T -- both give the same phi(T)

## Hypothesis-dropped counterexamples
- **completeness_statistic**: curved family N(theta, theta^2): sufficient statistic not complete; there is no UMVUE -- two unbiased estimators of theta exist with crossing variance functions
- **sufficiency**: an unbiased function of a complete-but-not-sufficient statistic is not improvable to the UMVUE by this route

## Common misuse
- applying it to a curved exponential family or a parameter-restricted model where completeness fails
- believing the UMVUE is therefore the best estimator -- it can be dominated in MSE by a biased rule

## Related nodes (non-prerequisite)
- strengthens: rao_blackwell_theorem
- uses: completeness_statistic

## Sources
lehmann_casella_tpe, casella_berger_2e
