# span

## Type
definition

## Statement
span(S) is the set of all linear combinations of finitely many elements of S. By convention span(empty) = {0}.

## Symbols
- `S` — a subset of V, possibly infinite
- `span(S)` — type: subspace of V

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
linear_combination, subspace

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
Well-formed for any S, finite or not, because only finite subsums are formed. The empty convention is forced by the empty-sum convention, not chosen freely.

## Specialization / boundary cases
- span of a single nonzero v is the line Fv
- span(empty) = {0}, so the empty set is a basis of the zero space and dim{0} = 0
- span of the standard basis of F^n is F^n

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: span is a definition with no hypotheses; the only trap is the empty case, which is why the convention is stated

## Common misuse
- confusing span(S) with S: span is closed under the operations, S need not be
- assuming span(S) has |S| dimensions -- only if S is independent (dimension_well_defined)

## Related nodes (non-prerequisite)
- required_by: basis, row_space, column_space

## Sources
axler_lada_4e
