# induced_norm

## Type
definition

## Statement
||v|| = sqrt(<v,v>), well-defined because <v,v> is real and nonnegative. It satisfies ||v|| = 0 iff v = 0, ||av|| = |a| ||v||, and the triangle inequality.

## Symbols
- `||v||` — type: nonnegative real number
- `|a|` — modulus of the scalar

## Epistemic status
definition  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
inner_product, real_number

## Hypotheses
<.,.> an inner product
## Type / well-formedness check
Well-formed: the square root is of a nonnegative REAL, guaranteed by conjugate-symmetry (realness) and positive definiteness (nonnegativity). Both axioms are used just to make the definition type-check.

## Specialization / boundary cases
- F^n standard: ||x|| = sqrt(sum |x_i|^2), the Euclidean norm
- ||av|| = |a| ||v|| uses |a|, not a -- over C this matters: ||iv|| = ||v||

## Hypothesis-dropped counterexamples
- **positive_definiteness**: for an indefinite form sqrt(<v,v>) is not even real for some v (Minkowski again)
- **not_every_norm_is_induced**: the 1-norm and infinity-norm on R^2 are genuine norms but come from NO inner product -- they fail the parallelogram_law, which is exactly the characterisation

## Common misuse
- applying Cauchy-Schwarz or orthogonal projection in a normed space whose norm is not induced by an inner product (e.g. L^1) -- neither is available there

## Related nodes (non-prerequisite)
- required_by: cauchy_schwarz, orthonormal_basis, best_approximation, matrix_norms

## Sources
axler_lada_4e
