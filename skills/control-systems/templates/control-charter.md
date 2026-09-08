# Control charter

The first deliverable — written before any architecture or tuning.

```yaml
control_charter:
  objective:
    decision_owner: ""
    controlled_variables: []        # name, unit, target / reference / envelope
    manipulated_variables: []       # actuator, range, rate limit, latency, failure modes
    measured_variables: []          # sensor, unit, noise, bias, latency, dropout behaviour
    disturbances: []                # source, magnitude, rate, bandwidth
    performance_targets: []         # rise / settle / overshoot / steady-state error / energy ...
    acceptable_tradeoffs: ""        # what may be given up for what
  plant:
    description: ""
    state_variables: []
    operating_envelope: ""          # ranges of every relevant variable
    operating_modes: []
    known_delays: ""
    nonlinearities: []
  constraints:
    hard_safety_limits: []          # never-exceed values; the unsafe set
    soft_constraints: []
    sampling_and_latency_budget: ""
    compute_budget: ""
    energy_cost_wear_limits: []
  safety_gate:
    hazards: []                     # hazard, severity, likelihood
    fail_safe_state: ""
    how_the_plant_reaches_it: ""
    independent_protections: []     # interlocks, safety filter, redundant sensing
    operator_authority_and_override: ""
    emergency_stop: ""
    applicable_standards: []
  model:
    source: "first_principles | identified | grey_box | simulation | unknown"
    representation: ""              # transfer function | state space | hybrid automaton
    validity_domain: ""             # operating point + range the model is trusted over
    uncertainty_register: []        # class, source, magnitude
    identification_validation_evidence: []
    evidence_gaps: []
  risk_classification: ""           # advisory-only | low-risk | supervised |
                                    #   high-consequence | prohibited-until-review
  deployment:
    target_environment: ""
    test_assets: []                 # SIL / PIL / HIL rigs, pilot site
    rollout_constraints: []
  assumptions_made: []              # anything filled in without confirmation
  blocking_questions: []            # minimal questions that must be answered first
```

When an assumption is load-bearing enough to rank and track — with a triage
score, a disconfirming signal, and an earliest indicator — promote it to the
[assumption register](../../unknown-discovery/templates/assumption-register.md)
from [`unknown-discovery`](../../unknown-discovery/SKILL.md) rather than
expanding this list. (The `uncertainty_register` above stays here — it is the
plant-model envelope; the assumption register is for the premises that, if
wrong, change the design.)
