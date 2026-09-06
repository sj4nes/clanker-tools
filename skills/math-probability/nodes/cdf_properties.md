# cdf_properties

## Type
theorem

## Statement
F_X is nondecreasing, right-continuous, with lim_{x -> -inf} F_X = 0 and lim_{x -> +inf} F_X = 1. Conversely, every function with these four properties is the CDF of some random variable.

## Symbols
- `F_X` — the CDF, type: R -> [0,1]

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
cdf, continuity_of_probability, limsup_liminf, sequence_limit

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: forward: monotonicity + continuity_of_probability on the nested half-lines. Converse: on ([0,1], B, lambda) set X(u) = inf{ t : F(t) >= u }; check { X <= x } = { u : u <= F(x) }, so P(X <= x) = F(x)
derives_from: continuity_of_probability
lean_status: cited — Billingsley Thm 12.4; Durrett Thm 1.2.2

## Type / well-formedness check
nondecreasing: monotonicity of P. Right-continuity and the limits: continuity of probability along { X <= x_n } for x_n decreasing to x (resp. to -inf, +inf). The converse builds X = F^{-1}(U) on ([0,1], lambda) via the quantile function.

## Specialization / boundary cases
- a pure-jump F (step function with jumps summing to 1): F_X of a discrete X
- F absolutely continuous: F(x) = integral_{-inf}^x f, X has density f
- the Cantor function: a continuous F with F' = 0 a.e. -- a singular continuous law, neither discrete nor absolutely continuous

## Hypothesis-dropped counterexamples
- **right_continuity**: a function that is left-continuous with jumps is not a CDF in this convention -- it would be x |-> P(X < x)
- **the_limit_conditions**: F(x) = arctan(x)/pi + 1/2 works; F(x) = arctan(x) does not reach 1 (defective / sub-probability distribution -- mass escapes to +inf)

## Common misuse
- forgetting a CDF can have both jumps and a density (mixed) or be singular continuous
- assuming F strictly increasing (it is flat wherever the law has no mass)

## Related nodes (non-prerequisite)
- used_by: convergence_in_distribution, probability_integral_transform
- characterizes: laws on R

## Sources
billingsley_probability_measure, durrett_pte
