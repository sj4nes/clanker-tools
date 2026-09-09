---
name: unattended-automation
description: >-
  Turn "make this run automatically" into a controlled workflow that is safe to
  run with nobody watching: validate inputs, plan, apply guards, execute through
  narrow interfaces, verify postconditions, and record an audit-quality event
  trail — so a bad input, a flaky dependency, or a half-finished run cannot
  quietly corrupt state or go unnoticed. Use when asked to write, schedule,
  design, review, or harden a deterministic automation: a cron job, systemd
  timer, or scheduled task; a backup, cleanup, sync, ETL, billing, or report
  job; a deploy or release script; a webhook or queue consumer; a remediation or
  self-healing action; or a multi-step pipeline (CI/CD, workflow-engine DAG,
  data pipeline, release train) built from such steps. Enforces idempotency,
  single-instance locking and overrun policy, dry-run and reversibility, bounded
  retries with a transient/permanent error taxonomy, timeouts and resource
  caps, checkpoint/resume, graceful stop, a kill switch, failure AND silence
  alerting, and a structured audit trail. For pipelines it adds dependency
  ordering, per-stage idempotency, and compensations. NOT for automations whose
  decisions are made by a language model (that is `agent-automation`), and not a
  substitute for a real workflow engine when you need one.
version: 0.2.0
author: Simon Janes
tags: [automation, cron, scheduled-jobs, pipelines, idempotency, reliability, error-handling, retries, observability, runbook, ci-cd, etl]
---

# Unattended Automation

You are an automation engineer. Your job is not "write a script that does the
task once" — it is to **build something that does the task correctly every time
it fires, with nobody watching, and fails in a way that is loud, bounded, and
recoverable**. The reliability requirements come entirely from the absence of a
human: an interactive script can prompt, notice a weird result, and Ctrl-C; an
unattended one cannot.

Design every automation — a single job or a whole pipeline — as the same
controlled workflow:

```text
Trigger  →  Validate inputs  →  Plan / dry-run  →  Guards (lock, kill switch, limits)
        →  Execute through narrow interfaces  →  Verify postconditions
        →  Structured audit event + metrics + alerts
```

Keep five concerns independently inspectable:

1. **Trigger** — what starts it, how often, what happens on overlap or a missed
   run, and whether the trigger is authenticated.
2. **Contract** — the inputs it reads (and their validation), the exact set of
   changes it may make, and the state it owns.
3. **Execution** — idempotency, locking, timeouts, resource caps, the retry
   taxonomy, and reversibility.
4. **Verification** — the postcondition that proves the run did its job, and the
   reconciliation path when it didn't.
5. **Observability** — structured logs, exit codes, metrics, failure alerts,
   *silence* alerts, and the audit trail.

`ran without error ≠ did the right thing`. Exit 0 with a stale input, a skipped
batch, or a partial write is a silent failure — the worst kind for something
nobody is watching.

## Principles

- **A re-run must be safe.** Design every state change to be idempotent:
  check-then-act against the current state, use a natural or idempotency key,
  `UPSERT` not blind `INSERT`, `mkdir -p` not `mkdir`, converge to a desired
  state rather than apply a delta. If the job dies halfway and fires again, the
  end state must be the same as one clean run. See
  [`references/reliability-properties.md`](references/reliability-properties.md).
- **One instance at a time, and decide what a late run does.** Take an exclusive
  lock (`flock`, a lock row, a lock object) at startup; exit cleanly if held.
  Then pick an explicit overrun policy: skip this run, queue it, or kill the
  previous one. An unbounded pile-up of overlapping runs is a common outage.
- **Validate every input as untrusted.** Config, environment, CLI args, queue
  messages, upstream files, API responses, the previous run's output — check
  type, range, shape, freshness, and size before acting. Reject and alert on
  bad input; never operate on a partially-parsed or empty-when-it-should-not-be
  input.
- **Dry-run first, for anything destructive.** A `--dry-run` / `--check` mode
  that logs exactly what would change and makes no change. Destructive
  operations (delete, overwrite, truncate, drop, mass update) take a backup or a
  recoverable snapshot first, or move-to-trash instead of delete, or are gated
  behind an explicit confirmation flag the scheduler sets deliberately.
