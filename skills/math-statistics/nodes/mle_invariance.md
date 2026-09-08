# mle_invariance

## Type
proposition

## Statement
If theta_hat is an MLE of theta and g is any function, then g(theta_hat) is an MLE of g(theta) (using the induced / profile likelihood L*(eta) = sup_{g(theta) = eta} L(theta)).

## Symbols
- `g` — an arbitrary function of the parameter (need not be one-to-one)
- `L*(eta) = sup_{theta: g(theta) = eta} L(theta)` — the induced likelihood, whose maximizer is g(theta_hat)

## Epistemic status
proposition  ·  regime: exact

## Prerequisites (tsort edges into this node)
maximum_likelihood_estimator, prob_continuous_mapping

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: the maximizer of the induced likelihood L*(eta) = sup_{g(theta)=eta} L(theta) is attained at eta = g(theta_hat)
derives_from: prob_continuous_mapping
lean_status: core — argmax g(argmax L) = argmax L* is a set-identity; the 1-D monotone case is proof-checks.lean Stat.mle_invariance_monotone

## Type / well-formedness check
A closure property of the argmax under composition. For non-injective g one adopts the induced-likelihood definition and the property holds by construction.

## Specialization / boundary cases
- MLE of sigma is sqrt of the MLE of sigma^2 (which uses divisor n)
- MLE of the odds p/(1-p) is Xbar/(1-Xbar)
- MLE of P(X > c) in N(mu, sigma^2) is 1 - Phi((c - Xbar)/sigma_hat)

## Hypothesis-dropped counterexamples
- **bias_is_not_preserved**: invariance is about the argmax, NOT about unbiasedness -- g(theta_hat) is typically biased even if theta_hat was unbiased (Jensen). E.g. sqrt(S^2) is a biased estimator of sigma.

## Common misuse
- assuming the delta-method standard error transfers without the |g'| factor
- expecting g(UMVUE) to be the UMVUE of g(theta) -- invariance is an MLE property, not a UMVUE property

## Related nodes (non-prerequisite)
- uses: maximum_likelihood_estimator

## Sources
casella_berger_2e, zehna_1966
