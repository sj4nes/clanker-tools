# smith_normal_form_boundary

## Type
theorem

## Statement
STATED, OUT OF SCOPE: over a principal ideal domain R, every finitely generated module is a direct sum of cyclic modules R/(d_1) (+) ... (+) R/(d_k) (+) R^f with d_1 | d_2 | ... | d_k. Specialising R = F[t] to the module V made into an F[t]-module by t acting as T gives the RATIONAL and JORDAN canonical forms; specialising R = Z gives the classification of finitely generated abelian groups, and the Smith normal form of an integer matrix.

## Symbols
- `d_i` — the invariant factors
- `R^f` — the free part, f its rank

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
jordan_normal_form, primary_decomposition, rref_uniqueness

## Hypotheses
R a PID, M finitely generated

## Proof provenance
technique: cited; the proof is the structure theorem for finitely generated modules over a PID, developed in a graduate algebra course and out of scope for this release
derives_from: primary_decomposition
lean_status: stated_not_proved

## Type / well-formedness check
Well-formed as a statement of module theory. It is the SINGLE theorem that explains why row reduction over a field gives RREF (rref_uniqueness) and over Z gives Smith normal form -- two canonical forms that look unrelated until this common generalisation.

## Specialization / boundary cases
- R = F a field: every module is free, invariant factors are trivial, and the theorem degenerates to 'every vector space has a basis' -- which is why linear algebra over a field is so much simpler
- R = F[t] with t acting as T: the invariant factors are the invariant factors of T, the last one being m_T; the primary decomposition into (t - lambda)^k pieces is exactly jordan_normal_form
- R = Z: finitely generated abelian groups, and the Smith normal form diag(d_1,...,d_r,0,...) of an integer matrix

## Hypothesis-dropped counterexamples
- **R_being_a_PID**: over a non-PID such as Z[x] or F[x,y] the structure theorem fails; modules can be badly behaved and no canonical form exists
- **finite_generation**: an infinitely generated module over a PID need not decompose (the rationals Q as a Z-module are not a direct sum of cyclics)

## Common misuse
- expecting a Jordan-like form over a general commutative ring
- treating this release's jordan_normal_form as proved: it is stated, and its natural proof is this theorem

## Related nodes (non-prerequisite)
- generalizes: jordan_normal_form, rref_uniqueness

## Sources
dummit_foote_3e, lang_algebra_3e
