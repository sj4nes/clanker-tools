# mgf

## Type
definition

## Statement
The moment generating function of X is M_X(t) = E[e^{tX}], for those real t where the expectation is finite. If M_X is finite on an open interval around 0, it determines the law and all moments.

## Symbols
- `M_X` — the MGF, type: (subset of R) -> (0, inf]
- `t` — a real parameter, type: real

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
expectation, lotus

## Hypotheses
(none — unconditional within scope)

## Well-definedness
e^{tX} > 0 so E[e^{tX}] in (0, inf] is always defined; the set { t : M_X(t) < inf } is an interval containing 0.

## Type / well-formedness check
M_X(0) = 1 always; M_X(t) may be +inf for all t != 0 (e.g. Cauchy, lognormal). The useful hypothesis is 'M_X finite on (-h, h) for some h > 0' (X is then sub-exponential).

## Specialization / boundary cases
- X ~ N(mu, sigma^2): M_X(t) = exp(mu t + sigma^2 t^2 / 2), finite for all t
- X ~ Exponential(lambda): M_X(t) = lambda/(lambda - t) for t < lambda only
- X ~ Poisson(lambda): M_X(t) = exp(lambda(e^t - 1))

## Hypothesis-dropped counterexamples
- **finiteness_near_0**: X ~ Cauchy or lognormal: M_X(t) = inf for every t != 0, so the MGF carries no information -- use the characteristic function instead

## Common misuse
- assuming the MGF exists
- using it for heavy-tailed distributions where only the CF works
- concluding equality in law from agreement at finitely many t

## Related nodes (non-prerequisite)
- always_replaced_by: characteristic_function (which always exists)
- generates: moment (mgf_moments)
- multiplies: mgf_sum_independent

## Sources
billingsley_probability_measure, durrett_pte
