# double_dual

## Type
theorem

## Statement
The evaluation map ev: V -> V^**, ev(v)(f) = f(v), is linear and INJECTIVE for every V, and is an isomorphism exactly when V is finite-dimensional. It is CANONICAL -- defined with no choice of basis.

## Symbols
- `ev` — the canonical evaluation, type: linear map V -> V^**
- `V^**` — the dual of the dual

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
dual_basis, dual_space, finite_dimensional

## Hypotheses
V finite-dimensional for surjectivity

## Proof provenance
technique: injectivity: if v != 0 extend v to a basis and take the coordinate functional, which is nonzero on v (this uses basis existence, hence AC in infinite dimension). Surjectivity in finite dimension by the dimension count dim V^** = dim V^* = dim V
derives_from: dual_basis
lean_status: cited

## Type / well-formedness check
Well-formed: ev(v) is a functional on V^*, since f -> f(v) is linear in f. The definition mentions no basis, which is precisely the point.

## Specialization / boundary cases
- V = F^n: ev identifies column vectors with functionals on row vectors, the familiar 'a vector is what it does to covectors'

## Hypothesis-dropped counterexamples
- **finite_dimensionality**: for V = F[t], dim V^* > dim V and dim V^** > dim V^*, so ev is injective but far from surjective. In functional analysis the CONTINUOUS dual restores surjectivity for reflexive spaces only -- L^1 is a standard non-reflexive example
- **canonicity_vs_existence**: V is isomorphic to V^* in finite dimension too, but only after choosing a basis. The point of this node is that V -> V^** needs NO choice, which is what makes 'double dual' a genuine identification and 'dual' merely an isomorphism

## Common misuse
- citing dim V = dim V^* as if it made V and V^* canonically the same -- it does not, and the distinction is the whole content of tensor variance (contravariant vs covariant indices)

## Related nodes (non-prerequisite)
- illustrated_by: infinite_dimensional_boundary

## Sources
hoffman_kunze_2e, axler_lada_4e
