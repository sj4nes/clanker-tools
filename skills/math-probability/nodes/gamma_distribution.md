# gamma_distribution

## Type
definition

## Statement
X ~ Gamma(k, theta), shape k > 0, scale theta > 0: density f_X(x) proportional to x^{k-1} e^{-x/theta} on x > 0 (normalizer Gamma(k) theta^k). E[X] = k theta, Var(X) = k theta^2. For integer k it is the sum of k iid Exponential(1/theta).

## Symbols
- `X` — a gamma variable, type: Omega -> (0, inf)
- `k` — shape, type: positive real
- `theta` — scale, type: positive real

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
convolution_formula, expectation, exponential_distribution, iid, pdf, variance

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: for integer k, convolution_formula on k iid Exponential(1/theta); E and Var by k-fold sum of the exponential's 1/lambda and 1/lambda^2. General k via the Gamma-function integral
derives_from: convolution_formula
lean_status: cited — Grimmett-Stirzaker 4.14

## Type / well-formedness check
the flexible right-skewed family on (0, inf): shape k < 1 gives a pole at 0, k = 1 is exponential, k large approaches normal. Closed under sums with common scale (shapes add). Rate parameterization uses beta = 1/theta.

## Specialization / boundary cases
- k = 1: Exponential(1/theta)
- Gamma(k, 2) with 2k = nu integer: chi-squared with nu degrees of freedom
- conjugate prior for the rate of a Poisson / the precision of a normal
- k -> inf: (X - k theta)/sqrt(k theta^2) -> N(0,1)

## Hypothesis-dropped counterexamples
- **common_scale_for_the_sum_rule**: Gamma(k_1, theta_1) + Gamma(k_2, theta_2) with theta_1 != theta_2 is NOT gamma -- the sum rule needs a shared scale
- **shape_and_scale_vs_shape_and_rate**: software differs; mixing them scales the mean by theta^2

## Common misuse
- adding gammas with different scales
- confusing scale theta with rate 1/theta

## Related nodes (non-prerequisite)
- sum_of: exponential_distribution
- special_case: chi-squared, Erlang
- conjugate_to: Poisson rate, normal precision

## Sources
grimmett_stirzaker, durrett_pte
