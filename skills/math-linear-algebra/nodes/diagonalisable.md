# diagonalisable

## Type
definition

## Statement
T is diagonalisable if V has a basis of eigenvectors of T; equivalently its matrix is A = PDP^{-1} with D diagonal. A property of the OPERATOR, not of any matrix representing it.

## Symbols
- `P` — the matrix whose COLUMNS are the eigenvectors
- `D` — diag(lambda_1,...,lambda_n)

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
basis, eigenvalue, similarity, triangular_matrix

## Hypotheses
V finite-dimensional
## Type / well-formedness check
Well-formed. The columns of P are the eigenvectors in the same order as the diagonal entries of D -- a correspondence that is easy to invert by mistake.

## Specialization / boundary cases
- D itself is diagonalisable with P = I
- any matrix with n distinct eigenvalues in F (distinct_eigenvalues_diagonalisable)
- every real symmetric matrix, with P ORTHOGONAL (spectral_theorem_symmetric) -- a much stronger conclusion

## Hypothesis-dropped counterexamples
- **existence_of_a_full_eigenbasis**: [[1,1],[0,1]] is not diagonalisable over ANY field
- **the_field**: [[0,-1],[1,0]] is not diagonalisable over R (no eigenvalues) but IS over C. Diagonalisability is field-relative
- **similarity_versus_orthogonal_similarity**: P is merely invertible here. Requiring P orthogonal is a strictly stronger property, available exactly for normal matrices

## Common misuse
- assuming P can be taken orthogonal for a general diagonalisable matrix: it can only for normal ones
- using A = PDP^{-1} to compute A^k without checking diagonalisability first

## In the wild
- A^k = PD^kP^{-1} makes powers, matrix exponentials, and the long-run behaviour of linear recurrences and Markov chains computable in closed form

## Related nodes (non-prerequisite)
- required_by: diagonalisability_criterion, spectral_theorem_symmetric

## Sources
axler_lada_4e, strang_5e
