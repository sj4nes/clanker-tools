# math-statistics — build in progress

Mathematical statistics as a curated, dependency-ordered knowledge capsule,
built with the [`math-theorem-tree`](../math-theorem-tree/SKILL.md) method. Sits
on top of [`math-probability`](../math-probability/SKILL.md).

## Status: Stages 1-2 complete (graph + all node entries authored)

| Artifact | State |
|---|---|
| `scope.md` | done — included/excluded, foundational stance, `regime` tag policy |
| `conventions.md` | done — foundational stance, notation, cycle-avoidance record |
| `notation.md`, `objects.md` | done — master symbol list, type vocabulary |
| `nodes/nodes.tsv` | 206 nodes (58 cited roots + 148 capsule nodes) |
| `edges/dependencies.plan` | 396 evidence-commented edges |
| `edges/dependencies.edges` | generated, `graph-check` clean |
| `edges/relations.tsv` | 24 non-prerequisite relations |
| `edges/cycles.md` | done — acyclic; 5 potential cycles recorded as avoided |
| `nodes/<id>.md` detail pages | **done — 206**, generated from `build/specs/spec_*.py` |
| `results/<id>.yaml` | **done — 206**, dependency lists pulled from the graph |
| `sources/bibliography.md` | done — ~90 references |
| `indexes/` | done — tsort-order, hypothesis, regime, counterexample, status, symbol (KWIC), prerequisite-paths, reverse-dependencies |
| `validation/proof-checks.lean` + `.md` | **done (Stage 3)** — Lean 4.33, no Mathlib, exit 0: 26 genuine universal cores + 8 `decide` instance checks; `lean_status` 38 core / 6 instance / 103 cited |
| `validation/instance-checks.bc` | **not started (Stage 4)** |
| `SKILL.md` | written last, once the release is `reviewed` |

Regenerate all node pages + YAMLs after editing a spec:
`python3 build/gen-results.py`  (then `sh validation/graph-check.sh`).

## Remaining stages

3. `validation/proof-checks.lean` — the finitary algebraic / inequality cores
   (bias–variance decomposition, score identity, information equality,
   CRLB-via-Cauchy–Schwarz, Rao–Blackwell-via-total-variance, Neyman–Pearson
   swap, `E[S^2] = sigma^2`, normal equations, Gauss–Markov quadratic form,
   posterior-mean-completes-the-square, chi-squared df additivity). Deep
   asymptotics (`mle_*`, `wilks_theorem`, `glivenko_cantelli`,
   `karlin_rubin_theorem`, `bootstrap_consistency`, `bernstein_von_mises`)
   stay `lean_status: cited`.
4. `validation/instance-checks.bc` — CRLB at named models, the `n − 1`
   correction, `t`/`χ²`/`F` critical values and `t → Normal`, Neyman–Pearson
   thresholds, the Rao–Blackwell variance drop, OLS on a 3-point design,
   Wald-interval coverage, Benjamini–Hochberg step-up.
5. Build the discovery views; write `SKILL.md`; changelog; publish Release 0.1.
