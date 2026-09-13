# triangle_inequality

## Type
corollary

## Statement
||u + v|| <= ||u|| + ||v||, with equality iff one of u, v is a NONNEGATIVE real multiple of the other.

## Symbols
- `c` — a nonnegative real scalar in the equality case

## Epistemic status
corollary  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
cauchy_schwarz, induced_norm

## Hypotheses
induced norm

## Proof provenance
technique: ||u+v||^2 = ||u||^2 + 2 Re<u,v> + ||v||^2 <= ||u||^2 + 2|<u,v>| + ||v||^2 <= (||u||+||v||)^2 by Cauchy-Schwarz
derives_from: cauchy_schwarz
lean_status: cited

## Type / well-formedness check
Well-formed. Note the equality condition is strictly stronger than in Cauchy-Schwarz: dependence is not enough, the multiple must be NONNEGATIVE REAL.

## Specialization / boundary cases
- v = -u: ||0|| = 0 <= 2||u||, strict unless u = 0 -- the multiple -1 is negative, so no equality, illustrating the sharper condition
- the reverse triangle inequality | ||u|| - ||v|| | <= ||u - v|| follows by substitution

## Hypothesis-dropped counterexamples
- **the_equality_condition**: u and v = -u are dependent (so Cauchy-Schwarz is tight) but ||u + v|| = 0 < 2||u||. Dependence gives equality in Cauchy-Schwarz, not in the triangle inequality

## Common misuse
- quoting 'equality iff dependent' for the triangle inequality

## Related nodes (non-prerequisite)
- special_case_of: cauchy_schwarz

## Sources
axler_lada_4e
