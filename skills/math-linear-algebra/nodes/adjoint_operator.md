# adjoint_operator

## Type
definition

## Statement
The adjoint T^* is the unique operator with <Tv, w> = <v, T^* w> for all v, w. It exists and is unique in finite dimension; its matrix in ORTHONORMAL bases is the conjugate transpose. (ST)^* = T^*S^*, (T^*)^* = T, and (aT)^* = conj(a) T^*.

## Symbols
- `T^*` — type: linear map W -> V (note the direction reverses, as for dual_map)

## Epistemic status
definition  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
conjugate_transpose, finite_dimensional, inner_product, linear_map, orthonormal_basis

## Hypotheses
V, W finite-dimensional inner product spaces

## Proof provenance
technique: for fixed w, v -> <Tv,w> is a functional, hence equals <v, u> for a unique u by Riesz (finite-dimensional, via an orthonormal basis); set T^*w := u and check linearity
derives_from: orthonormal_basis
lean_status: cited

## Type / well-formedness check
Well-formed: existence and uniqueness follow from the Riesz representation of the functional v -> <Tv, w> in finite dimension. The matrix identity holds ONLY in orthonormal bases -- in a general basis the adjoint's matrix is G^{-1}A^*G with G the Gram matrix.

## Specialization / boundary cases
- V = W = F^n standard: T^* is A^*
- T unitary: T^* = T^{-1}
- T self-adjoint: T^* = T

## Hypothesis-dropped counterexamples
- **orthonormality_of_the_basis**: in a non-orthonormal basis with Gram matrix G, the adjoint's matrix is G^{-1}A^*G, not A^*. Assuming otherwise is the source of the 'why is my adjoint wrong in a weighted inner product' error
- **finite_dimensionality**: in infinite dimension the adjoint of an UNBOUNDED operator need not exist on the whole space -- densely defined adjoints and domain issues are the substance of unbounded operator theory, entirely outside this capsule
- **adjoint_versus_dual**: the dual map T^t: W^* -> V^* needs no inner product and does not conjugate; T^* does both. They correspond under the Riesz identification, which is CONJUGATE-linear over C

## Common misuse
- using A^T rather than A^* over C
- assuming the matrix of the adjoint is the conjugate transpose in an arbitrary basis

## Related nodes (non-prerequisite)
- contrasts_with: dual_map
- required_by: self_adjoint, adjoint_kernel_image, normal_matrix

## Sources
axler_lada_4e, hoffman_kunze_2e
