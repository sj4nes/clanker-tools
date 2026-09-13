# parallelogram_law

## Type
identity

## Statement
||u+v||^2 + ||u-v||^2 = 2||u||^2 + 2||v||^2. It CHARACTERISES induced norms: a norm satisfies it if and only if it comes from an inner product (Jordan-von Neumann).

## Symbols
- `u, v` — arbitrary vectors

## Epistemic status
mathematical_identity  ·  field_scope: real_or_complex

## Prerequisites (tsort edges into this node)
induced_norm, inner_product

## Hypotheses
induced norm for the identity; a general norm for the characterisation

## Proof provenance
technique: expand both squared norms via <u+v,u+v> and <u-v,u-v> and add: the cross terms cancel. The Jordan-von Neumann converse (recovering the inner product by polarisation and verifying bilinearity) is CITED
derives_from: induced_norm
lean_status: dim_core — LinAlg.parallelogram (n = 2)

## Type / well-formedness check
Well-formed. The identity direction is a one-line expansion; the CHARACTERISATION (the converse) is cited, not proved here.

## Specialization / boundary cases
- v = 0: reduces to 2||u||^2 = 2||u||^2
- u perp v: combined with pythagorean_theorem it gives ||u+v|| = ||u-v||

## Hypothesis-dropped counterexamples
- **the_norm_being_induced**: on R^2 with the 1-norm, take u = (1,0), v = (0,1): ||u+v||_1 = 2 and ||u-v||_1 = 2, so the left side is 8, while the right side is 2 + 2 = 4. The 1-norm comes from no inner product -- this is the standard witness

## Common misuse
- assuming every norm supports orthogonality and projection: the parallelogram law is the exact test, and it fails for all p-norms except p = 2

## Related nodes (non-prerequisite)
- required_by: polarisation_identity

## Sources
axler_lada_4e, jordan_von_neumann_1935
