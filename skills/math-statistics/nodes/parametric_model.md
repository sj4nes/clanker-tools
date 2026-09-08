# parametric_model

## Type
definition

## Statement
A parametric model is a statistical model whose index set Theta is a subset of R^d for a fixed finite d; theta is the parameter.

## Symbols
- `d` — the (fixed, finite) dimension of the parameter, type: positive integer
- `theta` — a parameter value, type: point of Theta subset R^d

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
statistical_model

## Hypotheses
(none — unconditional within scope)
## Well-definedness
d is fixed in advance and does not depend on the sample size n.

## Type / well-formedness check
Theta must be a subset of a fixed R^d; 'finite-dimensional' is the whole content. Models with d growing with n, or infinite-dimensional nuisance parts, are semi-/non-parametric and out of scope.

## Specialization / boundary cases
- d = 1: a scalar parameter (Bernoulli p, Poisson lambda, exponential rate)
- d = 2: N(mu, sigma^2), Gamma(shape, rate), the simple linear model's (slope, intercept) with sigma^2 known
- Theta open: needed for the interior-point regularity condition later

## Hypothesis-dropped counterexamples
- **finite_fixed_dimension**: a location model with an unknown error density f is nonparametric in f; the CRLB and MLE-normality theory below does not apply to f without extra structure

## Common misuse
- counting the sample size or the number of observed categories as part of d
- treating a nonparametric functional (a density value, a quantile) as a 'parameter' with a Fisher information

## Related nodes (non-prerequisite)
- generalizes_from: statistical_model
- historically_precedes: kernel_density_estimator

## Sources
casella_berger_2e, van_der_vaart_asymptotic
