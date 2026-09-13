# determinant_rank_minors

## Type
theorem

## Statement
rank A = the largest r for which some r x r submatrix of A (an r x r MINOR) has nonzero determinant. A THEOREM -- not the definition of rank (edges/cycles.md, cycle 3).

## Symbols
- `an r x r minor` — the determinant of the submatrix on some r rows and r columns

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
determinant, determinant_invertible_iff, laplace_expansion, matrix_rank

## Hypotheses
A in F^{m x n}

## Proof provenance
technique: if rank A = r, pick r independent columns and then r independent rows of the resulting m x r matrix: the r x r block is invertible so its determinant is nonzero. Conversely a nonzero r x r minor exhibits r independent columns
derives_from: matrix_rank
lean_status: cited

## Type / well-formedness check
Well-formed. It relates two independently defined quantities -- rank as a dimension, minors as determinants -- and is exactly the bridge cycle 3 was resolved to make possible.

## Specialization / boundary cases
- r = 1: rank >= 1 iff some entry is nonzero
- r = n = m: rank n iff det A != 0, recovering determinant_invertible_iff
- the leading principal minors version is Sylvester's criterion for positive definiteness (psd_characterisations) -- but that needs the LEADING PRINCIPAL minors, which is a strictly stronger condition than 'some minor'

## Hypothesis-dropped counterexamples
- **all_minors_versus_leading_ones**: A = [[0,0],[0,-1]] has a nonzero leading... no: its leading 1x1 minor is 0 while it has a nonzero 2x2... take A = [[0,1],[1,0]]: both leading principal minors are 0 and -1, so 'leading minors nonzero' fails, yet rank A = 2. Only ALL minors, not the leading ones, characterise rank
- **cost**: there are C(m,r)C(n,r) minors -- this is a characterisation, never an algorithm

## Common misuse
- computing rank by minors rather than elimination
- confusing this with Sylvester's criterion, which uses only LEADING PRINCIPAL minors and characterises positive definiteness, not rank

## Related nodes (non-prerequisite)
- required_by: psd_characterisations

## Sources
horn_johnson_2e, hoffman_kunze_2e
