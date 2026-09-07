# Backlog

Lightweight, repo-native task tracker for **near-term, actionable** work on
skills that already exist. No external issue tracker yet — this file is it.

Organised by domain, then by skill. Keep entries short; lead each with the
**skill** it concerns (bold), then link to the file or node it touches.

Format:

```
- [ ] **skill-name:** short description  (context / where)
- [x] **skill-name:** done thing  (2026-09-06)
```

For the **speculative, long-horizon roadmap** of candidate new skills and
capsules — organised by domain, low confidence, no commitments — see
[`BACKLOG-BACKLOG.md`](BACKLOG-BACKLOG.md).

---

## Physics

### physics-thermodynamics

- [ ] **physics-thermodynamics:** Release 0.2 scope expansion — open systems and
      chemical potential (`dG = −S dT + V dP + μ dN`), phase equilibria +
      Clausius–Clapeyron, a real-gas node (van der Waals) as the correction the
      ideal-gas model omits.  (`scope.md` "Excluded" list)
- [ ] **physics-thermodynamics:** per-node detail pages (`nodes/<id>.md`) — the
      capsule currently collapses to the formula view; promote the 15 `draft`
      derived-formula nodes to `reviewed` with per-node `bc`/`lean` cross-checks.
- [ ] **physics-thermodynamics:** `upmd` tutorial via `formula-tree-tutorial` —
      "Why heat engines have a ceiling", `zeroth_law` → `carnot_efficiency`.
- [ ] **physics-thermodynamics:** cross-capsule — `physics-thermoacoustics`
      re-declares ideal-gas + first/second-law + entropy primitives; replace with
      `requires` edges into this capsule's developed nodes (0.2, mirrors the
      `math-*` stack pattern).

## Mathematics

### math-probability  (new capsule — Release 0.1 COMPLETE, 2026-09-06; polish pending)

The missing foundational floor under `design-of-experiments`, `simulation`,
`unknown-discovery` (forecast ledger + calibration), and any future statistics /
ML skill. Built with [`math-theorem-tree`](skills/math-theorem-tree/SKILL.md);
sits on top of `math-sets-functions-cardinality` (σ-algebras, measures) and
`math-real-analysis` (limits, integration).

**Done (2026-09-06):** `scope.md`, `conventions.md`, `objects.md`, `notation.md`,
`SKILL.md`, `README.md`; the **131-node registry** (`nodes/nodes.tsv`) and the
fully-evidenced **399-edge DAG** (`edges/dependencies.plan`) — `tsort` clean,
acyclic (BSD stderr-checked), 0 isolated; `edges/cycles.md` (4 would-be cycles
resolved: independence↔conditional via factorization def, expectation↔integral
via cited integral, + 2 modelling slips); generated indexes (hypothesis, status,
prereq-paths, counterexample, symbol/KWIC, reverse-deps); `validation/proof-checks.lean`
(Mathlib-free, **exit 0** — genuine: union bound, finite-support expectation
additivity by induction, Markov by induction; `decide` instances: Bayes,
Var=E[X²]−E[X]², binomial(4,½) mean/var, Jensen φ=square);
`validation/instance-checks.bc` (**exit 0** — Bernoulli/binomial/Poisson/exp/normal
moments, Poisson limit, memorylessness, standardized-binomial → Φ(1) CLT trend);
`sources/bibliography.md`. Convergence-mode tag defined in `conventions.md` (the
choice_grade analogue). 6 headline `results/*.yaml` written (kolmogorov_axioms,
bayes_theorem, markov_inequality, chebyshev_inequality, expectation_linearity,
central_limit_theorem).

**Added 2026-09-06 (session 2):** ALL 131 `results/<id>.yaml` + ALL 131
`nodes/<id>.md` — generated from one spec table `build/gen-results.py` (deps read
from the graph, so no drift), 6 headline entries hand-written.
`edges/relations.tsv` (45 non-prerequisite relations incl. `P(A|B)=P(A)` as
`equivalent_to` on `independence_events`). `build/check-consistency.py` (YAML↔graph
deps, source keys, relation endpoints — **all green**). New bibliography keys.
128 nodes promoted `draft`→`reviewed` in `nodes.tsv` (3 boundary nodes stay
`draft`). `build/all.sh` green end to end.

