# linear_map

## Type
definition

## Statement
T: V -> W is linear if T(au + bv) = aT(u) + bT(v) for all a,b in F and u,v in V. Equivalently T preserves addition and scalar multiplication separately.

## Symbols
- `T` — the map, type: function V -> W between F-vector spaces
- `V, W` — vector spaces over the SAME field F

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
function, vector_space

## Hypotheses
V, W vector spaces over the same field F

## Proof provenance
technique: definition
lean_status: cited

## Type / well-formedness check
Well-formed only when V and W are over the same field: aT(u) requires the scalar a to act on W. A map between an R-space and a C-space is linear only after fixing which field is acting.

## Specialization / boundary cases
- T(0) = 0 always -- a linear map cannot be an affine translation
- V = W = F: the linear maps are exactly x -> cx; the map x -> x + 1 is affine, NOT linear
- differentiation on polynomials, and integration over a fixed interval, are both linear

## Hypothesis-dropped counterexamples
- **homogeneity**: over C, complex CONJUGATION is additive and R-homogeneous but not C-homogeneous: conj(iz) = -i conj(z) != i conj(z). Such maps are called conjugate-linear (antilinear) and appear in the second slot of the complex inner product
- **additivity**: x -> |x| on R is homogeneous for positive scalars only and fails additivity
- **same_field**: a Q-linear map R -> R need not be R-linear: AC gives discontinuous additive functions (see basis_existence_general)

## Common misuse
- calling x -> Ax + b linear: it is affine. This is the standard abuse in machine learning and statistics, harmless only if the bias is absorbed into an extra coordinate
- assuming linear implies continuous: true in finite dimension, false in general

## In the wild
- every model of the form 'output is a weighted sum of inputs': regression, convolution, the Fourier and Laplace transforms, quantum-mechanical observables

## Related nodes (non-prerequisite)
- required_by: kernel, image_subspace, matrix_of_linear_map

## Sources
axler_lada_4e, hoffman_kunze_2e
