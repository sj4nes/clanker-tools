# Extraction

The graph database is not the intelligence. The difficult, valuable capability
is mapping messy evidence — text, tables, tickets, chat, tool output — into
structured, calibrated, role-labelled claims.

## The target

From:

> "After Finance approved the $40k Q3 budget, Maya chose managed PostgreSQL for
> Atlas because the team lacked DBA capacity. The change is effective October 1."

Extract **one** `Decision` hyperedge, not a scatter of binary edges:

```
Decision:
  subject:          Project Atlas
  decision_maker:   Maya
  selected_option:  Managed PostgreSQL
  constraint:       "team lacks DBA capacity"  (justification)
  approver:         Finance
  budget:           $40k, Q3
  valid_time:       start 2026-10-01, end open
  epistemic_status: asserted
  provenance:       <the sentence above>
```

Compare the binary decomposition:

```
Finance —approved→ budget-q3        Maya —chose→ postgres
postgres —for→ atlas                atlas —needs→ dba-capacity
```

Re-joined, those license: "Finance approved Postgres" (it approved a budget),
"the Q3 budget covers all of Atlas" (it covered this decision), "Postgres is
in use now" (it is effective October 1). The single edge asserts none of them.

## Extraction guardrails

- **Do not invent participants.** A role the source does not fill stays
  `unknown`. An extracted approver that the text never names is a fabricated
  fact.
- **Keep the source span.** Every edge carries the exact text (or table cell,
  or tool-output line) it came from. An edge with no span cannot be audited and
  does not enter the model.
- **Separate fact from inference.** "Maya chose X" — `asserted`. "X will reduce
  cost" — a prediction, `proposed`. "Therefore the migration is low-risk" —
  `inferred`. Never collapse the three.
- **Capture negation and modality.** "must not", "may", "should", "considered",
  "rejected", "declined" are materially different from the bare verb. A
  `rejected_option` role is not a `selected_option` role.
- **Attach time.** `valid_time` on every edge. "effective October 1" is a
  `start`; "the Q3 budget" bounds a budget authority; "the previous policy"
  signals a `superseded` predecessor. Most apparent contradictions are just two
  edges with disjoint or nested intervals.
- **Canonicalize cautiously.** Link "Maya", "M. Okafor", and "the DBA lead" to
  one node only at high identity confidence. A wrong merge fabricates a fact
  that no source states.
- **Avoid over-fragmentation.** A meaningful decision, event, or requirement is
  usually one hyperedge. A dozen edges each stripped of the shared context is
  worse than the prose — it *looks* structured while having lost the point.
- **Preserve scope as a role.** "for Project X", "in the EU region", "for
  enterprise customers", "under the Q3 budget" go *inside* the edge as `scope`
  / `budget` roles. This is the anti-context-collapse rule: if you factor scope
  out, a later join will assert the unscoped version.

## Worked examples

### An incident (Event + CausalHypothesis)

> "The 14:03 deploy of api-gateway 4.1 coincided with p99 latency rising from
> 120ms to 800ms for EU mobile traffic. Rolled back at 14:19; latency
> recovered. Root cause suspected to be a connection-pool default."

```
Event:
  actor: deploy-bot          target: api-gateway (prod, EU)
  input: release 4.1
  valid_time: {start: 14:03, end: 14:19}
  epistemic_status: observed
Event (State change):
  subject: p99-latency  scope: EU-mobile
  from: 120ms  to: 800ms   valid_time: {start: ~14:03, end: ~14:19}
  epistemic_status: observed
CausalHypothesis:
  cause: connection-pool default (4.1)   effect: the latency rise
  condition: EU-mobile traffic pattern
  epistemic_status: proposed         # "suspected" -> not asserted
  diagnostic_evidence_needed: pool metrics for the window; 4.0->4.1 config diff
```

### A requirement (Requirement)

> "Production deploys require: green CI on the release SHA, a security sign-off
> recorded in the change ticket, and a deploy inside the Tue/Thu 10:00–16:00
> window. The on-call may waive the window for a Sev-1 fix."

```
Requirement:
  subject: action:deploy   target: environment:production
  constraint: [ci-green(sha), security-signoff(ticket), window(Tue/Thu 10-16)]
  exception: {conjunct: window, waivable_by: role:on-call, when: sev1-fix}
  valid_time: {start: <policy date>, end: null}
  epistemic_status: asserted
```

The three conjuncts become the terms of the precondition conjunction in
`references/planning-and-governance.md`. The exception is itself role- and
condition-scoped — it does not waive `ci-green` or `security-signoff`.
