# orthogonality

## Type
definition

## Statement
u perp v if <u,v> = 0. A set is orthogonal if its elements are pairwise orthogonal, orthonormal if in addition every element has norm 1. Orthogonality is SYMMETRIC (since <v,u> = conj(<u,v>)).

## Symbols
- `perp` — the orthogonality relation, type: symmetric relation on V

## Epistemic status
definition  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
inner_product, inner_product_space

## Hypotheses
an inner product space
## Type / well-formedness check
Well-formed and symmetric by conjugate-symmetry. Note 0 is orthogonal to everything including itself -- the only vector with that property, by positive definiteness.

## Specialization / boundary cases
- the standard basis of F^n is orthonormal
- in R^2, (1,1) perp (1,-1)
- uncorrelated centred random variables are orthogonal under <X,Y> = E[XY]

## Hypothesis-dropped counterexamples
- **positive_definiteness**: over F_2 with the form sum x_iy_i, the vector (1,1) satisfies <x,x> = 1+1 = 0, so it is orthogonal to ITSELF while nonzero. Every orthogonality argument -- independence of orthogonal sets, orthogonal decomposition, projection -- collapses. This is why the four_subspaces theorem is stated over any field in DIMENSIONS only, with orthogonality deferred to adjoint_kernel_image

## Common misuse
- assuming orthogonal implies independent without excluding 0 (orthogonal_implies_independent needs the vectors nonzero)
- importing orthogonality into a general field

## Related nodes (non-prerequisite)
- required_by: orthonormal_basis, orthogonal_complement, orthogonal_projection

## Sources
axler_lada_4e
