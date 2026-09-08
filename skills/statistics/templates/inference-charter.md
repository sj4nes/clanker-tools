# Inference charter

The first deliverable — written before any model is fit. The data already
exists; this fixes what question it is being asked.

```yaml
charter:
  question: ""                   # the quantitative question in one sentence
  estimand: ""                   # theta = T(P): a functional of the distribution
                                 #   (mean, difference in means, coefficient, quantile,
                                 #    risk / odds / rate ratio, variance component, CDF functional)
  target_population_or_dgp: ""   # the population or data-generating process theta refers to
  decision_or_claim: ""          # what the answer feeds; who acts on it
  minimum_meaningful_magnitude: ""  # smallest value of the estimand that changes anything

  dataset:
    source: ""                   # census | probability sample | convenience | opt-in | admin extract
    unit_of_observation: ""
    rows: ""
    independent_units: ""        # clusters / periods, NOT rows, if dependent
    variables: []
    collection_period: ""
    known_provenance_issues: []  # selection, survivorship, truncation, censoring, weighting

  prior_evidence: []
  causal_reading_wanted: ""      # yes/no; if yes, the identification argument goes in the report
  assumptions_made: []           # anything filled in without confirmation
  blocking_questions: []         # minimal questions that must be answered before analysis
```
