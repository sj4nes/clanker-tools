# Epistemic map and assumptions

The first two deliverables: sort what is known, then make the assumptions
explicit and prioritized.

## The taxonomy, in use

For every claim in scope, place it in exactly one category and record the
response it points to.

| Category | Diagnostic question | Response |
|---|---|---|
| Known known | Is this well-supported *within a stated scope*? | Document; monitor; re-verify the scope periodically |
| Known unknown | Is there an answer we could learn? | Measure / research / test / model — put it in the learning backlog |
| Unknown known | Does someone already know this but the decision-maker does not? | Search records, incident reports, tickets; interview operators; fix retrieval and escalation |
| Unknown unknown | Could a relevant factor / failure / stakeholder / dependency be unimagined here? | Diversify perspectives; scan adjacent domains; stress-test; instrument for anomalies |
| Ambiguity | Do several meanings fit the same words? | Write the competing interpretations; pick and define terms |
| Deep uncertainty | Are plausible futures / model structures available but not credible probabilities? | Scenario set, robustness, reversible commitments, signposts — **no point probability** |
| Measurement blind spot | Does the system emit an adequate observation of this variable? | Instrument; audit; use a proxy with its caveat stated |
| Model-form uncertainty | Could the causal / system model itself be wrong? | Compare independent models; seek disconfirming evidence; validate externally |
| Tail / rare-event | Are high-impact outcomes underrepresented in the history? | Fault tree, FMEA, stress test, scenario, safety margin |

Distinguish **uncertainty** (a probability we are unsure of) from **ignorance**
(we do not know which model applies) from **blindness** (we have never observed
the variable). They need different actions and different language.

## Epistemic-map schema

```yaml
epistemic_map:
  known_knowns:
    - claim: ""
      evidence: []
      scope: ""            # where / when / for whom this holds
      confidence: "low | medium | high"
      owner: ""
      review_date: ""
  known_unknowns:
    - question: ""
      why_it_matters: ""   # which decision it feeds
      learnable_by: ""     # method, roughly
  unknown_knowns_to_retrieve:
    - what: ""
      likely_holder: ""    # team, record system, individual
      retrieval_step: ""
  ambiguities:
    - term: ""
      interpretations: []
  measurement_blind_spots:
    - variable: ""
      current_observation: "none | inadequate proxy | ..."
      instrumentation_or_proxy: ""
  model_form_uncertainties:
    - model: ""
      alternative_structure: ""
      disconfirming_check: ""
  deep_uncertainties:
    - question: ""
      scenarios: []
      distinguishing_indicators: []
      robust_action: ""
  tail_risks:
    - outcome: ""
      mechanism: ""
      earliest_indicator: ""
  unknown_unknown_candidates:      # areas, not enumerated items
    - boundary_crossing: ""        # what sits just outside the stated system boundary
      under_represented_stakeholder: ""
      untested_regime: ""
```

The last block is honest about its limits: it names *where* unknown unknowns are
more likely (boundary crossings, excluded stakeholders, regimes never tested),
not a list of specific unknowns — which would be a contradiction in terms.

## Assumption extraction

Assumptions hide in: plans and roadmaps, requirements, models and their
parameters, forecasts, dashboards and metric definitions, data pipelines,
contracts and SLAs, incentive structures, interface contracts between teams, and
the stories stakeholders tell about why something works.

Convert each implicit statement into a testable claim. "Demand will scale with
onboarding volume" becomes a register entry:

| Field | Example |
|---|---|
| Assumption | Demand grows roughly proportionally with onboarding volume |
| Category | causal / behavioural |
| Why it matters | Sets the staffing and capacity plan |
| Evidence | Six months of correlation, single segment |
| Confidence | Medium |
| Scope | Current product, existing segments, normal seasonality |
| Impact if wrong (I) | High — capacity over- or under-built |
| Uncertainty (U) | Medium–high — one segment, short history |
| Reversibility of the dependent decision (R) | Low — capacity commitment is a 12-month lease |
| Dependency centrality (D) | High — three downstream plans use it |
| Disconfirming signal | Conversions per onboarded account drop > 15 % for two weeks |
| Earliest indicator | Weekly per-account conversion rate, segmented |
| Probe | Segmented cohort analysis; randomized onboarding cadence |
| Owner | Growth analytics |
| Review trigger | Before the next capacity commitment |

### Categories

factual · causal · behavioural · technical · data-quality · operational · legal
/ regulatory · financial · adversarial / security · ethical / social · temporal
/ stationarity · scaling · dependency / supply-chain · measurement · governance
/ authority.

## Key Assumptions Check

Flag assumptions that are simultaneously: highly uncertain; highly
consequential; hard to reverse; weakly evidenced; shared by several independent
decisions; and likely to fail under scale, stress, adversarial behaviour, or the
passage of time. These are the register's front page.

## The triage score

```
P = I · U · (1 − R) · D
```

- `I` — impact if the assumption is wrong (normalized 0–1 or a 1–5 scale)
- `U` — uncertainty about the assumption (0–1)
- `R` — reversibility of the decision that depends on it (0 = irreversible,
  1 = fully reversible), so `(1 − R)` rewards irreversibility
- `D` — dependency centrality: how many downstream decisions rely on it

`P` is a **triage aid, not a validated risk metric**. Always keep `I`, `U`, `R`,
`D` and the one-line rationale beside the score. Do not sum `P` across
assumptions, do not treat a `P` ranking as a probability, and re-score when
evidence changes. Its only job is to decide what to challenge and probe first.
