# Decision report

Written after the run, against the locked analysis plan.

```yaml
decision_report:
  decision_question: ""            # as understood at the start
  main_result_plain_language: ""   # one or two sentences: effect + interval + threshold comparison

  primary_result:
    estimand: ""
    effect: ""                     # magnitude with units
    uncertainty_interval: ""       # CI / credible interval + level
    practical_threshold: ""
    cleared_threshold: ""          # yes | no | ambiguous
  guardrail_movements: []          # each metric, its change, whether it breached its threshold
  secondary_results: []

  what_the_data_support: ""
  evidence_class: ""               # randomized | randomized-compromised | quasi | observational | simulation

  uncertainty_and_sensitivity:
    dominant_sensitivity_drivers: []
    conditions_that_reverse_the_decision: []
    value_of_information: ""        # which new measurement would most reduce decision uncertainty

  validity_limits:
    internal: []                   # noncompliance, attrition, contamination, SRM, implementation failure
    external: []                   # population, time period, operating regime the result does NOT extend to
    untestable_assumptions: []

  implementation_fidelity: ""       # was the intervention delivered as designed?

  confirmatory_vs_exploratory:
    confirmatory_findings: []       # pre-specified, decision-authoritative
    exploratory_findings: []        # hypothesis-generating; need a confirmatory follow-up

  explicit_non_claims: []           # what this experiment does NOT establish

  recommendation: ""                # the pre-specified action implied by the decision rule
  reproducibility_metadata: ""      # code, seeds, environment, data snapshot
```
