# Reference architecture

A production automation does not let an LLM directly call arbitrary APIs based on
raw prose. Deterministic control layers wrap the model. The model's job is to
propose an intent and a structured action; the application's job is to decide
whether that action is permitted, execute it safely, and make the execution
reconstructable later.

```text
Trigger / Event
  ↓
Input validation & normalization
  ↓
Context retrieval  ── untrusted-data boundary
  ↓
Agent proposes a typed plan
  ↓
Policy engine evaluates each proposed action
  ↓
Approval gate for elevated-risk actions
  ↓
Tool executor with least-privilege credentials
  ↓
Postcondition verification
  ↓
Structured audit log, metrics, alerts
```

## The decision / execution split

Decision-making (what should happen) is separated from execution (making it
happen) for every irreversible operation. The model may reason about intent; it
must not be the thing that decides authorization or performs the side effect.
Practically: the model returns data, and a non-LLM function is the only code path
that holds credentials and calls the tool.

## The typed plan

Rather than interpreting "clean up old customer files" and deleting records, the
agent must output a typed action:

```json
{
  "action": "archive_records",
  "record_ids": ["rec_1042", "rec_1043"],
  "reason": "Retention policy says inactive records older than 7 years may be archived",
  "confidence": 0.92,
  "requires_approval": true
}
```

`confidence` and `requires_approval` are the model's self-report — advisory
only. The policy engine independently sets the real approval requirement and
never treats a low `requires_approval` as permission to skip a check.

## Policy confirmation (worked example)

For the plan above, non-LLM policy code confirms **all** of:

- The action name is on the allowlist.
- Every `record_id` exists and belongs to the allowed tenant.
- The initiator has authority to archive records.
- Each record's inactivity age actually satisfies the 7-year retention rule
  (checked against the source of truth, not the model's claim).
- The requested change is archival, not deletion — the action class matches.
- A human has approved if the action exceeds the organization's risk threshold.

Any failed check → `deny` or `blocked`, logged with the rule ID. The model's
`reason` string is never itself accepted as evidence that a rule is satisfied.

## Executor wrapper skeleton

All safety-relevant work happens outside the LLM. The agent cannot bypass
`validate_tenant_scope`, policy evaluation, approval checks, idempotency, timeout
enforcement, or postcondition verification.

```python
def execute_action(action, context):
    validate_schema(action)
    validate_tenant_scope(action, context.tenant_id)
    validate_allowlist(action.name)

    risk = classify_risk(action, context)
    policy = evaluate_policy(action, context, risk)
    log_event("action_evaluated", action=action, policy=policy)

    if policy.decision == "deny":
        return blocked("POLICY_DENIED", policy.rule_ids)

    if policy.requires_approval:
        approval = get_valid_approval(action, context)
        if not approval:
            return blocked("APPROVAL_REQUIRED")

    idempotency_key = make_idempotency_key(action, context)

    try:
        result = call_tool(
            action.name,
            sanitize_parameters(action.parameters),
            idempotency_key=idempotency_key,
            timeout_seconds=20,
        )
    except TransientToolError as exc:
        return retry_or_escalate(action, context, exc)
    except Exception as exc:
        log_internal_error(action, context, exc)
        return failed("UNEXPECTED_EXECUTION_ERROR")

    verified = verify_postcondition(action, result, context)
    log_event("action_completed", action=action, result=result, verified=verified)
    if not verified:
        return reconcile_or_escalate(action, result, context)
    return succeeded(result)
```

`verification/executor.py` in this skill is a runnable elaboration of this
skeleton with an in-memory tool and a test suite.

## Multi-agent note

When one agent's output feeds another, the boundary rules still apply: the
upstream agent's output is untrusted input to the downstream one, each agent has
its own scoped identity, and a circuit breaker between them prevents a failed or
manipulated agent from driving a cascade of actions.

Source: OWASP AI Agent Security Cheat Sheet —
https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html
