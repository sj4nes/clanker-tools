# determinant_existence_uniqueness

## Type
theorem

## Statement
There is EXACTLY ONE multilinear alternating form D on the columns of F^{n x n} with D(I) = 1. Stated deliberately WITHOUT naming 'the determinant' -- this is what makes the subsequent definition non-circular (edges/cycles.md, cycle 2).

## Symbols
- `D` — the unique normalised alternating multilinear form

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
identity_matrix, multilinear_alternating_form, permutation_sign

## Hypotheses
F a commutative field, n fixed

## Proof provenance
technique: UNIQUENESS: expand each column in the standard basis by multilinearity, giving a sum over all index functions; alternation kills every non-injective one, leaving a sum over S_n with coefficients forced by the swap rule and D(I) = 1. EXISTENCE: verify that the resulting Leibniz sum is multilinear and alternating
derives_from: multilinear_alternating_form
lean_status: cited

## Type / well-formedness check
Well-formed as an existence-and-uniqueness statement about a class of functions, with no forward reference. Uniqueness is what makes 'the determinant' a definite description.

## Specialization / boundary cases
- n = 2: uniqueness forces D = ad - bc
- dropping the normalisation D(I) = 1 leaves a ONE-DIMENSIONAL space of alternating forms, all scalar multiples of det -- normalisation is what selects one

## Hypothesis-dropped counterexamples
- **the_normalisation**: without D(I) = 1, D = 0 also qualifies and uniqueness fails outright
- **alternation**: without it, many multilinear forms exist (the permanent among them)

## Common misuse
- proving existence by writing the Leibniz formula and calling it the definition -- the point of this ordering is that the CHARACTERISATION comes first and the formula is derived

## Related nodes (non-prerequisite)
- required_by: determinant, leibniz_formula

## Sources
hoffman_kunze_2e, lang_algebra_3e
