---
name: bayes-bridge
description: The Bayesian inferential apparatus as a bridge between the `math-probability` capsule's Bayes' theorem and the `math-statistics` skill's estimation machinery — priors/likelihood/posterior, worked conjugate families (Beta-Bernoulli, Normal-Normal, Gamma-Poisson), Bayes factors and marginal likelihood, Bayesian model comparison with Lindley's paradox as its hypothesis-dropped counterexample, and a credible-vs-confidence-interval contrast on the same worked example. A `bridge`-archetype knowledge capsule -- roots imported (cited, not redeveloped) from math-probability and math-statistics; native content is the connective tissue neither endpoint states. Use when you need to link a probability-theory Bayes'-theorem statement to a statistics-skill estimation result, to state or check a Bayes factor / marginal likelihood / conjugate-update computation, or to explain precisely how a credible interval differs from a confidence interval. Built with the math-theorem-tree method.
---

# bayes-bridge

A `bridge`-archetype capsule (see `BACKLOG-BACKLOG.md`'s "Cross-domain
bridges" pattern) connecting [`math-probability`](../math-probability/SKILL.md)'s
`bayes_theorem` to [`math-statistics`](../math-statistics/SKILL.md)'s
Bayesian-methods area (`bayes_estimator`, `conjugate_prior`,
`credible_interval`, `bernstein_von_mises`, `bayes_risk`, …). Read
[`scope.md`](scope.md) first for the full included/excluded boundary and
foundational stance.

## What's native here vs. imported

Every node typed `bridge` in `nodes/nodes.tsv` (`area: imports`) is cited
from its source capsule, not redeveloped — no in-edges, no re-proof. The 8
native nodes are the actual content of this release:

- `prior` — the missing standalone definition neither endpoint states.
- `posterior_prop_prior_times_likelihood` — Bayes' theorem restated for a
  continuous parameter, naming the marginal likelihood as the omitted
  normalizer.
- `conjugate_families` — **one node**, three worked instances (Beta-Bernoulli,
  Normal-Normal known-variance, Gamma-Poisson), each a closed-form update
  with a `bc`-checked numeric case. One page, not three near-duplicates —
  they share a single proof pattern (multiply kernels, recognize the
  family).
- `marginal_likelihood`, `bayes_factor`, `jeffreys_scale`,
  `bayesian_model_comparison` — the real content gap: Bayes factors and
  model comparison are absent from both endpoint capsules.
- `lindleys_paradox` — the hypothesis-dropped counterexample for
  `bayesian_model_comparison` (drop "prior not diffuse relative to the
  data's precision"): a worked instance where a diffuse proper prior makes
  the Bayes factor favor `M0` roughly 46:1 while a same-data classical test
  rejects `M0` at `alpha=0.05`.
- `credible_vs_confidence` — the numeric coincidence (flat prior, same
  interval) and interpretive divergence between `credible_interval_cited`
  and `normal_mean_ci_known_variance_cited`, with `bernstein_von_mises_cited`
  explaining why the coincidence holds asymptotically, not in general.

## The `contrasts_with` relation

`bayesian_model_comparison` vs. `likelihood_ratio_test_cited`, and
`credible_vs_confidence` vs. `normal_mean_ci_known_variance_cited`: same
question, two paradigms, deliberately **not** unified as a `tsort`
prerequisite. Recorded in `edges/relations.tsv` as `contrasts_with` — see
`conventions.md` for why this extends, rather than misuses, the
`math-theorem-tree` relation vocabulary.

## Cross-capsule tie-in that isn't a capsule

`unknown-discovery` (forecast ledger, Brier-score calibration) is a
methodology skill, not a `math-theorem-tree` capsule — no node registry to
edge into. The correspondence between a Bayes-factor-style odds update and a
forecast-ledger probability revision is documented as an `illustrated_by`
relation in `edges/relations.tsv` and in prose in `conventions.md`, not a
real graph edge.

## Build and verify

```sh
sh build/all.sh                        # graph -> tsort -> bc, all in one
sh build/build-tree.sh                 # 24 nodes, 28 edges, acyclic, 0 isolated
bc -q -l validation/instance-checks.bc  # conjugate updates, Lindley's paradox, the flat-prior coincidence
```

## Release 0.1 at a glance

24 nodes (15 imported `bridge` roots + 9 native: 3 definitions
[`prior`, `marginal_likelihood`, `bayes_factor`], 1 theorem
[`posterior_prop_prior_times_likelihood`], 1 `construction`
[`conjugate_families`], 1 `notation_convention` [`jeffreys_scale`], 1
`principle_law` [`bayesian_model_comparison`], 1 `counterexample`
[`lindleys_paradox`], 1 `diagnostic` [`credible_vs_confidence`]), 28
`tsort` edges, acyclic (0 isolated), plus 4 `edges/relations.tsv` entries
(`contrasts_with` x2, `illustrated_by` x1, `equivalent_to` x1 — none of them
`tsort` edges). No new foundational commitments; every proof technique is
either a cited restatement of an imported root, a direct algebraic
consequence, or a worked `bc` numeric instance — no Lean cores in this
release (see `scope.md`'s proof policy for why).

## Method verification (Release 0.1)

| Stage | Tool | Result |
|---|---|---|
| graph + sort | GNU `tsort` | 24 nodes, 28 edges, **acyclic**; every edge respected; 0 isolated |
| type checks | this skill | 5 headline nodes, all **well_formed** (`validation/type-checks.md`) |
| instances | GNU `bc` 7.0.3 | clean run: the three conjugate posteriors, Lindley's-paradox `BF_01 approx 46.3` at the classical rejection boundary, the flat-prior credible/confidence coincidence (`validation/instance-checks.md`) |
| relations | this skill | `contrasts_with` (2), `illustrated_by` (1), `equivalent_to` (1) — verified none are `tsort` edges |

Full results: `validation/instance-checks.md`, `validation/type-checks.md`.
