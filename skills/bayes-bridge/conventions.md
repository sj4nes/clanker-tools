# Conventions — `bayes-bridge`

## Foundational stance

No new foundational commitments. This capsule inherits both endpoints':
classical logic and ZFC (via `math-sets-functions-cardinality`, through
`math-probability`), Kolmogorov probability, and `math-statistics`'s
frequentist/Bayesian dual apparatus. Its own contribution is the connective
nodes listed in `scope.md` — the Bayes-factor apparatus, the worked
conjugate instances, and the credible-vs-confidence contrast — everything
else is a cited, `bridge`-typed import.

## Imported roots — the `bridge` type

Following the precedent set by `math-statistics:prob_beta` (a `bridge`-typed
node citing `math-probability:beta_distribution` rather than redeveloping
it), every node here that states a result belonging to another capsule is
typed `bridge`, `area: imports`, `status: reviewed`, with a
`primary_statement` ending `-- <capsule>:<node_id>`. These nodes have no
in-edges in `edges/dependencies.plan` (their prerequisites live in their
source capsule's own graph); native nodes edge *into* them wherever the
statement or proof actually needs the cited fact.

## Prior

Neither `math-probability` nor `math-statistics` has a standalone `prior`
node — `math-statistics` uses the word informally, attached to
`conjugate_prior` and `bayes_estimator`. This capsule adds `prior` as a
native `definition` node (a distribution over the parameter, in the same
vocabulary `math-probability`'s distribution catalogue uses) so
`posterior_prop_prior_times_likelihood` and `bayesian_model_comparison` have
a proper prerequisite to point to.

## Known variance only

All Normal-family content (the Normal-Normal conjugate case,
`credible_vs_confidence`'s worked instance) fixes `sigma^2` known throughout
Release 0.1. The unknown-variance case needs the Normal-Inverse-Gamma
conjugate family and Student-t posteriors/intervals — out of scope; noted at
every node it would otherwise touch.

## `contrasts_with` — a relation type not in the base vocabulary

The `math-theorem-tree` method's relation table (`generalizes`,
`equivalent_to`, `strengthens`, …) does not name a "same question, two
paradigms, deliberately not unified" relation, which is exactly what links
`bayesian_model_comparison` to `likelihood_ratio_test_cited` and
`credible_vs_confidence` to `normal_mean_ci_known_variance_cited`. Added as
`contrasts_with` in `edges/relations.tsv`, following the method's own
license to extend the relation vocabulary as long as the result is **never**
a `tsort` edge (§"Which relations become `tsort` edges" explicitly frames
the listed table as non-exhaustive). This resolves `scope.md`'s second open
scoping question: no `requires`/predecessor chain into
`likelihood_ratio_test_cited` beyond what `lindleys_paradox` already needs
for its own statement.

## Cross-capsule tie-in that is not a capsule

`unknown-discovery` is a methodology skill (forecast ledger, Brier-score
calibration), not a `math-theorem-tree` capsule — it has no `nodes/nodes.tsv`
to edge into. The correspondence between a Bayes-factor-style odds update
and a forecast-ledger probability revision is recorded as an
`illustrated_by` relation in `edges/relations.tsv`, targeting
`unknown-discovery:forecast_ledger` by name only (not a registered node id),
and is prose-documented above at scope item 5. This mirrors how the
`math-*` capsule stack already records discharges that are real
correspondences but not real graph edges (see
`math-sets-functions-cardinality/edges/cross-capsule.md`).

## Notation

See `notation.md` for the master symbol list. `theta` always denotes the
parameter being inferred; `x` (or `x_1..x_n`) always the observed data;
`M0`/`M1` the two models under comparison in the model-comparison area.
`BF_10` is always `p(x|M1)/p(x|M0)` — the "10" subscript order is fixed
throughout so a Bayes factor value is never read backwards.
