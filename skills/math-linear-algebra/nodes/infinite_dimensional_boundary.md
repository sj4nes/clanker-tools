# infinite_dimensional_boundary

## Type
regime

## Statement
A CATALOGUE of the results in this capsule that FAIL without finite-dimensionality, each with its standing counterexample. Stated as a regime node so the hypothesis's cost is visible in one place.

## Symbols
- `S` — the right shift on F^N (sequences), S(x_1,x_2,...) = (0,x_1,x_2,...)
- `L` — the left shift, L(x_1,x_2,...) = (x_2,x_3,...)

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
adjoint_operator, basis_existence_general, double_dual, eigenvalue_existence_closed, finite_dimensional, injective_surjective_equivalence, one_sided_inverse_square, rank_nullity

## Hypotheses
V infinite-dimensional

## Proof provenance
technique: each item is the hypothesis-dropped counterexample already recorded on the corresponding node; no new argument
lean_status: cited

## Type / well-formedness check
Well-formed as a catalogue. Each entry is a claim already proved (with its hypothesis) elsewhere in the capsule; this node collects the counterexamples rather than introducing new mathematics.

## Specialization / boundary cases
- rank_nullity: S is injective (nullity 0) and not surjective -- no finite count relates the dimensions
- injective_surjective_equivalence: S injective not surjective; L surjective not injective, both on the SAME space
- one_sided_inverse_square: LS = I but SL != I
- double_dual: dim V^* > dim V for V = F[t], so evaluation is injective but far from surjective
- eigenvalue_existence_closed: S has NO eigenvalue over C
- adjoint_operator: an unbounded densely-defined operator has an adjoint only on a proper domain
- basis_existence: needs Zorn, hence full AC (basis_existence_general)
- orthogonal_decomposition: the finitely-supported sequences U inside l^2 satisfy U^perp = {0} yet U != l^2

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: this node IS the counterexample catalogue

## Common misuse
- importing finite-dimensional intuition into functional analysis: nearly every sharp theorem in this capsule has a counterexample one dimension past finiteness
- assuming that because a statement is true for all n it is true in the limit

## Related nodes (non-prerequisite)
- illustrated_by: 

## Sources
axler_lada_4e, conway_functional_analysis
