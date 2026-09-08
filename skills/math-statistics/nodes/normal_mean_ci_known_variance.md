# normal_mean_ci_known_variance

## Type
proposition

## Statement
For X_1..X_n iid N(mu, sigma^2) with sigma^2 KNOWN, the interval Xbar +- z_{1-alpha/2} sigma / sqrt(n) has coverage exactly 1 - alpha for every mu.

## Symbols
- `z_{1-alpha/2}` — the upper alpha/2 quantile of N(0,1) (1.96 for alpha = 0.05)

## Epistemic status
proposition  ·  regime: exact

## Prerequisites (tsort edges into this node)
pivot_method, prob_normal, prob_standard_normal, sample_mean

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: pivot method with Q = sqrt(n)(Xbar - mu)/sigma ~ N(0,1)
derives_from: pivot_method
lean_status: core

## Type / well-formedness check
Exact. Invert the pivot sqrt(n)(Xbar - mu)/sigma ~ N(0,1). Width 2 z sigma/sqrt(n) is NON-random (sigma known) -- the only randomness is the center.

## Specialization / boundary cases
- alpha = 0.05: Xbar +- 1.96 sigma/sqrt(n)
- the 'margin of error' of a poll (with sigma^2 = p(1-p) plugged in) -- a slight abuse since sigma^2 is then estimated
- sample size for a target width w: n = (2 z sigma / w)^2

## Hypothesis-dropped counterexamples
- **sigma_known**: sigma is essentially never known; using an estimate S in the z-interval undercovers at small n -- that is exactly why the t-interval exists (normal_mean_ci_unknown_variance)
- **normality**: for non-normal data the coverage is approximate (1 - alpha + O(n^{-1/2}) by the CLT), reasonable for large n

## Common misuse
- plugging S for sigma and keeping z (rather than t) at small n
- treating the realized interval's endpoints as a 95%-probable range for mu

## Related nodes (non-prerequisite)
- uses: pivot_method, sample_mean
- approximated_by: 

## Sources
casella_berger_2e
