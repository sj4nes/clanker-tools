# Objects — type vocabulary

| Object | Type | Lives in |
|---|---|---|
| `theta` | parameter | per-application: `[0,1]` (Beta-Bernoulli), `R` (Normal mean), `(0,infinity)` (Gamma-Poisson rate) |
| `x`, `x_1..x_n` | observed data | per-application, matching the likelihood's sample space |
| `pi(theta)`, `pi(theta\|x)` | density function | nonnegative, integrates to 1 over the parameter space |
| `L(theta)` | function of `theta`, data fixed | nonnegative real-valued; **not** a density in `theta` |
| `p(x)` | the marginal likelihood | positive real (when finite) |
| `M0, M1` | models | each a full specification of a likelihood + prior over `theta` |
| `BF_10` | Bayes factor | positive real, `= p(x\|M1)/p(x\|M0)` |
| `C(x)` | an interval (credible or confidence) | subset of `R`, or `[0,1]` for a rate parameter |

## Well-formedness rules used throughout

- A density (`pi`, `L` normalized) must integrate to 1 over its stated
  domain; `L(theta)` alone need not (it is a function of `theta`, not a
  density in `theta`, even though it *is* a density in `x` for fixed
  `theta`) — this is the standard likelihood-vs-density type confusion
  flagged on `posterior_prop_prior_times_likelihood`'s common-misuse list.
- A Bayes factor's subscript order is fixed (`BF_10 = p(x|M1)/p(x|M0)`) —
  `BF_01 = 1/BF_10`, never silently swapped.
- Coverage statements (`coverage_probability_cited`) are functions of
  `theta` with `x` (or the interval) as the random quantity; credible-set
  statements (`credible_interval_cited`) are functions of `x` with `theta`
  as the random quantity given `x`. `credible_vs_confidence` exists
  specifically to keep these two function signatures from being conflated.
