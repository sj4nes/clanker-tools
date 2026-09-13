# isometry_characterisation

## Type
theorem

## Statement
For a linear T on a finite-dimensional inner product space the following are equivalent: T preserves the norm (||Tv|| = ||v||); T preserves the inner product (<Tv,Tw> = <v,w>); T^*T = I; T maps some (hence every) orthonormal basis to an orthonormal basis.

## Symbols
- `T` — a linear map on a finite-dimensional inner product space

## Epistemic status
proved_theorem  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
induced_norm, inner_product, orthogonal_matrix, polarisation_identity

## Hypotheses
T linear, V finite-dimensional

## Proof provenance
technique: norm-preserving implies inner-product-preserving by polarisation; inner-product-preserving says <T^*Tv, w> = <v,w> for all w, hence T^*T = I; the basis statement by direct computation
derives_from: polarisation_identity
lean_status: cited

## Type / well-formedness check
Well-formed. The step from norm-preservation to inner-product-preservation is POLARISATION, which is why the node depends on polarisation_identity and hence indirectly on char != 2.

## Specialization / boundary cases
- T orthogonal/unitary: the matrix form of the theorem
- T a permutation of an orthonormal basis: an isometry

## Hypothesis-dropped counterexamples
- **linearity**: the Mazur-Ulam phenomenon aside, a NONLINEAR norm-preserving map need not preserve inner products -- e.g. any norm-preserving bijection of the sphere that is not a rotation
- **finite_dimensionality**: in infinite dimension T^*T = I (an isometry) does NOT give TT^* = I: the right shift on l^2 is a non-surjective isometry. Surjectivity is an extra hypothesis there, supplied automatically here by injective_surjective_equivalence
- **char_two**: polarisation fails, so norm-preservation would not recover the form

## Common misuse
- assuming an isometry is invertible in infinite dimension (the shift again)
- using a real polarisation argument over C

## Related nodes (non-prerequisite)
- special_case_of: cauchy_schwarz

## Sources
axler_lada_4e
