# Runbook: <automation name>

## At a glance

- **Owner**: · **On-call**:
- **Schedule**: · **Expected duration**:
- **Kill switch**: `<mechanism — flag file path / config key / feature flag>`
- **Lock**: `<location>`
- **Checkpoint**: `<path>`
- **Audit log**: `<location>`
- **Dashboards / alerts**: `<links>`

## Pause the automation

1. Set the kill switch: `<exact command>`.
2. The next scheduled run will exit `3` (`skipped_kill_switch`) and change
   nothing; the silence monitor stays satisfied.
3. To also stop an in-flight run: `<send SIGTERM / scale to zero>` — it releases
   the lock and writes a resumable checkpoint.
4. Note the pause in `<incident channel / log>`.

## Run it manually

- Dry run: `DRY_RUN=1 <command>` — logs the plan, changes nothing.
- Real run: `<command>`. It takes the same lock, so it will not collide with the
  scheduler.
- One-shot with a narrower scope: `<how to limit MAX_ITEMS / target>`.

## Did the last run half-complete?

1. Find the last run's audit events: `<query by run_id / grep AUDIT_LOG>`.
2. Look for `outcome`: `success` = fine; `stopped` / `partial` /
   `reconciliation_needed` / `failed` = investigate.
3. Check the checkpoint file for `last_processed` and `processed_count`.
4. Compare the recorded `changes` against the target system's current state.

## Reconcile

1. From the audit event's `plan` and `changes`, list what was intended vs done.
2. For each not-done item: re-run the job (idempotent) or apply the single
   effect manually with the same idempotency key — never a new key.
3. For any double-applied effect: apply the compensation once.
4. For a broken pipeline: consult the run manifest; resume from the last
   `succeeded` stage, or run compensations for committed `external-commit`
   stages in reverse.
5. Record the reconciliation in the audit log; close the alert.

## Alert → action

| Alert | Likely cause | First action |
|---|---|---|
| Exit 2 (bad input) | Upstream file missing/stale/malformed | Check the upstream producer; do NOT just re-run |
| Exit 4 (reconcile) | Postcondition mismatch or limit hit | Reconcile section above |
| Exit 5 / circuit open | Dependency outage | Check dependency status; breaker resets after cooldown |
| Exit 1 (unknown) | Bug or unhandled case | Pull audit + app logs for the `run_id`; page owner |
| Silence / no success in N | cron didn't fire / host down / process hung | Check scheduler, host, and for a stuck lock past its TTL |
| Lock stuck | Previous run killed without cleanup | Verify no process is running, then remove `<lock>` |

## Escalation

| Situation | Contact | SLA |
|---|---|---|
| Data loss / wrong deletion | Owner + data on-call | immediate |
| Silent for > `<N>` intervals | Platform on-call | `<time>` |
| Reconciliation compensation failed | Owner | `<time>` |
