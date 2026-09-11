# bayesian_model_comparison

## Type
principle_law

## Statement
For two models `M0`, `M1` with proper priors and data `x`:
`P(M1|x)/P(M0|x) = BF_10 * P(M1)/P(M0)` — posterior odds equal the Bayes
factor times prior odds. Unlike a nested-hypothesis significance test, `M0`
and `M1` need not be nested, and the result reports evidence *for* `M0`
(posterior odds `< 1`), not merely a failure to reject it.

## Symbols
- `M0, M1`: two candidate models for the same data `x`, not required nested
- `P(M1)/P(M0)`: prior odds, positive reals fixed before seeing `x`
- `BF_10`: the Bayes factor (imported node `bayes_factor`)

## Epistemic status
proved_theorem (a direct application of `bayes_theorem_cited` to the
discrete model-indicator random variable).

## Prerequisites (tsort edges into this node)
bayes_factor, prior, jeffreys_scale

## Hypotheses
Both models assign a well-defined, finite, nonzero marginal likelihood to
`x`; both priors are proper (see `lindleys_paradox` for what breaks
otherwise, and for the diffuse-but-proper failure mode).

## Proof provenance
technique: Bayes' theorem applied to `P(M_i | x) prop P(x | M_i) P(M_i)`,
divided for `i=1` over `i=0`.
derives_from: bayes_theorem_cited.
lean_status: not_attempted — a one-line algebraic consequence of Bayes'
theorem, recorded as `proved_theorem` on the strength of that derivation,
not separately kernel-checked in this release.

## Type / well-formedness check
`P(x|M_i)` is `marginal_likelihood` evaluated at model `M_i`; the ratio is a
positive real whenever both marginal likelihoods are positive. Checked:
`validation/type-checks.md#bayesian_model_comparison`.

## Specialization / boundary cases
Equal prior odds (`P(M1) = P(M0)`): posterior odds equal the Bayes factor
exactly — the case usually reported when no strong prior model preference is
stated.

## Hypothesis-dropped counterexamples
Drop "proper priors on each model": `lindleys_paradox` — a diffuse-enough
proper prior on `M1` already reverses the classical test's verdict; an
*improper* prior on `M1` makes `BF_10` undefined up to an arbitrary constant
(a sharper failure than the paradox, noted but not separately worked here).

## Common misuse
Reading `BF_10 > 1` as "`M1` is true" rather than as a graded evidence
ratio (`jeffreys_scale` gives the conventional reading); comparing Bayes
factors computed under different priors on the same nominal model as though
`BF` were prior-independent.

## Related nodes (non-prerequisite)
contrasts_with: `likelihood_ratio_test_cited` — the frequentist analogue
compares the same two models by a likelihood ratio at their MLEs, with no
prior and a fixed rejection threshold rather than a continuous evidence
scale. See `edges/relations.tsv` for why this is a relation, not a `tsort`
edge (resolves `scope.md`'s second open scoping question).

## Sources
[kass_raftery_1995] "Bayes Factors", JASA; [gelman_bda3] §7.4.
