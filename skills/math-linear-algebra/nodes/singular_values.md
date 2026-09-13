# singular_values

## Type
definition

## Statement
The singular values sigma_1 >= ... >= sigma_p >= 0 (p = min(m,n)) of A in F^{m x n} are the nonnegative square roots of the eigenvalues of A^*A (equivalently of AA^*). rank A = the number of NONZERO singular values.

## Symbols
- `sigma_i` — type: nonnegative real
- `p` — min(m,n)

## Epistemic status
definition  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
conjugate_transpose, eigenvalue, gram_matrix, matrix_rank, positive_definite, spectral_theorem_symmetric

## Hypotheses
A in F^{m x n}

## Proof provenance
technique: A^*A is Hermitian PSD by gram_matrix; its spectrum is real and nonnegative; AA^* has the same nonzero eigenvalues (since AB and BA share nonzero spectrum)
derives_from: gram_matrix
lean_status: cited

## Type / well-formedness check
Well-formed: A^*A is Hermitian POSITIVE SEMIDEFINITE (gram_matrix), so its eigenvalues are real and nonnegative (spectral_theorem_symmetric, positive_definite) and the square roots are real. Every step of this justification is a separate prerequisite, which is why the node has five incoming edges.

## Specialization / boundary cases
- A square symmetric PSD: the singular values ARE the eigenvalues
- A square symmetric indefinite: sigma_i = |lambda_i| -- the absolute values, so SVD loses sign information the eigendecomposition keeps
- A orthogonal: all singular values 1
- A = uv^*: one nonzero singular value ||u|| ||v||

## Hypothesis-dropped counterexamples
- **singular_values_are_not_eigenvalues**: [[0,1],[0,0]] has both eigenvalues 0 but singular values 1 and 0. A nilpotent matrix can have large singular values -- the two spectra measure different things (spectral_radius versus norm)
- **the_conjugate_matters**: over C, using A^TA instead of A^*A gives the wrong (possibly negative or complex) values -- see conjugate_transpose

## Common misuse
- treating singular values as eigenvalues for a non-symmetric matrix
- computing them by forming A^*A explicitly: that squares the condition number; use a direct SVD algorithm

## Related nodes (non-prerequisite)
- required_by: singular_value_decomposition, matrix_norms, condition_number

## Sources
horn_johnson_2e, trefethen_bau
