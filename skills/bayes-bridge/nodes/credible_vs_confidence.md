# credible_vs_confidence

## Type
diagnostic

## Statement
Worked side-by-side on the same problem — a Normal mean `theta`, known
variance `sigma^2`, flat (improper uniform) prior — the 95% credible
interval (`credible_interval_cited`) and the 95% confidence interval
(`normal_mean_ci_known_variance_cited`) are the *same numeric interval*,
`xbar +- 1.96 sigma/sqrt(n)`, but say different things: the credible
interval is a probability-1-alpha statement about `theta` given the observed
`x` (`theta` random, interval fixed by the data); the confidence interval is
a coverage statement about the procedure across repeated samples (`theta`
fixed, interval random). `bernstein_von_mises_cited` is the node explaining
*why* the numeric coincidence is not an accident under regularity and large
`n` — it does not hold in general (informative priors, small samples,
non-regular models all break the coincidence while both intervals remain
individually well-defined).

## Symbols
- `theta`: the normal mean, real, fixed (confidence view) or random
  (credible view — the same symbol, two readings)
- `sigma^2`: known variance
- `xbar`, `n`: sample mean and size

## Epistemic status
proposition (the numeric coincidence under a flat prior is a computed fact
about this specific case; the interpretive contrast is definitional, not a
theorem to prove).

## Prerequisites (tsort edges into this node)
credible_interval_cited, normal_mean_ci_known_variance_cited,
coverage_probability_cited, bernstein_von_mises_cited,
posterior_prop_prior_times_likelihood

## Hypotheses
Flat (improper) prior on `theta` for the coincidence case; known `sigma^2`
in both intervals' formulas.

## Proof provenance
technique: direct computation — under `pi(theta) = 1`, the posterior from
`posterior_prop_prior_times_likelihood` is exactly `N(xbar, sigma^2/n)`, whose
central 95% region is `xbar +- 1.96 sigma/sqrt(n)`, matching
`normal_mean_ci_known_variance_cited` termwise.
derives_from: posterior_prop_prior_times_likelihood.
lean_status: not_attempted; `bc` instance check at concrete `(xbar, sigma, n)`.

## Type / well-formedness check
Both intervals are `[lower, upper] subset R`; `coverage_probability_cited`
is a function of `theta`, the credible interval's `1-alpha` is a function of
`x` — different domains, checked not to be silently conflated. Checked:
`validation/type-checks.md#credible_vs_confidence`.

## Specialization / boundary cases
Informative prior (`tau0^2` finite, not flat): from `conjugate_families`'s
Normal-Normal case, the credible interval shifts toward the prior mean and
narrows relative to `tau0^2`; the confidence interval is unaffected (it
never used a prior) — the two now numerically diverge, the general case
`bernstein_von_mises_cited` says converges back as `n -> infinity`.

## Hypothesis-dropped counterexamples
Drop "known variance": both interval formulas change (to `t`-based and
posterior-predictive forms respectively) but the same contrast pattern
holds; out of scope to re-derive here (0.1 fixes known variance throughout).
Drop "flat prior": see the specialization case above — the coincidence is
specifically a flat-prior phenomenon, not a general equivalence of the two
interval types.

## Common misuse
Interpreting a 95% confidence interval as "95% probability `theta` is in
this interval" — that is the credible interval's reading, not the
confidence interval's; the two only *coincide numerically*, under a flat
prior, not *interpretively*, ever.

## Related nodes (non-prerequisite)
contrasts_with: `normal_mean_ci_known_variance_cited` (see
`edges/relations.tsv`).

## Sources
[gelman_bda3] §4.1 (credible vs. confidence interpretation);
[wasserman_all_of_statistics] §11.9 (the flat-prior coincidence).