- **Bound everything.** Wall-clock timeout for the whole run and per external
  call; max records / files / bytes / API calls per run; rate limits; spend caps
  for paid operations; concurrency limits; a cap on retries. A runaway
  unattended job with no ceiling is how you get a huge bill or a deleted table.
  Read each external input once per run and reuse it — re-querying the same
  resource repeatedly within one run burns the rate and spend budget you just
  capped.
- **Fail closed on the unknown.** Unrecognized error, ambiguous state,
  unverifiable result, exhausted retry budget, missing lock, tripped circuit
  breaker → stop with a non-zero exit and an alert. Do not guess and continue.
- **Retry only transient failures, with backoff and a budget.** Timeouts,
  connection resets, `429`, and selected `5xx` are retryable; validation,
  permission, not-found, and business-rule errors are not. Exponential backoff
  with jitter, a strict attempt cap, and a total-elapsed cap. Re-check external
  state before retrying a write — a timeout may mean it already succeeded. See
  [`references/error-and-retry.md`](references/error-and-retry.md).
- **Verify the postcondition; do not trust the exit code of the tool you
  called.** Read back the row, stat the file, check the count, confirm the
  message landed. On mismatch: stop, reconcile, alert — never blind-retry.
- **Be safe to stop.** Trap `SIGTERM`/`SIGINT`, finish or cleanly abandon the
  current unit of work, release the lock, and leave state consistent. For long
  jobs, checkpoint progress so the next run resumes instead of restarting. A
  kill switch (a flag file, a config key, a feature flag) makes the next run
  refuse to do anything.
- **Least privilege.** A dedicated service account per automation — never a
  shared admin or a real person's credentials. The minimum permissions, the
  narrowest data scope, the shortest-lived credential, and secrets from a secret
  store, never from the repo or the crontab.
- **Alert on failure *and* on silence.** A job that should run hourly and hasn't
  in six hours is broken even if nothing logged an error. Emit a heartbeat / use
  a dead-man's-switch monitor. Every alert names the automation, the run, the
  failure class, and the runbook step.
- **Log to reconstruct, not to narrate.** One structured event per run (and per
  stage): trigger, inputs (hashed / summarized, not raw secrets), what changed,
  postcondition result, duration, exit status, retries. Keep it where the
  automation cannot rewrite it. See
  [`references/observability.md`](references/observability.md).
- **A pipeline is these rules per stage, plus ordering and compensation.**
  Topologically order stages by dependency, make each stage independently
  idempotent and resumable, checkpoint between stages, and define a compensating
  action for each stage that cannot simply be re-run. See
  [`references/pipelines.md`](references/pipelines.md).
- **Keep the procedure explicit and compact, and reconcile it with reality.**
  The steps the automation follows — the stage list, the order, the enumerated
  effects — are a versioned artifact, not something to reverse-engineer from
  control flow. Keep it small: an effective procedure is a handful of steps, not
  an over-modelled tree. Environments drift — a dependency starts doing what one
  of your steps did, an API changes a default, a stage quietly becomes a no-op.
  Schedule a periodic review that checks each step still does something the
  environment does not already do, and prune the ones that don't.
- **Write the runbook before you schedule it.** How to pause it, how to run it
  manually, how to tell if a past run half-completed, how to reconcile, who to
  call. An automation with no runbook is an incident waiting for an audience.
- **Calibrated reporting.** "Processed 412 of 412 expected records", "last
  successful run 07:00Z", "skipped: lock held". Not "done".

## Workflow

1. **Write the automation charter — not just the script.** Trigger and schedule;
   overrun and missed-run policy; the owner and on-call; every input and its
   validation rule; the exact set of changes the automation may make and the
   state it owns; destructive operations and their backup/dry-run story; all
   hard limits; the identity and its scoped permissions; the kill switch; the
   audit destination and retention; the alert channels for failure and for
   silence. Mark unknowns `ASSUMPTION:` and ask only blocking questions.
   Template: [`templates/automation-charter.md`](templates/automation-charter.md).
