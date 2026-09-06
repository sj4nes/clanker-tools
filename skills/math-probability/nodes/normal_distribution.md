# normal_distribution

## Type
definition

## Statement
X ~ N(mu, sigma^2), sigma > 0: density f_X(x) = (1/(sigma sqrt(2 pi))) exp(-(x - mu)^2 / (2 sigma^2)). E[X] = mu, Var(X) = sigma^2, M_X(t) = exp(mu t + sigma^2 t^2 / 2), phi_X(t) = exp(i mu t - sigma^2 t^2 / 2).

## Symbols
- `X` — a normal variable, type: Omega -> R
- `mu` — mean, type: real
- `sigma^2` — variance, type: positive real

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
abstract_integral, expectation, pdf, variance

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: normalization by the Gaussian integral integral e^{-x^2/2} dx = sqrt(2 pi); MGF by completing the square; E = mu, Var = sigma^2 from M''(0)
derives_from: abstract_integral
lean_status: core — validation/instance-checks.bc -- standard normal pdf integrates to 1, second moment 1

## Type / well-formedness check
parameterized by the VARIANCE sigma^2 (not sigma). The universal limit law (CLT), the maximum-entropy law for a given mean and variance, closed under affine maps and independent sums, and the only law where zero correlation implies independence (jointly).

## Specialization / boundary cases
- mu = 0, sigma = 1: standard normal Z; X = mu + sigma Z
- sum of independent normals is normal (variances add); the sample mean of iid normals is exactly normal
- 68-95-99.7 within 1-2-3 sigma; tail P(Z > z) approx phi(z)/z

## Hypothesis-dropped counterexamples
- **light_tails**: financial returns, network delays, and many natural quantities have heavier-than-Gaussian tails -- assuming normality drastically underestimates extreme-event probabilities (a 5-sigma event is ~1 in 3.5 million under normality, far more common in reality)
- **the_CLT_does_not_make_everything_normal**: the CLT needs iid-ish summands with finite variance; a single dominant term, heavy tails, or strong dependence breaks it

## Common misuse
- assuming normality for skewed or heavy-tailed data
- using sigma where sigma^2 is the parameter
- treating a large-sample CLT approximation as exact in the tails (Berry-Esseen: the error is O(1/sqrt n) and worst in the tails)

## Related nodes (non-prerequisite)
- standardizes_to: standard_normal
- closed_under: normal_affine_closure
- limit_in: central_limit_theorem

## Sources
billingsley_probability_measure, durrett_pte
