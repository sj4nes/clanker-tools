# conditional_distribution

## Type
definition

## Statement
For jointly continuous (X, Y) with f_X(x) > 0, the conditional density of Y given X = x is f_{Y|X}(y | x) = f_{X,Y}(x, y) / f_X(x). The discrete analogue uses pmfs.

## Symbols
- `f_{Y|X}` — the conditional density, type: (R x R) -> [0, inf)
- `f_X` — the marginal density of X, type: R -> [0, inf)

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
joint_distribution, marginal_distribution, pdf

## Hypotheses
(none — unconditional within scope)

## Well-definedness
integral f_{Y|X}(y|x) dy = integral f_{X,Y}(x,y) dy / f_X(x) = f_X(x)/f_X(x) = 1 for a.e. x; the exceptional set { f_X = 0 } is P_X-null.

## Type / well-formedness check
for each fixed x with f_X(x) > 0, y |-> f_{Y|X}(y|x) is a genuine probability density (nonnegative, integrates to 1). Conditioning on the measure-zero event { X = x } is legitimate here because of the density; the general case needs conditional_expectation_abstract / regular conditional distributions.

## Specialization / boundary cases
- independence: f_{Y|X}(y|x) = f_Y(y), no dependence on x
- bivariate normal: Y | X = x is normal with mean mu_Y + rho (sigma_Y/sigma_X)(x - mu_X) -- the linear regression line
- (X,Y) uniform on the triangle 0 < y < x < 1: Y | X = x is Uniform(0, x)

## Hypothesis-dropped counterexamples
- **positive_marginal_density**: where f_X(x) = 0 the ratio is 0/0 -- conditioning on a value X never takes is undefined
- **existence_of_a_joint_density**: for singular joints (e.g. Y = X^2) there is no f_{X,Y}; conditioning requires the abstract construction (Borel-Kolmogorov paradox: the answer depends on how the conditioning event is approached)

## Common misuse
- conditioning on { X = x } without a joint density (Borel-Kolmogorov paradox)
- treating f_{Y|X}(y|x) as a function of x for fixed y as if it were a density in x

## Related nodes (non-prerequisite)
- requires: joint_distribution, marginal_distribution
- generalizes_to: conditional_expectation_abstract
- used_by: conditional_expectation_elementary

## Sources
durrett_pte, grimmett_stirzaker
