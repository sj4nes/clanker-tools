# linear_system

## Type
definition

## Statement
Ax = b with A in F^{m x n}, b in F^m. It is CONSISTENT iff b is in col(A); its solution set is then x_p + null(A), an AFFINE subspace (a coset), where x_p is any particular solution.

## Symbols
- `x_p` — any particular solution
- `x_p + null(A)` — type: coset of null(A) in F^n

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
column_space, gaussian_elimination, matrix, null_space

## Hypotheses
b in col(A) for consistency

## Proof provenance
technique: if Ax_p = b then Ax = b iff A(x - x_p) = 0
derives_from: column_space
lean_status: cited

## Type / well-formedness check
Well-formed; the solution set is a subspace ONLY when b = 0. For b != 0 it is affine and contains no zero vector, which is why solution sets of inhomogeneous systems are not vector spaces.

## Specialization / boundary cases
- b = 0: the solution set is null(A), a genuine subspace
- A invertible: a unique solution x = A^{-1}b
- rank A = m < n: consistent for every b, with an (n - m)-dimensional family of solutions

## Hypothesis-dropped counterexamples
- **consistency**: if b is not in col(A) there is NO solution; least_squares then replaces the equation by minimising ||Ax - b||, which always has a solution
- **affine_not_linear**: treating the solution set as a subspace leads to the false claim that a sum of two solutions is a solution -- it solves Ax = 2b

## Common misuse
- averaging two solutions of an inhomogeneous system and expecting a solution: the AVERAGE is one (affine combinations are preserved), the SUM is not
- concluding from 'more equations than unknowns' that there is no solution -- that depends on rank, not on shape

## Related nodes (non-prerequisite)
- required_by: cramers_rule, least_squares, condition_number

## Sources
strang_5e
