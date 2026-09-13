# algebraically_closed_field

## Type
hypothesis

## Statement
F is algebraically closed if every nonconstant polynomial in F[t] has a root in F, equivalently splits into linear factors. The hypothesis behind every 'there exists an eigenvalue' statement.

## Symbols
- `F` — the scalar field

## Epistemic status
definition  ·  field_scope: algebraically_closed

## Prerequisites (tsort edges into this node)
complex_number, field

## Hypotheses
F algebraically closed
## Type / well-formedness check
Well-formed over any field. C is the instance this capsule uses, supplied by the cited fundamental_theorem_of_algebra.

## Specialization / boundary cases
- F = C by the fundamental theorem of algebra
- the algebraic closure of any field exists (needs AC in general), so every capsule result tagged algebraically_closed can be reached by passing to F-bar -- at the cost of leaving the original field

## Hypothesis-dropped counterexamples
- **algebraic_closure**: over R the rotation by 90 degrees, [[0,-1],[1,0]], has characteristic polynomial t^2 + 1 and NO real eigenvalue. Every statement of the form 'an operator has an eigenvalue', 'is triangularisable', 'has a Jordan form' fails over R for this matrix
- **over_Q**: even worse: [[0,2],[1,0]] has char poly t^2 - 2, with no root in Q

## Common misuse
- applying Jordan form or Schur triangularisation to a real matrix and expecting real output -- the output is complex unless the spectrum happens to be real, which for SYMMETRIC matrices is guaranteed by a different theorem

## Related nodes (non-prerequisite)
- required_by: eigenvalue_existence_closed, schur_triangularisation, primary_decomposition, jordan_normal_form

## Sources
axler_lada_4e, hoffman_kunze_2e
