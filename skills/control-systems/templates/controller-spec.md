# Controller specification

The architecture and control law with the evidence that it is stable and robust.

```yaml
controller_spec:
  architecture:
    control_layers: []              # fast loop / supervisory / safety / human / monitoring
    topology: ""                    # feedback | feedforward | cascade | ratio | split-range |
                                    #   decoupling | supervisory | MPC | hybrid | + safety filter
    estimator: ""                   # none | Luenberger observer | Kalman | EKF/UKF | ...
    sampling_scheme: ""             # per-loop rates, hold type, synchronisation, data age
    data_path_and_trust_boundaries: ""
    human_override_and_bumpless_transfer: ""
  structural_feasibility:
    controllability: ""             # rank result + practical interpretation
    observability: ""               # rank result + Gramian conditioning + unstable-mode check
    multivariable_interaction: ""   # RGA / coupling assessment
  controller:
    family: ""                      # on-off | PID | lead-lag | pole-placement | LQR | LQG |
                                    #   MPC | H-infinity | gain-scheduled | adaptive | SMC | NMPC | RL
    rationale: ""                   # why this is the least-complex adequate choice
    control_law: ""                 # equations or algorithm
    parameters: []                  # gains / weights / horizons / covariances + how chosen
    reference_handling: ""
  practical_elements:
    saturation_and_rate_limits: ""
    anti_windup: ""
    derivative_filtering: ""
    sensor_failure_behaviour: ""
    communication_loss_behaviour: ""
    fault_detection_isolation_recovery: ""
    safety_filter_or_constraint_enforcement: ""
  stability_evidence:
    nominal: ""                     # closed-loop eigenvalues / Routh / root locus / Nyquist
    margins: ""                     # gain margin, phase margin, crossover, bandwidth
    sensitivity_functions: ""       # peak |S|, peak |T|
    discrete_check_at_actual_Ts: ""
  robustness_evidence:
    declared_uncertainty_envelope: ""
    result_across_envelope: ""      # stability + performance at the corners / over the set
    worst_case_scenario: ""
  computation:
    worst_case_execution_time: ""
    deadline_and_fallback: ""
```
