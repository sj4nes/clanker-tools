# subspace

## Type
definition

## Statement
A subset U of V is a subspace if 0 is in U and U is closed under addition and scalar multiplication. Equivalently, U is a vector space under the operations restricted from V.

## Symbols
- `U` — the subspace, type: subset of V closed under the operations

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
vector_space

## Hypotheses
V a vector space, U a subset of V
## Type / well-formedness check
Well-formed. Requiring 0 in U rather than merely U nonempty is equivalent GIVEN closure under scalar multiplication (take a = 0), but stating it explicitly rules out the empty set, which satisfies both closure conditions vacuously and is NOT a vector space.

## Specialization / boundary cases
- {0} and V are subspaces of V (the trivial ones)
- in R^3: the origin, every line through the origin, every plane through the origin, and R^3 -- and nothing else
- ker T and im T are subspaces, which is what makes rank and nullity dimensions

## Hypothesis-dropped counterexamples
- **containing_zero**: the empty set is closed under both operations vacuously but is not a vector space -- the axioms require an identity
- **closure_under_scalar_multiplication**: the first quadrant of R^2 is closed under addition but not under multiplication by -1
- **closure_under_addition**: the union of the two coordinate axes in R^2 is closed under scalar multiplication but (1,0) + (0,1) leaves it -- this is why subspace_intersection is about INTERSECTIONS, not unions

## Common misuse
- calling an affine subspace (a line NOT through the origin) a subspace -- solution sets of Ax = b are affine, not linear, unless b = 0; see linear_system

## Related nodes (non-prerequisite)
- required_by: span, kernel, image_subspace

## Sources
axler_lada_4e
