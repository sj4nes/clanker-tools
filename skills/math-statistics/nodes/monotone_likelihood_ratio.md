# monotone_likelihood_ratio

## Type
hypothesis

## Statement
A family { f(x; theta) } has monotone likelihood ratio in a statistic T(x) if for every theta_1 > theta_0 the ratio f(x; theta_1) / f(x; theta_0) is a nondecreasing function of T(x).

## Symbols
- `T(x)` — the statistic in which the ratio is monotone -- the natural sufficient statistic in an exponential family

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
likelihood_function

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
An ordering condition on the family. It is what upgrades 'most powerful for a simple alternative' (Neyman-Pearson) to 'UNIFORMLY most powerful for a one-sided composite alternative' (Karlin-Rubin).

## Specialization / boundary cases
- every one-parameter exponential family with natural statistic T has MLR in T (the ratio is exp((eta_1 - eta_0) T - (A(eta_1) - A(eta_0))), increasing in T since eta_1 > eta_0)
- N(theta, 1) in T = Xbar; Bernoulli(theta) in T = sum X_i; Uniform(0, theta) in T = X_(n) (a non-exponential-family example with MLR)
- the noncentral t and noncentral chi^2 families have MLR in their natural statistics

## Hypothesis-dropped counterexamples
- **MLR_holds**: the Cauchy location family does NOT have MLR -- the likelihood ratio is not monotone, there is no UMP one-sided test, and the one-sided testing problem genuinely has no best solution
- **two_sided**: MLR gives UMP tests only for ONE-SIDED hypotheses; for H0: theta = theta_0 vs H1: theta != theta_0 even an MLR family has no UMP test

## Common misuse
- assuming a UMP one-sided test exists for a family whose MLR has not been checked
- expecting MLR to deliver a UMP two-sided test

## Related nodes (non-prerequisite)
- required_by: karlin_rubin_theorem
- uses: likelihood_function

## Sources
lehmann_romano_tsh, karlin_rubin_1956
