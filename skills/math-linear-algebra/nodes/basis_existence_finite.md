# basis_existence_finite

## Type
theorem

## Statement
If V is finite-dimensional then every finite spanning set CONTAINS a basis, and every linearly independent list EXTENDS to a basis. CHOICE-FREE: both processes terminate after finitely many steps.

## Symbols
- `S` — a finite spanning set
- `L` — an independent list

## Epistemic status
proved_theorem  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
basis, dependence_lemma, finite_dimensional

## Hypotheses
V finite-dimensional

## Proof provenance
technique: contains: repeatedly apply dependence_lemma to delete a redundant vector; the list is finite so this halts. Extends: adjoin any vector outside the current span, which preserves independence; Steinitz bounds the number of steps
derives_from: dependence_lemma
lean_status: partial — LinAlg.list_induction_skeleton -- the termination skeleton only; the dependence-lemma step is not formalised

## Type / well-formedness check
Well-formed. The choice-freeness is a real content claim, not a technicality: it is what distinguishes this from basis_existence_general.

## Specialization / boundary cases
- S already independent: the basis is S itself
- L empty: extending the empty list yields a basis from scratch

## Hypothesis-dropped counterexamples
- **finite_dimensionality**: for an infinite-dimensional V the deletion process need not halt and the extension process needs transfinite recursion -- i.e. Zorn. See basis_existence_general, whose choice grade is needs_full_AC

## Common misuse
- believing every vector space has a CONSTRUCTIBLE basis: this theorem gives one only in the finitely generated case

## Related nodes (non-prerequisite)
- generalizes: 
- contrasts_with: basis_existence_general

## Sources
axler_lada_4e
