# matrix_rank

## Type
definition

## Statement
rank A = dim col(A) = dim row(A) = the number of pivots in any echelon form of A = rank of the map x -> Ax.

## Symbols
- `rank A` — type: natural number, at most min(m, n)

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
column_space, dimension, pivot_columns, rank

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
Well-formed as a definite description because of row_rank_equals_column_rank and rref_uniqueness -- three descriptions, one number.

## Specialization / boundary cases
- rank A = 0 iff A = 0
- rank A = min(m,n): full rank
- rank of a rank-one matrix uv^T is 1 for nonzero u, v

## Hypothesis-dropped counterexamples
- **the_field**: rank is FIELD-DEPENDENT for a matrix with entries in a subfield: [[1,1],[1,1]] has rank 1 over Q and over F_2; but consider [[1,1],[1,-1]] -- rank 2 over Q, rank 1 over F_2 since -1 = 1 there. Always state the field
- **exact_arithmetic**: numerically, rank is decided by a singular-value threshold, not by exact vanishing (condition_number)

## Common misuse
- reporting a floating-point rank without a tolerance
- assuming rank(A+B) = rank A + rank B or rank(AB) = rank A * rank B -- see rank_inequalities

## Related nodes (non-prerequisite)
- required_by: rank_inequalities, invertibility_equivalences, singular_values

## Sources
strang_5e, horn_johnson_2e
