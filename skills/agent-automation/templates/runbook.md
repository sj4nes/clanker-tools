# Runbook: <automation name>

## At a glance

- **Owner**: · **On-call**:
- **Kill switch**: `<how to set — flag, config key, endpoint>`
- **Audit log**: `<where — dataset / index / bucket>`
- **Circuit-breaker state**: `<where to read it>`

## Kill switch

**When to use**: unexpected side effects, a spike in denials or errors, a
suspected prompt-injection incident, an upstream data-quality problem.

1. Set `<kill switch>` — this makes the executor refuse every state-changing
   action immediately.
2. Confirm the `kill_switch_engaged` event appears in the audit log.
3. Notify the owner.
4. Investigate using the audit-query recipes below before re-enabling.

## Circuit-breaker reset

**Trip condition**: `<N failures in M minutes / anomaly rule>`.

1. Confirm the underlying dependency is healthy (status page, direct probe).
2. Check for a backlog of un-run triggers and decide whether to replay or drop.
3. Reset via `<procedure>`.
4. Watch the first `<K>` runs; re-trip manually if error rate stays high.

## Reconciliation (postcondition failure / partial saga)

1. Pull every `tool_execution_completed` and `postcondition_verified` event for
   the affected `run_id`.
2. For each write, check the target system's current state against the intended
   postcondition.
3. If a write did not land: re-submit with the **same idempotency key** (never a
   new one).
4. If a write landed twice: apply the compensating action once.
5. For a broken saga: run outstanding compensations in reverse step order, each
   verified; open a ticket for any compensation that fails.
6. Record a manual `reconciliation_started` / resolution note in the audit log.

## Audit-query recipes

- **Everything for one run**: filter `run_id = ...`, sort by `timestamp`.
- **All denials today**: `event_type = action_blocked` OR `policy.decision = deny`.
- **Approvals and approvers**: `event_type = approval_recorded`.
- **Writes to system X**: `event_type = tool_execution_completed AND tool.name = X`.
- **Limit breaches**: `event_type = limit_exceeded`.
- **Possible injection**: `error.class = external_safety_issue`.

## Escalation

| Situation | Contact | SLA |
|---|---|---|
| Uncontrolled side effect | Owner + security | immediate |
| Circuit breaker stuck open > 1h | Platform on-call | 1h |
| Reconciliation compensation failed | Owner | 4h |
| Suspected prompt-injection incident | Security | immediate |
