# basu_theorem

## Type
theorem

## Statement
If T is a complete sufficient statistic for theta and A is an ancillary statistic, then T and A are independent (under every P_theta).

## Symbols
- `T` — complete sufficient statistic
- `A` — ancillary statistic
- `T _||_ A` — statistical independence, for every theta

## Epistemic status
proved_theorem  ·  regime: exact

## Prerequisites (tsort edges into this node)
ancillary_statistic, completeness_statistic, prob_independence_rv, sufficiency

## Hypotheses
completeness_statistic, sufficiency

## Proof provenance
technique: ancillarity gives a constant marginal; completeness upgrades 'constant in mean' to 'constant a.s.', i.e. independence
derives_from: completeness_statistic
lean_status: core — validation/proof-checks.lean Stat.basu_step -- E[h(T)] = 0 for all theta and h = P(A in B|T) - c forces h = 0, hence independence

## Type / well-formedness check
An independence conclusion. Proof: for any event B for A, P_theta(A in B) is a constant c (ancillarity); E_theta[ P(A in B | T) - c ] = 0 for all theta; completeness forces P(A in B | T) = c a.s., i.e. A _||_ T.

## Specialization / boundary cases
- N(mu, sigma^2) sigma^2 known: Xbar (complete sufficient for mu) _||_ S^2 (ancillary for mu). Gives Xbar _||_ S^2 with NO Jacobian computation.
- uniform(0, theta): X_(n) (complete sufficient) _||_ (X_(1)/X_(n), ..., X_(n-1)/X_(n)) (ancillary ratios)
- exponential(rate): sum X_i _||_ (X_1/sum X_i, ..., X_n/sum X_i) -- the normalized spacings

## Hypothesis-dropped counterexamples
- **completeness_statistic**: drop completeness (curved family, or restricted parameter): T and A can be dependent even though A is ancillary and T is sufficient -- the standard Xbar _||_ S^2 shortcut is not available
- **sufficiency**: if T is complete but not sufficient the argument's first step (constant conditional given T) has no reason to hold

## Common misuse
- using Basu to claim independence of two statistics neither of which is ancillary (S^2 and Xbar for UNKNOWN sigma^2 -- S^2 is not ancillary for sigma^2, so Basu does not apply to that pair; independence there is a separate fact)
- forgetting the conclusion is independence for EVERY theta, a strong statement

## In the wild
- the cleanest proof that the t-statistic's numerator and denominator are independent, hence that it has a t distribution
- deriving moments of ratios (E[X_(1)/X_(n)] etc.) by factoring the joint expectation

## Related nodes (non-prerequisite)
- proof_route_for: normal_sample_mean_variance_independence
- requires: completeness_statistic, ancillary_statistic

## Sources
basu_1955, lehmann_casella_tpe
