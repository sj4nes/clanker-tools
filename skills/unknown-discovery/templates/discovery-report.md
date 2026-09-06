# Discovery report

The final package. Separates evidence from interpretation from assumption from
hypothesis from scenario from recommendation.

```yaml
discovery_report:
  scope:
    decision_and_owner: ""
    system_boundary: ""
    time_horizon: ""
    what_would_change_the_decision: ""
  epistemic_map:
    known_knowns: []               # claim + evidence + scope
    known_unknowns: []             # question + why it matters + how learnable
    unknown_knowns_to_retrieve: [] # what + likely holder + retrieval step
    ambiguities: []
    measurement_blind_spots: []
    model_form_uncertainties: []
    deep_uncertainties: []         # question + scenarios + distinguishing indicators
    tail_risks: []
    unknown_unknown_candidate_areas: []   # boundary crossings, excluded stakeholders, untested regimes
  assumption_register: []          # see templates/assumption-register.md — ranked, with disconfirming signals
  alternative_hypotheses:
    question: ""
    ranked_hypotheses: []
    evidence_matrix_summary: ""
    diagnostic_evidence_needed: []
    what_would_change_our_mind: []
  risk_and_surprise_map:
    - scenario: ""
      causal_mechanism: ""
      earliest_indicator: ""
      existing_safeguard: ""
      safeguard_gap: ""
  learning_backlog:                # value-of-information ranked
    - question: ""
      probe_or_method: ""
      discriminates: []
      expected_decision_value: ""  # low | medium | high, or EVPI if computed
      cost_and_duration: ""
      reversible: true
      safety_boundary: ""
      success_criteria: ""
      disconfirming_outcome: ""
      stop_rule: ""
      owner: ""
  monitoring_plan:
    indicators: []                 # name + watches + measurement + threshold + response
    escalation: []
    reassessment_cadence: ""
  forecast_ledger:
    forecasts: []                  # forecast + probability + deadline + base rate
    calibration_method: "Brier score + bucketed calibration review"
  limits:
    unresolved_deep_uncertainties: []
    claims_not_being_made: []
    reassessment_required_when: ""
```
