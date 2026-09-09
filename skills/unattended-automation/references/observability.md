# Observability for unattended work

Nobody is watching, so the automation must make its own status legible after the
fact and must shout when something is wrong — including when "wrong" is "it
stopped running and said nothing".

## The five questions a run's record must answer

1. **What triggered it?** — schedule, queue message, webhook, manual; source and
   (if applicable) authenticity.
2. **What did it intend to do?** — the plan: which records / files / targets,
   how many.
3. **What did it actually change?** — IDs, paths, counts, before/after where
   cheap; retries per call.
4. **Did it work?** — the postcondition result, not just the exit code.
5. **What did it cost?** — duration, items processed, API calls, spend, retry
   count.

## Structured events, not prose

One event per run, and one per stage for a pipeline, as a single JSON object per
line (schema:
[`../templates/audit-event.schema.json`](../templates/audit-event.schema.json)).
Query and alert on fields; never grep prose. Include correlation IDs
(`run_id`, and `parent_run_id` for a stage or a retry) so a run reconstructs in
one filter.

Redact: no raw secrets, tokens, full PII, or full payloads — use fingerprints
(`sha256:…`), summaries, counts, and resource identifiers.

Store events where the automation's own credentials cannot rewrite them (a
separate log sink, an append-only store, a different account). For regulated
work, make them tamper-evident and set a retention period.

## Exit codes

Pick a convention and keep it across all your automations. A workable one:

| Code | Meaning | Scheduler / alert reaction |
|---|---|---|
| 0 | Success (including "nothing to do") | none |
| 1 | Generic / unknown failure | page |
| 2 | Bad input or config | page; do not auto-retry (will re-fail) |
| 3 | Skipped — lock held or kill switch set | none (this is normal) |
| 4 | Partial success — reconciliation needed | ticket + notify |
| 5 | Dependency unavailable / circuit open | retry later; page if sustained |
| 75 | `EX_TEMPFAIL` — transient, re-run the whole job soon | auto-retry |

"Nothing to do" is exit 0, not a silent no-op — the event still records that the
run happened and found zero work.

## Metrics

Minimum: `runs_total{outcome=}`, `run_duration_seconds`, `items_processed`,
`retries_total`, and — the important one — `seconds_since_last_success`. Alert
thresholds live on these.

## Alert on failure AND on silence

- **Failure**: any exit code that maps to page/ticket above, or an event with
  `outcome != success`. The alert names the automation, the `run_id`, the
  failure class, and the runbook section.
- **Silence**: a job that should run every hour and whose
  `seconds_since_last_success` exceeds, say, 2–3 intervals is broken even if
  nothing errored — cron didn't fire, the host is down, the scheduler forgot,
  the process hung past its timeout and was killed without logging. Implement
  with a heartbeat the job pings on success plus an external monitor
  (dead-man's-switch service, a "no data" alert on the metric, a separate
  watcher job).

A pipeline also alerts on "running too long" — a stage that has been `running`
past its expected duration is likely hung.

## Audit trail vs application log

The application log is for debugging (verbose, short retention, may contain
detail). The audit trail is the durable, structured, redacted record of *what
changed* — longer retention, restricted access, ideally append-only. Keep them
separate; do not make operators reconstruct "what did the 03:00 run delete?"
from debug logs.
