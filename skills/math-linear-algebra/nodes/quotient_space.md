# quotient_space

## Type
construction

## Statement
For a subspace U of V, the quotient V/U is the set of cosets v + U with (v+U) + (w+U) = (v+w) + U and a(v+U) = av + U. WELL-DEFINED precisely because U is a subspace.

## Symbols
- `v + U` — a coset, type: element of the quotient set V/U
- `pi` — the canonical projection V -> V/U, v -> v + U, linear and surjective

## Epistemic status
constructive_result  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
quotient_set, subspace, vector_space

## Hypotheses
U a subspace of V

## Proof provenance
technique: verify the vector-space axioms on cosets; each reduces to the corresponding axiom in V applied to representatives
derives_from: quotient_set
lean_status: cited

## Well-definedness
Each operation is defined on representatives; independence of representative follows from U being closed under + (for addition) and under scalar multiplication (for scaling). A subset failing either closure yields no quotient.

## Type / well-formedness check
The type check IS the well-definedness check, as in every quotient construction: if v + U = v' + U and w + U = w' + U then (v+w) - (v'+w') = (v - v') + (w - w') lies in U by closure under addition; and av - av' = a(v - v') lies in U by closure under scalars. Both closures are used, one per operation.

## Specialization / boundary cases
- U = {0}: V/U is isomorphic to V
- U = V: V/U = {0}
- V = R^2, U = the x-axis: V/U is the set of horizontal lines, isomorphic to R by the y-value

## Hypothesis-dropped counterexamples
- **U_being_a_subspace**: if U is merely a subset closed under addition but not scaling -- say the nonnegative x-axis in R^2 -- the scalar operation on cosets is not well-defined, since v + U = v' + U no longer implies av + U = av' + U
- **closure_under_addition**: similarly, a subset closed under scaling but not addition (the union of the axes) breaks coset addition

## Common misuse
- picturing V/U as a subspace of V: it is not, it is a space of COSETS. A complement W with V = U (+) W is isomorphic to V/U but is a genuine choice, not canonical
- assuming the projection has a canonical section: it does not without extra structure (an inner product supplies one)

## Related nodes (non-prerequisite)
- required_by: first_isomorphism_theorem, quotient_dimension

## Sources
hoffman_kunze_2e, axler_lada_4e