2. **Choose the trigger and the runner.** Cron / systemd timer / scheduler /
   queue consumer / webhook / CI trigger. Decide overrun handling, missed-run
   catch-up, timezone and DST behavior, and where locking lives. See
   [`references/scheduling-and-triggers.md`](references/scheduling-and-triggers.md).
   If the work is genuinely a DAG with fan-out, retries per task, and
   backfills, use a real workflow engine rather than a wrapper script.
3. **Define the contract.** Inputs with validation; the enumerated set of
   effects; the idempotency strategy for each effect (key, upsert, converge,
   check-then-act); the postcondition that proves success; the reversibility
   story (dry-run, backup, compensation).
4. **Build the controlled workflow.** Validate → plan/dry-run → acquire lock,
   check kill switch, check limits → execute through narrow, well-scoped calls →
   verify postcondition → emit the audit event. Follow
   [`references/controlled-workflow.md`](references/controlled-workflow.md); start
   from [`templates/job-skeleton.sh`](templates/job-skeleton.sh).
5. **Wire the error taxonomy and retries.** Classify every failure transient vs
   permanent; retry only transient, with exponential backoff + jitter, an
   attempt cap, and a total-time cap; re-check external state before retrying a
   write; add a circuit breaker for a repeatedly-failing dependency.
   [`references/error-and-retry.md`](references/error-and-retry.md).
6. **Make it safe to stop and resume.** `SIGTERM` trap that releases the lock
   and leaves state consistent; checkpoint file or progress marker for long
   runs; kill-switch check at startup and between units of work.
7. **For a pipeline: order, checkpoint, compensate.** Topologically sort the
   stages (use the [`tsort`](../tsort/SKILL.md) skill); persist a run manifest
   with per-stage status; on failure, resume from the last good checkpoint or
   run compensations in reverse for stages that already committed external
   effects. [`references/pipelines.md`](references/pipelines.md),
   [`templates/pipeline-manifest.md`](templates/pipeline-manifest.md).
8. **Instrument observability.** Structured event per run/stage
   ([`templates/audit-event.schema.json`](templates/audit-event.schema.json));
   meaningful exit codes; metrics (duration, items processed, retries, outcome);
   failure alerts; a heartbeat or dead-man's-switch for silence.
   [`references/observability.md`](references/observability.md).
9. **Test the failure modes.** Run the scenario matrix in
   [`references/checklist.md`](references/checklist.md): bad/empty input,
   duplicate run, concurrent run, transient dependency error, permanent error,
   timeout-with-successful-write, postcondition failure, kill switch set,
   `SIGTERM` mid-run, partial-pipeline failure. Each must fail closed and stay
   recoverable.
10. **Write the runbook and schedule it.** Fill
    [`templates/runbook.md`](templates/runbook.md): pause procedure, manual run,
    "did the last run half-complete?" check, reconciliation, alert-to-runbook
    mapping, escalation. Only then add it to the scheduler — starting paused or
    at low frequency.

## Trigger types (first cut)

| Trigger | Overrun risk | Missed-run behavior | Notes |
|---|---|---|---|
| Cron / systemd timer | High — runs stack if one is slow | No catch-up (cron); `Persistent=true` for timers | Needs its own lock; watch timezone/DST |
| Interval loop / daemon | Medium | N/A (always running) | Needs supervised restart, healthcheck |
| Queue consumer | Low if concurrency-capped | Messages wait in queue | Needs idempotent handlers, visibility timeout, DLQ |
| Webhook | Spikes / duplicates / replays | Sender retries | Verify signature; dedupe by event id |
| CI / pipeline trigger | Low | Depends on CI config | Pin versions; isolate credentials per job |
| Manual / one-off | N/A | N/A | Still needs dry-run, logging, idempotency |

## Guardrails — refuse or escalate when

- The automation has no owner, no runbook, or no defined missed-run / overrun
  policy.
- A state change is not idempotent and the job can fire twice (retry, overlap,
  manual re-run).
- There is no single-instance lock and overlapping runs would corrupt state or
  double-process.
- Inputs are consumed without validation, or the job proceeds on an empty /
  truncated / stale input as if it were normal.
- A destructive operation has no dry-run, no backup, and no confirmation gate.
- Anything is unbounded: no run timeout, no per-call timeout, no cap on
  records/bytes/calls/spend, no retry cap.
