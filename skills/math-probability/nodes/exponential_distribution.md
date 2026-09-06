# exponential_distribution

## Type
definition

## Statement
X ~ Exponential(lambda), lambda > 0: density f_X(x) = lambda e^{-lambda x} for x >= 0. E[X] = 1/lambda, Var(X) = 1/lambda^2, M_X(t) = lambda/(lambda - t) for t < lambda. Memoryless.

## Symbols
- `X` — an exponential variable, type: Omega -> [0, inf)
- `lambda` — the rate, type: positive real

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
expectation, memorylessness, mgf, pdf, variance

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: normalization integral_0^inf lambda e^{-lambda x} dx = 1; E[X] = integral x lambda e^{-lambda x} dx = 1/lambda by parts; memorylessness from P(X > t) = e^{-lambda t}
derives_from: pdf
lean_status: core — validation/instance-checks.bc -- Exponential(0.5): E=2, Var=4, memoryless check

## Type / well-formedness check
the unique memoryless distribution on [0, inf): P(X > s + t | X > s) = P(X > t). The waiting time between events of a rate-lambda Poisson process; the continuous analogue of the geometric.

## Specialization / boundary cases
- lambda = 1: standard exponential; -log(U) for U ~ Uniform(0,1)
- min of independent Exponentials(lambda_i) ~ Exponential(sum lambda_i) -- competing risks
- sum of k iid Exponential(lambda) ~ Gamma(k, 1/lambda)

## Hypothesis-dropped counterexamples
- **memorylessness**: the Weibull, gamma (shape != 1), and lognormal are NOT memoryless -- using an exponential for aging components (increasing hazard) underestimates late failures
- **constant_hazard_rate**: f_X(x)/P(X > x) = lambda is constant; real lifetimes usually have a bathtub or increasing hazard

## Common misuse
- modeling component lifetimes with wear-out as exponential
- confusing the rate lambda with the mean 1/lambda

## Related nodes (non-prerequisite)
- discrete_analogue: geometric_distribution
- characterized_by: memorylessness
- sum_gives: gamma_distribution

## Sources
grimmett_stirzaker, durrett_pte
