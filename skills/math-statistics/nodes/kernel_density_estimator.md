# kernel_density_estimator

## Type
definition

## Statement
The kernel density estimator of f from X_1, ..., X_n is f_hat_h(x) = (1/(n h)) sum_{i=1}^n K( (x - X_i) / h ), where K is a kernel (a symmetric density, e.g. Gaussian or Epanechnikov) and h > 0 is the bandwidth.

## Symbols
- `K` — the kernel, type: symmetric probability density with int u^2 K(u) du = kappa_2 < inf
- `h` — the bandwidth / smoothing parameter -- the crucial tuning knob
- `f_hat_h` — a genuine density (integrates to 1) if K is

## Epistemic status
definition  ·  regime: distribution_free

## Prerequisites (tsort edges into this node)
iid_sample, prob_pdf

## Hypotheses
(none — unconditional within scope)

## Proof provenance
technique: E[f_hat_h(x)] = (K_h * f)(x), a convolution smoothing of f; Var[f_hat_h(x)] = (n h)^{-1} f(x) R(K) + O(1/n)
derives_from: kde_bias_variance_tradeoff
lean_status: core

## Type / well-formedness check
A statistic-valued function; a smoothed version of the empirical measure. It is biased for f (unlike the ECDF for F) -- density estimation is genuinely nonparametric, with a bias-variance tradeoff controlled by h (kde_bias_variance_tradeoff).

## Specialization / boundary cases
- h -> 0 with n h -> inf: f_hat_h(x) -> f(x) in probability at each continuity point
- the choice of K barely matters (efficiency within a few %); the choice of h matters enormously
- multivariate KDE suffers the curse of dimensionality -- the rate degrades to n^{-2/(4+d)}

## Hypothesis-dropped counterexamples
- **h_chosen_well**: h too small: f_hat is a spiky mess (n bumps); h too large: f_hat is oversmoothed and hides real features (bimodality). There is no h that is right everywhere if f has varying curvature -- adaptive bandwidths address this.
- **f_smooth**: if f has a discontinuity or a kink (uniform density's edges, an exponential at 0) the KDE smears it and the bias there is O(1), not O(h^2) -- boundary bias

## Common misuse
- using the default bandwidth (often Silverman's rule, optimal only for near-Gaussian f) on a clearly multimodal or skewed sample
- reading small wiggles in a KDE as real structure
- KDE near a hard boundary (nonnegative data at 0) without a boundary correction

## In the wild
- exploratory data visualization (the smooth alternative to a histogram); the violin plot is a KDE
- naive Bayes classifiers with continuous features; density-ratio estimation; the Parzen-window classifier

## Related nodes (non-prerequisite)
- required_by: kde_bias_variance_tradeoff
- uses: prob_pdf

## Sources
silverman_density_estimation, wand_jones_kernel_smoothing, tsybakov_nonparametric
