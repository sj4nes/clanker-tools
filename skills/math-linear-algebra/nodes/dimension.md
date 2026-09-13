# dimension

## Type
definition

## Statement
dim V is the common cardinality of any basis of V, well-defined by the preceding theorem. dim{0} = 0. Written dim_F V when the scalar field needs emphasis.

## Symbols
- `dim V` — type: natural number (finite case) or cardinal (general case)
- `dim_F V` — dimension over the scalar field F

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
dimension_well_defined, finite_dimensional

## Hypotheses
V finite-dimensional (for the natural-number-valued version)
## Type / well-formedness check
Well-formed only BECAUSE dimension_well_defined precedes it -- this is the definitional-order resolution recorded as cycle 4.

## Specialization / boundary cases
- dim F^n = n
- dim {0} = 0 with the empty basis
- dim_R C = 2 but dim_C C = 1: the subscript is not decorative
- dim F^{m x n} = mn, the fact behind matrix_addition_scalar

## Hypothesis-dropped counterexamples
- **well_definedness**: without dimension_well_defined the notation dim V would depend on the basis chosen and every counting argument in the capsule would collapse
- **the_scalar_field**: R has dimension 1 over R and infinite (continuum) dimension over Q

## Common misuse
- comparing dimensions over different fields
- assuming dim(U + W) = dim U + dim W -- that needs the sum to be DIRECT (dimension_formula_sum)

## Related nodes (non-prerequisite)
- required_by: rank, nullity, rank_nullity

## Sources
axler_lada_4e
