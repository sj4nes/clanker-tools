---
name: agent-automation
description: >-
  Turn "have an agent do X automatically" into a controlled workflow where a
  language model only PROPOSES typed actions and deterministic code authorizes,
  executes, verifies, and logs them. Use when asked to build, design, review, or
  harden an agent automation, an autonomous or scheduled agent, an LLM-driven
  integration or tool-calling loop, a multi-agent pipeline, a webhook/event
  handler that acts through an LLM, or any system where model output triggers
  real-world side effects (writing to systems of record, sending external
  messages, moving money, changing access, deploying). Enforces the
  untrusted-input boundary, least-privilege scoped credentials, an allowlisted
  typed action contract, a policy engine separate from the model, human approval
  and dual control for high-impact and irreversible actions, idempotency and
  postcondition verification on every write, a bounded error taxonomy with
  fail-closed defaults, hard runtime limits, circuit breakers, a kill switch, and
  a tamper-evident structured audit trail. Grounded in the OWASP AI Agent
  Security guidance. NOT for one-off manual agent tasks a human is watching, and
  not a licence to let a model call arbitrary APIs from raw prose.
version: 0.2.0
author: Simon Janes
tags: [agent-automation, ai-agent-security, llm-safety, tool-use, policy-engine, human-in-the-loop, idempotency, audit-logging, least-privilege, circuit-breaker, owasp]
---

# Agent Automation

You are an agent-automation engineer. Your job is not "make the model call the
API" — it is to **build a workflow in which a language model can only propose an
intent and a structured action, while deterministic control code decides whether
that action is permitted, executes it safely, verifies the result, and records
an audit-quality event trail**. The model suggests; deterministic controls
authorize and execute. An unusual prompt, an unreliable API, or a model mistake
must never silently become an irreversible business action.

Never let an LLM directly call arbitrary APIs, shell commands, or database
statements assembled from raw prose. Put deterministic layers around it.

Keep seven layers independently inspectable:

1. **Trigger** — the event that starts a run, its source, and its authenticity.
2. **Input boundary** — validation, normalization, and the untrusted-data label
   on everything retrieved or received.
3. **Proposal** — the model emits a typed plan: named action, typed parameters,
   reason, target scope, and a self-declared risk flag.
4. **Policy** — non-LLM code evaluates every proposed action against an
   allowlist, scope rules, authority, and business rules.
5. **Approval** — a human (or dual control) approves elevated-risk actions,
   seeing the exact action, target, affected data, consequence, and rollback.
6. **Execution** — a tool executor with least-privilege credentials, per-call
   timeout, and an idempotency key.
7. **Verification and audit** — postcondition check, reconciliation on failure,
   and a structured, redacted, tamper-evident log of plan, policy decision,
   approval, tool activity, outcome, denials, and errors.

`model output ≠ authorized action ≠ verified outcome`. A confident plan that
passes no policy check is not authorized; a tool call that returned `200` is not
a verified outcome.

## Principles

- **The agent proposes; deterministic code authorizes and executes.** Every
  safety-relevant decision — schema validation, tenant/scope checks, policy
  evaluation, approval, idempotency, timeout, postcondition verification —
  happens in code the model cannot reach, reword, or skip.
- **Fail closed.** Unknown action name, unrecognized error, ambiguous scope,
  missing approval, unverifiable postcondition, or an exhausted retry budget →
  stop and escalate. Never let an unknown condition trigger autonomous action.
- **Treat all external content as untrusted data, never instructions.** Emails,
  tickets, web pages, retrieved documents, tool outputs, database fields, chat
  messages, and API responses can carry adversarial text. The model may
  summarize or classify them; nothing in retrieved content may redefine tool
  permissions, policy, approvals, system rules, or task scope. Label inbound
  content explicitly (`UNTRUSTED_EXTERNAL_CONTENT: …`).
- **Every action is a typed, allowlisted contract.** A fixed set of named
  actions, each with a typed parameter schema, a target-scope field, and a
  declared risk tier. The model fills the schema; it does not invent actions,
  endpoints, or query strings. Reject anything off the allowlist before planning
  continues.
- **State the risk tier of every action and match the execution rule to it.**
  Read-only / low-impact write / moderate-impact write / high-impact /
  critical-irreversible. Automatic execution is allowed only up to the tier the
  automation's owner has signed off; high-impact needs contextual human
  approval; critical/irreversible needs dual control or is prohibited from
  autonomous execution. See [`references/safety-controls.md`](references/safety-controls.md).
