# Experiment charter

The first deliverable — written before any design matrix or sample size.

```yaml
charter:
  decision_question: ""          # the causal / optimization question in one sentence
  decision_owner: ""             # who acts on the result
  action_alternatives: []        # what could be done differently depending on the outcome
  objective_class: ""            # causal-confirmation | screening | optimization | robustness |
                                 #   estimation | equivalence | mechanism | dose-response |
                                 #   rollout | model-comparison | simulation-study
  evidence_class: ""             # randomized | randomized-compromised | quasi-experiment |
                                 #   observational | simulation
  intervention_or_factors: []    # each with its levels / settings
  comparison_conditions: []      # control(s): status quo | placebo | active comparator | ...
  experimental_unit: ""          # the SMALLEST independently randomized thing
  target_population_or_domain: ""
  primary_outcome:
    name: ""
    operational_definition: ""
    scale_and_unit: ""
    observation_window: ""
    direction_of_improvement: ""
    data_source: ""
    minimum_practical_effect: ""  # the smallest effect that changes the decision
  secondary_outcomes: []
  guardrail_outcomes: []          # each with a "must not worsen beyond" threshold
  unacceptable_harms_or_costs: []
  time_to_decision: ""
  constraints:
    budget: ""
    duration: ""
    traffic_or_units_available: ""
    equipment_or_sites: ""
    staffing: ""
    governance_ethics_privacy_safety: []
  prior_evidence_and_baseline_data: []
  interference_risks: []          # spillover | contamination | carryover | learning | network effects
  randomization_feasibility: ""   # can units be independently assigned? what blocks it?
  desired_confidence_or_precision: ""
  assumptions_made: []            # anything filled in without confirmation
  blocking_questions: []          # the minimal questions that must be answered before designing
```

When an assumption is load-bearing enough to rank and track — with a triage
score, a disconfirming signal, and an earliest indicator — promote it to the
[assumption register](../../unknown-discovery/templates/assumption-register.md)
from [`unknown-discovery`](../../unknown-discovery/SKILL.md) rather than
expanding this list.
