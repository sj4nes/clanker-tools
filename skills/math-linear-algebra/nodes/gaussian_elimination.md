# gaussian_elimination

## Type
algorithm

## Statement
Reduce A to (reduced) row echelon form by elementary row operations: locate a pivot, normalise, clear the column, move down and right. Cost ~ (2/3)n^3 operations for n x n. Computes rank, a null-space basis, the inverse, and solutions of Ax = b.

## Symbols
- `n` — matrix size
- `the pivot` — the entry used to clear a column, required nonzero

## Epistemic status
constructive_result  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
elementary_row_operation, row_echelon_form, rref_uniqueness

## Hypotheses
F a field (so pivots can be inverted)

## Proof provenance
technique: correctness because each step is an elementary operation and the terminal shape is echelon by construction; uniqueness of the result from rref_uniqueness
derives_from: row_echelon_form
lean_status: cited

## Type / well-formedness check
Well-formed as an algorithm over any field: every step is an elementary row operation, so the output is row equivalent to the input by construction. Termination is immediate (one column per step).

## Specialization / boundary cases
- A invertible: applying the same operations to [A | I] yields [I | A^{-1}]
- A singular: elimination halts with a zero row, exhibiting a dependence

## Hypothesis-dropped counterexamples
- **exact_arithmetic**: in floating point, elimination WITHOUT pivoting is unstable: the 2x2 system with a tiny pivot epsilon loses all accuracy. See lu_pivoting_regime. This capsule's statements are all exact-arithmetic statements
- **F_a_field**: over Z the scaling step is unavailable

## Common misuse
- reporting a computed rank from floating-point elimination without a tolerance: numerical rank is a different, threshold-dependent notion (see condition_number)
- treating the operation count as the cost of solving a least-squares problem: forming A^TA squares the condition number, which is why qr_factorisation is preferred

## In the wild
- the solver behind essentially every dense linear system in scientific computing; the LU-with-partial-pivoting routines in LAPACK are this algorithm with a pivot-selection rule

## Related nodes (non-prerequisite)
- historically_precedes: 
- required_by: linear_system, lu_factorisation

## Sources
strang_5e, golub_van_loan_4e
