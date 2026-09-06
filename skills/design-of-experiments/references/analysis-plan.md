# Analysis-plan generation

Produce the analysis plan **before any outcome is examined**. Changing it after
seeing data converts a confirmatory experiment into an exploratory one — say so
if that happens.

## Required fields

- Primary estimand.
- Primary outcome and measurement window.
- Secondary, exploratory, and guardrail outcomes.
- Inclusion / exclusion criteria.
- Analysis population: ITT, modified ITT, per-protocol, as-treated, or another
  defined set — with the rationale.
- Main statistical model.
- Covariates and the reason each is included (pre-treatment only).
- Random / fixed effects and the treatment of clustering.
- Interaction terms planned in advance.
- Missing-data assumptions and handling (MCAR / MAR / MNAR; complete-case,
  multiple imputation, IPW, mixed model).
- Outlier and data-quality rules (defined by mechanism, not by "weakens the
  result").
- Multiple-testing correction or hierarchical / gatekeeping testing strategy.
- Interim-analysis schedule and stopping rules (efficacy, futility, harm).
- Sensitivity analyses (alternative models, alternative missing-data
  assumptions, per-protocol vs ITT, unmeasured-confounding bounds for
  quasi-experiments).
- Subgroup analysis plan (pre-specified subgroups, interaction tests, not
  post-hoc slicing).
- Effect sizes and uncertainty intervals to be reported.
- Visualization plan.
- Decision rule — the exact mapping from result to action.
- Reproducibility / version-control requirements (code, seeds, environment,
  locked before unblinding).

## Model selection by outcome type

| Outcome | Typical analysis | Key cautions |
|---|---|---|
| Continuous, ~normal | Linear regression, ANCOVA, mixed-effects | Residuals, heteroskedasticity, outliers, baseline adjustment |
| Binary | Logistic regression; risk-difference / risk-ratio regression; log-binomial or Poisson with robust SE | Odds ratios mislead when the outcome is common — report absolute effects |
| Count | Poisson or negative-binomial regression | Exposure offset; test and model overdispersion |
| Time to event | Kaplan–Meier, Cox, accelerated failure time | Censoring assumptions; check proportional hazards |
| Ordered categorical | Ordinal (proportional-odds) regression | Test the proportional-odds assumption |
| Repeated / longitudinal | Mixed models, GEE, state-space / time-series | Correlation structure, missingness, timing |
| Clustered | Mixed effects, cluster-robust SE, randomization inference | Too few clusters invalidates the usual asymptotics — use small-sample corrections or permutation |
| Factorial response | ANOVA / regression with interactions | Don't interpret main effects under a dominant interaction |
| Simulation output | Replication-based intervals; paired / common-random-number comparison; batch means | Warm-up removal, autocorrelation, RNG-stream handling |

## Estimation over binary significance

Default to reporting:

- effect magnitude with units;
- an uncertainty interval;
- comparison to the pre-specified practical threshold;
- probability / compatibility with decision-relevant values;
- sensitivity to assumptions;
- implementation fidelity;
- trade-offs against guardrails.

A p-value alone is never the decision report. Contrast:

> "Variant B was statistically significant."

with:

> "Relative to the current experience, B increased completed checkout by 0.8
> percentage points (95% CI 0.1 to 1.5 pp). It did not clear the pre-specified
> 1.0-pp practical-success threshold with high confidence, and mobile latency
> rose 18 ms. The pre-specified recommendation is to continue only with a
> latency-optimization follow-up."

## Sequential and adaptive experiments — legitimate methods

Efficient, but only when the adaptation rule is pre-specified:

- Group-sequential designs with pre-specified interim looks and alpha spending
  (O'Brien–Fleming, Pocock, Lan–DeMets).
- Futility stopping (conditional power, predictive probability).
- Multi-armed bandits for allocation — with explicit inferential caveats
  (post-selection inference, non-uniform exposure).
- Bayesian sequential decision rules.
- Adaptive sample-size re-estimation (blinded preferred).
- Response-adaptive randomization — strong justification, pre-specified control
  of type-I error.
- Dose escalation / de-escalation (3+3, CRM, BOIN).
- Bayesian optimization and simulation optimization.
- Sequential factorial screening and augmentation / foldover.

For regulated clinical contexts, adaptive designs must preserve reliable
treatment-effect estimation, control the chance of erroneous conclusions,
pre-specify the design, and protect trial integrity. The same principles apply
outside medicine.

## What the plan must prevent

- Repeated looks with stop-on-first-favorable-p.
- Changing primary metrics after seeing outcomes.
- Removing "outliers" that weaken a desired result.
- Redefining the treatment mid-run without declaring a new experiment.
- Overlapping experiments that contaminate assignment.
- Calling an adaptive experiment valid when the adaptation was not
  pre-specified.
