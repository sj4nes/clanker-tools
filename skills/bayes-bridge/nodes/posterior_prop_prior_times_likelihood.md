# posterior_prop_prior_times_likelihood

## Type
theorem

## Statement
`pi(theta | x) prop pi(theta) L(theta)`, where the omitted normalizing
constant is `p(x) = integral pi(theta) L(theta) d theta` — the
`marginal_likelihood`. This is `bayes_theorem_cited` restated for a
continuous parameter with the denominator left as an unevaluated integral,
which is exactly the object `marginal_likelihood` and `bayes_factor` name.

## Symbols
- `theta`: the parameter, type per application
- `pi(theta)`: the `prior` density
- `L(theta)`: the `likelihood_function_cited`, `x` fixed
- `pi(theta|x)`: the posterior density

## Epistemic status
proved_theorem — a direct restatement of `bayes_theorem_cited` for a
continuous parameter (density in place of the discrete sum).

## Prerequisites (tsort edges into this node)
bayes_theorem_cited, likelihood_function_cited, prior

## Hypotheses
`pi(theta) L(theta)` integrable in `theta` over the parameter space (so the
normalizer is finite and positive) — the same condition that makes
`marginal_likelihood` well-defined.

## Proof provenance
technique: Bayes' theorem, continuous case (density ratio in place of
`P(A|B_j)P(B_j)/sum`).
derives_from: bayes_theorem_cited.
lean_status: stated; instance-checked as a `bc` arithmetic identity at the
conjugate-family sample points in `conjugate_families`, not separately
kernel-checked here (mirrors how `math-probability` handles `bayes_theorem`
itself).

## Type / well-formedness check
`pi(theta) L(theta)` is a nonnegative function of `theta`; dividing by its
integral over the parameter space yields a proper density (integrates to 1)
whenever that integral is finite and positive. Checked:
`validation/type-checks.md#posterior_prop_prior_times_likelihood`.

## Specialization / boundary cases
Discrete `theta` (finitely many models): reduces exactly to
`bayes_theorem_cited`'s stated form, with the integral becoming
`bayesian_model_comparison`'s sum over models.

## Hypothesis-dropped counterexamples
Drop integrability: an improper prior (`pi(theta) = 1` on an unbounded
parameter space) can still yield a proper posterior in many standard models
(the Normal-Normal case as `tau0^2 -> infinity` in `conjugate_families`), but
the *marginal likelihood* itself is then undefined up to an arbitrary
constant — the root cause of the improper-prior failure mode noted on
`lindleys_paradox` and `bayesian_model_comparison`.

## Common misuse
Treating `pi(theta) L(theta)` (the un-normalized posterior) as already a
density — it only integrates to 1 after dividing by `marginal_likelihood`,
which is why `marginal_likelihood` is a first-class node here rather than an
afterthought.

## Related nodes (non-prerequisite)
None beyond the `requires` edges above.

## Sources
[gelman_bda3] §1.3; [casella_berger] §7.2.3.
