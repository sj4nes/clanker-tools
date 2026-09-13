# row_rank_equals_column_rank

## Type
theorem

## Statement
dim row(A) = dim col(A) for every A in F^{m x n}, over any field. This common value is rank A.

## Symbols
- `rank A` — the common value

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
column_space, matrix_rank, pivot_columns, row_space, rref_uniqueness

## Hypotheses
F a field

## Proof provenance
technique: via RREF: row operations preserve row(A) exactly, and preserve the dependence relations among columns, so both counts equal the number of pivots. (Alternative: the rank factorisation A = CR with C of full column rank exhibits both ranks as the inner dimension.)
derives_from: rref_uniqueness
lean_status: cited

## Type / well-formedness check
Well-formed, and non-obvious: the two spaces live in DIFFERENT ambient spaces (F^n and F^m) and are usually not isomorphic in any canonical way. Only their dimensions coincide.

## Specialization / boundary cases
- A a column vector: both ranks are 1 unless A = 0
- A = [[1,2],[2,4]]: rank 1 both ways, though row(A) is spanned by (1,2) in F^2 and col(A) by (1,2)^T in F^2 -- here they coincide only because A is symmetric

## Hypothesis-dropped counterexamples
- **F_a_field**: over a commutative ring the notion of rank splits into several inequivalent ones (McCoy rank, determinantal rank) and this equality can fail
- **the_spaces_are_not_equal**: for A = [[1,1],[0,0]], row(A) is spanned by (1,1) while col(A) is spanned by (1,0)^T -- equal dimension, different subspaces

## Common misuse
- concluding row(A) = col(A) from the theorem: it asserts equality of DIMENSIONS only
- assuming it is obvious -- it is the one genuinely surprising elementary theorem in the subject

## In the wild
- the reason the number of independent equations equals the number of independent unknowns-directions in a linear system, hence the basis of every degrees-of-freedom count

## Related nodes (non-prerequisite)
- required_by: four_subspaces, matrix_rank

## Sources
hoffman_kunze_2e, strang_5e
