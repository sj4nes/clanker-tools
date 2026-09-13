# dimension_well_defined

## Type
theorem

## Statement
Any two bases of a finitely generated vector space have the same (finite) number of elements.

## Symbols
- `|B|` — the cardinality of the basis, type: natural number

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
basis_existence_finite, induction_principle, steinitz_exchange

## Hypotheses
V finitely generated

## Proof provenance
technique: apply steinitz_exchange twice: B independent and B' spanning gives |B| <= |B'|; swapping the roles gives the reverse
derives_from: steinitz_exchange
lean_status: core — LinAlg.basis_card_eq

## Type / well-formedness check
Well-formed and logically prior to 'dimension': this theorem is what makes the definition of dim V a definite description rather than a choice.

## Specialization / boundary cases
- F^n: every basis has exactly n elements, so dim F^n = n
- C over R has dimension 2; C over C has dimension 1 -- the theorem fixes the number only once the SCALAR FIELD is fixed

## Hypothesis-dropped counterexamples
- **finite_generation**: for infinite-dimensional spaces the statement survives as a cardinality equality, but only with AC-dependent cardinal arithmetic; the elementary Steinitz argument does not apply
- **F_being_a_field**: over a general ring the analogous statement (the invariant basis number property) can FAIL: there are rings with R isomorphic to R^2 as modules. Fields always have IBN

## Common misuse
- assuming two bases are related by a permutation -- they are related by an invertible change_of_basis matrix, which is far more general

## Related nodes (non-prerequisite)
- required_by: dimension

## Sources
axler_lada_4e, hoffman_kunze_2e
