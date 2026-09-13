# block_matrix

## Type
definition

## Statement
A matrix partitioned into submatrix blocks. Conformably partitioned blocks multiply by the same formula as entries: (AB)_{ij} = sum_k A_{ik}B_{kj} with the products now matrix products, IN THAT ORDER.

## Symbols
- `A_{ik}` — a BLOCK, type: submatrix

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
index_convention, matrix, matrix_multiplication

## Hypotheses
conformable partitions
## Type / well-formedness check
Well-formed when the column partition of the left factor matches the row partition of the right. The order within each block product matters, since block entries do not commute -- unlike scalars.

## Specialization / boundary cases
- block diagonal: the product is block diagonal with the blocks multiplied separately
- block upper triangular: det is the product of the diagonal blocks' determinants

## Hypothesis-dropped counterexamples
- **block_commutativity**: the scalar 2x2 determinant formula ad - bc becomes AD - CB or AD - BC or ... none of which is generally right: det[[A,B],[C,D]] = det(AD - CB) requires C and D to COMMUTE. The correct general statement uses the schur_complement
- **conformability**: ill-typed otherwise

## Common misuse
- applying the 2x2 determinant formula to blocks without a commutativity hypothesis (see above) -- a very common error

## Related nodes (non-prerequisite)
- required_by: schur_complement

## Sources
horn_johnson_2e