**Added 2026-09-06 (session 3 — polish):** rewrote `validation/proof-checks.lean`
using Lean 4.33 core `grind`/`omega` (still **no Mathlib, exit 0, no warnings**):
**15 genuine universal cores** now — union bound, incl-excl 2/3, Bayes
denominator, indicator algebra (`ind_and/or/compl`), `wsum_const` (E[c]=c),
`expectation_linearity` (universal in a,b, list induction), `centid` (the
centered-moment identity behind `Var=E[X²]−E[X]²` and `law_of_total_variance`),
`var_affine`, `markov_finite`, `chebyshev_reduction_fwd`, `jensen_sq` (universal
via the `t(n−t)(x−y)²` factorization), `cov_bilinear_raw`, `var_of_sum_raw`,
`corr_bound_iff` — plus `decide` instance grids. **36 nodes now `lean_status:
core`** (was ~15), 41 `cited`; every `lean_ref` points at a real declaration.
`proof-checks.md` rewritten with the genuine-vs-instance table keyed to nodes.
New `build/gen-validation-md.py` renders `validation/{type-checks,
specialization-cases,instance-checks}.md` (131 `## <node>` sections each) from
the YAMLs, so every `checks:` anchor resolves; wired into `build/all.sh`.

**Remaining for 0.1 / 0.2:** `upmd` tutorial via a probability analogue of
`formula-tree-tutorial`; a `math-measure-and-integration` capsule as the floor
below (would discharge the 6 cited integration bridges); Release 0.2 martingales
+ stochastic processes (the 3 boundary nodes).

**Target ~130 nodes** (2026-09-06, user): probability at this level is a
naturally high concept-load domain; 131 stays. No trim.

- [x] **math-probability:** `scope.md` — Kolmogorov axioms; σ-algebras and
      probability measures (discharge from `math-sets-functions-cardinality`);
      random variables, distribution / density / CDF; expectation, variance,
      moments, MGF/characteristic function; independence and conditional
      probability; **Bayes' theorem** as a node; joint / marginal / conditional
      distributions; covariance and correlation; key families (Bernoulli,
      binomial, Poisson, geometric, uniform, normal, exponential, gamma, beta);
      transformations and the change-of-variables formula; **inequalities**
      (Markov, Chebyshev, Jensen, Cauchy–Schwarz, Hoeffding); **limit theorems**
      (WLLN, SLLN, CLT, continuity theorem); conditional expectation as a
      projection; a stated-not-proved boundary node for martingales / stochastic
      processes (out of scope for 0.1).  Exclude: measure-theoretic
      probability *beyond* the σ-algebra/measure entry, stochastic processes,
      statistical inference (its own skill).
- [x] **math-probability:** graph + `tsort` — 131 nodes, 399 edges, acyclic,
      0 isolated; both would-be cycles resolved (see `edges/cycles.md`).
      Target revised to ~130 (high concept-load domain — kept, no trim).
      (2026-09-06)
- [x] **math-probability:** Lean validation — 15 genuine universal `grind`/`omega`
      cores + `decide` instance grids (Mathlib-free, Lean 4.33, exit 0, no
      warnings); 36 nodes `lean_status: core`, every `lean_ref` points at a real
      declaration; `proof-checks.md` rewritten. (2026-09-06)
- [x] **math-probability:** all 131 result YAMLs + 131 node pages +
      `relations.tsv` + `check-consistency.py`; `nodes.tsv` statuses promoted;
      `validation/{type-checks,specialization-cases,instance-checks}.md`
      generated (131 sections each) via `gen-validation-md.py`. (2026-09-06)
- [x] **math-probability:** `every_choice_grade` analogue — convergence-mode tag
      table in `conventions.md`; each limit-theorem YAML carries
      `convergence_mode:` (see `central_limit_theorem.yaml`). (2026-09-06)

### statistics  (follows math-probability — planned)

Analysis-methodology skill (sibling of `design-of-experiments`,
`unknown-discovery`), **not** a capsule: the disciplined workflow for inference
on data *already collected* — the gap `design-of-experiments` explicitly
refuses. Estimator choice and properties (bias / consistency / efficiency /
sufficiency), sampling distributions, confidence and credible intervals,
hypothesis testing and its misuse, likelihood, the bootstrap, regression, model
checking, multiplicity. Rests on `math-probability`.

- [ ] **statistics:** `SKILL.md` skeleton + `verification/` first — Monte Carlo
      of estimator coverage / error rates / the assumption-violation failures
      (mirrors the `design-of-experiments` verification pattern).

### bayes-bridge  (sidebar — planned, needs both endpoints)

A `bridge`-archetype connector once `math-probability` **and** `statistics`
exist: the Bayesian inferential apparatus as the link between the probability
capsule's Bayes' theorem and the statistics skill's estimation — priors /
likelihood / posterior, conjugacy, credible vs confidence intervals, posterior
predictive, Bayesian model comparison (Bayes factors, marginal likelihood), and
the decision-theory / calibration tie-in to `unknown-discovery`'s forecast
ledger. Named for the *correspondence*, not for "Bayes". See the "Cross-domain
bridges" section of [`BACKLOG-BACKLOG.md`](BACKLOG-BACKLOG.md).

