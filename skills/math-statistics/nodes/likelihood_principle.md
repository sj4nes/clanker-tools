# likelihood_principle

## Type
regime

## Statement
The likelihood principle: all the evidence about theta contained in the data x is captured by the likelihood function L(theta; x), up to a positive multiplicative constant; two experiments yielding proportional likelihoods for theta warrant identical inference. Birnbaum's theorem: sufficiency + conditionality together IMPLY the likelihood principle.

## Symbols
- `proportional` — L(theta; x_1) = c(x_1, x_2) L(theta; x_2) for all theta, with c > 0 free of theta
- `the tension` — Bayesian and pure-likelihood methods obey it; frequentist methods using tail areas (p-values, confidence intervals, unbiasedness) generally VIOLATE it

## Epistemic status
heuristic  ·  regime: bayesian

## Prerequisites (tsort edges into this node)
conditionality_principle, likelihood_function, sufficiency_principle

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: Birnbaum 1962: the sufficiency principle and the conditionality principle jointly entail the likelihood principle; the proof is a short combinatorial argument on mixture experiments (though its premises have been re-examined, e.g. Evans 2013, Mayo 2014)
derives_from: sufficiency_principle
lean_status: cited

## Type / well-formedness check
A strong, contested normative principle. Its bite: the stopping rule of a sequential experiment is irrelevant to the evidence (only the observed likelihood matters), which conflicts with frequentist error control. Birnbaum's derivation from two mild-seeming principles is the surprise.

## Specialization / boundary cases
- binomial vs negative-binomial sampling giving the same observed (successes, failures): the likelihoods are proportional, so a likelihoodist / Bayesian analysis is identical -- but the frequentist p-value DIFFERS (different sample spaces)
- sequential trials: under the likelihood principle, 'we stopped when it looked significant' does not change the evidence in the observed data -- diametrically opposed to frequentist alpha-spending
- fully obeyed by Bayesian posteriors and by pure-likelihood (Royall) inference

## Hypothesis-dropped counterexamples
- **accepting_both_premises_unrestrictedly**: the principle is CONTESTED. Frequentists reject it (or reject one of Birnbaum's premises) precisely because it outlaws pre-data error-rate control; Mayo (2014) and others dispute the theorem's premises. This node states the principle and the theorem; it does not adjudicate.

## Common misuse
- citing the likelihood principle as settled fact -- it is a genuine, live foundational dispute
- using it to dismiss all concern about stopping rules / multiplicity in a frequentist analysis (which does not accept the principle)

## Related nodes (non-prerequisite)
- uses: likelihood_function, sufficiency_principle, conditionality_principle
- equivalent_to: sufficiency_principle

## Sources
birnbaum_1962, berger_wolpert_likelihood_principle, mayo_2014
