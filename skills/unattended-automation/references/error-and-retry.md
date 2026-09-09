# Error handling and retries

An unattended job cannot ask a human what an error means, so it must classify
errors itself and react per class. "On error, retry" is how a flaky dependency
becomes a thundering herd and how a permission bug becomes a million log lines.

## Error taxonomy

| Class | Example | Default behavior | Retry? | Alert? |
|---|---|---|---|---|
| Validation | Missing config key, unparseable input, stale upstream file | Abort before any change | No | Yes |
| Authentication | Expired token, bad key | Refresh via the approved path; else abort | Once, then no | Yes if unresolved |
| Authorization | Service account lacks the permission | Abort | No | Yes |
| Not found | Referenced record / file / queue does not exist | Abort or skip the unit (declare which) | No | Yes |
| Conflict | Row changed since the plan; optimistic-lock failure | Re-read state, recompute the unit | Bounded | If repeated |
| Transient dependency | Timeout, connection reset, `503`, DNS blip | Backoff and retry | Yes, bounded | After budget |
| Rate limit | `429`, quota exceeded | Honor `Retry-After`; lower concurrency | Yes, bounded | If sustained |
| Postcondition failure | Tool said OK, read-back disagrees | Stop the unit, reconcile | No | Yes |
| Resource limit | Hit `max_items` / spend cap / timeout | Stop cleanly at the boundary | No | Yes (info) |
| Unknown | Unrecognized exception / non-zero from a sub-tool | Fail closed, preserve context | No | Yes |

## Retry rules

- Retry **only** transient dependency errors, rate limits, and (bounded)
  conflicts. Never retry validation, authz, not-found, or business-rule errors —
  they will fail identically every time and just delay the alert.
- **Exponential backoff with jitter**: `sleep = min(cap, base * 2**attempt) *
  (0.5 + random()/2)`. Jitter matters when many jobs or workers retry at once.
- **Two caps**: a max attempt count (e.g. 3–5) and a max total elapsed time
  (e.g. 60s) — whichever hits first ends the retries.
- **One retry budget per run**: if retries across all calls exceed a threshold,
  the dependency is unhealthy — stop the run rather than grind through it.
- **Wrap the call, not the loop**: retry a single external call, not the whole
  processing loop, or you reprocess already-done units.

## Re-check before retrying a write

A timeout or a dropped connection on a state-changing call does **not** mean the
change failed — the request may have landed and the response been lost. Before
retrying:

1. Query the target for the intended state (by idempotency key or natural key).
2. If it is already there, treat the call as succeeded — do not send it again.
3. Only if it is genuinely absent, retry (with the same idempotency key).

Without this, retries create duplicate charges, duplicate emails, double-shipped
orders.

## Circuit breaker

For a dependency that fails repeatedly: after N failures in a window, "open" the
breaker — stop calling it, fail fast, alert. Stay open for a cooldown, then let
one trial call through ("half-open"); close on success, re-open on failure. In a
scheduled job the breaker state persists to a file or a row so the *next* run
also fails fast instead of re-discovering the outage. A breaker prevents one
broken dependency from consuming every run's whole timeout budget.

## Saga: multi-system writes

Do not assume a job that writes to several systems is atomic. Execute one step
at a time, verify each, and define a compensating action for each step that
commits an external effect:

```text
1. reserve_inventory   → compensate: release_reservation
2. charge_card         → compensate: refund_charge
3. create_shipment     → compensate: cancel_shipment
4. send_confirmation   → compensate: send_correction
```

On failure at step k, run compensations for k-1 … 1 in reverse, each verified.
A compensation that itself fails escalates immediately and leaves a
reconciliation task in the audit trail. Prefer ordering steps so the
hardest-to-compensate one is last.

## Exit codes

Map classes to distinct exit codes so the scheduler and alerting can react
differently (see [`observability.md`](observability.md)):
`0` success, `1` generic/unknown failure, `2` bad input/config, `3` skipped
(lock or kill switch), `4` partial success / reconciliation needed,
`5` dependency unavailable / circuit open, `75` (`EX_TEMPFAIL`) transient —
retry the whole job later.
