# laplace_expansion

## Type
theorem

## Statement
det A = sum_{j=1}^n (-1)^{i+j} A_{ij} M_{ij} for ANY fixed row i, and symmetrically along any fixed column, where M_{ij} is the (i,j) minor (the determinant of A with row i and column j deleted).

## Symbols
- `M_{ij}` — the (i,j) MINOR, type: element of F
- `C_{ij} = (-1)^{i+j} M_{ij}` — the (i,j) COFACTOR

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
determinant, leibniz_formula, multilinear_alternating_form

## Hypotheses
A square, n >= 2

## Proof provenance
technique: group the Leibniz sum by the value of sigma at the chosen index, and identify each group with a signed minor
derives_from: leibniz_formula
lean_status: cited

## Type / well-formedness check
Well-formed. The checkerboard sign (-1)^{i+j} depends on the index_convention starting at 1; 0-based indexing flips every sign.

## Specialization / boundary cases
- n = 2 along the first row: det = a(d) - b(c)
- A with a row of mostly zeros: expanding along it is efficient -- the one case where cofactor expansion beats elimination
- expanding along a row with a DIFFERENT row's cofactors gives 0, which is the identity behind the adjugate

## Hypothesis-dropped counterexamples
- **indexing_from_one**: 0-based indexing negates every cofactor sign
- **cost**: recursive cofactor expansion costs O(n!) -- the same disaster as Leibniz. It is a structural tool, not an algorithm

## Common misuse
- using cofactor expansion to compute a determinant of size beyond about 4
- forgetting the alternating sign entirely (computing sum_j A_{ij} M_{ij}, which is not the determinant)

## Related nodes (non-prerequisite)
- required_by: adjugate, determinant_rank_minors

## Sources
hoffman_kunze_2e
