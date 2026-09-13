# orthonormal_basis

## Type
definition

## Statement
An orthonormal basis is a basis that is an orthonormal set. Relative to one, coordinates are simply <v, e_i>: no matrix inversion, and the change-of-basis matrix is UNITARY.

## Symbols
- `e_i` — the orthonormal basis vectors
- `<v,e_i>` — the i-th Fourier coefficient

## Epistemic status
definition  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
basis, induced_norm, orthogonal_implies_independent, orthogonality

## Hypotheses
V an inner product space
## Type / well-formedness check
Well-formed. The coordinate formula is the payoff: for a general basis, coordinates require solving a linear system; for an orthonormal one they are n inner products.

## Specialization / boundary cases
- the standard basis of F^n
- existence in every finite-dimensional inner product space is gram_schmidt
- the Fourier basis on L^2[0,2pi]: the infinite-dimensional analogue, where 'basis' means a convergent series, not a finite combination

## Hypothesis-dropped counterexamples
- **orthonormality**: for a general basis, v = sum <v,b_i> b_i is FALSE -- the correct coefficients come from the inverse Gram matrix (gram_matrix), and the discrepancy is exactly the failure of orthogonality
- **finite_dimensionality**: an orthonormal SET need not be a basis in infinite dimension even if maximal -- the algebraic and topological notions of basis diverge (see linear_combination)

## Common misuse
- using the coefficient formula <v, b_i> with a non-orthonormal basis -- the single most common error in applied projection work

## Related nodes (non-prerequisite)
- required_by: gram_schmidt, orthogonal_projection, parseval_identity, adjoint_operator

## Sources
axler_lada_4e
