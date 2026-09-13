# char_poly_roots_are_eigenvalues

## Type
theorem

## Statement
lambda is an eigenvalue of A if and only if p_A(lambda) = 0. THE THEOREM JOINING the two independent definitions of eigenvalue and determinant (edges/cycles.md, cycle 1).

## Symbols
- `p_A(lambda)` — the characteristic polynomial evaluated at lambda, type: element of F

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
characteristic_polynomial, determinant_invertible_iff, eigenvalue, injective_iff_trivial_kernel

## Hypotheses
A square, V finite-dimensional

## Proof provenance
technique: Av = lambda v for some v != 0 iff ker(lambda I - A) != {0} iff lambda I - A is not injective iff not invertible (injective_surjective_equivalence) iff det(lambda I - A) = 0 (determinant_invertible_iff)
derives_from: determinant_invertible_iff
lean_status: cited

## Type / well-formedness check
Well-formed. The chain is: lambda is an eigenvalue iff (A - lambda I) has nontrivial kernel iff it is singular iff its determinant vanishes -- three separately proved equivalences composed.

## Specialization / boundary cases
- A triangular: the eigenvalues are exactly the diagonal entries
- n = 2: the eigenvalues are the roots of t^2 - tr(A)t + det(A), so they sum to tr(A) and multiply to det(A)

## Hypothesis-dropped counterexamples
- **finite_dimensionality**: the determinant does not exist for an operator on an infinite-dimensional space; spectral theory there is not polynomial
- **the_field**: p_A may have NO root in F (the real rotation), in which case A has no eigenvalue over F even though p_A exists and has degree n

## Common misuse
- using the characteristic polynomial to COMPUTE eigenvalues numerically: root-finding on p_A is catastrophically ill-conditioned (the Wilkinson polynomial). Practical algorithms (QR iteration) never form p_A
- concluding from deg p_A = n that there are n eigenvalues: there are n roots only WITH MULTIPLICITY and only over an algebraically closed field

## Related nodes (non-prerequisite)
- required_by: eigenvalue_existence_closed, invertibility_equivalences

## Sources
hoffman_kunze_2e, trefethen_bau
