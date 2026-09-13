# steinitz_exchange

## Type
lemma

## Statement
If (u_1,...,u_m) is linearly independent in V and (w_1,...,w_n) spans V, then m <= n; moreover the u's can be exchanged into the spanning list, so that (u_1,...,u_m, w_{i_1},...,w_{i_{n-m}}) still spans V.

## Symbols
- `m` — length of the independent list
- `n` — length of the spanning list

## Epistemic status
proved_lemma  ·  field_scope: any_field

## Prerequisites (tsort edges into this node)
basis, dependence_lemma, finite_dimensional, induction_principle

## Hypotheses
(u_i) independent, (w_j) spans V, both lists finite

## Proof provenance
technique: induction on m: adjoin u_1 to the spanning list making it dependent, apply dependence_lemma to remove some w, and repeat. The removed vector is always a w, not a previously inserted u, because the u's are independent
derives_from: dependence_lemma
lean_status: cited

## Type / well-formedness check
Well-formed. The inequality m <= n is the whole engine of dimension theory: it is the statement that no independent family can be longer than any spanning family.

## Specialization / boundary cases
- m = 1: any single nonzero vector can replace some member of a spanning list
- m = n: the u's themselves then span, which is the 'n independent vectors in an n-dimensional space form a basis' corollary

## Hypothesis-dropped counterexamples
- **independence_of_the_u**: without it the bound is false: in F^1, (1, 1, 1) is a 'longer than spanning' list precisely because it is dependent
- **finiteness**: in F[t], (1, t, t^2, ...) is independent and infinite while no finite list spans -- the inequality is vacuous, and dimension theory must be redone with cardinals

## Common misuse
- reading it as 'any independent set extends to a basis' -- that is basis_existence_finite, a consequence
- using it to compare two INDEPENDENT lists: it compares independent against spanning

## In the wild
- the source of every 'you cannot have more than n independent constraints in n dimensions' argument, including the rank bound in statistics and the degrees-of-freedom count in ANOVA

## Related nodes (non-prerequisite)
- required_by: dimension_well_defined

## Sources
axler_lada_4e, hoffman_kunze_2e
