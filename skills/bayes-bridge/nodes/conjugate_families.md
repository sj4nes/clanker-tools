# conjugate_families

## Type
construction

## Statement
Three worked conjugate-prior/likelihood pairs, each closing
`posterior_prop_prior_times_likelihood` into an exact closed-form posterior
update, with the posterior mean reported as the natural point estimate
(`bayes_estimator_cited` / `posterior_mean_rule_cited`, squared loss).

**1. Beta–Bernoulli/Binomial.** Prior `theta ~ Beta(a, b)`. Data: `n`
Bernoulli(theta) trials with `s` successes. Posterior:
`theta | x ~ Beta(a + s, b + n - s)`.
Posterior mean: `(a+s) / (a+b+n)` — a weighted average of the prior mean
`a/(a+b)` (weight `a+b`) and the sample mean `s/n` (weight `n`).

**2. Normal–Normal, known variance.** Prior `theta ~ N(mu0, tau0^2)`. Data:
`x_1..x_n ~ N(theta, sigma^2)` i.i.d., `sigma^2` known. Posterior:
`theta | x ~ N(mu_n, tau_n^2)` with
`tau_n^2 = 1 / (1/tau0^2 + n/sigma^2)` and
`mu_n = tau_n^2 (mu0/tau0^2 + n xbar/sigma^2)`.
Posterior mean is again a precision-weighted average of the prior mean and
the sample mean.

**3. Gamma–Poisson.** Prior `theta ~ Gamma(a, b)` (shape `a`, rate `b`).
Data: `x_1..x_n ~ Poisson(theta)` i.i.d., sum `s = sum x_i`. Posterior:
`theta | x ~ Gamma(a + s, b + n)`.
Posterior mean: `(a+s) / (b+n)`, again prior/sample weighted by `b` vs `n`.

## Symbols
- `theta`: the parameter, type varies by instance (rate in [0,1], real mean,
  or positive rate)
- `a, b` (Beta/Gamma) or `mu0, tau0^2` (Normal): prior hyperparameters, fixed
  reals with the stated positivity constraints
- `x_1..x_n`: i.i.d. data, type per instance (Bernoulli outcome, real,
  nonnegative integer)
- `s`, `xbar`: sufficient statistics (sum of successes, sample mean)

## Epistemic status
constructive_result (each posterior is derived by direct algebraic
manipulation of `prior x likelihood`, not cited as a black box).

## Prerequisites (tsort edges into this node)
posterior_prop_prior_times_likelihood, conjugate_prior_cited,
bernoulli_distribution_cited, beta_distribution_cited,
normal_distribution_cited, gamma_distribution_cited,
poisson_distribution_cited, bayes_estimator_cited, posterior_mean_rule_cited

## Hypotheses
i.i.d. sampling within each instance; known variance in the Normal-Normal
case (the unknown-variance case, needing the Normal-Inverse-Gamma family, is
out of scope for 0.1 — see `scope.md`); positive hyperparameters.

## Proof provenance
technique: multiply the density kernels (`prior x likelihood`), drop
`theta`-free factors, recognize the resulting kernel as the named family
(standard "complete the square" for Normal-Normal, direct exponent
collection for the other two).
derives_from: posterior_prop_prior_times_likelihood.
lean_status: not attempted — these are algebraic density-kernel
manipulations, not identities suited to a Mathlib-free kernel check; the
`bc` instance checks below are the verification for this release.
bc_status: verified — see `validation/instance-checks.md#conjugate_families`.

## Type / well-formedness check
Each posterior is checked to stay in its prior's family (the defining
property of `conjugate_prior_cited`) and each hyperparameter update keeps the
domain constraints (Beta shape params `>0`, Gamma shape/rate `>0`, Normal
variance `>0`). Checked: `validation/type-checks.md#conjugate_families`.

## Specialization / boundary cases
- Beta–Bernoulli at `a=b=1` (uniform prior): posterior is `Beta(1+s, 1+n-s)`,
  the classic Laplace rule-of-succession form.
- Normal–Normal as `tau0^2 -> infinity` (flat/improper prior): `mu_n -> xbar`,
  the posterior mean collapses to the MLE — the mechanism behind
  `credible_vs_confidence`'s numeric coincidence.
- Gamma–Poisson at `n=0` (no data): posterior equals the prior, as required.

## Hypothesis-dropped counterexamples
- Drop conjugacy (use a non-conjugate prior, e.g. a uniform-on-a-bounded-
  interval prior for a Normal mean with unbounded support): the posterior has
  no closed form and needs numerical integration or MCMC — out of scope here,
  flagged as the boundary this release does not cross.
- Drop known variance in the Normal case: the posterior marginal for `theta`
  is no longer Normal (Student-t after marginalizing an unknown variance) —
  the standard motivation for the excluded Normal-Inverse-Gamma family.

## Common misuse
Treating the posterior mean as "the" Bayes estimate regardless of loss
(it is specifically the squared-loss Bayes estimator —
`posterior_median_rule` from `math-statistics` is the absolute-loss
alternative, not imported here since 0.1 only needs the mean).
Forgetting the known-variance assumption and applying the Normal-Normal
update with an estimated `sigma^2` plugged in as if it were exact.

## Related nodes (non-prerequisite)
equivalent_to (via math-statistics): `prob_beta` bridge stub in
`math-statistics/nodes/nodes.tsv` names the same Beta–Bernoulli conjugacy;
this node is the worked instance that stub pointed at without stating.

## Sources
[gelman_bda3] Chapter 2 (conjugate prior distributions, Beta-Binomial,
Normal-Normal, Gamma-Poisson all worked); [casella_berger] Section 7.2.3.
