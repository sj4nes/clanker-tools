# lu_pivoting_regime

## Type
regime

## Statement
Unpivoted LU exists iff every leading principal minor of A is nonzero. Partial pivoting (choose the largest-magnitude available pivot) is required otherwise, and is standard practice regardless for numerical stability.

## Symbols
- `A_{1:k,1:k}` — the leading k x k principal submatrix

## Epistemic status
definition  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
lu_factorisation

## Hypotheses
exact arithmetic for the existence clause; floating point for the stability clause

## Proof provenance
technique: existence by induction on k, the k-th pivot being the ratio of consecutive leading minors; the stability claim is CITED from numerical analysis, not established in this capsule
derives_from: lu_factorisation
lean_status: cited

## Type / well-formedness check
Well-formed; the minors condition is exact-arithmetic. The stability claim is a numerical statement about floating-point behaviour and is labelled as such, not proved here.

## Specialization / boundary cases
- A symmetric positive definite: all leading minors are positive (psd_characterisations), so no pivoting is needed for existence OR stability -- the reason Cholesky needs no pivoting
- A strictly diagonally dominant: likewise pivot-free

## Hypothesis-dropped counterexamples
- **nonzero_leading_minors**: [[0,1],[1,0]] again: invertible, no unpivoted LU
- **exactness_versus_stability**: A = [[1e-20, 1],[1, 1]] HAS an unpivoted LU in exact arithmetic, but computing it in double precision returns a factorisation whose product is nowhere near A. Existence and usability are different questions

## Common misuse
- reading 'LU exists' as 'LU is safe to compute'
- treating growth factors and backward-error bounds as established here: they are cited numerical-analysis results, outside this capsule's scope (see scope.md)

## Sources
golub_van_loan_4e, higham_asna_2e
