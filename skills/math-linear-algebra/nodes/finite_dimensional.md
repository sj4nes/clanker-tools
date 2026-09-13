# finite_dimensional

## Type
hypothesis

## Statement
V is finite-dimensional if it has a finite spanning set. A FIRST-CLASS HYPOTHESIS, never ambient: every result that needs it carries a tsort edge to this node.

## Symbols
- `V` — a vector space over F
- `S` — a finite spanning set, type: finite subset of V

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
finite_set

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
Well-formed before dimension is available -- it says a finite spanning set EXISTS, not that any number is well-defined. That ordering is what lets steinitz_exchange and dimension_well_defined come afterwards.

## Specialization / boundary cases
- F^n is finite-dimensional with the standard spanning set of size n
- the space of polynomials of degree <= d is finite-dimensional (dimension d+1); the space of ALL polynomials is not

## Hypothesis-dropped counterexamples
- **finiteness**: F[t] (all polynomials) has no finite spanning set. Dropping the hypothesis breaks rank_nullity (the shift operator on F[t] is injective, not surjective, with zero nullity), injective_surjective_equivalence, double_dual, and the existence of an eigenvalue -- see infinite_dimensional_boundary for the catalogue

## Common misuse
- assuming it silently because the examples are all F^n: most of this capsule's sharpest theorems are FALSE without it
- confusing it with 'has a basis' -- every vector space has a basis given AC (basis_existence_general); what finite-dimensionality buys is that the basis is finite and choice-free

## Related nodes (non-prerequisite)
- illustrated_by: infinite_dimensional_boundary

## Sources
axler_lada_4e
