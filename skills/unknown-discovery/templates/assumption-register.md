# Assumption register and alternative-hypothesis register

Two living registers, each with a review date. Neither is ever "done".

## Assumption register

One entry per assumption. Sorted by the triage score `P = I · U · (1−R) · D`,
components kept.

```yaml
assumptions:
  - id: "A1"
    assumption: ""                  # stated as a testable claim
    category: ""                    # factual | causal | behavioural | technical |
                                    #   data-quality | operational | legal | financial |
                                    #   adversarial | ethical | stationarity | scaling |
                                    #   dependency | measurement | governance
    why_it_matters: ""              # which decision it feeds
    evidence: []
    confidence: "low | medium | high"
    scope: ""                       # where / when / for whom it holds
    triage:
      impact_if_wrong: 0            # I
      uncertainty: 0                # U
      reversibility_of_decision: 0  # R  (0 = irreversible, 1 = fully reversible)
      dependency_centrality: 0      # D
      score: 0                      # I · U · (1−R) · D  — triage only, not a risk metric
      rationale: ""
    disconfirming_signal: ""        # the observation that would show it failing  (mandatory)
    earliest_indicator: ""          # the metric / event that shows it first      (mandatory)
    probe: ""                       # link to the learning-backlog item
    owner: ""
    review_trigger: ""
    status: "open | probing | confirmed | refuted | retired"
```

## Alternative-hypothesis register

```yaml
alternative_hypotheses:
  question: ""
  hypotheses:
    - id: "H1"
      statement: ""
      prior_rationale: ""
      current_standing: "front-runner | live | weakened | ruled out"
  evidence_matrix:
    - item: ""
      source_reliability: "low | medium | high"
      under: { H1: "expected | unexpected | neutral | missing", H2: "..." }
      diagnostic: true
  diagnostic_evidence_needed: []
  what_would_change_our_mind: []
  review_date: ""
```
