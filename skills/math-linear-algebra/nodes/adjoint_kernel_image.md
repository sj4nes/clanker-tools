# adjoint_kernel_image

## Type
theorem

## Statement
ker(T^*) = (im T)^perp and im(T^*) = (ker T)^perp. In matrix terms: null(A^T) = col(A)^perp and null(A) = row(A)^perp -- the four fundamental subspaces are TWO ORTHOGONAL PAIRS.

## Symbols
- `perp` — orthogonal complement in the relevant space

## Epistemic status
proved_theorem  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
adjoint_operator, four_subspaces, image_subspace, kernel, orthogonal_complement, orthogonal_decomposition

## Hypotheses
F = R or C, finite-dimensional

## Proof provenance
technique: w in ker T^* iff <v, T^*w> = 0 for all v iff <Tv, w> = 0 for all v iff w perp im T. The second identity follows by applying the first to T^* and using (T^*)^* = T plus orthogonal_decomposition
derives_from: adjoint_operator
lean_status: cited

## Type / well-formedness check
Well-formed over R or C only: it upgrades the dimension statement of four_subspaces (valid over any field) to an ORTHOGONALITY statement, which needs an inner product.

## Specialization / boundary cases
- A with full column rank: null(A) = {0}, so row(A) = F^n
- the consistency condition for Ax = b is exactly b perp null(A^T) -- the Fredholm alternative in finite dimension

## Hypothesis-dropped counterexamples
- **the_field_being_R_or_C**: over F_2 the 'orthogonal complement' of the span of (1,1) contains (1,1) itself, so the pair is not complementary. The DIMENSIONS from four_subspaces are still correct; the orthogonality is not. This node is precisely where the capsule's any_field results end and the real_or_complex ones begin
- **finite_dimensionality**: in infinite dimension one gets ker(T^*) = (im T)^perp with the CLOSURE of the image, so im(T^*) = (ker T)^perp requires closed range

## Common misuse
- stating 'the row space and null space are orthogonal complements' as a general-field fact
- using it for an operator with non-closed range in infinite dimension

## In the wild
- the Fredholm alternative: Ax = b is solvable iff b is orthogonal to every solution of A^Ty = 0 -- the standard consistency test
- the geometry of the four subspaces as taught in applied linear algebra

## Related nodes (non-prerequisite)
- required_by: least_squares, svd_four_subspaces, projection_matrix_characterisation

## Sources
strang_5e, axler_lada_4e
