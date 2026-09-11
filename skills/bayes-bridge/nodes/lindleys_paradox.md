# lindleys_paradox

## Type
counterexample

## Statement
There exist a sample size `n`, data `xbar`, and a significance level `alpha`
such that the classical `likelihood_ratio_test_cited` rejects `H0: theta = 0`
at level `alpha`, while the Bayes factor `BF_10` under a diffuse proper prior
on the alternative — `theta ~ N(0, tau0^2)` with `tau0^2` large relative to
the data's precision — favors `H0` by a substantial margin. The two
procedures disagree, at the same data, because they answer different
questions with different sensitivity to the prior's spread.

## Symbols
- `n`: sample size, positive integer
- `xbar`: the observed sample mean, real
- `sigma^2`: known data variance, fixed positive real (1, in the worked
  instance)
- `tau0^2`: the alternative prior's variance, positive real, made diffuse

## Epistemic status
counterexample (this is the required hypothesis-dropped demonstration for
`bayesian_model_comparison`: drop "the prior on `M1` is not diffuse relative
to the data's precision" and the two model-comparison procedures diverge).

## Prerequisites (tsort edges into this node)
bayesian_model_comparison, likelihood_ratio_test_cited

## Hypotheses
Normal-mean testing setup, known variance, a **proper** prior on `M1`
(an improper prior makes `BF_10` undefined up to an arbitrary constant — a
different, sharper failure than the paradox itself).

## Proof provenance
technique: closed-form Bayes factor for the Normal-Normal point-null-vs-
diffuse-alternative test (Savage–Dickey-style ratio of two Normal
marginals), evaluated at a concrete instance where the classical rejection
boundary is fixed by construction.
derives_from: bayesian_model_comparison (this is its worked failure case,
not a separate derivation).
lean_status: not_attempted — a numeric demonstration, not an algebraic
identity; verified by `bc` instance check.
bc_status: verified — see `validation/instance-checks.md#lindleys_paradox`.

## Type / well-formedness check
Both marginal likelihoods (`xbar ~ N(0, sigma^2/n)` under `H0`;
`xbar ~ N(0, sigma^2/n + tau0^2)` under `H1`) are well-formed Normal
densities with the stated variances; `BF_10` is their ratio, a positive
real. Checked: `validation/type-checks.md#lindleys_paradox`.

## Specialization / boundary cases
- `tau0^2 -> 0` (a nearly point-mass prior on `M1` concentrated at 0): `M1`
  becomes observationally close to `M0` and the paradox does not appear —
  the effect is specifically a property of prior diffuseness, not of
  Bayesian model comparison generally.
- `n` fixed, `tau0^2 -> infinity`: `BF_10 -> 0` for any fixed `xbar != 0` —
  the paradox sharpens without bound (the "Jeffreys–Lindley" limiting case).

## Hypothesis-dropped counterexamples
This node *is* the hypothesis-dropped counterexample for
`bayesian_model_comparison`; it has no further counterexample of its own
within scope.

## Common misuse
Concluding "Bayes factors are wrong" or "p-values are wrong" from this
divergence, rather than reading it as: a p-value does not condition on `M1`
at all, and a Bayes factor is sensitive to how diffuse the prior under `M1`
is — both are working as designed, on different questions.

## Related nodes (non-prerequisite)
contrasts_with: `likelihood_ratio_test_cited` (see `edges/relations.tsv`).

## Sources
[lindley_1957] "A statistical paradox"; [jeffreys_1961] Theory of
Probability, §5.2.
