# normal_variance_ci

## Type
proposition

## Statement
For X_1..X_n iid N(mu, sigma^2), the interval ( (n-1)S^2 / chi^2_{n-1, 1-alpha/2},  (n-1)S^2 / chi^2_{n-1, alpha/2} ) has coverage exactly 1 - alpha for sigma^2. It is asymmetric about S^2.

## Symbols
- `chi^2_{n-1, q}` — the q-quantile of chi^2_{n-1}
- `asymmetry` — the chi^2 distribution is right-skewed, so the interval is not S^2 +- something

## Epistemic status
proposition  ·  regime: exact

## Prerequisites (tsort edges into this node)
pivot_method, scaled_sample_variance_chi_squared

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: pivot method with Q = (n-1)S^2/sigma^2 ~ chi^2_{n-1}
derives_from: scaled_sample_variance_chi_squared
lean_status: core

## Type / well-formedness check
Exact under normality. Invert the pivot (n-1)S^2/sigma^2 ~ chi^2_{n-1}. Equal-tailed is conventional but far from shortest for small n.

## Specialization / boundary cases
- take sqrt of the endpoints for a CI on sigma (the SD)
- n = 10, alpha = 0.05: the interval spans roughly (0.47 S^2, 3.3 S^2) -- variance is hard to pin down
- the shortest 1 - alpha interval uses unequal tail probabilities chosen to minimize length

## Hypothesis-dropped counterexamples
- **normality**: THIS PROCEDURE HAS NO ROBUSTNESS. For data with kurtosis != 3 (any non-normal shape) the coverage can be far from 1 - alpha even for large n, because (n-1)S^2/sigma^2 is not chi^2_{n-1} and its shape depends on the 4th moment. Use a bootstrap or a kurtosis-corrected interval.

## Common misuse
- using it for a variance CI with visibly non-normal data -- unlike the t-interval for the mean, this one does not self-correct via the CLT at usual n
- reporting a symmetric S^2 +- interval

## Related nodes (non-prerequisite)
- uses: pivot_method, scaled_sample_variance_chi_squared

## Sources
casella_berger_2e
