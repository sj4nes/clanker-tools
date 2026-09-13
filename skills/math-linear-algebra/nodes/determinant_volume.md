# determinant_volume

## Type
proposition

## Statement
Over R, |det A| is the factor by which A scales n-dimensional (Lebesgue) volume, and sgn(det A) records whether A preserves or reverses orientation.

## Symbols
- `vol` — n-dimensional Lebesgue measure, CITED from outside this capsule
- `A(S)` — the image of a measurable set S

## Epistemic status
proposition  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
determinant, determinant_multiplicative, real_number

## Hypotheses
F = R, a translation-invariant measure (cited)

## Proof provenance
technique: the volume of the parallelepiped spanned by the columns is multilinear and alternating in them and equals 1 on the unit cube, so by determinant_existence_uniqueness it IS |det|. The measure-theoretic justification that such a volume exists is cited
derives_from: determinant_multiplicative
lean_status: cited

## Type / well-formedness check
Well-formed only over R and only given a notion of volume, which this capsule does NOT construct -- the measure-theoretic content is cited. What IS internal is the uniqueness argument: any translation-invariant, multilinear-in-columns volume function must be a multiple of det.

## Specialization / boundary cases
- n = 1: |det[a]| = |a|, the length scaling
- n = 2: |ad - bc| is the area of the parallelogram spanned by the columns
- A orthogonal: |det A| = 1, so rigid motions preserve volume -- see orthogonal_matrix
- A singular: det = 0 and the image lies in a proper subspace, of volume 0

## Hypothesis-dropped counterexamples
- **the_field_being_R**: over C the analogue involves |det A|^2 as the real 2n-dimensional volume factor, not |det A|
- **the_existence_of_volume**: the measure-theoretic input is genuinely external; this node is the capsule's clearest example of a result whose INTUITION is standard and whose FOUNDATION is cited

## Common misuse
- reading det as a volume in a general field where no measure exists
- forgetting the absolute value and reporting a negative volume

## In the wild
- the Jacobian factor in the change-of-variables theorem for multiple integrals
- the |det Sigma|^{-1/2} normalising constant of the multivariate normal density

## Sources
lang_algebra_3e, strang_5e
