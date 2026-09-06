# conditional_expectation_elementary

## Type
definition

## Statement
For discrete Y, E[X | Y = y] = sum_x x P(X = x | Y = y) (or the density analogue integral x f_{X|Y}(x|y) dx), defined for y with P(Y = y) > 0 (resp. f_Y(y) > 0). The function y |-> E[X | Y = y] is g(y); then E[X | Y] := g(Y).

## Symbols
- `X` — an integrable random variable, type: L^1(P)
- `Y` — the conditioning variable, type: Omega -> R
- `g` — the regression function y |-> E[X|Y=y], type: R -> R

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
conditional_distribution, conditional_probability, expectation, pmf

## Hypotheses
(none — unconditional within scope)

## Well-definedness
for each y with positive mass/density, x |-> p_{X|Y}(x|y) is a probability distribution, so its mean g(y) is a well-defined number when E|X| < inf; the exceptional y-set is P_Y-null.

## Type / well-formedness check
the concrete, computational conditional expectation. E[X | Y] is a RANDOM VARIABLE (a function of Y); E[X | Y = y] is a NUMBER for each y. Matches the abstract E[X | sigma(Y)] where both are defined.

## Specialization / boundary cases
- X, Y independent: E[X | Y] = E[X] (constant)
- X = Y: E[X | Y] = Y
- bivariate normal: E[Y | X] = mu_Y + rho (sigma_Y/sigma_X)(X - mu_X) -- linear regression
- E[X | Y] is the best predictor of X from Y in mean square (conditional_expectation_l2_projection)

## Hypothesis-dropped counterexamples
- **positive_mass_or_density_at_y**: conditioning on { Y = y } with P(Y = y) = 0 and no joint density is ambiguous (Borel-Kolmogorov) -- needs the abstract construction
- **integrability_of_X**: E[X | Y = y] can fail to exist for each y if E|X| = inf

## Common misuse
- treating E[X | Y] as a number
- conditioning on a measure-zero value without a joint density
- assuming E[X | Y] is linear in Y (only for jointly normal or by construction)

## Related nodes (non-prerequisite)
- generalizes_to: conditional_expectation_abstract
- requires: conditional_distribution

## Sources
durrett_pte, grimmett_stirzaker
