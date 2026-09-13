# spectral_theorem_normal

## Type
theorem

## Statement
Over C, A is UNITARILY diagonalisable if and only if A is NORMAL: A = U D U^* with U unitary and D diagonal (generally complex).

## Symbols
- `U` — unitary
- `D` — complex diagonal

## Epistemic status
proved_theorem  ·  field_scope: algebraically_closed

## Prerequisites (tsort edges into this node)
diagonalisable, fundamental_theorem_of_algebra, normal_matrix, orthogonal_matrix, schur_triangularisation

## Hypotheses
F = C, finite-dimensional

## Proof provenance
technique: forward: A = UDU^* gives AA^* = UDD^*U^* = UD^*DU^* = A^*A since diagonal matrices commute. Backward: by schur_triangularisation A = QTQ^* with T upper triangular; normality of A forces normality of T, and a normal triangular matrix is diagonal (compare the (1,1) entries of TT^* and T^*T and induct)
derives_from: schur_triangularisation
lean_status: cited

## Type / well-formedness check
Well-formed over C. Note D is complex in general -- realness of the diagonal is the extra content of self-adjointness, not of normality.

## Specialization / boundary cases
- A Hermitian: D is real (self_adjoint_real_eigenvalues), recovering the complex form of spectral_theorem_symmetric
- A unitary: D has entries of modulus 1
- A skew-Hermitian: D is purely imaginary

## Hypothesis-dropped counterexamples
- **normality**: [[1,1],[0,1]] is not normal and not diagonalisable
- **the_field_being_C**: a real orthogonal rotation is normal and is unitarily diagonalisable over C, but NOT orthogonally diagonalisable over R -- its eigenvalues are not real. Over R the correct statement is the real normal form with 2x2 rotation blocks
- **unitary_versus_merely_invertible**: a diagonalisable non-normal matrix (e.g. [[1,1],[0,2]]) has A = PDP^{-1} with P invertible but NOT unitary. Normality is exactly the obstruction

## Common misuse
- expecting a real orthogonal diagonalisation of a real normal but non-symmetric matrix
- confusing diagonalisable (P invertible) with unitarily diagonalisable (P unitary) -- the latter is strictly stronger and is what gives numerical stability

## Related nodes (non-prerequisite)
- generalizes: spectral_theorem_symmetric

## Sources
horn_johnson_2e, axler_lada_4e
