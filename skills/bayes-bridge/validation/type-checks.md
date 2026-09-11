# Type / well-formedness checks

For each native headline node: every symbol's type (per `objects.md`), each
operation's domain/codomain, and that the statement is well-formed. A
passing type check is necessary, not sufficient — see each node's own page
for the fuller discussion; this file is the terse worksheet.

## posterior_prop_prior_times_likelihood
`pi(theta)`: density on the parameter space, `>=0`, integrates to 1.
`L(theta)`: nonnegative function of `theta` (data `x` fixed) — **not**
required to integrate to 1 in `theta` (it is a density in `x`, not `theta`).
`pi(theta) L(theta)`: nonnegative function of `theta`; dividing by its
`theta`-integral (the marginal likelihood, assumed finite and positive)
yields a proper density. **well_formed.**

## conjugate_families
Each instance's posterior stays in the stated family (`Beta`, `Normal`,
`Gamma`) with hyperparameters computed by the stated formula; every
hyperparameter update preserves its domain constraint (positive shape/rate,
positive variance). Checked symbolically per instance in `nodes/conjugate_families.md`;
confirmed numerically in `validation/instance-checks.md`. **well_formed.**

## marginal_likelihood / bayes_factor / bayesian_model_comparison
`p(x|M_i)`: a positive real whenever `pi_i(theta) L_i(theta)` is
integrable over `M_i`'s parameter space. `BF_10 = p(x|M1)/p(x|M0)`: positive
real ratio, well-defined whenever both marginal likelihoods are positive and
finite (flagged as failing under an improper prior — see
`lindleys_paradox`). Posterior odds `= BF_10 * prior odds`: both sides
positive reals, dimensionally consistent (odds-to-odds). **well_formed.**

## lindleys_paradox
`xbar ~ N(0, sigma^2/n)` under `H0` and `xbar ~ N(0, sigma^2/n + tau0^2)`
under `H1`: both well-formed Normal marginal densities with the stated
variances (a standard "integrate out the prior on theta" computation).
`BF_10`: the ratio of these two densities at the observed `xbar`, positive
real. **well_formed.**

## credible_vs_confidence
`credible_interval_cited`'s `C(x)` and `normal_mean_ci_known_variance_cited`'s
`C(x)`: both subsets of `R`, same functional form
`xbar +- z_{1-alpha/2} sigma/sqrt(n)` under the flat prior — confirmed they
are literally the same set, not merely numerically close, by direct
substitution (`posterior_prop_prior_times_likelihood` with `pi(theta)=1`
gives posterior `N(xbar, sigma^2/n)` exactly).
`coverage_probability_cited(theta)` (a function of `theta`, `x` random) is
**not** conflated with `P(theta in C(x) | x)` (a function of `x`, `theta`
random given `x`) — different domains, checked explicitly. **well_formed.**
