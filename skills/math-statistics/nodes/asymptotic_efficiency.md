# asymptotic_efficiency

## Type
definition

## Statement
A sqrt(n)-asymptotically-normal estimator is (asymptotically) efficient if its asymptotic variance equals the Cramer-Rao bound I(theta)^{-1} for every theta.

## Symbols
- `I(theta)^{-1}` — the inverse Fisher information -- the smallest asymptotic variance a regular estimator can have

## Epistemic status
definition  ·  regime: asymptotic

## Prerequisites (tsort edges into this node)
asymptotic_variance, cramer_rao_lower_bound, fisher_information

## Hypotheses
fisher_information_positive_definite

## Proof provenance
technique: the MLE achieves it (mle_asymptotic_normality); the Hajek convolution / LAM theorems show no regular estimator can do better
derives_from: cramer_rao_lower_bound
lean_status: cited

## Type / well-formedness check
Ties an estimator to the information bound. Under regularity the MLE is efficient. The Hodges 'superefficient' estimator beats I^{-1} at a single point but at the cost of exploding risk nearby -- which is why the definition demands the equality for EVERY theta and modern theory uses the local-asymptotic-minimax formulation (see local_asymptotic_minimax).

## Specialization / boundary cases
- MLE under regularity: efficient
- method-of-moments: efficient only when the moment equations coincide with the score (exponential family, natural parametrization)
- one-step Newton from a sqrt(n)-consistent start: efficient (the 'one-step estimator')

## Hypothesis-dropped counterexamples
- **for_all_theta**: Hodges' estimator (shrink Xbar to 0 when |Xbar| < n^{-1/4}) has asymptotic variance 0 at theta = 0 and sigma^2 elsewhere -- 'superefficient' at one point, but its finite-sample maximum risk blows up near 0. Superefficiency on a Lebesgue-null set is the only way to beat I^{-1}, and it is not a free lunch.

## Common misuse
- reading 'efficient' as 'best at every finite n' -- it is a large-n statement
- assuming an efficient estimator is also robust or admissible

## Related nodes (non-prerequisite)
- required_by: hajek_convolution_theorem
- uses: cramer_rao_lower_bound, fisher_information

## Sources
van_der_vaart_asymptotic, lehmann_casella_tpe
