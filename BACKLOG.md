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
