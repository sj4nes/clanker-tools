# Discovery charter

The first deliverable — written before any assumption mining or scanning.

```yaml
discovery_charter:
  decision_or_system:
    description: ""
    decision_to_be_made: ""
    decision_owner: ""
    time_horizon: ""
    stakeholders: []
    system_boundary: ""            # what is in scope; what is explicitly out
    what_would_change_the_decision: ""
  cost_of_error:
    downside_if_wrong: ""
    reversibility: "reversible | costly to reverse | irreversible"
    safety_privacy_legal_constraints: []
  current_knowledge:
    established_facts: []
    existing_models_and_forecasts: []
    prior_incidents_or_near_misses: []
    available_data_and_instrumentation: []
    known_gaps_already_recognized: []
  current_assumptions:
    explicit: []
    implicit_sources_to_mine:       # where the unstated assumptions live
      - plans
      - requirements
      - models_and_parameters
      - dashboards_and_metric_definitions
      - data_pipelines
      - contracts_and_slas
      - incentives
      - team_interfaces
      - stakeholder_narratives
  scan_scope:
    domains: []
    adjacent_domains: []
    geographic_temporal_scope: ""
    sources: []                     # literature, incidents, filings, support notes, advisories, ...
  constraints:
    budget_time_access: ""
    governance_or_ethics_review_required: ""
  assumptions_made: []              # anything filled in without confirmation
  blocking_questions: []            # minimal questions that must be answered first
```
