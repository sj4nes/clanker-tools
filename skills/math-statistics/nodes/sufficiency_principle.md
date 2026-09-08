# sufficiency_principle

## Type
regime

## Statement
The sufficiency principle: if T is a sufficient statistic for theta and T(x) = T(y) for two data sets x, y, then x and y must lead to the same inference about theta.

## Symbols
- `'the same inference'` — the same point estimate, interval, test decision, posterior -- whatever the inferential output is

## Epistemic status
heuristic  ·  regime: exact

## Prerequisites (tsort edges into this node)
neyman_fisher_factorization, sufficiency

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: the likelihood function depends on the data only through T (Neyman-Fisher factorization), and most inference schools agree inference should depend on the data only through the likelihood-relevant part
derives_from: neyman_fisher_factorization
lean_status: cited

## Type / well-formedness check
A normative principle, not a theorem. It is very widely accepted (nearly all standard methods obey it) and follows from the factorization of the likelihood through T.

## Specialization / boundary cases
- obeyed by MLE, Bayes, UMVUE, LRT -- all are functions of any sufficient statistic
- the basis for reducing a whole sample to (Xbar, S^2) in normal-theory inference with no loss

## Hypothesis-dropped counterexamples
- **none_all_hypotheses_essential**: the principle is a stance; there is nothing to 'drop'. A method violating it (e.g. one depending on the order in which iid data arrived) would be regarded as defective.

## Common misuse
- confusing it with the (much stronger, more contested) likelihood principle
- assuming a method is 'good' merely because it obeys sufficiency -- it is a minimal requirement

## Related nodes (non-prerequisite)
- uses: neyman_fisher_factorization, sufficiency
- required_by: likelihood_principle

## Sources
birnbaum_1962, berger_wolpert_likelihood_principle