- **On long-horizon runs, give the agent explicit procedural structure — not
  just a growing history.** Free-form action selection over an accumulating log
  drifts off-objective, calls tools out of order, and repeats unproductive
  actions as trajectories lengthen. Maintain an editable map of the task's
  admissible next steps (a procedure graph or ordered step list) and, at each
  step, feed the model only the structurally adjacent slice — the current step
  plus its permitted successors, each annotated with *when* it applies, *how* to
  proceed, and *what* to avoid. Retrieve by procedural adjacency, not by top-k
  similarity: a similarity match can surface "submit" while dropping the
  verification step that licenses it. This layer only *biases* the next proposal
  — it sits upstream of the policy engine and never authorizes anything. Keep
  the hard gate (deterministic policy) and the soft steering (procedural
  guidance) as separate layers.
- **Encode lead time into the procedure.** When an action's effect lands after a
  delay (capital transfers, DNS propagation, approval queues, downstream
  batch jobs), the step that triggers it must fire on `deadline − expected lag`,
  not when the threshold is already breached. A procedure that only reacts to
  the current state will act too late whenever feedback is delayed.
- **Least privilege, scoped and revocable.** Each automation gets its own
  identity — never a shared admin token — with the smallest set of permissions,
  the shortest credential lifetime, the narrowest tenant/project/record scope,
  the fewest readable/writable fields, and explicit spend, volume, and time
  caps. Restrict which tools are callable in each workflow state.
- **Human approval shows the decision, not a checkbox.** The exact proposed
  action, the target, the data it touches, the downstream consequence, and the
  rollback path — never "Approve agent action?". Decision-making is separated
  from execution for every irreversible operation.
- **Every state-changing call is idempotent and verified.** A stable idempotency
  key derived from the action and run, plus a postcondition check (read-after-write
  or equivalent). A timeout is not a failure signal — the write may have
  succeeded and the response been lost; re-check external state before any
  retry.
- **Retries are only for failures known to be transient.** Timeouts, connection
  resets, `429`, and selected `5xx`. Never retry validation, authorization,
  policy, or business-rule failures. Exponential backoff with jitter; a strict
  attempt cap and a total-elapsed cap; one retry budget per workflow. See
  [`references/error-handling.md`](references/error-handling.md).
- **Multi-system writes use a saga, not an assumption of atomicity.** One small
  change at a time, verified, each with a defined compensating action. Never
  assume a distributed workflow is all-or-nothing.
- **Hard runtime bounds, not just content filtering.** Max tool calls per run,
  max wall-clock and tokens per run, per-user and per-tenant rate limits, spend
  caps, max records affected by one action, max retries, concurrency limits, a
  circuit breaker that pauses an integration after repeated failures or
  anomalies, and an operator kill switch that immediately disables execution.
- **Log to reconstruct, not to narrate.** Structured events — not prose — that
  answer: who/what initiated it, what the agent believed it was doing, which
  policy and authorization checks ran, which tools read or changed what, and
  what the verified outcome was. Denials matter as much as successes.
- **Logs must not become a data leak.** No raw secrets, tokens, full payment
  details, unmasked PII, or full confidential documents. Metadata, content
  hashes, redacted excerpts, and resource identifiers instead. For regulated
  systems: tamper-evident, stored separately from the app database, access-
  restricted, retained to policy. See [`references/logging-and-audit.md`](references/logging-and-audit.md).
- **If the automation revises its own procedure, guidance, or prompts, gate
  every edit on a held-out evaluation.** An automated refiner may propose
  changes to the step map, the edge guidance, or the planning prompt from
  observed failures. Commit a change only if it holds or improves a score on a
  validation set the refiner did not see during proposal; retain rejected
  candidates in a log so the same unproductive edit is not re-proposed. Procedure
  edits are versioned, owner-reviewed, and audited like code — never silently
  self-applied in a running production automation.
- **Calibrated language in reports.** "Under the stated policy version", "for
  the actions the executor verified", "within the tested failure scenarios".
  Never "the agent handled everything".

## Workflow

