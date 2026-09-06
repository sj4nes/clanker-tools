# Pre-registered analysis plan

Locked before any outcome data is examined. Timestamp it.

```yaml
analysis_plan:
  primary_estimand: ""            # ATE | ATT | CATE | ITT | per-protocol | interaction | quantile | ...
  decision_rule: ""               # exact mapping from result -> action

  primary_outcome:
    name: ""
    measurement_window: ""
  secondary_outcomes: []
  exploratory_outcomes: []
  guardrail_outcomes: []           # each with its threshold

  population:
    analysis_set: ""               # ITT | mITT | per-protocol | as-treated
    inclusion_criteria: []
    exclusion_criteria: []

  primary_model:
    form: ""                       # e.g. linear regression / logistic / Cox / mixed-effects / GEE
    outcome_type: ""               # continuous | binary | count | time-to-event | ordinal | repeated
    covariates: []                 # pre-treatment only; each with rationale
    random_or_fixed_effects: ""
    clustering_treatment: ""       # cluster-robust SE | mixed model | randomization inference
    planned_interactions: []

  missing_data:
    assumed_mechanism: ""          # MCAR | MAR | MNAR
    handling: ""                   # complete-case | multiple imputation | IPW | mixed model
  outlier_rules: ""                # defined by mechanism, not by effect on the result
  data_quality_rules: []

  multiplicity: ""                 # Bonferroni | Holm | hierarchical gatekeeping | none (+ justification)

  interim_analyses:
    schedule: ""
    alpha_spending: ""             # O'Brien-Fleming | Pocock | Lan-DeMets | none
    efficacy_stop_rule: ""
    futility_stop_rule: ""
    harm_stop_rule: ""

  sensitivity_analyses: []         # alternative models, alternative missing-data assumptions,
                                   #   per-protocol vs ITT, unmeasured-confounding bounds
  subgroups: []                    # pre-specified only; interaction test, not post-hoc slicing

  reporting:
    effect_sizes: ""
    uncertainty_intervals: ""      # CI / credible interval; level
    practical_threshold_comparison: ""
    visualization_plan: ""

  reproducibility:
    code_location: ""
    seeds: ""
    environment: ""
    locked_before_unblinding: true

  sample_size:
    method: ""                     # power-based | precision-based
    target: ""                     # power (1-beta) or interval half-width
    alpha: ""
    assumed_sigma_or_baseline_rate: ""
    assumed_source: ""
    minimum_detectable_effect: ""
    adjustments_applied: []        # clustering (DE), allocation, ANCOVA, multiplicity,
                                   #   interim, attrition, overdispersion, autocorrelation, ...
    raw_n: ""
    effective_n: ""
```
