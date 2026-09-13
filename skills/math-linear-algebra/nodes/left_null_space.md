# left_null_space

## Type
definition

## Statement
The left null space of A is null(A^T) = {y in F^m : A^T y = 0} = {y : y^T A = 0}, a subspace of F^m of dimension m - rank A.

## Symbols
- `y` — a left null vector, type: element of F^m

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
null_space, transpose

## Hypotheses
(none — unconditional within scope)
## Type / well-formedness check
Well-formed. The two descriptions agree because y^T A = 0 (a row identity) transposes to A^T y = 0.

## Specialization / boundary cases
- A of full row rank: the left null space is {0}, and Ax = b is solvable for EVERY b
- each left null vector y gives a consistency condition y^T b = 0 on b for Ax = b to be solvable

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: a definition

## Common misuse
- ignoring it when diagnosing an inconsistent system: inconsistency is exactly the existence of a y in null(A^T) with y^T b != 0

## Related nodes (non-prerequisite)
- required_by: four_subspaces

## Sources
strang_5e
