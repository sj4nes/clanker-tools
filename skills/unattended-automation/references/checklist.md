# Pre-deploy checklist and failure-scenario matrix

## Checklist

Before adding the automation to a scheduler, confirm all of:

- [ ] Named owner and on-call, and a runbook exists.
- [ ] Trigger, schedule, timezone, overrun policy, and missed-run policy are
      decided and documented.
- [ ] Every input has an explicit validation rule; the job aborts on
      missing/empty/stale/oversized input.
- [ ] The set of effects is enumerated; each has an idempotency strategy.
- [ ] A re-run of a completed job is a no-op (verified, not assumed).
- [ ] Single-instance lock is in place and released on every exit path including
      signals.
- [ ] Every destructive operation has a dry-run, a backup or soft-delete, or a
      deliberate confirmation gate.
- [ ] Hard limits set: run timeout, per-call timeout, max items/bytes/calls,
      spend cap, retry cap, concurrency cap.
- [ ] Error taxonomy implemented: transient vs permanent; retry only transient
      with backoff + jitter + budget.
- [ ] Writes re-check external state before a retry.
- [ ] Circuit breaker for the flakiest dependency, with persisted state.
- [ ] Postcondition check after execution; mismatch exits non-zero and does not
      blind-retry.
- [ ] `SIGTERM`/`SIGINT` handled; a killed run leaves consistent state.
- [ ] Long runs checkpoint and resume; fan-out checkpoints per item.
- [ ] Kill switch checked at startup and between units.
- [ ] Dedicated least-privilege identity; secrets from a secret store, not the
      repo or crontab.
- [ ] One structured audit event per run/stage, redacted, stored where the job
      cannot rewrite it.
- [ ] Meaningful exit codes wired to scheduler/alert reactions.
- [ ] Alert on failure AND on silence (heartbeat / dead-man's switch).
- [ ] For a pipeline: stages topologically ordered, run manifest persisted,
      resume-vs-compensate default chosen, compensations tested.
- [ ] Scheduled to start paused or at low frequency, with a plan to ramp.

## Failure-scenario test matrix

Run each; every one must fail closed and leave a recoverable state.

| Scenario | Inject | Expected |
|---|---|---|
| Missing/invalid input | Unset a required config key; feed malformed JSON | Abort before any change; exit 2; audit `outcome: rejected`; alert |
| Empty / stale input | Point at an empty dir; use a 3-day-old "daily" file | Abort (not "process zero rows silently"); alert |
| Duplicate run | Run the job twice on the same inputs | Second run is a no-op; no duplicate effect; both runs audited |
| Concurrent run | Start a second instance while the first holds the lock | Second exits 3 `skipped_locked`; no interleaved writes |
| Transient dependency error | Make the dependency fail 2× then succeed | Retried with backoff; run succeeds; retries recorded |
| Permanent error | Make the dependency return 403 / not-found | No retry; abort; exit 1/2; alert |
| Timeout after successful write | Dependency commits then times out | Re-check finds the write; treated as success; not repeated |
| Postcondition failure | Tool returns success but read-back disagrees | Exit 4; reconciliation event; no blind retry |
| Resource limit | Make the plan exceed `max_items` / spend cap | Abort before execution; exit 4/1; alert |
| Kill switch set | Create the kill-switch flag | Run exits 3 `skipped_kill_switch`; no effect; scheduler + silence monitor still satisfied |
| SIGTERM mid-run | Send `SIGTERM` during processing | Current unit finishes or cleanly abandons; lock released; checkpoint written; next run resumes |
| Circuit open | Trip the breaker via repeated failures | Subsequent runs fail fast (exit 5) without exhausting the timeout; alert on sustained |
| Pipeline stage failure | Fail stage k with an earlier `external-commit` stage | Resume from k, or compensate k-1…1 in reverse per the pipeline's default; manifest reflects it |
| Silence | Stop triggering the job entirely | Dead-man's-switch / `seconds_since_last_success` alert fires within the configured window |
