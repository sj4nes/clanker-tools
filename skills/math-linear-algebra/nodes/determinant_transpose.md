# determinant_transpose

## Type
theorem

## Statement
det(A^T) = det(A) for every square A over any field. Consequently every row statement about determinants has an identical column statement.

## Symbols
- `A^T` — the transpose

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
determinant, leibniz_formula, permutation_sign, transpose

## Hypotheses
A square

## Proof provenance
technique: in the Leibniz sum, reindex by sigma^{-1}: prod_i A_{i,sigma(i)} = prod_j A_{sigma^{-1}(j), j}, and sgn(sigma^{-1}) = sgn(sigma)
derives_from: leibniz_formula
lean_status: dim_core — LinAlg.det_transpose (n = 2)

## Type / well-formedness check
Well-formed. The result is not obvious from the definition, which privileges COLUMNS; it is what makes the row/column asymmetry of the setup disappear.

## Specialization / boundary cases
- A symmetric: the statement is trivially true
- the reason 'det A != 0 iff the ROWS are independent' and 'iff the COLUMNS are independent' are the same criterion

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: true for every square matrix over every field. Over a noncommutative ring it fails, which is one reason determinants are a commutative-algebra notion

## Common misuse
- assuming the analogous det(A^*) = det(A) over C: in fact det(A^*) = conj(det A), so det(A^*A) = |det A|^2 is real and nonnegative -- a fact used constantly for Gram determinants

## Related nodes (non-prerequisite)
- required_by: determinant_multiplicative

## Sources
hoffman_kunze_2e
