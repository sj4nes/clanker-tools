# The four properties, and how to get them

A reliable automation is **observable**, **bounded**, **reversible where
possible**, and **safe to stop**. Each is a set of concrete mechanisms, not an
attitude.

## Observable

You can tell, without being there, what it did and whether it worked.

- One structured event per run (and per stage): trigger, input fingerprints,
  the plan, actual changes, postcondition result, retries, duration, exit code.
- Meaningful exit codes (see [`observability.md`](observability.md)).
- Metrics: run count, success/failure count, duration, items processed, retries,
  age of last success.
- An alert on failure **and** an alert on silence (heartbeat / dead-man's
  switch). A scheduled job that simply stops firing is the failure mode plain
  error-alerting misses.
- Logs and audit events stored where the automation cannot rewrite them.

## Bounded

It cannot run away.

- **Time**: a wall-clock timeout for the whole run (`timeout(1)`, a supervisor
  kill, a scheduler max-runtime) and a timeout on every external call.
- **Volume**: a cap on records / files / bytes / rows / API calls processed per
  run, checked against the *plan* before execution. Exceeding it aborts and
  alerts — it usually means an upstream bug.
- **Money**: a spend cap for paid APIs or transactional operations; stop and
  alert at the cap.
- **Concurrency**: a single-instance lock, plus a cap on parallel workers within
  a run.
- **Retries**: an attempt cap and a total-elapsed cap per call; one retry budget
  for the run.
- **Blast radius**: scope every query and credential so that even a logic bug
  can only touch this automation's own data.

## Reversible where possible

A mistake can be undone, or at least contained.

- **Dry-run / check mode** for anything destructive: log the plan, change
  nothing. Make it the default in non-production.
- **Backup before mutate**: snapshot the table, copy the file, export the
  records — before a delete / overwrite / truncate / mass update. Keep the
  backup long enough to notice a problem.
- **Soft delete**: move to a dated trash directory, set a `deleted_at` column,
  tag-and-sweep-later — instead of an irreversible `rm` / `DELETE`.
- **Staged rollout**: change 1%, verify, then 10%, then 100% — for automations
  that touch many things or many hosts.
- **Compensations**: for external effects that cannot be rolled back (a charge,
  an email, a provisioned resource), define and test the compensating action
  (refund, correction notice, deprovision). See
  [`error-and-retry.md`](error-and-retry.md).
- Some things are genuinely irreversible (a sent email, a published release, a
  destroyed backup). Those get a confirmation gate the scheduler sets
  deliberately, or human approval, or they are not automated.

## Safe to stop

Killing it — by signal, deploy, host reboot, or kill switch — never corrupts
state.

- **Signal handling**: trap `SIGTERM`/`SIGINT`; finish the current unit of work
  or cleanly abandon it, release the lock, flush logs, exit with a distinct
  code. Do not start a new unit after a stop is requested.
- **Atomic units**: structure work so each unit either fully commits or does
  not. Write to a temp file and `rename(2)`; use a transaction; use an
  idempotency key so a re-run finishes what a kill interrupted.
- **Checkpoint / resume**: for long runs, persist progress (last processed ID,
  offset, cursor, per-stage status) after each unit. The next run reads the
  checkpoint and resumes rather than restarting from zero or, worse,
  reprocessing.
- **Kill switch**: a flag file / config key / feature flag checked at startup
  and between units. When set, the current run winds down and future runs
  refuse to act (they still run, log `skipped_kill_switch`, and exit cleanly, so
  the scheduler and silence-monitor stay happy).

## Idempotency patterns (the load-bearing one)

| Pattern | Use when | Example |
|---|---|---|
| Check-then-act | The target state is queryable | `if not exists(user): create(user)` |
| Idempotency key | The downstream supports it | `POST /charges` with `Idempotency-Key: run42-inv8821` |
| Natural-key upsert | You own the store | `INSERT ... ON CONFLICT (key) DO UPDATE` |
| Converge to desired state | You manage config/resources | Declare the full desired set; add missing, remove extra |
| Content-addressed output | Producing files/artifacts | Name the output by a hash of its inputs; skip if present |
| Dedup ledger | Nothing else is available | Record `(key → done)` locally; skip keys already done |

If none of these is possible for a given effect, that effect is not safe to
automate unattended without a lock *and* a checkpoint *and* a postcondition
check that together guarantee exactly-once in practice — and you should say so
explicitly.
