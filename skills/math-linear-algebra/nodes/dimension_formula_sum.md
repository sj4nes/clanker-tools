# dimension_formula_sum

## Type
theorem

## Statement
For finite-dimensional subspaces U, W of V: dim(U + W) = dim U + dim W - dim(U ∩ W). In particular the sum is direct iff dim(U + W) = dim U + dim W.

## Symbols
- `dim(U ∩ W)` — the overlap term, type: natural number

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
basis_existence_finite, dimension, finite_dimensional, subspace_intersection, sum_of_subspaces

## Hypotheses
U, W finite-dimensional subspaces

## Proof provenance
technique: take a basis of U ∩ W, extend it to a basis of U and separately to a basis of W; the union is a basis of U + W, and the count follows
derives_from: basis_existence_finite
lean_status: core — LinAlg.dim_sum_inter

## Type / well-formedness check
Well-formed; all four terms are finite by dimension_of_subspace. Often called the Grassmann formula, and it is the linear-algebra analogue of inclusion-exclusion for two sets.

## Specialization / boundary cases
- U ∩ W = {0}: recovers dim(U (+) W) = dim U + dim W
- two planes in R^3: 3 = 2 + 2 - 1, so they must meet in a line -- the standard non-obvious consequence
- U subset W: dim(U + W) = dim W and dim(U ∩ W) = dim U, so the identity is trivially true

## Hypothesis-dropped counterexamples
- **finite_dimensionality**: for infinite-dimensional subspaces the cardinal arithmetic degenerates (infinity + infinity = infinity) and the formula carries no information
- **two_summands**: the three-subspace analogue dim(U+W+X) = sum dim - sum dim(pairwise) + dim(triple) is FALSE. The x-axis, y-axis and diagonal in R^2 give 2 versus 1+1+1-0-0-0+0 = 3. Unlike sets, subspaces do not satisfy inclusion-exclusion beyond two terms

## Common misuse
- using an inclusion-exclusion formula for three or more subspaces (see above) -- this is the single most common error with this theorem

## In the wild
- the dimension count behind degrees of freedom in ANOVA decompositions and behind codimension arguments in constrained optimisation

## Sources
axler_lada_4e, halmos_fdvs
