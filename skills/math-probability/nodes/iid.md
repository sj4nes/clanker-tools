# iid

## Type
definition

## Statement
A sequence (X_n) is independent and identically distributed if the X_n are mutually independent and all have the same law. The canonical hypothesis of the laws of large numbers and the classical CLT.

## Symbols
- `(X_n)` — an iid sequence, type: N -> (Omega -> R)
- `P_{X_1}` — the common law, type: probability measure on B(R)

## Epistemic status
definition

## Prerequisites (tsort edges into this node)
distribution_pushforward, independence_random_variables

## Hypotheses
(none — unconditional within scope)

## Well-definedness
the infinite product measure (P_{X_1})^{tensor N} on (R^N, B(R)^{tensor N}) exists (Kolmogorov extension) and realizes an iid sequence via coordinate projections.

## Type / well-formedness check
'identically distributed' constrains the marginals; 'independent' constrains the dependence. An iid sequence on a single probability space exists for any law (product / Kolmogorov extension construction).

## Specialization / boundary cases
- repeated independent trials of one experiment (coin, die, measurement with iid noise)
- the empirical distribution of an iid sample converges to P_{X_1} (Glivenko-Cantelli)
- a random sample in statistics IS an iid sequence (design permitting)

## Hypothesis-dropped counterexamples
- **identically_distributed**: independent but not identical: the Lindeberg CLT (lindeberg_clt) is what replaces 'identical' for a non-degenerate limit
- **independence**: identically distributed but dependent (e.g. a stationary time series): the LLN can still hold (ergodic theorem) but the CLT rate and variance change (long-range dependence)

## Common misuse
- assuming survey / observational data is iid when there is clustering, time trend, or selection
- treating 'identically distributed' as 'independent' or vice versa

## Related nodes (non-prerequisite)
- hypothesis_of: weak_law_large_numbers, strong_law_large_numbers, central_limit_theorem
- constructed_by: kolmogorov_extension_theorem

## Sources
billingsley_probability_measure, durrett_pte
