# invertible_operator

## Type
definition

## Statement
T in L(V) is invertible if there is S in L(V) with ST = TS = I. In FINITE dimension a one-sided inverse is automatically two-sided.

## Symbols
- `S = T^{-1}` — the inverse operator, unique when it exists

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
injective_surjective_equivalence, linear_isomorphism, linear_operator

## Hypotheses
V finite-dimensional for the one-sided clause

## Proof provenance
technique: one-sided suffices: ST = I forces T injective, hence surjective by injective_surjective_equivalence, hence bijective
derives_from: injective_surjective_equivalence
lean_status: cited

## Type / well-formedness check
Well-formed. Uniqueness of the inverse follows from associativity: S = S(TS') = (ST)S' = S'.

## Specialization / boundary cases
- V = F^n: invertible operators correspond to invertible matrices (invertibility_equivalences)

## Hypothesis-dropped counterexamples
- **finite_dimensionality**: on F[t] the shift operators L (delete the constant term) and R (multiply by t) satisfy LR = I but RL != I. A one-sided inverse is genuinely weaker in infinite dimension, and this pair is the standard witness

## Common misuse
- checking only ST = I for an operator on a function space and concluding invertibility

## Related nodes (non-prerequisite)
- required_by: invertible_matrix

## Sources
axler_lada_4e
