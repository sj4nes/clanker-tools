# ordered_field_hyp

## Type
hypothesis

## Statement
F carries a total order compatible with its arithmetic: a < b implies a + c < b + c, and 0 < a, 0 < b implies 0 < ab. Needed to say a scalar is POSITIVE, hence for positive-definiteness and inertia.

## Symbols
- `<` — the order, type: total order on F compatible with + and *

## Epistemic status
definition  ·  field_scope: ordered_field

## Prerequisites (tsort edges into this node)
real_number

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
Well-formed. An ordered field necessarily has characteristic 0 (since 1 > 0 forces 1 + 1 + ... > 0), so ordered_field implies char_not_2 -- recorded as a note, not as an edge, to keep the tags independent.

## Specialization / boundary cases
- F = R, the case every spectral result in this capsule is stated over
- F = Q is ordered too, so Sylvester's law of inertia holds over Q -- but the spectral theorem does not, because the eigenvalues need not be rational

## Hypothesis-dropped counterexamples
- **the_order**: C admits no compatible order (i^2 = -1 < 0 contradicts squares being nonnegative). So 'positive definite' over C must be read as 'the HERMITIAN form x^* A x takes positive REAL values', which is a different statement needing self-adjointness to even be real-valued
- **over_a_finite_field**: F_p has no compatible order at all; positive_definite and sylvester_law_of_inertia are simply not statable there

## Common misuse
- calling a complex symmetric (not Hermitian) matrix positive definite -- x^T A x is complex-valued and the phrase is meaningless

## Related nodes (non-prerequisite)
- required_by: positive_definite, sylvester_law_of_inertia

## Sources
hoffman_kunze_2e, horn_johnson_2e
