# bayes-bridge

**Status: scoping (2026-09-11).** Not yet a built capsule — `scope.md` is the
only deliverable so far.

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
Read [`scope.md`](scope.md) first.

## Next steps

1. Resolve the two open scoping questions in `scope.md`.
2. `conventions.md`, `objects.md`, `notation.md` — likely thin, since most
   objects/notation are imported from the two endpoint capsules.
3. `nodes/nodes.tsv` — the imported-root rows (tagged `imported_root`) plus
   the native nodes from scope items 2–5.
4. `edges/dependencies.plan` — `requires` edges from native nodes into
   imported roots; verify against the `tsort` skill's discipline.
5. `results/*.yaml` for the native headline nodes; `bc` instance checks for
   the conjugate updates and the Lindley's-paradox counterexample; a Lean
   instance check for `posterior_prop_prior_times_likelihood`.
