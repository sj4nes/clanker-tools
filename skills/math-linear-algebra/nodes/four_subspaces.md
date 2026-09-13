# four_subspaces

## Type
theorem

## Statement
For A in F^{m x n} of rank r: dim row(A) = r and dim null(A) = n - r inside F^n; dim col(A) = r and dim null(A^T) = m - r inside F^m. The two pairs are complementary in dimension. ORTHOGONALITY of the pairs is a separate statement needing an inner product (adjoint_kernel_image).

## Symbols
- `r` — the rank of A

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
column_space, left_null_space, null_space, rank_nullity, row_rank_equals_column_rank, row_space

## Hypotheses
A in F^{m x n} of rank r

## Proof provenance
technique: row rank = column rank = r gives two of the four; rank_nullity applied to A and to A^T gives the other two
derives_from: row_rank_equals_column_rank
lean_status: core — LinAlg.four_subspace_dims

## Type / well-formedness check
Well-formed over ANY field, because it is purely a dimension count. Over a field with no inner product the four spaces still have these dimensions; they simply are not orthogonal to anything.

## Specialization / boundary cases
- A square invertible: r = n, both null spaces trivial, both row and column space all of F^n
- A = 0: r = 0, null(A) = F^n and null(A^T) = F^m

## Hypothesis-dropped counterexamples
- **orthogonality_is_not_part_of_this**: over F_2 the vector (1,1) satisfies x^T x = 0, so 'orthogonal complement' is degenerate and null(A) need not complement row(A) in the orthogonal sense. The DIMENSIONS are still right. Orthogonality genuinely requires R or C -- this is exactly why adjoint_kernel_image is a separate node with field_scope real_or_complex

## Common misuse
- stating the theorem as 'row space and null space are orthogonal complements' over a general field
- expecting dim col(A) = m: it is r, and equals m only for full row rank

## In the wild
- the four-subspace picture organises every solvability question: existence of a solution (b in col A), uniqueness (null A trivial), and the consistency conditions (null A^T)

## Related nodes (non-prerequisite)
- required_by: adjoint_kernel_image, svd_four_subspaces

## Sources
strang_5e
