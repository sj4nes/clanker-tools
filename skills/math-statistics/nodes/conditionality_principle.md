# conditionality_principle

## Type
regime

## Statement
The conditionality principle: if the experiment actually performed was selected by a random mechanism ANCILLARY to theta (a mixture of experiments), then inference should be conditional on which experiment was in fact run, ignoring the ones that were not.

## Symbols
- `a mixture experiment` — flip a coin; heads -> measure with the precise instrument, tails -> the crude one
- `the ancillary statistic` — which experiment was chosen -- its law is free of theta

## Epistemic status
heuristic  ·  regime: exact

## Prerequisites (tsort edges into this node)
ancillary_statistic, iid_sample, prob_marginal_distribution

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: the choice of experiment carries no information about theta (ancillary); averaging over unrealized experiments dilutes the analysis with irrelevant variability
derives_from: ancillary_statistic
lean_status: cited

## Type / well-formedness check
A normative principle. It says the relevant reference set for a frequentist calculation is 'repetitions of the experiment I actually did', not 'repetitions of the random choice of experiment'. Widely (not universally) accepted.

## Specialization / boundary cases
- the classic example (Cox 1958): a measurement is made by a randomly chosen instrument of known, different precisions -- report the SE of the instrument used, not a mixture SE
- conditioning on the observed information (rather than expected) in likelihood inference is a conditionality-principle move (Efron-Hinkley)
- conditioning on ancillary configuration statistics in location-scale models -> exact conditional inference (Fisher, Fraser)

## Hypothesis-dropped counterexamples
- **the_selector_is_ancillary**: if which 'experiment' is run depends on theta (informative sampling, response-adaptive designs), conditioning on it can bias the analysis -- the principle applies only to theta-ancillary selection

## Common misuse
- conditioning on a statistic that is only approximately ancillary and ignoring the approximation
- using it to justify ignoring a genuinely informative selection mechanism

## Related nodes (non-prerequisite)
- uses: ancillary_statistic, iid_sample
- required_by: likelihood_principle

## Sources
cox_1958, birnbaum_1962, berger_wolpert_likelihood_principle
