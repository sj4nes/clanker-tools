# pdf

## Type
definition

## Statement
The probability density function of an absolutely continuous X is f_X = dP_X/dlambda, the Radon-Nikodym derivative: P(X in B) = integral_B f_X dlambda. f_X >= 0 lambda-a.e. and integral_R f_X = 1.

## Symbols
- `f_X` — the density, type: R -> [0, inf), defined lambda-a.e.
- `P_X` — the law, type: probability measure << lambda

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
absolutely_continuous_rv, abstract_integral, radon_nikodym

## Hypotheses
(none — unconditional within scope)

## Well-definedness
existence and a.e.-uniqueness of f_X is exactly Radon-Nikodym for P_X << lambda; the normalization integral f_X = P_X(R) = 1.

## Type / well-formedness check
f_X is defined only up to a lambda-null set; f_X(x) is NOT a probability (it can exceed 1) but f_X(x) dx is an infinitesimal probability. Where F_X is differentiable, f_X = F_X'.

## Specialization / boundary cases
- Uniform(a,b): f_X = 1/(b-a) on [a,b]
- standard normal: f_X(x) = e^{-x^2/2}/sqrt(2 pi)
- Exponential(lambda): f_X(x) = lambda e^{-lambda x} for x >= 0

## Hypothesis-dropped counterexamples
- **absolute_continuity**: a discrete or singular X has no density; writing 'f_X' for them is a type error

## Common misuse
- treating f_X(x) as P(X = x)
- assuming f_X <= 1
- forgetting f_X is only an a.e. equivalence class (pointwise values are not meaningful without a continuity choice)

## Related nodes (non-prerequisite)
- requires: radon_nikodym
- analogue_of: pmf
- used_by: lotus, transformation_univariate, convolution_formula

## Sources
billingsley_probability_measure, folland_real_analysis
