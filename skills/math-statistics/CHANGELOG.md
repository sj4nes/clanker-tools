# Changelog

## Release 0.1 — 2026-09-08

First release. Mathematical statistics from the statistical model to the
classical large-sample theory, the exact Gaussian core, and the Gaussian linear
model, built with the [`math-theorem-tree`](../math-theorem-tree/SKILL.md)
method.

### Graph

- **206 nodes** — 58 cited roots (`prob_*` into `math-probability`, `ra_*` into
  `math-real-analysis`, one `linear_algebra_background` bridge with no capsule),
  plus 148 capsule nodes across: the model / likelihood / regularity block,
  exponential families, sufficiency–completeness–Basu, the optimality theorems
  (Cramér–Rao, Rao–Blackwell, Lehmann–Scheffé), the methods (MoM, MLE,
  M-estimators, Bayes), decision theory (admissibility, minimax, James–Stein),
  the exact Gaussian core (`t`/`χ²`/`F` constructed, the sampling-distribution
  theorems), interval estimation, hypothesis testing (Neyman–Pearson,
  Karlin–Rubin, LRT/Wilks, Wald/score, p-values, multiplicity), the
  nonparametric glue (ECDF, Glivenko–Cantelli, DKW, bootstrap, KDE), and the
  Gaussian linear model (OLS, Gauss–Markov, the exact t- and F-tests, FWL).
- **396 evidence-commented edges** (`edges/dependencies.plan`); acyclic,
  BSD-stderr-checked; 5 potential cycles recorded as avoided-by-modeling
  (`edges/cycles.md`). 24 non-prerequisite relations (`edges/relations.tsv`).

### Foundational stance

- Probability is the floor: every probabilistic object and theorem is a cited
  root. The `t`, `χ²`, `F` distributions are the exception — `construction`
  nodes built here from the normal and gamma.
- The six **regularity conditions** are first-class `hypothesis` nodes edged
  into every theorem that needs them.
- Finite-dimensional linear algebra is cited background with no capsule — the
  one acknowledged gap.
- Frequentist and Bayesian both included; a prior is a modeling-input node.

### Per-result tag

Every inferential result carries `regime: { exact | asymptotic |
distribution_free | bayesian }` — the analogue of `math-probability`'s
`convergence_mode`. Indexed in `indexes/regime-index.md`. Distribution: 59
exact, 24 asymptotic, 11 distribution_free, 9 bayesian.

### Validation

- **Lean** (`validation/proof-checks.lean`, Lean 4.33, no Mathlib, exit 0, no
  `sorry`/`axiom`/warnings): 26 genuine universal cores + 8 `decide` instance
  checks over one fixed 3×2 design. `lean_status` across the 206 YAMLs: 38
  `core`, 6 `instance`, 103 `cited`. No epistemic-status label upgraded past
  what the kernel or a cited proof establishes. Table in
  `validation/proof-checks.md`.
- **bc** (`validation/instance-checks.bc`, `bc -l`, exit 0): 8 sections — the
  CRLB at named models, the `n−1` divisor by enumeration, `t`/`χ²`/`F`
  relations, the Neyman–Pearson threshold, the Rao–Blackwell variance drop, OLS
  on a 3-point design, Wald-interval undercoverage, Benjamini–Hochberg vs
  Bonferroni.
- `build/check-consistency.py` green: every YAML ↔ graph dependency list, every
  source key in `sources/bibliography.md` (~90 refs), every relation endpoint
  registered.
- **201 nodes `reviewed`**, 5 boundary nodes (`le_cam_lan_theory`,
  `hajek_convolution_theorem`, `local_asymptotic_minimax`, `donsker_theorem`,
  `minimax_rate`) kept `draft` — Release 0.2 territory.

### Generated views

`indexes/`: topological order, hypothesis index, regime index, counterexample
index, status index, symbol (KWIC) index, minimal prerequisite paths for the
headline theorems, reverse-dependency index.

### Known limitations / next

- No `math-linear-algebra` capsule below this one (candidate future floor).
- Release 0.2 territory: the LAN / Hájek / LAM machinery proved rather than
  stated; martingale and sequential methods; a deeper empirical-process layer;
  GLMs beyond the exponential-family + MLE mention.
- The `statistics` analysis-methodology skill (sibling of `design-of-experiments`)
  will cite this capsule for the theorems.
