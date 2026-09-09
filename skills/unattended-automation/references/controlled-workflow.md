# The controlled workflow (single job)

Every unattended job runs the same ordered pipeline. The order matters: each
step is a gate that makes the next step safe.

```text
1. Validate inputs        — nothing downstream runs on bad data
2. Plan / dry-run         — compute the intended changes without making them
3. Guards                 — lock, kill switch, limit checks (cheap, fail fast)
4. Execute                — narrow, scoped calls; one unit of work at a time
5. Verify postconditions  — prove the intended state exists
6. Emit audit event       — structured record of trigger, inputs, changes, outcome
```

## 1. Validate inputs

Treat config, environment variables, CLI args, queue messages, upstream files,
API responses, and the previous run's output as untrusted. Check:

- **Presence** — every required input is set (fail on missing, do not default
  silently for anything that matters).
- **Type and range** — numbers parse and fall in bounds; enums are known values.
- **Shape** — JSON/CSV parses fully; expected keys/columns present; row count is
  plausible.
- **Freshness** — the upstream file's timestamp is within the expected window; a
  "today's export" that is three days old is a failure, not an input.
- **Size** — not empty when it must not be; not absurdly large (a sign of an
  upstream bug).

On any failure: exit non-zero with a specific message, emit the audit event with
`outcome: rejected`, alert. Do not partially process.

## 2. Plan / dry-run

Compute the full set of intended changes as data — the list of record IDs to
update, files to delete, messages to send — before making any of them. Benefits:

- A `--dry-run` mode is just "stop after this step and log the plan".
- You can enforce the "max records per run" limit against the plan and abort
  before touching anything.
- The plan goes in the audit event, so a later reconciliation knows what the run
  intended.

## 3. Guards (fail fast, cheap first)

In order:

1. **Kill switch** — a flag file / config key / feature flag. If set, log
   `outcome: skipped_kill_switch` and exit 0 (or a distinct code). Nothing else
   runs.
2. **Lock** — acquire an exclusive single-instance lock (`flock` on a lockfile,
   `mkdir` of a lock directory, a `SELECT ... FOR UPDATE` lock row, a lock
   object with a TTL). If held, apply the overrun policy (usually: log
   `outcome: skipped_locked`, exit 0). Always release on exit, including on
   signal.
3. **Limits** — plan size vs `max_items`; projected spend vs cap; current time
   vs a maintenance-window blackout. Abort before execution if exceeded.

## 4. Execute through narrow interfaces

- One unit of work at a time (one record, one file, one message), so a crash
  leaves a known boundary and a checkpoint is meaningful.
- Each state change idempotent (see
  [`reliability-properties.md`](reliability-properties.md)).
- Per-call timeout on every external call.
- The retry taxonomy from [`error-and-retry.md`](error-and-retry.md) wraps each
  call — not the whole loop.
- Check the kill switch between units for a long run.
- Update the checkpoint after each completed unit.

## 5. Verify postconditions

The tool returning success is a claim, not proof. Independently observe the
intended state:

- Wrote a row → read it back and check the fields.
- Deleted files → stat them and confirm they are gone (and that you deleted the
  count you planned to, not more).
- Sent a message → check the provider's sent log or a delivery receipt.
- Produced a report → check it exists, is non-empty, and has the expected row
  count.

On mismatch: stop, do not retry blindly, emit `outcome: postcondition_failed`,
alert, and leave a reconciliation task.

## 6. Emit the audit event

One structured event (schema:
[`../templates/audit-event.schema.json`](../templates/audit-event.schema.json)):
trigger and its source, input fingerprints and freshness, the plan, what
actually changed (IDs / paths / counts), retries per call, duration,
postcondition result, exit status. Write it somewhere the job cannot later
rewrite.

## Worked example: nightly stale-file cleanup

| Step | What it does |
|---|---|
| Validate | `RETENTION_DAYS` is an int in `[1, 3650]`; `TARGET_DIR` exists and is inside the allowed root; the dir is not empty (empty = probably a mount failure → abort). |
| Plan | List files older than `RETENTION_DAYS`; that list is the plan. Abort if `len(plan) > MAX_DELETES` (a spike means something is wrong upstream). |
| Guards | Kill switch: `/etc/cleanup/PAUSED` absent. Lock: `flock /var/lock/cleanup.lock`. |
| Execute | For each file: move to a dated trash dir (reversible) rather than `rm`; per-file, log the move. |
| Verify | Each planned file is no longer in `TARGET_DIR` and *is* in trash; deleted count == planned count. |
| Audit | Event: `{trigger: "cron", planned: 143, moved: 143, trash_dir: "...", duration_s: 12, exit: 0}`. |
| Silence alert | Dead-man's-switch pinged on success; monitor alerts if no ping in 26h. |

A separate weekly job purges the trash dir older than N days — itself a
controlled workflow.
