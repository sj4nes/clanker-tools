# eigenvalue_existence_closed

## Type
theorem

## Statement
Over an ALGEBRAICALLY CLOSED field, every operator on a nonzero finite-dimensional space has an eigenvalue. FALSE over R.

## Symbols
- `T` — an operator on V
- `dim V` — required nonzero and finite

## Epistemic status
proved_theorem  ·  field_scope: algebraically_closed

## Prerequisites (tsort edges into this node)
algebraically_closed_field, char_poly_roots_are_eigenvalues, characteristic_polynomial, finite_dimensional

## Hypotheses
F algebraically closed, 0 < dim V < infinity

## Proof provenance
technique: p_T has degree n >= 1, hence a root lambda in F by algebraic closedness; then char_poly_roots_are_eigenvalues. (Axler's determinant-free route: the n+1 vectors v, Tv, ..., T^n v are dependent, giving a polynomial annihilating v, which factors into linear terms)
derives_from: char_poly_roots_are_eigenvalues
lean_status: cited

## Type / well-formedness check
Well-formed. Both hypotheses are load-bearing and both have standing counterexamples; this node is the clearest instance of the capsule's field_scope tag doing real work.

## Specialization / boundary cases
- V = C^n: every complex square matrix has a complex eigenvalue
- dim V = 1: T is multiplication by a scalar, which IS the eigenvalue

## Hypothesis-dropped counterexamples
- **algebraic_closedness**: the real rotation [[0,-1],[1,0]] has no real eigenvalue. Every real operator on an ODD-dimensional space does have one (p_T has odd degree, hence a real root by the intermediate value theorem) -- so the failure is specifically an even-dimensional real phenomenon
- **finite_dimensionality**: the right shift on the space of sequences has no eigenvalue at all: Rx = lambda x forces x = 0. This is an infinite-dimensional operator over C, so algebraic closedness does not save it
- **nonzero_V**: on V = {0} there are no nonzero vectors, hence no eigenvectors

## Common misuse
- assuming a real matrix has real eigenvalues -- it does if it is SYMMETRIC (self_adjoint_real_eigenvalues), which is a different and stronger hypothesis
- applying it to differential or integral operators on function spaces

## Related nodes (non-prerequisite)
- required_by: schur_triangularisation
- illustrated_by: infinite_dimensional_boundary

## Sources
axler_lada_4e
