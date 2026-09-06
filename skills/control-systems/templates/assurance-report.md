# Assurance report

The final deliverable — states what was designed, what evidence supports it, and
what remains uncertain.

```yaml
assurance_report:
  objective_and_scope: ""
  risk_classification: ""
  system_architecture: ""             # layers, controller, estimator, safety supervisor
  controller_summary: ""              # family, key parameters, least-complex-adequate note
  assumptions_and_validated_range: []  # operating regime the evidence actually covers
  model:
    representation_and_validity_domain: ""
    uncertainty_envelope: ""
    identification_validation_evidence: []
  stability_and_performance_evidence:
    nominal_stability: ""
    robustness_margins_over_envelope: ""
    performance_vs_targets: []         # worst-case + percentile, not just nominal
  safety:
    hard_constraints_and_independent_protections: ""
    fail_safe_state_and_how_reached: ""
    human_override_and_handover: ""
    security_controls: []
  test_campaign:
    scenario_coverage: []
    verification_results: []           # which checks passed, which failed
    validation_evidence: []
    validation_gaps: []
  uncertainty_and_sensitivity:
    dominant_drivers: []
    conditions_that_reverse_the_recommendation: []
    value_of_information: ""            # the next test / measurement that most reduces risk
  deployment:
    ladder_level_reached: ""            # 1..10 from verification-validation-deployment.md
    rollout_gates: []
    telemetry_and_alerting_plan: ""
    rollback_and_safe_state_procedure: ""
    drift_detection_and_reidentification_governance: ""
  residual_risks: []
  prohibited_uses_or_escalation_conditions: []
  explicit_non_claims: []              # e.g. "simulation alone does not show hardware safety"
  revision_history: []
```
