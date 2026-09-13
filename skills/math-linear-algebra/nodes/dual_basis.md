# dual_basis

## Type
theorem

## Statement
If B = (b_1,...,b_n) is a basis of a finite-dimensional V, the functionals b_i^* defined by b_i^*(b_j) = delta_{ij} form a basis of V^*. Hence dim V^* = dim V.

## Symbols
- `b_i^*` — the i-th coordinate functional, type: element of V^*
- `delta_{ij}` — 1 if i = j, else 0

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
basis, dual_space, finite_dimensional, linear_map_determined_by_basis

## Hypotheses
V finite-dimensional

## Proof provenance
technique: independence: applying a vanishing combination to b_j isolates the j-th coefficient. Spanning: f = sum_i f(b_i) b_i^* since both sides agree on the basis
derives_from: linear_map_determined_by_basis
lean_status: cited

## Type / well-formedness check
Well-formed: each b_i^* exists and is unique by linear_map_determined_by_basis applied with W = F. Note b_i^* depends on the WHOLE basis B, not just on b_i.

## Specialization / boundary cases
- V = F^n with the standard basis: b_i^* is the i-th coordinate function, the i-th row of I

## Hypothesis-dropped counterexamples
- **finite_dimensionality**: for V = F[t] with basis (1, t, t^2, ...), the functionals t^i -> coefficient are independent but do NOT span V^*: the functional 'sum of all coefficients' is not a finite combination of them. dim V^* > dim V strictly
- **the_whole_basis_matters**: b_1^* changes if b_2 is replaced, even though b_1 is untouched -- the dual basis is not computed entrywise

## Common misuse
- treating b_i^* as depending only on b_i, which leads to wrong duals after a partial basis change

## Related nodes (non-prerequisite)
- required_by: double_dual, annihilator

## Sources
hoffman_kunze_2e
