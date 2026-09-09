# Automation charter: <name>

> The contract for what this automation does, when, and within what bounds.
> Fill every field. Mark unknowns `ASSUMPTION:` and confirm before scheduling.

## Purpose and ownership

- **What it does (one sentence)**:
- **Why it must be automated (vs run by hand)**:
- **Owner (accountable)**:
- **On-call / operators**:
- **Explicitly out of scope**:

## Trigger and schedule

- **Trigger type**: cron | systemd timer | scheduler | queue consumer | webhook | CI | manual
- **Schedule / frequency**:
- **Timezone** (prefer UTC):
- **Overrun policy**: skip this run | queue/serialize | kill previous
- **Missed-run policy**: skip | run once on recovery | backfill intervals | watermark
- **Trigger authentication** (webhooks/queues):

## Contract

### Inputs (each is untrusted)

| Input | Source | Validation rule | On failure |
|---|---|---|---|
|  |  | type/range/shape/freshness/size |  |

### Effects (the complete set this automation may cause)

| Effect | Target system | Idempotency strategy | Destructive? | Reversal |
|---|---|---|---|---|
|  |  | check-then-act / key / upsert / converge / ledger | yes/no | dry-run + backup / soft-delete / compensation / none |

### Postcondition

- **What proves a run succeeded**:
- **How it is checked** (read-after-write / count / receipt):
- **Reconciliation path on mismatch**:

## Limits

- Run timeout: · Per-call timeout:
- Max items / bytes / calls per run:
- Spend cap (run / day):
- Retry cap (per call / per run): · Concurrency cap:
- Maintenance-window blackout:

## Procedure

- **Steps and order** (versioned; keep compact):
- **Drift review cadence** (confirms each step still does something the environment doesn't already do):
- **Change control** (who may edit steps/thresholds; held-out check before it goes live):

## Identity and secrets

- **Service account** (dedicated):
- **Permissions granted** (least privilege):
- **Data scope**:
- **Secret source** (secret store, not repo/crontab):

## Safe to stop

- **Kill switch** (mechanism + who sets it):
- **Signal handling** (SIGTERM behavior):
- **Checkpoint / resume** (what is persisted, where):
- **Circuit breaker** (dependency, trip condition, state location):

## Observability

- **Audit event destination** (separate from app DB):
- **Schema**: [`audit-event.schema.json`](audit-event.schema.json)
- **Retention**:
- **Exit-code convention**:
- **Failure alert channel**:
- **Silence alert** (heartbeat / dead-man's switch + window):

## Pipeline (if multi-stage)

- **Stages and dependencies** (→ `tsort`):
- **Run manifest location**:
- **Failure default**: resume from checkpoint | compensate and stop
- **Compensations defined and tested**: [ ]

## Sign-off

- [ ] Owner approved the effects and limits.
- [ ] Procedure is versioned with a drift-review cadence set.
- [ ] Failure-scenario matrix passes (`references/checklist.md`).
- [ ] Runbook complete ([`runbook.md`](runbook.md)).
- [ ] Scheduled paused / low-frequency with a ramp plan.
