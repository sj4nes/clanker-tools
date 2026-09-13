# leibniz_formula

## Type
theorem

## Statement
det A = sum_{sigma in S_n} sgn(sigma) prod_{i=1}^n A_{i, sigma(i)}. A THEOREM identifying the unique normalised alternating form, not the definition.

## Symbols
- `sigma` — a permutation, type: element of S_n
- `n!` — the number of terms

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
determinant, determinant_existence_uniqueness, permutation_sign

## Hypotheses
A square

## Proof provenance
technique: this is exactly the formula produced by the uniqueness argument of determinant_existence_uniqueness
derives_from: determinant_existence_uniqueness
lean_status: cited

## Type / well-formedness check
Well-formed; the sum has n! terms, each a product of n entries, one from each row and each column.

## Specialization / boundary cases
- n = 2: two terms, ad - bc
- n = 3: six terms
- A triangular: only sigma = id contributes a nonzero product (determinant_triangular)

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: an identity for square A over any field

## Common misuse
- using it as an ALGORITHM: n! terms is catastrophic (20! exceeds 10^18). Compute determinants by elimination in O(n^3) via determinant_row_operations and determinant_triangular
- assuming the formula is the definition, which obscures why det is multiplicative

## Related nodes (non-prerequisite)
- required_by: determinant_transpose, determinant_triangular, laplace_expansion

## Sources
hoffman_kunze_2e
