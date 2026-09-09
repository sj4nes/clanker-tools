# Automation charter: <name>

> The charter is the contract for what this automation may do. Fill every field.
> Mark unknowns as `ASSUMPTION:` and confirm before launch.

## Purpose and ownership

- **Task / decision the automation owns**:
- **Human owner (accountable)**:
- **Operators (can pause / reset / reconcile)**:
- **What is explicitly out of scope**:

## Trigger

- **Trigger source** (schedule / webhook / queue / manual):
- **Authenticity check** (signature, mTLS, allowlisted caller):
- **Expected volume** (runs/day, peak):

## Identity and credentials

- **Agent identity** (dedicated, not shared):
- **Permissions granted** (least privilege — list each):
- **Tenant / project / record scope**:
- **Readable fields / writable fields**:
- **Credential lifetime and refresh path**:
- **Network destinations allowed**:

## Action contract

See [`action-policy.md`](action-policy.md) for the typed schemas. Summary:

| Action | Risk tier | Execution rule (auto / approval / dual control / forbidden) |
|---|---|---|
|  |  |  |

## Untrusted inputs

- **External content this automation consumes**:
- **How it is labeled / isolated**:
- **What that content may NEVER influence**: tool permissions, policy, approvals, task scope.

## Hard limits

- Max tool calls per run:
- Max wall-clock per run:
- Max tokens per run:
- Max records affected per action:
- Max retries per tool / per workflow:
- Per-tenant rate limit:
- Spend cap (per run / per day):
- Concurrency limit:

## Safety controls

- **Kill-switch mechanism and who can set it**:
- **Circuit-breaker trip condition** (N failures in window / anomaly):
- **Circuit-breaker reset procedure**: see [`runbook.md`](runbook.md).

## Audit

- **Event destination** (separate from app DB):
- **Schema**: [`audit-event.schema.json`](audit-event.schema.json)
- **Redaction rules** (no secrets / no unmasked PII / hashes for payloads):
- **Tamper-evidence** (hash chain / write-once):
- **Retention period**:

## Sign-off

- [ ] Owner has approved the action contract and execution rules.
- [ ] Failure-scenario tests pass (see `references/production-checklist.md`).
- [ ] Runbook complete.
