# Scope — `bayes-bridge` Release 0.1

## What this is

A `bridge`-archetype capsule (per `BACKLOG-BACKLOG.md`'s "Cross-domain
bridges" pattern) connecting the *developed nodes* of two existing
`math-theorem-tree` releases:

- [`math-probability`](../math-probability/SKILL.md) — has `bayes_theorem`
  (headline node) and the discrete/continuous distribution catalogue.
- [`math-statistics`](../math-statistics/SKILL.md) — already has a
  substantial Bayesian-methods area: `bayes_estimator`, `posterior_mean_rule`,
  `posterior_median_rule`, `conjugate_prior`, `credible_interval`,
  `bernstein_von_mises`, `bayes_risk`, `bayes_rule_minimizes_bayes_risk`, plus
  the confidence-interval family (`coverage_probability`,
  `confidence_set_test_duality`, `normal_mean_ci_known_variance`,
  `wald_interval`, …) it will be contrasted against.

**A bridge imports roots, it does not re-derive them.** Every node named
above is `requires`-eligible as an imported root (cited, not redeveloped);
this capsule's own nodes are the *connective tissue* those two releases don't
yet state: the explicit conjugate-family instances (worked, not just defined
in the abstract), the credible-vs-confidence side-by-side, Bayes factors and
marginal likelihood (absent from both endpoint capsules — the one genuine
content gap this release fills), Bayesian model comparison, and the
calibration tie-in to `unknown-discovery`'s forecast ledger.

## Included (Release 0.1)

1. **The inferential triad, stated as a bridge diagram.** `prior` (a
   distribution over `theta`, imported from `math-probability`'s
   distribution catalogue) × `likelihood_function` (imported from
   `math-statistics`) → `posterior` via `bayes_theorem` (imported from
   `math-probability`), with `posterior_prop_prior_times_likelihood` as this
   capsule's own node stating the un-normalized form and naming the missing
   normalizer as the marginal likelihood (the hook into item 3).
2. **Worked conjugate families** (new nodes here; `conjugate_prior` imported
   as the general definition): Beta–Bernoulli/Binomial (closes the loop
   `math-probability:beta_distribution` ↔ `math-statistics:prob_beta`,
   already flagged as a bridge stub there), Normal–Normal with known
   variance, Gamma–Poisson. Each node: the closed-form posterior update, the
   posterior mean as a data/prior weighted average (the "conjugacy as
   shrinkage" reading), a `bc` instance at concrete hyperparameters.
3. **Bayes factors and marginal likelihood** (new — the actual content gap).
   `marginal_likelihood` (the normalizing constant `∫ L(θ) π(θ) dθ`,
   named but left undefined at `posterior_prop_prior_times_likelihood`),
   `bayes_factor` (`p(x|M1)/p(x|M2)`), the Jeffreys scale as a
   `notation_convention`, and `bayesian_model_comparison` as the headline
   node tying them together. Boundary-flagged: **Lindley's paradox** as a
   hypothesis-dropped counterexample (a Bayes factor can favor `M0` while
   every classical test rejects it at the same data — the improper-prior /
   prior-sensitivity failure mode).
4. **Credible vs. confidence, side by side.** One `results/` entry that
   states both `credible_interval` (imported) and the confidence-interval
   family (imported) on the *same* worked example (normal mean, known
   variance) so the numeric coincidence under a flat prior and the
   *interpretive* difference (a fixed random interval covering a fixed
   parameter, vs. a fixed interval assigning probability to a random
   parameter) are both visible. `bernstein_von_mises` (imported) is the
   asymptotic node that explains *why* they coincide in large samples and
   under regularity, not in general.
5. **Calibration tie-in to `unknown-discovery`.** A `relations.tsv`
   (non-`tsort`) entry connecting `bayes_factor`/`posterior` updating to
   `unknown-discovery`'s forecast ledger and Brier-score calibration review —
   record as `illustrated_by`, not `requires`: `unknown-discovery` is a
   methodology skill, not a `math-theorem-tree` capsule, so it has no node
   registry to edge into. Document the correspondence in prose
   (`conventions.md` or a short `bridges.md`), the same way the
   `math-*` capsules record cross-capsule discharges that aren't real edges.

## Excluded (out of scope for 0.1)

- **MCMC / computational Bayesian inference** (Gibbs sampling, Metropolis–
  Hastings, HMC, variational inference). This capsule is about the
  *inferential identities*, not sampling algorithms — a natural Release 0.2
  or a separate `bayesian-computation` skill.
- **Hierarchical / empirical Bayes models**, hyperprior structure, shrinkage
  estimators beyond the single-level conjugate cases in item 2.
- **Nonparametric Bayes** (Dirichlet process priors, Gaussian processes).
- **Objective/reference priors** (Jeffreys prior, reference priors) beyond a
  one-line note that flat/improper priors are the Lindley-paradox failure
  mode named in item 3 — a deeper treatment is out of scope.
- **Full decision theory** beyond what `math-statistics` already has
  (`bayes_risk`, `bayes_rule_minimizes_bayes_risk` are imported, not
  redeveloped).

## Level and background

Upper-undergraduate / early-graduate, matching both endpoint capsules.
Assumes `math-probability` (Bayes' theorem, the named distributions) and
`math-statistics` (likelihood, estimators, interval methods) already read.

## Foundational stance

No new foundational commitments — this capsule inherits both endpoints'
stances (classical logic, ZFC via `math-sets-functions-cardinality`,
Kolmogorov probability). Its own contribution is purely connective: new
nodes are the missing Bayes-factor apparatus and the worked conjugate
instances; everything else is an imported, cited root.

## Proof policy

- Conjugate-family posterior derivations: worked algebraically in the node
  entry, `bc`-checked at concrete hyperparameters (not a general Lean proof —
  these are calculus identities, not deep theorems).
- `posterior_prop_prior_times_likelihood`: a one-line Bayes'-theorem
  application — Lean-checked as an instance (mirrors how `math-probability`
  Lean-checks `bayes_theorem` itself, cited from there).
- Lindley's paradox: a worked numeric counterexample (`bc`), not a Lean
  proof — it's a phenomenon demonstration, the capsule's
  hypothesis-dropped-counterexample obligation for `bayesian_model_comparison`.

## Epistemic-status policy

Same five-way split as the two endpoint capsules
(`definition`/`proved_theorem`/`proposition`/`constructive_result`/
`counterexample`), plus: every imported root node is tagged `imported_root`
with its source capsule and id, distinguished from nodes native to this
capsule.

## Open scoping questions (resolve before Release 0.1 freeze)

- Whether the three conjugate families are worth full node pages each, or
  one `results/conjugate-families.yaml` table with three instances — leaning
  toward the table (they share one proof pattern; three near-duplicate node
  pages would violate "one canonical statement per result").
- Whether `bayesian_model_comparison` needs its own `tsort` predecessor
  chain into `math-statistics:likelihood_ratio_test` (the frequentist
  analogue) as an `equivalent_to`-adjacent relation, or whether that's scope
  creep for 0.1 — leaning toward a `relations.tsv` entry (`contrasts_with`),
  not a `requires` edge, kept out of the headline count.
