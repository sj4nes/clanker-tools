# spectral_theorem_symmetric

## Type
theorem

## Statement
A real symmetric A has an ORTHONORMAL basis of eigenvectors: A = Q D Q^T with Q orthogonal and D real diagonal. Equivalently a real matrix is orthogonally diagonalisable if and only if it is symmetric.

## Symbols
- `Q` — orthogonal, columns the orthonormal eigenvectors
- `D` — real diagonal of eigenvalues

## Epistemic status
proved_theorem  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
compactness_cited, diagonalisable, extreme_value_cited, finite_dimensional, induction_principle, invariant_subspace, orthogonal_decomposition, orthogonal_matrix, orthonormal_basis, rayleigh_quotient, real_number, self_adjoint_real_eigenvalues

## Hypotheses
A real symmetric, finite-dimensional

## Proof provenance
technique: induction on n. Existence of one eigenvector: R_A is continuous on the COMPACT unit sphere (compactness_cited), so it attains its maximum (extreme_value_cited) at some x, and a Lagrange/first-order argument shows Ax = R_A(x) x. Its eigenvalue is real by self_adjoint_real_eigenvalues. Then x^perp is A-invariant (because A is self-adjoint), A restricted to it is again symmetric, and the induction runs. ALTERNATIVE ROUTE not encoded as edges: complexify, apply schur_triangularisation, and note that a Hermitian triangular matrix is diagonal
derives_from: rayleigh_quotient
lean_status: instance — LinAlg.sym_spectral_instance (the 2x2 case worked explicitly). The general theorem is CITED: its Rayleigh/compactness step needs real analysis, unavailable Mathlib-free

## Type / well-formedness check
Well-formed over R. The converse direction is immediate ((QDQ^T)^T = QD^TQ^T = QDQ^T), so symmetry is exactly characterised -- an unusually clean iff.

## Specialization / boundary cases
- A diagonal already: Q = I
- A = [[2,1],[1,2]]: eigenvalues 3 and 1 with orthonormal eigenvectors (1,1)/sqrt2 and (1,-1)/sqrt2
- A a projection: D has only 0s and 1s, recovering projection_matrix_characterisation
- A a covariance matrix: this IS the principal component decomposition

## Hypothesis-dropped counterexamples
- **symmetry**: [[1,1],[0,1]] is not symmetric and is not diagonalisable at all; [[0,-1],[1,0]] is not symmetric and has no real eigenvalues. Both fail in different ways
- **realness_of_the_field**: the complex-symmetric [[1,i],[i,-1]] satisfies A^T = A over C and is NOT diagonalisable -- the correct complex hypothesis is Hermitian (spectral_theorem_normal)
- **finite_dimensionality**: for a self-adjoint operator on an infinite-dimensional Hilbert space there need be no eigenvectors at all (multiplication by x on L^2[0,1]); the spectral theorem becomes a statement about projection-valued measures, entirely outside this capsule

## Common misuse
- applying it to a non-symmetric matrix and expecting an orthogonal eigenbasis
- applying it to a complex symmetric matrix

## In the wild
- principal component analysis: the covariance matrix's orthonormal eigenbasis IS the set of principal directions, and the eigenvalues the explained variances
- normal modes of a conservative vibrating system; the diagonalisation of a quadratic form in constrained optimisation and in the second-derivative test
- the theorem math-statistics cites for quadratic forms in normal variables and for Cochran's theorem

## Related nodes (non-prerequisite)
- generalizes: 
- required_by: spectral_decomposition, psd_characterisations, singular_values, sylvester_law_of_inertia

## Sources
axler_lada_4e, horn_johnson_2e
