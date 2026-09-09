# Action contract and policy: <automation name>

The model may only emit actions from this list, with parameters matching the
schema. Anything else is rejected before execution.

## Action: `<action_name>`

- **Description**:
- **Read or write**: write
- **Risk tier**: read-only | low-impact write | moderate-impact write | high-impact | critical-irreversible
- **Execution rule**: automatic | requires approval | requires dual control | forbidden (autonomous)

### Parameter schema

| Parameter | Type | Constraints | Required |
|---|---|---|---|
| `record_ids` | array<string> | each matches `^rec_\d+$`, max 50 items | yes |
| `reason` | string | 1–500 chars | yes |

### Target scope

- **Scope field**: `record_ids` must all resolve to entities in `context.tenant_id`.
- **Ownership / authority rule**: initiator role in `{operations_manager, admin}`.

### Policy checks (deterministic, outside the model)

1. Action name is on the allowlist.
2. Parameters validate against the schema above.
3. Every referenced ID exists and is inside the allowed tenant/scope.
4. The initiator has authority for this action.
5. Business rule: `<state the rule and the source of truth it is checked against>`.
6. Action class matches the declared change (e.g. archival, not deletion).
7. Run is within its hard limits (tool-call count, spend, records/action).

### Postcondition (proves the action worked)

- **Method**: read-after-write
- **Check**: `get_record(id).status == "archived"` for every id.
- **On failure**: stop, reconcile, escalate — no blind retry.

### Idempotency

- **Key derivation**: `f"{run_id}:{action_name}:{sorted(record_ids)}"`
- **Dedup layer**: server-side idempotency key | local completed-key ledger

### Rollback / compensation

- **Compensating action**: `unarchive_records(record_ids)`
- **Preconditions for rollback**:

---

## Policy output classes

| Decision | Meaning | Next step |
|---|---|---|
| `allow` | All checks passed, tier permits automatic execution | Execute |
| `allow_with_approval` | Checks passed, tier requires a human | Approval gate |
| `deny` | A check failed | `blocked(reason, rule_ids)`; log; stop |

Every decision records: `policy_version`, `rules_matched`, `risk_tier`.
