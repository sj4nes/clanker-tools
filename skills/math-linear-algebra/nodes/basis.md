# basis

## Type
definition

## Statement
A basis of V is a linearly independent family that spans V. DEFINED WITHOUT REFERENCE TO ANY NUMBER -- this is what makes dimension provable rather than assumed (see edges/cycles.md, cycle 4).

## Symbols
- `(b_i)_{i in I}` — the basis, type: indexed family in V; I may be infinite

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
linear_independence, span

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
Well-formed with no appeal to dimension. The definition is stated for arbitrary index sets, so it covers the infinite-dimensional case handled by basis_existence_general.

## Specialization / boundary cases
- the standard basis (e_1,...,e_n) of F^n
- the empty family is a basis of {0}
- (1, t, t^2, ...) is a basis of F[t]: infinite, but every element is still a FINITE combination
- (1, i) is a basis of C as an R-vector space, but (1) is a basis of C as a C-vector space -- dimension depends on the field of scalars

## Hypothesis-dropped counterexamples
- **independence**: a spanning set that is dependent gives non-unique coordinates: in R^2, (e_1, e_2, e_1+e_2) spans but 0 has infinitely many representations
- **spanning**: an independent family that does not span gives coordinates only on a proper subspace

## Common misuse
- assuming a basis is unique: every space of dimension >= 1 over an infinite field has infinitely many. What IS unique is the CARDINALITY (dimension_well_defined) and the coordinates relative to a FIXED ordered basis
- assuming a basis of an infinite-dimensional space is countable or usable -- a Hamel basis of R over Q has cardinality of the continuum and cannot be exhibited

## Related nodes (non-prerequisite)
- required_by: steinitz_exchange, ordered_basis, dimension_well_defined

## Sources
axler_lada_4e, hoffman_kunze_2e