- [ ] **bayes-bridge:** hold until `math-probability` and `statistics` are both
      in `skills/`; `bc` for conjugate-update closed forms and a
      credible-vs-confidence-interval contrast, Lean for the
      posterior ∝ prior × likelihood identity.

### math-logic-and-proof

- [ ] **math-logic-and-proof:** Mathlib-backed completeness formalisation — connect
      `godel_completeness_theorem` to `Mathlib.ModelTheory` (`FirstOrder.Language` +
      its completeness development) and upgrade `lean_status` from `cited` to
      `mathlib_cited` where the kernel actually verifies the link. Also
      `post_completeness_theorem` for a countable atom set is feasible in plain
      Lean (Lindenbaum by `Nat`-recursion + LEM, truth lemma by structural
      induction — no Mathlib).  (`validation/proof-checks.lean`, `validation/proof-checks.md`)
- [ ] **math-logic-and-proof:** `ptx` symbol / KWIC index — a keyword-in-context
      index over the corpus so every result mentioning `sup`, `epsilon`,
      `sigma_algebra`, … is findable; confirm every lead with `rg`.  (would live at
      `indexes/symbol-index.md`; see the sibling
      `math-sets-functions-cardinality/build/gen-symbol-index.sh`)
- [ ] **math-logic-and-proof:** Promote `draft` nodes to `reviewed` — most of the
      130 registry rows are still `status: draft`. Walk the math-theorem-tree
      step-7 validations per node (type check, ≥1 specialisation, ≥1
      hypothesis-dropped counterexample, Lean/bc cross-check) and bump `status` in
      `nodes/nodes.tsv` + `results/*.yaml` as each passes.  (`nodes/nodes.tsv`)
- [ ] **math-logic-and-proof:** Formalise the `Deriv ↔ H` round trip (currently
      `nd_hilbert_equivalence` is `lean_status: partial` — only the deduction
      theorem + `H.self` are checked). Needs a weakening lemma for `Deriv` and
      Hilbert derivations of the `∧`/`RAA` schemas.  (`validation/proof-checks.lean`)
- [ ] **math-logic-and-proof:** Add the remaining `validation/` worksheet files the
      result YAMLs point at: `type-checks.md`, `specialization-cases.md`,
      `instance-checks.md` (only `proof-checks.md` and the `.lean` / `.bc` exist so far).

### math-sets-functions-cardinality

- [ ] **math-sets-functions-cardinality:** Release 0.2 — replace its five logic
      primitives (`proposition_logic`, `predicate_logic`, `quantifier_negation`,
      `quantifier_order`, `proof_methods`) with `requires` edges into the
      corresponding developed nodes in `math-logic-and-proof`.  (cross-capsule; see
      `math-logic-and-proof/edges/cross-capsule.md`)

## Analysis & inference methodology

### simulation

- [ ] **simulation:** Consider a `templates/` charter + reporting skeleton the skill
      can emit (currently the templates live inline in `references/workflow.md`).
- [ ] **simulation:** Extend `verification/` beyond the M/M/1 DES case — one
      continuous-time (analytic ODE benchmark) and one Monte Carlo (dependence /
      tail-risk) worked check would cover more of the paradigm table.
- [ ] **simulation:** Cross-link with `design-of-experiments` — step-9 "design the
      experiment" could point at `design-of-experiments/references/simulation-doe.md`
      instead of restating.

### design-of-experiments

- [ ] **design-of-experiments:** Cross-link with `simulation` — the simulation
      skill's step-9 "design the experiment" could point at this skill's
      `references/simulation-doe.md` instead of restating.

### visualization-design

- [ ] **visualization-design:** cross-link with `simulation` and
      `design-of-experiments` — their reporting steps could point at
      `references/evidence-and-domains.md` for the plot catalogue instead of
      restating it.
- [ ] **visualization-design:** extend `verification/` with a diagram-grammar
      check (parse a Mermaid/DOT source, confirm every edge style has a declared
      meaning in a legend node).

### unknown-discovery

- [ ] **unknown-discovery:** cross-link — step 6 hands off to `simulation`,
      `design-of-experiments`, `control-systems`, `tla-checker`/`lean`; their
      charters could point back at `templates/assumption-register.md` for the
      assumption / hypothesis registers instead of restating.
- [ ] **unknown-discovery:** worked end-to-end example — take one messy decision
      (capacity commitment or a post-release metric drop) through steps 1–9:
      charter → epistemic map → ranked assumptions → premortem + ACH → signal
      cards → VoI-ranked backlog → forecast ledger → monitoring plan; `check.py`
      recomputes the EVPI / Brier / diagnosticity claims, wired into `run.sh`.

## Tutorials