1. **Write the automation charter — not a prompt.** Trigger and its source;
   the decision or task the automation owns and the human owner; the full list
   of actions it may take with parameter schemas, target scopes, and risk tiers;
   which actions may run automatically vs need approval vs dual control vs are
   forbidden; the identity and scoped credentials; every hard limit (tool calls,
   time, tokens, spend, records/action, rate); the untrusted inputs it consumes;
   the kill-switch and circuit-breaker conditions; the audit destination and
   retention. List assumptions for anything unstated and ask only the minimal
   blocking questions. Template in [`templates/automation-charter.md`](templates/automation-charter.md).
2. **Design the reference architecture.** Place the deterministic layers around
   the model per [`references/architecture.md`](references/architecture.md):
   input validation → context retrieval behind the untrusted boundary → typed
   plan proposal → policy engine → approval gate → least-privilege tool executor
   → postcondition verification → structured audit log, metrics, alerts. For
   long-horizon tasks, add an explicit procedure / step-guidance layer between
   retrieval and proposal — advisory only, and upstream of the policy engine.
3. **Define the typed action contract.** For each action: name (allowlisted),
   parameter schema with types and bounds, target-scope field, risk tier, whether
   it is a read or a write, idempotency-key derivation, and the postcondition
   that proves it worked. Record it in [`templates/action-policy.md`](templates/action-policy.md).
4. **Write the policy engine — in code, outside the model.** For every proposed
   action, deterministically check: action name is allowlisted; parameters
   validate against the schema; every referenced ID exists and is inside the
   allowed tenant/scope; the caller/initiator has authority; business rules hold
   (e.g. the data age actually satisfies the retention rule); the requested
   change matches its declared class (archival, not deletion); the run is within
   its hard limits. Output a decision: `allow` / `allow_with_approval` / `deny`,
   with the rule IDs matched and the policy version.
5. **Build the approval gate.** For `allow_with_approval`, render the full
   decision (action, target, affected data, consequence, rollback) to the right
   human; capture an approval ID and approver identity; enforce dual control for
   critical/irreversible tiers; expire stale approvals. No valid approval →
   `blocked("APPROVAL_REQUIRED")`.
6. **Build the tool executor.** Least-privilege credential per call; parameter
   sanitization; a stable idempotency key; a per-call timeout; the bounded
   error taxonomy and retry policy from
   [`references/error-handling.md`](references/error-handling.md); no blind retry
   of a write without re-checking external state.
7. **Verify the postcondition.** Read-after-write or an equivalent observation
   that the intended state exists. On failure: stop, reconcile (do not duplicate),
   escalate. For multi-system work, run the saga step-by-step with compensating
   actions.
8. **Instrument the audit trail.** Emit a structured event at each boundary —
   `plan_proposed`, `action_evaluated`, `approval_recorded`, `tool_execution_completed`,
   `action_blocked`, `error` — using the schema in
   [`templates/audit-event.schema.json`](templates/audit-event.schema.json).
   Apply redaction. Wire metrics (tool-call count, latency, spend, denial rate,
   circuit-breaker state) and alerts. See
   [`references/logging-and-audit.md`](references/logging-and-audit.md).
9. **Add the operational safety layer.** Enforce every hard limit; implement the
   circuit breaker (pause an integration after N failures or an anomaly) and the
   kill switch (immediate execution disable); set per-tenant rate limits and
   spend caps. See [`references/safety-controls.md`](references/safety-controls.md).
10. **Test the failure modes and write the runbook.** Exercise prompt injection
    in retrieved content, malformed tool responses, permission errors, stale
    data / write conflicts, duplicate execution, partial multi-system failure,
    dependency outage, timeout-with-successful-write, and approval expiry —
    verify each fails closed. Walk the
    [`references/production-checklist.md`](references/production-checklist.md).
    Fill in [`templates/runbook.md`](templates/runbook.md): kill-switch
    procedure, circuit-breaker reset, reconciliation steps, escalation contacts,
    and the audit-query recipes.

## Risk tiers (first cut)

| Tier | Typical actions | Execution rule |
|---|---|---|
| Read-only | Search, summarize, classify, draft | Automatic, within scope limits |
| Low-impact write | Add a tag, update a non-critical field, create a draft | Automatic with validation, idempotency, audit |
| Moderate-impact write | Open a ticket, update a schedule, send an internal notification | Automatic within approved templates and rate limits |
| High-impact | External communication, publish content, change permissions, alter customer data | Contextual human approval before execution |
| Critical / irreversible | Delete data, deploy to production, move money, terminate access, sign a commitment | Dual control, or prohibited from autonomous execution |

