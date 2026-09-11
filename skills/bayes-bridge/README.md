# bayes-bridge

**Status: Release 0.1 built (2026-09-11).**

A `bridge`-archetype capsule (see `BACKLOG-BACKLOG.md`'s "Cross-domain
bridges") connecting [`math-probability`](../math-probability/SKILL.md)'s
`bayes_theorem` to [`math-statistics`](../math-statistics/SKILL.md)'s
estimation apparatus, which already carries most of the Bayesian-methods
area (`bayes_estimator`, `conjugate_prior`, `credible_interval`,
`bernstein_von_mises`, `bayes_risk`, …). This capsule's own content is the
connective tissue neither endpoint states: worked conjugate-family
instances, Bayes factors / marginal likelihood (the one real content gap —
absent from both endpoints), the credible-vs-confidence side-by-side, and a
documented (non-`tsort`) tie-in to `unknown-discovery`'s forecast ledger.

Built with the [`math-theorem-tree`](../math-theorem-tree/SKILL.md) method.

- Start: [`SKILL.md`](SKILL.md) · [`scope.md`](scope.md) · [`conventions.md`](conventions.md) · [`objects.md`](objects.md)
- Graph: [`nodes/nodes.tsv`](nodes/nodes.tsv) · [`edges/dependencies.plan`](edges/dependencies.plan) · [`edges/relations.tsv`](edges/relations.tsv)
- Results: [`results/`](results/) (5 native headline YAMLs) · [`nodes/`](nodes/) (5 native detail pages)
- Verification: [`validation/instance-checks.md`](validation/instance-checks.md) · [`validation/type-checks.md`](validation/type-checks.md)

## Build

```sh
sh build/all.sh                        # graph -> tsort -> bc
sh build/build-tree.sh                 # 24 nodes, 28 edges, acyclic, 0 isolated
bc -q -l validation/instance-checks.bc  # conjugate updates, Lindley's paradox, the flat-prior coincidence
```

## Release 0.1 at a glance

24 nodes (15 cited `bridge` roots from `math-probability`/`math-statistics`
+ 9 native), 28 `tsort` edges, acyclic, 0 isolated. Headline native results:
`posterior_prop_prior_times_likelihood`, `conjugate_families` (one node,
three worked instances — Beta-Bernoulli, Normal-Normal known-variance,
Gamma-Poisson), `bayesian_model_comparison`, `lindleys_paradox` (a diffuse
proper prior makes `BF_01 approx 46.3` at data a classical test rejects at
`alpha=0.05`), `credible_vs_confidence`. Two `contrasts_with` relations
(`bayesian_model_comparison` ↔ `likelihood_ratio_test_cited`,
`credible_vs_confidence` ↔ `normal_mean_ci_known_variance_cited`) keep the
Bayesian/frequentist correspondence documented without forcing it into a
`tsort` edge.

## Resolved scoping questions

- **Conjugate families:** one node (`conjugate_families`), one results YAML
  with three `specialization_cases` — not three near-duplicate node pages,
  since all three share a single proof pattern (multiply kernels, recognize
  the family).
- **Model-comparison contrast:** `contrasts_with` in `edges/relations.tsv`,
  not a `requires` chain into `math-statistics:likelihood_ratio_test`.
