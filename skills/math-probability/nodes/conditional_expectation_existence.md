# conditional_expectation_existence

## Type
theorem

## Statement
For every X in L^1(Omega, F, P) and every sub-sigma-algebra G subset F, E[X | G] exists and is P-a.s. unique.

## Symbols
- `X` — an integrable random variable, type: L^1(P)
- `G` — a sub-sigma-algebra, type: sigma-algebra subset F

## Epistemic status
proved_theorem

## Prerequisites (tsort edges into this node)
conditional_expectation_abstract, lp_space, radon_nikodym

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: Radon-Nikodym on (Omega, G, P|_G) applied to the finite signed measure A |-> integral_A X dP; uniqueness because two versions Z_1, Z_2 have integral_A (Z_1 - Z_2) = 0 for all A in G, forcing Z_1 = Z_2 a.s. (take A = {Z_1 > Z_2})
derives_from: radon_nikodym
lean_status: cited — Williams Thm 9.2; Durrett Thm 4.1.1

## Type / well-formedness check
two standard constructions: (a) Radon-Nikodym -- nu(A) = integral_A X dP is a (signed) measure on (Omega, G) with nu << P|_G, so nu has a G-measurable density, which is E[X|G]; (b) for X in L^2, orthogonal projection onto the closed subspace L^2(G), then extend to L^1 by density and monotonicity.

## Specialization / boundary cases
- X in L^2: E[X | G] is the L^2-orthogonal projection of X onto L^2(Omega, G, P) -- the geometric picture
- X = 1_B: E[1_B | G] is the 'conditional probability' P(B | G), a G-measurable [0,1]-valued random variable

## Hypothesis-dropped counterexamples
- **integrability_of_X**: without X in L^1 (or X >= 0), the signed measure A |-> integral_A X dP may not be finite and Radon-Nikodym does not apply directly
- **sigma_finiteness_is_automatic**: P|_G is a probability measure, so the sigma-finiteness hypothesis of Radon-Nikodym is free here

## Common misuse
- assuming a REGULAR conditional distribution always exists (it does on Polish spaces; the a.s.-unique random variable E[X|G] always exists, the measure-valued version needs more)
- expecting a canonical pointwise version

## Related nodes (non-prerequisite)
- uses: radon_nikodym, lp_space
- defines: conditional_expectation_abstract

## Sources
williams_probability_martingales, durrett_pte
