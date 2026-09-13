# normal_matrix

## Type
definition

## Statement
A is normal if AA^* = A^*A. The class contains the self-adjoint (A^* = A), skew-adjoint (A^* = -A), and unitary (A^* = A^{-1}) matrices, and is EXACTLY the class of unitarily diagonalisable matrices.

## Symbols
- `A^*` — the conjugate transpose

## Epistemic status
definition  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
adjoint_operator, orthogonal_matrix, self_adjoint

## Hypotheses
A square
## Type / well-formedness check
Well-formed for square A. The definition is a commutation condition, which is what makes the 'iff unitarily diagonalisable' characterisation (spectral_theorem_normal) surprising and useful.

## Specialization / boundary cases
- the three named subclasses above
- a real ROTATION matrix is orthogonal hence normal, and is unitarily diagonalisable OVER C (eigenvalues e^{+-i theta}) though not over R
- a diagonal matrix is normal

## Hypothesis-dropped counterexamples
- **normality_is_not_automatic**: [[1,1],[0,1]] has AA^* = [[2,1],[1,1]] and A^*A = [[1,1],[1,2]] -- not equal. It is not normal, and indeed not diagonalisable at all
- **normal_does_not_mean_self_adjoint**: a unitary matrix is normal with eigenvalues on the unit circle, generally not real
- **sums_and_products_of_normals_need_not_be_normal**: normality is not preserved by addition or multiplication unless the matrices commute

## Common misuse
- assuming a normal matrix has real eigenvalues (only the self-adjoint ones do)
- assuming the normal matrices form an algebra

## Related nodes (non-prerequisite)
- generalizes: self_adjoint
- required_by: spectral_theorem_normal, spectral_radius

## Sources
horn_johnson_2e
