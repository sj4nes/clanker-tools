# natural_parameter_space

## Type
definition

## Statement
The natural parameter space is H = { eta in R^k : int h(x) exp(eta . T(x)) dmu(x) < inf }; it is convex, and the family is 'full' if H is used in its entirety.

## Symbols
- `H` — the natural parameter space, type: convex subset of R^k
- `int(H)` — its interior, where A is analytic and all moments of T exist

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
exponential_family, ra_convex_function

## Hypotheses
(none — unconditional within scope)
## Well-definedness
H is determined by h, T, mu; convex and possibly all of R^k (Gaussian, Bernoulli) or a half-line (gamma with one parameter) or open (some heavy-carrier families).

## Type / well-formedness check
Convexity is by Holder's inequality. On int(H), A is C^infinity (indeed analytic) and E_eta|T|^m < inf for all m -- this is why exponential families are 'regular' with no fuss.

## Specialization / boundary cases
- Bernoulli: H = R (all eta give a finite sum)
- N(mu, sigma^2): H = R x (-inf, 0) -- the second natural parameter must be negative
- gamma(shape a, rate b), a known: H = (-inf, 0) in the rate's natural parameter -eta

## Hypothesis-dropped counterexamples
- **eta_in_interior**: at a boundary point of H (if the family is defined there) A may be finite but not differentiable, or E[T] infinite -- the moment identities and PD information fail. 'Full-rank' results need int(H).

## Common misuse
- assuming H = R^k -- for the normal-variance and gamma-rate parameters it is a half-space
- evaluating A' or A'' at a boundary eta

## Related nodes (non-prerequisite)
- required_by: cumulant_function, exponential_family_completeness

## Sources
brown_exponential_families
