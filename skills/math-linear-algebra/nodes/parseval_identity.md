# parseval_identity

## Type
theorem

## Statement
For an orthonormal BASIS (e_1,...,e_n): ||v||^2 = sum_i |<v,e_i>|^2, and more generally <u,v> = sum_i <u,e_i> conj(<v,e_i>). Coordinates in an orthonormal basis are an ISOMETRY onto F^n.

## Symbols
- `(e_i)` — an orthonormal BASIS, not merely an orthonormal set

## Epistemic status
proved_theorem  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
basis_unique_representation, bessel_inequality, finite_dimensional, orthonormal_basis

## Hypotheses
(e_i) an orthonormal basis, V finite-dimensional

## Proof provenance
technique: expand v = sum <v,e_i> e_i and compute <u,v> using orthonormality; every cross term vanishes
derives_from: bessel_inequality
lean_status: cited

## Type / well-formedness check
Well-formed. The statement is that the coordinate map is not just a linear isomorphism (coordinate_isomorphism) but an ISOMETRY -- it preserves the inner product, not only the linear structure.

## Specialization / boundary cases
- V = F^n with the standard basis: the identity is the definition of the norm
- the Fourier series case: sum |c_n|^2 = (1/2pi) integral |f|^2, the classical Parseval theorem -- infinite-dimensional and CITED

## Hypothesis-dropped counterexamples
- **spanning**: for a non-spanning orthonormal set only Bessel's INEQUALITY holds; the deficit is the squared distance to the span
- **completeness_in_infinite_dimension**: an orthonormal set can be maximal yet fail Parseval in an INCOMPLETE inner product space -- completeness is what upgrades maximal-orthonormal to Parseval, and this capsule does not develop it

## Common misuse
- applying Parseval to a truncated basis (that is Bessel)
- assuming a maximal orthonormal set in an infinite-dimensional space satisfies Parseval without completeness

## In the wild
- the energy-preservation property of the Fourier and wavelet transforms; the decomposition of total variance into orthogonal components in PCA and ANOVA

## Related nodes (non-prerequisite)
- special_case_of: bessel_inequality

## Sources
axler_lada_4e