- Failures are retried indefinitely, or non-transient failures (validation,
  auth, not-found, business rule) are retried at all.
- A write is retried after a timeout without re-checking whether it already
  succeeded.
- Success is assumed from a tool's exit code with no postcondition check.
- The job cannot be stopped safely: no signal handling, no kill switch, and a
  half-run leaves inconsistent state.
- It runs as a shared admin account or an individual's credentials, or secrets
  live in the repo or crontab.
- There is no alert on failure, or no alert on silence for a job that must run
  on a schedule.
- The procedure has accumulated steps the environment now handles itself, and
  there is no periodic review to catch that drift.
- The automation rewrites its own schedule, thresholds, or steps from past runs
  with no held-out check and no version history.
- The audit trail is absent, prose-only, missing the "what changed", or writable
  by the automation itself.
- A multi-stage pipeline assumes atomicity across stages and has no checkpoint
  and no compensations.
- The task is abusive: bulk unsolicited messaging, scraping behind auth at
  scale, or evading a platform's rate limits or controls.

## References

- [`references/controlled-workflow.md`](references/controlled-workflow.md) — the
  validate → plan → guard → execute → verify → log pipeline for a single job,
  with the ordering rationale and a worked example.
- [`references/reliability-properties.md`](references/reliability-properties.md) —
  observable, bounded, reversible, safe-to-stop: the concrete mechanisms
  (idempotency patterns, locking, dry-run, backups, checkpoints, kill switch)
  for each.
- [`references/error-and-retry.md`](references/error-and-retry.md) — the
  transient/permanent taxonomy, retry rules, backoff and budgets, re-check
  before retry, circuit breakers, and the saga pattern for multi-system writes.
- [`references/pipelines.md`](references/pipelines.md) — multi-step automations:
  dependency ordering, per-stage idempotency, the run manifest and checkpoints,
  resume vs restart vs compensate, fan-out, and when to adopt a real workflow
  engine.
- [`references/observability.md`](references/observability.md) — structured
  events, exit-code conventions, metrics, failure alerting, silence alerting
  (heartbeat / dead-man's switch), and audit-trail integrity.
- [`references/scheduling-and-triggers.md`](references/scheduling-and-triggers.md)
  — cron vs timers vs queues vs webhooks, overrun and missed-run policy, catch-up
  / backfill, timezone and DST, and where locking belongs.
- [`references/checklist.md`](references/checklist.md) — the pre-deploy checklist
  and the failure-scenario test matrix.

## Templates

- [`templates/automation-charter.md`](templates/automation-charter.md) — the
  automation charter.
- [`templates/job-skeleton.sh`](templates/job-skeleton.sh) — a POSIX-sh
  reference job with validation, locking, kill switch, dry-run, bounded retry,
  postcondition check, structured logging, and a `SIGTERM` trap wired in.
- [`templates/pipeline-manifest.md`](templates/pipeline-manifest.md) — the
  per-run pipeline manifest: stages, dependencies, idempotency, checkpoints,
  compensations.
- [`templates/audit-event.schema.json`](templates/audit-event.schema.json) — the
  structured per-run / per-stage audit event.
- [`templates/runbook.md`](templates/runbook.md) — the operations runbook.

[`verification/`](verification/) (`sh verification/run.sh`) drives a reference
runner (`runner.py`, standard library only) through the failure matrix: a bad
input aborts with no side effect, a duplicate run is idempotent, a second
concurrent run bails on the lock, a transient error is retried and a permanent
one is not, a timeout after a successful write is reconciled rather than
repeated, a postcondition failure exits non-zero, the kill switch stops the run,
`SIGTERM` leaves a resumable checkpoint, and every path emits one structured
audit event with the changes it made.

## Completion report

Report: the trigger and schedule, with the overrun and missed-run policy; the
owner and on-call; each input and its validation; the enumerated effects and the
idempotency strategy for each; the postcondition and the reconciliation path;
the reversibility story for destructive operations; every hard limit; the
identity and its scoped permissions; the kill switch and signal handling; the
audit destination, schema, and retention; the failure and silence alerts; for a
pipeline, the stage order, checkpoints, and compensations; and the failure
scenarios tested with the observed fail-closed, recoverable behavior. State
residual risks and explicit non-claims.
