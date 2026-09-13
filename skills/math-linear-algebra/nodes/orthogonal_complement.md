# orthogonal_complement

## Type
definition

## Statement
U^perp = {v in V : <v,u> = 0 for all u in U}, a SUBSPACE of V for any subset U, with U^perp = (span U)^perp.

## Symbols
- `U^perp` — type: subspace of V

## Epistemic status
definition  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
orthogonality, span, subspace

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: intersection of the kernels of the functionals <., u>, hence a subspace
derives_from: orthogonality
lean_status: cited

## Type / well-formedness check
Well-formed for an arbitrary SUBSET U, since the defining conditions are linear in v. That U^perp is a subspace even when U is not is what makes the notation useful.

## Specialization / boundary cases
- {0}^perp = V and V^perp = {0} (the latter uses positive definiteness)
- in R^3, a plane's complement is its normal line
- U^perp = null(A^T) when U = col(A) -- this is adjoint_kernel_image

## Hypothesis-dropped counterexamples
- **positive_definiteness**: for a degenerate form, V^perp can be nonzero (the radical), and U + U^perp need not be V. Over F_2 with sum x_iy_i, the span of (1,1) is contained in its OWN perp
- **double_perp_needs_finite_dimension**: U subset (U^perp)^perp always, but equality needs U to be a finite-dimensional (or closed) subspace -- see orthogonal_decomposition

## Common misuse
- confusing U^perp (in V, needs an inner product) with the annihilator U^0 (in V^*, needs none)
- assuming (U^perp)^perp = U for a non-closed subspace of an infinite-dimensional space

## Related nodes (non-prerequisite)
- dual_of: annihilator
- required_by: orthogonal_decomposition, adjoint_kernel_image

## Sources
axler_lada_4e
