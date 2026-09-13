# orthogonal_projection

## Type
construction

## Statement
For a finite-dimensional subspace U with orthonormal basis (e_1,...,e_k), P_U v = sum_i <v,e_i> e_i. It is linear, idempotent (P^2 = P), self-adjoint, has image U and kernel U^perp, and is INDEPENDENT of which orthonormal basis of U is used.

## Symbols
- `P_U` — type: element of L(V)
- `(e_i)` — any orthonormal basis of U

## Epistemic status
constructive_result  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
linear_map, orthogonality, orthonormal_basis, subspace

## Hypotheses
U finite-dimensional, (e_i) orthonormal basis of U

## Proof provenance
technique: idempotence and self-adjointness by direct computation with orthonormality; the basis-free characterisation gives well-definedness
derives_from: orthonormal_basis
lean_status: cited

## Well-definedness
Independent of the orthonormal basis: if (f_j) is another, both formulas produce the unique u in U with v - u orthogonal to U, and uniqueness follows since a difference would lie in U ∩ U^perp = {0}.

## Type / well-formedness check
The type check is the WELL-DEFINEDNESS check: the formula is written in terms of a chosen orthonormal basis, so independence of that choice must be verified. It follows because P_U v is characterised basis-free as the unique u in U with v - u in U^perp.

## Specialization / boundary cases
- U a line spanned by unit e: P_U v = <v,e> e, the familiar scalar projection
- U = V: P = I; U = {0}: P = 0
- I - P_U is the orthogonal projection onto U^perp

## Hypothesis-dropped counterexamples
- **orthonormality_of_the_basis**: with a merely independent basis (b_i) of U, sum <v,b_i> b_i is NOT the projection; the correct formula is B(B^*B)^{-1}B^* v, i.e. the hat_matrix, and the discrepancy is the inverse Gram matrix
- **orthogonality_versus_oblique**: a general idempotent P is an OBLIQUE projection along ker P, which need not be U^perp. Self-adjointness is exactly what makes a projection orthogonal (projection_matrix_characterisation)

## Common misuse
- using the orthonormal formula with a non-orthonormal spanning set
- assuming any idempotent matrix is an orthogonal projection

## In the wild
- fitted values in least squares; conditional expectation onto a sigma-algebra is the L^2 orthogonal projection, which is why E[Y|X] is the best mean-square predictor

## Related nodes (non-prerequisite)
- required_by: gram_schmidt, best_approximation, projection_matrix_characterisation, spectral_decomposition

## Sources
axler_lada_4e
