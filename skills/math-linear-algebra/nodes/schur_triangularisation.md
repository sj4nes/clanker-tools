# schur_triangularisation

## Type
theorem

## Statement
Over C, every A in C^{n x n} is UNITARILY similar to an upper triangular matrix: A = QTQ^* with Q unitary and T upper triangular, whose diagonal carries the eigenvalues of A in any prescribed order.

## Symbols
- `Q` — unitary
- `T` — upper triangular, type: element of C^{n x n}

## Epistemic status
proved_theorem  ·  field_scope: algebraically_closed

## Prerequisites (tsort edges into this node)
eigenvalue_existence_closed, fundamental_theorem_of_algebra, gram_schmidt, induction_principle, invariant_subspace, orthogonal_matrix, orthonormal_basis

## Hypotheses
F = C (or any algebraically closed field, without the unitary clause)

## Proof provenance
technique: induction on n: take an eigenvector by eigenvalue_existence_closed, normalise it, extend to an orthonormal basis by gram_schmidt; in that basis A is block [[lambda, *],[0, A']], and the invariant subspace structure lets the induction run on A'
derives_from: eigenvalue_existence_closed
lean_status: cited

## Type / well-formedness check
Well-formed over C. The UNITARY similarity (rather than merely invertible) is the strength: it is numerically stable and it is what makes the spectral theorem for normal matrices a one-line corollary.

## Specialization / boundary cases
- A normal: the triangular factor is forced to be DIAGONAL, giving spectral_theorem_normal
- A real with real spectrum: Q can be taken real orthogonal (the real Schur form); with complex spectrum the real Schur form has 2x2 blocks

## Hypothesis-dropped counterexamples
- **algebraic_closedness**: over R, [[0,-1],[1,0]] is not triangularisable at all -- a triangular real matrix has its diagonal as real eigenvalues, and this one has none
- **triangular_is_not_diagonal**: Schur does NOT diagonalise: the strictly upper part is generally nonzero and carries the defectiveness

## Common misuse
- reading Schur as 'every complex matrix is diagonalisable' -- it is not, and the strictly-upper part is precisely the obstruction
- assuming T is unique: it is not (the eigenvalue order can be permuted, and the off-diagonal entries change accordingly)

## In the wild
- the target form of the QR algorithm, the standard numerical eigenvalue method: it computes a Schur factorisation, never the characteristic polynomial

## Related nodes (non-prerequisite)
- required_by: spectral_theorem_normal

## Sources
horn_johnson_2e, trefethen_bau
