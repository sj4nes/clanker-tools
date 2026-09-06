# Governance and failure modes

Discovery is a loop, not a one-off brainstorm. This keeps it alive and honest.

## Monitoring plan

Every high-priority assumption, hypothesis, and signal gets an indicator so that
new information actually changes action.

```yaml
monitoring_plan:
  indicators:
    - name: ""
      watches: ""              # which assumption / hypothesis / signal
      measurement: ""          # data source, cadence, who computes it
      threshold: ""            # the value that triggers a response
      response: ""             # review / escalate / execute contingency
  escalation:
    - trigger: ""
      to: ""                   # role / owner
      within: ""               # time
  reassessment_cadence: ""     # e.g. monthly, or before each commitment gate
```

Thresholds must be set *before* the data is seen, and must name a response —
"watch this number" with no response is not monitoring.

## Operating cadence

- **Before major commitments** — Key Assumptions Check, red team, premortem,
  scenario set, decision gates, and the probe plan.
- **During execution** — anomaly review, forecast updates, near-miss capture,
  instrumentation checks, escalation of threshold breaches.
- **After outcomes or incidents** — blameless surprise review, assumption and
  model update, lesson capture, revision of the monitors.

## Organizational memory

Convert surprises, near-misses, and resolved forecasts into a **searchable**
record, not isolated anecdotes: what was expected, what happened, which
assumption made the difference, what changed as a result, and the indicator now
watching for a recurrence. The next team should be able to find it before they
repeat it.

## Failure modes to reject

### A brainstorm is not a discovery process
A long risk list creates the illusion of thoroughness. Every item must carry a
causal mechanism, evidence, confidence, impact, earliest observable indicator,
owner, next learning action, and review date. No exceptions.

### Do not convert unknown unknowns into fake probabilities
If there is no defensible reference class, say the uncertainty is deep, name the
scenarios, name the distinguishing indicators, and recommend a robust or
reversible action.

### Do not collapse dissent prematurely
An operational plan may need one "most likely" story, but it must never erase
the alternatives. Keep the alternative-hypothesis register and a "what would
change our mind" section.

### Do not optimize for discovery volume
More alerts, more research threads, more dashboards can *worsen* situational
awareness. The target is actionable learning, with thresholds for escalation and
for closing an item.

### Do not let the system self-seal
If every contradiction is filed as "noise", "edge case", or "user error", the
process has failed. Contradictory evidence triggers an explicit review of its
provenance and its diagnostic value.

### Do not manufacture false confidence
"We ran a discovery process, therefore we have covered everything" is the
failure this skill exists to prevent. The report always states what remains
unknowable now and when to reassess.

## Evaluation cases

The correct behaviour in each is to recognize a blind spot, not to answer
confidently.

| Case | Required behaviour |
|---|---|
| Capacity model predicts stable service; operators report frequent manual workarounds | Flag missing operational telemetry; interview operators; reconcile the formal workflow with the actual work |
| Dashboard shows a sharp decline after a release | Hold competing hypotheses (regression / instrumentation bug / traffic-composition shift / outage / reporting lag); propose a discriminating check for each |
| Model works in normal weather; deployment planned across all seasons | Name the extrapolation; design seasonal stress simulations and data collection; conservative limits; staged rollout |
| Vendor claims high reliability with no raw failure data | Mark evidence insufficiency; demand failure definition, denominator, operating conditions, independent references |
| Safety controller never tested under sensor dropout | High-priority unknown; require fault injection, safe-state behaviour, independent protection, bounded validation |
| Strategy assumes customers will not adapt | Stakeholder inversion; behavioural research; scenario planning; post-launch adaptation indicators |
| A forecast is stated as "almost certain" | Require a quantified probability, a horizon, a reference class, disconfirming evidence, and a calibration record |
