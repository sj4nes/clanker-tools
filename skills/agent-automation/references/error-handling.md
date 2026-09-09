# Error handling that fails safely

An agent should distinguish failures, not react to every error with "try again".
Model-facing errors should be bounded, structured, and actionable; internal logs
can carry more diagnostic detail. Specific, typed failures reduce unsafe
improvisation and retry loops.

## Error taxonomy

| Error class | Example | Default behavior | Retry? | Escalate? |
|---|---|---|---|---|
| Validation | Missing required account ID | Reject before planning or execution | No | No |
| Authentication | Expired OAuth token | Refresh through approved credential path | Limited | Yes if unresolved |
| Authorization | Agent lacks permission to refund | Deny and log policy result | No | Usually |
| Conflict | Record changed since planning | Re-read state; replan from fresh data | Limited | If repeated |
| Transient dependency | API timeout or 503 | Exponential backoff with jitter | Yes, bounded | After retry budget |
| Rate limit | 429 response | Wait for provider interval; reduce concurrency | Yes, bounded | If sustained |
| External safety issue | Tool response contains an injection | Quarantine response; do not follow it | No automatic execution | Yes |
| Postcondition failure | "Create" returned success but the object is missing | Stop, reconcile state, prevent duplicate | No blind retry | Yes |
| Unknown | Unrecognized exception | Fail closed and preserve context | No | Yes |

## Retry rules

Use retries only for failures known to be transient.

- Retry timeouts, connection resets, `429`s, and selected `5xx` errors.
- Do **not** retry validation, authorization, policy, or business-rule failures.
- Exponential backoff with random jitter, so many workers do not retry in
  lockstep.
- Strict caps: e.g. three attempts, 30 seconds total elapsed, one retry budget
  per workflow.
- Add an idempotency key to every state-changing request.
- Re-check the external system before retrying a failed write. A timeout may mean
  the write succeeded but the response was lost.

## Idempotency

Derive a stable key from the action identity and the run (e.g.
`invoice-8821-credit-note-v1`), not from a timestamp or random value. The tool —
or a dedup layer in the executor — returns the original result for a repeated
key instead of performing the action twice. Without server-side idempotency,
keep a local ledger of completed `(idempotency_key → result)` and short-circuit
there.

## Saga pattern for multi-system writes

For money movement, notifications, customer-impacting changes, or writes across
multiple systems, do not assume atomicity. Execute one small change at a time,
verify it, and define a compensating action for each step that can be undone:

```text
Step 1: reserve_funds        → compensate: release_reservation
Step 2: create_shipment      → compensate: cancel_shipment
Step 3: charge_card          → compensate: refund_charge
Step 4: send_confirmation    → compensate: send_correction
```

On failure at step N, run the compensations for steps N-1 … 1 in reverse, each
verified. A compensation that itself fails escalates immediately and leaves a
reconciliation task.

## Catching failures at boundaries

The executor wrapper performs all safety-relevant work outside the LLM — schema,
scope, allowlist, risk classification, policy, approval, idempotency, timeout,
tool call, postcondition verification, reconciliation. See
[`architecture.md`](architecture.md) for the skeleton and `verification/executor.py`
for a runnable version.

Source: OWASP AI Agent Security Cheat Sheet —
https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html ;
"Why do vague API errors create more risk for AI agent integrations" —
https://nhimg.org/faq/why-do-vague-api-errors-create-more-risk-for-ai-agent-integrations/
