# rank

## Type
definition

## Statement
rank T = dim(im T). DEFINED WITHOUT DETERMINANTS OR MINORS -- see edges/cycles.md, cycle 3.

## Symbols
- `rank T` — type: natural number (or cardinal), at most dim W and at most dim V

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
dimension, image_subspace

## Hypotheses
im T finite-dimensional
## Type / well-formedness check
Well-formed whenever im T is finite-dimensional, which holds automatically when V is (the image of a spanning set spans the image).

## Specialization / boundary cases
- T = 0: rank 0
- T an isomorphism: rank = dim V = dim W
- T a projection onto a k-dimensional subspace: rank k

## Hypothesis-dropped counterexamples
- **finite_dimensionality_of_the_image**: for an infinite-rank operator the number is a cardinal and the counting theorems below carry no content

## Common misuse
- defining rank by minors and then using it before determinants exist -- the minor characterisation is the downstream theorem determinant_rank_minors
- assuming rank(AB) = rank(A)rank(B): rank is not multiplicative, see rank_inequalities

## Related nodes (non-prerequisite)
- required_by: rank_nullity, matrix_rank

## Sources
axler_lada_4e
