# coordinate_isomorphism

## Type
theorem

## Statement
If dim V = n < infinity then [.]_B : V -> F^n is an isomorphism for every ordered basis B. Hence any two F-spaces of the same finite dimension are isomorphic, and dimension is a COMPLETE invariant of finite-dimensional vector spaces.

## Symbols
- `[.]_B` — the coordinate isomorphism V -> F^n

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
dimension, ordered_basis

## Hypotheses
V finite-dimensional

## Proof provenance
technique: linearity from the uniqueness of coordinates; bijectivity from spanning and independence respectively
derives_from: basis_unique_representation
lean_status: cited

## Type / well-formedness check
Well-formed. 'Complete invariant' means dimension alone decides the isomorphism class -- an unusually strong classification, and the reason linear algebra is so much simpler than group or ring theory.

## Specialization / boundary cases
- V = F^n, B standard: the isomorphism is the identity
- every 3-dimensional real space -- polynomials of degree <= 2, symmetric 2x2 matrices, R^3 -- is isomorphic to R^3

## Hypothesis-dropped counterexamples
- **finite_dimensionality**: two infinite-dimensional spaces of the same Hamel dimension are still isomorphic, but the isomorphism is AC-dependent and unusable; more importantly, as TOPOLOGICAL spaces they need not be isomorphic at all
- **same_scalar_field**: C and R^2 are isomorphic as R-spaces but not as C-spaces (dimensions 1 and 2 over C... and R^2 is not even a C-space without extra structure)

## Common misuse
- concluding that because V is isomorphic to F^n there is a CANONICAL such isomorphism: there is not, it depends on B. The canonical map is V -> V^** (double_dual), which is why that node is singled out

## Related nodes (non-prerequisite)
- required_by: linear_isomorphism, change_of_basis

## Sources
axler_lada_4e, hoffman_kunze_2e
