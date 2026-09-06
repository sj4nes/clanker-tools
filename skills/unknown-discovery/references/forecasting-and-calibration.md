# Forecasting and calibration

Explicit probabilities make assumptions testable over time. A discovery process
without a forecast ledger cannot tell whether its own confidence is any good.

## The forecast ledger

Record every material forecast — one whose resolution would change an action —
as a probability with a deadline, a reference class or base rate, and the
disconfirming evidence that would move it.

| Forecast | Probability | Deadline | Base rate / evidence | Outcome | Score | Lesson |
|---|---|---|---|---|---|---|
| Demand exceeds capacity next quarter | 35 % | 2027-03-31 | Prior peaks, pipeline, capacity model | pending | pending | Reassess monthly |
| Supplier lead time exceeds 45 days | 15 % | 2026-12-31 | Historical distribution, contract change | pending | pending | Monitor shipping delays |

Rules:

- A forecast without a **deadline** and a **reference class** is not in the
  ledger.
- State the probability, not "likely" / "unlikely" — those are not auditable.
- If you cannot give a defensible probability, that is a **deep uncertainty**,
  not a forecast — see below.

## Brier score

For a binary event with outcome `o ∈ {0, 1}` and forecast probability `p`:

```
brier = (1/N) · Σ (p_i − o_i)²
```

Lower is better; it punishes confident wrong predictions hardest. A forecaster
who always reports the true probability `q` for an event cannot do better in
expectation than the irreducible `q(1 − q)` — the Brier score decomposes into
calibration + refinement (irreducible) terms. So:

- A **calibrated** forecaster's long-run Brier score approaches the mean of
  `q(1 − q)` over their forecasts.
- An **overconfident** forecaster (pushing probabilities toward 0/1) scores
  *worse* than that floor. `verification/` demonstrates both by Monte Carlo.

Do not compare Brier scores across forecasters facing different event sets — the
floor differs.

## Calibration review

Bucket resolved forecasts by stated probability (e.g. 0–10 %, 10–20 %, …) and
compare the stated probability to the observed frequency in each bucket.

> Across all claims assigned 70 %, did roughly 70 % occur?

Systematic patterns and their fix:

- **Overconfident** (90 % claims happen 70 % of the time) — widen intervals,
  regress stated probabilities toward the base rate.
- **Underconfident** (60 % claims happen 80 % of the time) — trust the analysis
  more; stop hedging.
- **Domain-blind** (well-calibrated overall, badly calibrated for one category)
  — flag that category for extra scrutiny and outside input.

The objective is not to sound confident. It is to make confidence auditable and
to learn where it is systematically wrong.

## Deep uncertainty — no fake precision

When there is no defensible basis for a number, do **not** invent one. State
instead:

```yaml
deep_uncertainty:
  question: ""
  why_no_probability: ""        # novel regime, adversarial response, structural break, ...
  scenarios:
    - name: ""
      narrative: ""
      distinguishing_indicators: []
  robust_or_reversible_action: ""
  reassessment_trigger: ""
```

A scenario set with signposts is a legitimate answer. A single made-up
percentage is not — it launders judgement into false rigour and defeats the
calibration review.