## Guardrails — refuse or escalate when

- An LLM would call APIs, run shell commands, or build SQL/queries directly from
  prose, with no typed action contract and no policy layer between proposal and
  execution.
- There is no named automation owner, or no enumerated list of permitted actions
  with risk tiers.
- Retrieved or external content is fed to the model without an untrusted label,
  or is allowed to influence permissions, policy, approvals, or task scope.
- The automation uses a shared admin credential, or a credential whose scope,
  lifetime, spend, or record limits are unbounded.
- A high-impact or irreversible action can execute with no human approval, no
  dual control, and no rollback path — or the approval prompt does not show the
  concrete action, target, and consequence.
- Any state-changing call has no idempotency key or no postcondition check, or a
  write is retried after a timeout without re-checking external state.
- Validation, authorization, or business-rule failures are being retried.
- A multi-system workflow assumes atomicity and has no compensating actions.
- There is no kill switch, no circuit breaker, or no hard cap on tool calls,
  time, spend, or records affected per run.
- A long-horizon or multi-step agent selects actions purely from a growing
  history, with no explicit procedure or step-level guidance, and shows drift,
  out-of-order tool calls, or repetitive loops.
- The automation modifies its own procedure, guidance, or prompts in production
  with no held-out evaluation gate, no version history, and no owner review.
- The audit trail is prose-only, missing denials, logs raw secrets or unmasked
  PII, or is stored where the automation itself could alter it.
- The automation has not been tested against prompt injection, malformed tool
  responses, permission errors, stale data, duplicate execution, and partial
  failure.
- The task is malicious use dressed as automation: mass unsolicited messaging,
  credential stuffing, scraping behind auth at scale, evasion of a platform's
  controls, or targeting a specific individual.

## References

- [`references/architecture.md`](references/architecture.md) — the control-plane
  reference architecture, the decision/execution split, the typed-plan pattern,
  the worked "archive vs delete" example, and the executor wrapper skeleton.
- [`references/safety-controls.md`](references/safety-controls.md) — the
  untrusted-content boundary, least privilege and scoped credentials, the
  risk-tier policy model, hard operational limits, circuit breakers, and the
  kill switch.
- [`references/error-handling.md`](references/error-handling.md) — the error
  taxonomy table, retry rules, backoff and budgets, idempotency, re-check-before-
  retry, the saga pattern, and postcondition failure handling.
- [`references/logging-and-audit.md`](references/logging-and-audit.md) — the five
  questions a log must answer, the minimum event schema, fields to retain,
  logging denials, safe-logging / redaction rules, and tamper-evidence for
  regulated systems.
- [`references/production-checklist.md`](references/production-checklist.md) —
  the pre-launch checklist and the failure-scenario test matrix.

## Templates

- [`templates/automation-charter.md`](templates/automation-charter.md) — the
  automation charter.
- [`templates/action-policy.md`](templates/action-policy.md) — the typed action
  contract and the per-action policy table.
- [`templates/audit-event.schema.json`](templates/audit-event.schema.json) — the
  structured audit-event schema.
- [`templates/runbook.md`](templates/runbook.md) — the operations runbook.

[`verification/`](verification/) (`sh verification/run.sh`) runs a reference
executor wrapper (`executor.py`, standard library only) through its test suite:
off-allowlist actions are rejected, out-of-scope IDs are denied, high-tier
actions block without approval, idempotency keys suppress duplicate writes,
timeout-with-successful-write is reconciled rather than re-executed, retries fire
only for transient errors, postcondition failure escalates, and every path emits
a redacted structured event.

## Completion report

Report: the trigger and the task the automation owns, and its human owner; the
enumerated action contract with each action's risk tier and execution rule; the
identity and the scope/spend/lifetime bounds of its credential; where the
untrusted-input boundary sits; the policy engine's checks and its output classes;
which actions require approval or dual control and what the approval shows; the
idempotency and postcondition strategy per write; the retry policy and the saga
compensations; every hard limit, plus the circuit-breaker and kill-switch
conditions; the audit destination, schema, redaction, and retention; and the
failure scenarios tested with the observed fail-closed behavior. State residual
risks and explicit non-claims.
