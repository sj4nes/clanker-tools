# basis_unique_representation

## Type
proposition

## Statement
A family B is a basis of V if and only if every v in V has EXACTLY ONE representation as a finite linear combination of members of B.

## Symbols
- `(a_b)` — the coordinate family, type: finitely supported function B -> F

## Epistemic status
proposition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
basis, linear_independence

## Hypotheses
B a family in V

## Proof provenance
technique: existence <=> spanning by definition; uniqueness <=> independence, since two representations of v differ by a vanishing combination
derives_from: linear_independence
lean_status: cited

## Type / well-formedness check
Well-formed. Existence of a representation is spanning; uniqueness is independence. The proposition is the bridge from the abstract definition to coordinates.

## Specialization / boundary cases
- B the standard basis of F^n: the coordinates are the components themselves

## Hypothesis-dropped counterexamples
- **independence**: with a dependent spanning family, 0 has more than one representation and coordinates are not functions
- **spanning**: with an independent non-spanning family, some v has no representation at all

## Common misuse
- assuming coordinates are basis-independent: they are defined only relative to a FIXED ORDERED basis, and change_of_basis is the whole theory of what happens otherwise

## Related nodes (non-prerequisite)
- required_by: ordered_basis, direct_sum

## Sources
axler_lada_4e