### theorem-tree-tutorial  (new meta skill — started 2026-09-06)

Math analogue of `formula-tree-tutorial`. `skills/theorem-tree-tutorial/`:
SKILL.md + `references/{upmd-mechanics,authoring-from-nodes,document-structure}.md`
drafted. Adds over the physics version: the **Lean-beat wrapper** (heredoc +
`lean` + exit check + `SKIP` guard — `upmd` has no Lean runner), the
**hypothesis-dropped-counterexample beat** (`cx_<id>` from each result YAML's
`counterexamples_when_dropped`), and **grade surfacing**
(`choice_grade` / `constructive_grade` / `convergence_mode`).

- [ ] **theorem-tree-tutorial:** VERIFY by generating a first tutorial. Suggested
      target: `math-probability` "Kolmogorov's three axioms → `boole_inequality`"
      (closure of 10, every check a Lean core or one-line `bc`). Gate:
      `upmd --ci --all` green, capstone + one middle `chk_` + one `lean_` beat
      run standalone. Fold fixes back into `references/`; add a README
      Verification-status row; write to `skills/math-probability/tutorial/`.
- [ ] **theorem-tree-tutorial:** decide the "one skill or two" question
      (`docs/tutorial-map.md` §7) — whether to merge with `formula-tree-tutorial`
      into `capsule-tutorial` once both are exercised.
- [ ] **theorem-tree-tutorial:** settle the cross-capsule `deps:` convention
      before any Tier-4 (discharge-chain) tutorial — `docs/tutorial-map.md` §7.

### physics-thermodynamics

- [ ] **physics-thermodynamics:** `upmd` tutorial "Why heat engines have a
      ceiling" (`zeroth_law` → `carnot_efficiency`) via `formula-tree-tutorial` —
      also listed under that capsule above; buildable today, no new infra.

## Cross-cutting

- [ ] **verification harnesses:** every methodology skill's `verification/` re-solves
      the same BSD-vs-GNU / `bc`-flags / Python-stdlib portability problem. Consider a
      shared `templates/verification/` harness or a short `docs/verifying-skills.md`
      capturing the fixes already discovered (see the Verification table in the README).

---

## Done

- [x] **physics-thermodynamics:** new capsule (Release 0.1) — 77-node acyclic
      graph (four laws, ideal gas, Carnot, entropy, potentials), `[M L T Θ N]`
      basis, `dU = δQ − δW` convention; scope/conventions/units, formula view,
      `edges/cycles.md` (5 cycles designed out), `build/run.sh` green (10 `bc`
      dimensional + 6 numeric checks, 8 Lean instance checks), registry-derived
      topic / assumption / prerequisite-path indexes.  (2026-09-06)

- [x] **unknown-discovery:** new skill — SKILL.md + 6 references
      (epistemic-map-and-assumptions, alternatives-and-challenge,
      signals-and-surprise, probes-and-value-of-information,
      forecasting-and-calibration, governance-and-failure-modes) + 3 templates
      (discovery-charter, assumption-register, discovery-report) + `verification/`
      (EVPI in `bc`; Monte-Carlo calibration / Brier floor; ACH diagnosticity;
      residual regime-shift masking; `P = I·U·(1−R)·D` triage); `sh run.sh` green.  (2026-09-06)

- [x] **visualization-design:** new skill — SKILL.md + 7 references
      (visual-selection, graphical-integrity, perception-and-hierarchy,
      accessibility, diagrams, evidence-and-domains, critique-engine) + 3
      templates + `verification/` (WCAG contrast + Tufte lie factor in `bc`,
      Okabe–Ito vs bad-palette CVD/grayscale check, rainbow-ramp failure);
      `sh run.sh` green.  (2026-09-06)

- [x] **visualization-design:** worked end-to-end example —
      `examples/support-contact-rate/` takes a messy monthly CSV + a loaded
      "make it go up and to the right" request through steps 1–9 (brief → job →
      Vega-Lite spec → integrity audit → a11y package → critique); `check.py`
      recomputes every claim, wired into `verification/run.sh`.  (2026-09-06)

- [x] **design-of-experiments:** `verification/` worked check — `bc` sample-size
      + adjustments, Monte Carlo power / design-effect / pseudoreplication-FPR /
      ANCOVA, and the 2^(4-1) alias structure two ways; `sh run.sh` green.  (2026-09-06)

- [x] **math-logic-and-proof:** capsule — 130-node acyclic graph, detail page for
      every node, 21 headline result YAMLs, Lean + bc validation, generated
      indexes; `sh build/all.sh` green.  (2026-09-06)
- [x] **simulation:** new skill — SKILL.md + 4 references + M/M/1 DES verification
      run; merged to main.  (2026-09-06)
