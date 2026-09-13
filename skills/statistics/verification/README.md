# `statistics` skill — verification run

The `statistics` skill is methodology-only (no bespoke CLI), so verification
means: re-solve cases with exact known answers using the workflow the skill
prescribes, and confirm each prescribed check — including each
negative-contrast guardrail — behaves as claimed.

This file was added 2026-09-13, later than the harness it documents. Two things
it records were found by writing it, not by running anything: the
[displacement table](#displacement-table) below, and the broken marker grep now
recorded in [`docs/bc-verification-audit.md`](../../../docs/bc-verification-audit.md).

**Cases.** Small-`n` Gaussian and Bernoulli/Poisson problems with closed forms —
chosen because each has an exact analytic answer *and* a naive procedure whose
failure is quantifiable at the same `n`. The point of every section is the
**contrast**, not the headline number.

## Run

```
sh skills/statistics/verification/run.sh
```

Tooling: `bc` 7.x (`-l`), Python 3 (stdlib only), macOS. ~13 s wall.

## What each step demonstrates (SKILL.md → result)

| Step | Prescribed check | Result |
|---|---|---|
| `bc` 1 — CRLB | efficiency of the estimator against the bound | Bernoulli / Poisson means **attained** (`1.000`); normal variance **not** (`0.900 = (n−1)/n`) — **pass** |
| `bc` 2 — multiplicity | FWER of 20 independent nulls, and the corrections bounding it | unadjusted `0.642`; Bonferroni `0.0488`, Šidák `0.0500` — **pass** |
| `bc` 3 — FDR | Benjamini–Hochberg step-up thresholds `k q / m` | `0.0025 … 0.05` over `k = 1…20` — **pass** |
| 2 — regime, exact vs asymptotic | exact t-interval coverage at `n = 5` | `0.950` at nominal `0.950` — **pass** |
| 2 — negative contrast | the naive z-interval at the same `n` | `0.880` — **undercovers** (the regime label is not cosmetic) |
| 3 — boundary behaviour | Wilson/score interval near `p = 0.08` | `0.963` — **pass** |
| 3 — negative contrast | the Wald interval there | `0.835` — **undercovers badly** (`wald_interval` counterexample) |
| 4 — distribution-free | percentile bootstrap for a mean of exponential data | `0.919` — **pass** |
| 4 — negative contrast | the same bootstrap for the **maximum** of uniform(0, θ) | `0.000` — **total failure** (`bootstrap_consistency` needs smoothness) |
| 5 — multiplicity, realised | Bonferroni over 20 true nulls | `0.047` — **pass** |
| 5 — negative contrast | the same 20 tests unadjusted | `0.638` (≈ 13× nominal) — **pass** (guardrail visibly trips) |
| 6 — sufficiency | Rao–Blackwell for `e^{−λ}`: mean preserved, variance cut | mean `0.3671` vs crude `0.3682` (target `0.3679`); variance `0.233 → 0.0143` — **pass** |
| 7 — finite-sample bias | variance MLE at `n = 4` vs the `n − 1` estimator | `0.750` vs `0.999` (true `1.000`) — **pass** (`mle_asymptotic_normality` is an `n → ∞` statement) |

## Displacement table

Required by [`docs/verifying-skills.md`](../../../docs/verifying-skills.md) §7:
every `SKILL.md` section must name the default behaviour it displaces, and the
verification must show that default failing. Rows no fixture can falsify are
marked `judgement`; rows that displace nothing nameable are tutorial material
and belong in `references/`.

`statistics` is the **second** skill through this rule (after `test-writing`,
where the rule was derived), and the first one it was not designed around.

### Covered — the default is demonstrated failing

| `SKILL.md` section | default behaviour it displaces | where that default visibly fails |
|---|---|---|
| principle: *know the best achievable variance* | quote an estimator's variance with no reference to what is achievable | `bc` 1 — efficiency `1.000` (attained) vs `0.900` (not) |
| principle: *prefer an exact procedure when the model supports one*; the **regime table** | use a normal approximation at any `n`, because that is the formula everyone writes | step 2 — z-interval covers `0.880` at `n = 5` where the t-interval covers `0.950` |
| principle: *handle multiplicity explicitly* | run 20 tests, report the significant ones | step 5 — realised FWER `0.638` unadjusted vs `0.047` Bonferroni |
| principle: *when the parametric model is doubtful, use a robust or distribution-free procedure* | treat "bootstrap" as assumption-free | step 4 — coverage `0.000` for the maximum of uniform(0, θ) |
| principle: *do not discard information: find the sufficient statistic* | keep the first estimator that is unbiased | step 6 — variance `0.233 → 0.0143` at the same mean |
| principle: *MLE guarantees are asymptotic and need regularity*; *unbiased is not the same as good* | read an MLE's asymptotic properties as finite-sample ones | step 7 — MLE reads `0.750` at `n = 4` against a true `1.000` |
| workflow 5, *name the regime* | report an interval with a level but no regime | steps 2 and 3 together: the same nominal 95 % delivers `0.950`, `0.880`, `0.963`, `0.835` depending on regime and boundary |

### `judgement` — no fixture can falsify these

| `SKILL.md` section | default behaviour it displaces | why unfalsifiable here |
|---|---|---|
| principle: *no estimand, no inference*; workflow 1, the charter | answer "is it significant?" as asked | the harness is *given* the estimand; refusing an ill-posed question cannot be shown by a case that is well-posed |
| principle: *list every model assumption and mark it checkable or not*; workflow 3 | carry assumptions as background prose | enumeration completeness has no oracle — a missed assumption looks like a shorter list |
| **method-selection table**; principle: *choose the test from optimality theory, not habit* | reach for the t-test / OLS by habit | a *routing* decision. Partly a reference row: the optimality basis lives in the capsule's `indexes/`, and the agent's prior on it is genuinely thin |
| principle: *calibrated language only*; workflow 9, report with limits | state a conclusion in the language of the finding rather than of the guarantee | a language property, not a numeric one |
| **guardrails** (refuse or escalate) | answer anyway, with a caveat | step 4's `0.000` is one guardrail firing, but the *refusal* itself is judgement |

### Gaps — demonstrable, but not demonstrated

These are the rule's actual yield: claims the skill makes that a fixture
**could** falsify and currently does not. Each is a concrete harness section,
not a research question.

| `SKILL.md` section | what the harness should show | why it is cheap |
|---|---|---|
| principle: *a confidence interval is an inverted test; report the interval, not a bare p* | the `n = 5` t-interval excludes `μ₀` **exactly** when the level-α test rejects, over many samples | exact duality; reuses step 2's sampler |
| principle: *under the null a p-value is uniform, so a non-significant result is not evidence of no effect* | p-values uniform under the null (KS or a decile histogram), and power at a plausible effect ≈ 0.2 at small `n` | one Monte Carlo loop |
| principle: *the DGP is a modelling assumption* — pseudoreplication | clustered data analysed at the observation level inflates the FPR | **already demonstrated in `design-of-experiments`** (`0.29` vs `0.06`): either cite it or port it. The most-cited principle in the skill with no local evidence |
| principle: *if a prior is used, justify it and test its influence* | the same data under two defensible priors at small `n`, and the posterior interval moving materially | conjugate Beta–Binomial, closed form |
| principle: *a regression coefficient is a projection; its exact tests need normal errors* | nothing at all — no regression case exists anywhere in the harness | the one row at risk of being tutorial prose rather than a gap; if no case is added, it should shrink to a pointer into the capsule |

## Findings folded back into the skill

- The `bc` snippet in `references/power-and-sample-size.md` said "503 total";
  corrected to 504. *(Recorded at the time in the README Verification row.)*
- Nothing in `SKILL.md`'s prescribed workflow needed a correctness fix: the
  steps produced the right calls and the right conclusions on every case.
- 2026-09-13, from the displacement table: **7 covered, 5 `judgement`,
  5 gaps.** The gaps are logged in `BACKLOG.md`. No `SKILL.md` claim was found
  *wrong* — the finding is that five of them are asserted on the skill's
  authority where the harness could carry them instead.
- 2026-09-13, incidental: `run.sh`'s `grep -q '*** FAIL'` never fired (ugrep
  exits 2 on the leading `*`, which shell `if` reads as false). Fixed to
  `grep -qF` here and in eight other harnesses; see
  [`docs/bc-verification-audit.md`](../../../docs/bc-verification-audit.md).

## The gates are necessary, not sufficient

`run.sh` catches mechanical defects, not judgement. The `judgement` block above
is the precise list of what stays human: choosing the estimand, deciding an
assumption list is complete, routing to a method, calibrating the language of a
conclusion, and refusing. As `SKILL.md` states — a p-value cannot tell you
whether the question was worth asking.

---

See [`docs/verifying-skills.md`](../../../docs/verifying-skills.md) for the
shared run-script shape, the displacement-table rule (§7), and the `bc` /
Python portability rules.
