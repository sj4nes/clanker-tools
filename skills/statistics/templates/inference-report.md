# Inference report

Written after the analysis. Every interval carries its regime and level.

```yaml
inference_report:
  question: ""
  estimand: ""                   # theta = T(P)
  target_population_or_dgp: ""
  main_result_plain_language: "" # one or two sentences: estimate + interval + threshold comparison

  provenance:
    independent_units: ""
    sampling_and_selection: ""
    missing_data_handling: ""    # + assumed mechanism
    weights_or_design: ""

  estimator:
    method: ""                   # MoM | MLE | M-estimator | Bayes | plug-in
    value: ""
    bias: ""                     # known bias / bias_of_sample_variance / finite-sample note
    variance_vs_crlb: ""         # attained? (crlb_attainment) or asymptotic target only
    rao_blackwell_umvue: ""      # if a complete sufficient statistic was used

  uncertainty:
    interval: ""                 # [lo, hi]
    level: ""                    # e.g. 95%
    regime: ""                   # exact | asymptotic | distribution_free | bayesian
    method: ""                   # t-pivot | Wald | profile likelihood | bootstrap | DKW | credible
    node: ""                     # math-statistics node

  tests:                         # pre-specified only
    - null_hypothesis: ""
      alternative: ""
      test: ""                   # NP | Karlin-Rubin | LRT+Wilks | Wald | score
      statistic_and_p: ""
      effect_and_interval: ""
  multiplicity:
    n_hypotheses: ""
    control: ""                  # FWER: Bonferroni/Holm | FDR: Benjamini-Hochberg | none (exploratory)
    adjusted_vs_unadjusted: ""

  model_checks:
    diagnostics_run: []
    robustness_comparison: ""    # model-based SE vs sandwich; parametric vs bootstrap interval
    conclusion_moved: ""         # yes/no under weaker assumptions

  bayesian:                      # if a prior was used
    prior: ""
    prior_sensitivity: ""
    bernstein_von_mises_note: "" # frequentist agreement is large-sample only

  limits:
    untestable_assumptions: []
    dominant_sensitivity_drivers: []
    conditions_that_reverse_the_conclusion: []
    external_validity: ""        # population / period the result does NOT extend to
    causal_reading: ""           # licensed? usually NO -- state why

  confirmatory_vs_exploratory:
    confirmatory_findings: []
    exploratory_findings: []     # need a confirmatory follow-up
  explicit_non_claims: []
  reproducibility_metadata: ""   # code, seeds, environment, data snapshot
```
