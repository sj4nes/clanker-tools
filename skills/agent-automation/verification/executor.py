"""Reference agent-automation executor wrapper (standard library only).

The language model only produces `Action` objects. Everything in this file is
deterministic control code the model cannot reach: allowlist, scope, policy,
approval, idempotency, timeout/retry taxonomy, postcondition verification,
reconciliation, and a redacted structured audit trail.

Run the test suite:  python3 executor.py
"""
from __future__ import annotations

import hashlib
import json
import re
import time
from dataclasses import dataclass, field
from typing import Any

# --------------------------------------------------------------------------- #
# Typed action contract
# --------------------------------------------------------------------------- #

RISK_TIERS = {
    "read_only": "auto",
    "low_impact_write": "auto",
    "moderate_impact_write": "auto",
    "high_impact": "approval",
    "critical_irreversible": "dual_control",
}

# name -> (risk_tier, param validator, postcondition predicate)
ALLOWLIST: dict[str, dict[str, Any]] = {
    "archive_records": {
        "risk_tier": "low_impact_write",
        "validate": lambda p: (
            isinstance(p.get("record_ids"), list)
            and 1 <= len(p["record_ids"]) <= 50
            and all(re.fullmatch(r"rec_\d+", r or "") for r in p["record_ids"])
        ),
    },
    "send_customer_email": {
        "risk_tier": "high_impact",
        "validate": lambda p: bool(p.get("to")) and bool(p.get("body")),
    },
    "delete_account": {
        "risk_tier": "critical_irreversible",
        "validate": lambda p: bool(p.get("account_id")),
    },
}


@dataclass
class Action:
    name: str
    parameters: dict[str, Any]
    reason: str = ""
    # model self-report; advisory only, never trusted for authorization
    requires_approval: bool = False


@dataclass
class Context:
    run_id: str
    tenant_id: str
    initiator_id: str
    initiator_role: str
    approvals: dict[str, dict] = field(default_factory=dict)  # action_name -> approval
    kill_switch: bool = False
    max_tool_calls: int = 10
    max_records_per_action: int = 50


class Result:
    def __init__(self, status: str, **kw):
        self.status = status
        self.__dict__.update(kw)

    def __repr__(self):
        return f"Result({self.status}, {self.__dict__})"


# --------------------------------------------------------------------------- #
# Audit trail (redacted, structured)
# --------------------------------------------------------------------------- #

AUDIT_LOG: list[dict] = []
_SECRET_KEYS = {"body", "to", "token", "password", "secret", "pii"}


def _fingerprint(obj: Any) -> str:
    return "sha256:" + hashlib.sha256(
        json.dumps(obj, sort_keys=True, default=str).encode()
    ).hexdigest()[:16]


def _redact(params: dict) -> dict:
    out = {}
    for k, v in params.items():
        out[k] = "<redacted>" if k.lower() in _SECRET_KEYS else v
    return out


def log_event(event_type: str, ctx: Context, **fields) -> None:
    if "parameters" in fields:
        fields["parameter_fingerprint"] = _fingerprint(fields.pop("parameters"))
    AUDIT_LOG.append(
        {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "event_id": f"evt_{len(AUDIT_LOG) + 1}",
            "run_id": ctx.run_id,
            "tenant_id": ctx.tenant_id,
            "actor": {"type": "agent", "id": "reference-automation"},
            "agent": {"id": "reference-automation", "version": "0.1.0"},
            "event_type": event_type,
            **fields,
        }
    )


# --------------------------------------------------------------------------- #
# In-memory world + tool with server-side idempotency
# --------------------------------------------------------------------------- #


class TransientToolError(Exception):
    pass


class PermanentToolError(Exception):
    pass


class World:
    def __init__(self):
        self.records = {f"rec_{i}": {"status": "active", "tenant": "acme"} for i in range(1, 6)}
        self.records["rec_9"] = {"status": "active", "tenant": "other"}
        self._idem: dict[str, Any] = {}
        self.email_count = 0
        # fault injection
        self.transient_fails_remaining = 0
        self.timeout_but_succeeds = False

    def call_tool(self, name: str, params: dict, idempotency_key: str) -> dict:
        if idempotency_key in self._idem:
            return self._idem[idempotency_key]  # dedup: no second side effect

        if self.transient_fails_remaining > 0:
            self.transient_fails_remaining -= 1
            raise TransientToolError("503")

        if name == "archive_records":
            for rid in params["record_ids"]:
                self.records[rid]["status"] = "archived"
            res = {"archived": list(params["record_ids"])}
        elif name == "send_customer_email":
            self.email_count += 1
            res = {"sent": True}
        elif name == "delete_account":
            res = {"deleted": params["account_id"]}
        else:
            raise PermanentToolError("unknown tool")

        self._idem[idempotency_key] = res
        if self.timeout_but_succeeds:
            # write landed, response lost
            raise TransientToolError("timeout")
        return res


# --------------------------------------------------------------------------- #
# Policy engine (deterministic, outside the model)
# --------------------------------------------------------------------------- #

POLICY_VERSION = "policy-2026-09-09"


def evaluate_policy(action: Action, ctx: Context, world: World) -> dict:
    spec = ALLOWLIST[action.name]  # allowlist already checked by caller
    rules: list[str] = []

    if not spec["validate"](action.parameters):
        return _deny("SCHEMA-INVALID", "parameters failed schema")

    ids = action.parameters.get("record_ids", [])
    if len(ids) > ctx.max_records_per_action:
        return _deny("LIMIT-RECORDS", "too many records for one action")
    for rid in ids:
        rec = world.records.get(rid)
        if rec is None:
            return _deny("SCOPE-MISSING", f"{rid} does not exist")
        if rec["tenant"] != ctx.tenant_id:
            return _deny("SCOPE-TENANT", f"{rid} outside tenant")

    if action.name == "send_customer_email" and ctx.initiator_role not in {
        "operations_manager",
        "admin",
    }:
        return _deny("AUTHZ-ROLE", "initiator lacks authority")

    tier = spec["risk_tier"]
    rules.append(f"TIER-{tier.upper()}")
    rule = RISK_TIERS[tier]
    if rule == "auto":
        return {"decision": "allow", "rules_matched": rules, "risk_tier": tier,
                "version": POLICY_VERSION}
    return {"decision": "allow_with_approval", "rules_matched": rules,
            "risk_tier": tier, "dual_control": rule == "dual_control",
            "version": POLICY_VERSION}


def _deny(rule_id: str, reason: str) -> dict:
    return {"decision": "deny", "rules_matched": [rule_id], "denial_reason": reason,
            "version": POLICY_VERSION}


# --------------------------------------------------------------------------- #
# Executor wrapper
# --------------------------------------------------------------------------- #


def make_idempotency_key(action: Action, ctx: Context) -> str:
    payload = json.dumps(
        [ctx.run_id, action.name, action.parameters], sort_keys=True, default=str
    )
    return hashlib.sha256(payload.encode()).hexdigest()[:24]


def verify_postcondition(action: Action, ctx: Context, world: World) -> bool:
    if action.name == "archive_records":
        return all(world.records[r]["status"] == "archived"
                   for r in action.parameters["record_ids"])
    if action.name == "send_customer_email":
        return world.email_count > 0
    if action.name == "delete_account":
        return True
    return False


def execute_action(action: Action, ctx: Context, world: World,
                   _tool_calls: list[int] | None = None) -> Result:
    calls = _tool_calls if _tool_calls is not None else [0]

    # 0. kill switch, before anything else
    if ctx.kill_switch:
        log_event("kill_switch_engaged", ctx, action={"name": action.name})
        return Result("blocked", reason="KILL_SWITCH")

    # 1. allowlist
    if action.name not in ALLOWLIST:
        log_event("action_blocked", ctx, action={"name": action.name},
                  policy={"decision": "deny", "rules_matched": ["ALLOWLIST"]})
        return Result("blocked", reason="NOT_ALLOWLISTED")

    # 2. policy
    policy = evaluate_policy(action, ctx, world)
    log_event("action_evaluated", ctx, action={"name": action.name,
              "risk_tier": policy.get("risk_tier")},
              parameters=action.parameters, policy=policy)
    if policy["decision"] == "deny":
        log_event("action_blocked", ctx, action={"name": action.name}, policy=policy)
        return Result("blocked", reason="POLICY_DENIED",
                      rule_ids=policy["rules_matched"])

    # 3. approval
    if policy["decision"] == "allow_with_approval":
        appr = ctx.approvals.get(action.name)
        needed = 2 if policy.get("dual_control") else 1
        if not appr or appr.get("expires_at", 1e18) < time.time() \
                or len(appr.get("approvers", [])) < needed:
            log_event("approval_requested", ctx, action={"name": action.name},
                      approval={"required": True, "dual_control": policy.get("dual_control")})
            return Result("blocked", reason="APPROVAL_REQUIRED")
        log_event("approval_recorded", ctx, action={"name": action.name},
                  approval={"approvers": appr["approvers"]})

    # 4. hard limit: tool calls per run
    if calls[0] >= ctx.max_tool_calls:
        log_event("limit_exceeded", ctx, action={"name": action.name})
        return Result("blocked", reason="TOOL_CALL_LIMIT")

    # 5. execute with bounded retry on transient errors only
    key = make_idempotency_key(action, ctx)
    max_attempts, deadline = 3, time.time() + 30
    for attempt in range(1, max_attempts + 1):
        calls[0] += 1
        try:
            log_event("tool_execution_started", ctx,
                      action={"name": action.name, "idempotency_key": key},
                      tool={"attempt": attempt})
            res = world.call_tool(action.name, action.parameters, key)
            status = "success"
            break
        except TransientToolError as exc:
            # re-check external state before deciding to retry a write
            if verify_postcondition(action, ctx, world):
                log_event("reconciliation_started", ctx,
                          action={"name": action.name},
                          error={"class": "transient_dependency",
                                 "message_redacted": str(exc), "retryable": False})
                res, status = {"reconciled": True}, "success"
                break
            if attempt == max_attempts or time.time() > deadline:
                log_event("error", ctx, action={"name": action.name},
                          error={"class": "transient_dependency",
                                 "message_redacted": str(exc), "retryable": True,
                                 "escalated": True})
                return Result("failed", reason="RETRY_BUDGET_EXHAUSTED")
            time.sleep(0)  # placeholder for backoff-with-jitter
        except PermanentToolError as exc:
            log_event("error", ctx, action={"name": action.name},
                      error={"class": "unknown", "message_redacted": str(exc),
                             "retryable": False, "escalated": True})
            return Result("failed", reason="PERMANENT_ERROR")

    # 6. postcondition
    verified = verify_postcondition(action, ctx, world)
    log_event("tool_execution_completed", ctx,
              action={"name": action.name, "idempotency_key": key},
              tool={"status": status, "response_fingerprint": _fingerprint(res)},
              outcome={"verified": verified,
                       "verification_method": "read_after_write"})
    if not verified:
        log_event("reconciliation_started", ctx, action={"name": action.name},
                  outcome={"verified": False})
        return Result("needs_reconciliation", reason="POSTCONDITION_FAILED")
    return Result("succeeded", result=res, idempotency_key=key)


# --------------------------------------------------------------------------- #
# Test suite
# --------------------------------------------------------------------------- #


def _fresh():
    AUDIT_LOG.clear()
    return World(), Context(run_id="run_1", tenant_id="acme",
                            initiator_id="u1", initiator_role="operations_manager")


def _assert(cond, msg):
    if not cond:
        raise AssertionError(msg)
    print(f"  ok: {msg}")


def run_tests() -> None:
    print("agent-automation executor verification")

    # 1. off-allowlist rejected
    w, c = _fresh()
    r = execute_action(Action("wire_transfer", {"amt": 1_000_000}), c, w)
    _assert(r.status == "blocked" and r.reason == "NOT_ALLOWLISTED",
            "off-allowlist action is rejected before execution")

    # 2. out-of-scope id denied
    w, c = _fresh()
    r = execute_action(Action("archive_records", {"record_ids": ["rec_9"]}), c, w)
    _assert(r.status == "blocked" and "SCOPE-TENANT" in r.rule_ids,
            "id outside tenant scope is denied")

    # 3. bad schema denied
    w, c = _fresh()
    r = execute_action(Action("archive_records", {"record_ids": ["nope"]}), c, w)
    _assert(r.status == "blocked" and "SCHEMA-INVALID" in r.rule_ids,
            "schema-invalid parameters are denied")

    # 4. low-impact write auto-executes and verifies
    w, c = _fresh()
    r = execute_action(Action("archive_records", {"record_ids": ["rec_1", "rec_2"]}), c, w)
    _assert(r.status == "succeeded" and w.records["rec_1"]["status"] == "archived",
            "low-impact write executes automatically and postcondition verifies")

    # 5. high-impact blocks without approval, proceeds with it
    w, c = _fresh()
    a = Action("send_customer_email", {"to": "x@y.z", "body": "hi"})
    r = execute_action(a, c, w)
    _assert(r.status == "blocked" and r.reason == "APPROVAL_REQUIRED",
            "high-impact action blocks without approval")
    c.approvals["send_customer_email"] = {"approvers": ["mgr_1"], "expires_at": time.time() + 999}
    r = execute_action(a, c, w)
    _assert(r.status == "succeeded", "high-impact action proceeds once approved")

    # 6. critical/irreversible needs dual control
    w, c = _fresh()
    a = Action("delete_account", {"account_id": "acc_1"})
    c.approvals["delete_account"] = {"approvers": ["mgr_1"], "expires_at": time.time() + 999}
    r = execute_action(a, c, w)
    _assert(r.status == "blocked", "critical action still blocked with only one approver")
    c.approvals["delete_account"]["approvers"].append("mgr_2")
    r = execute_action(a, c, w)
    _assert(r.status == "succeeded", "critical action proceeds under dual control")

    # 7. idempotency: duplicate submit -> no second side effect
    w, c = _fresh()
    a = Action("archive_records", {"record_ids": ["rec_3"]})
    execute_action(a, c, w)
    before = dict(w._idem)
    r = execute_action(a, c, w)
    _assert(r.status == "succeeded" and w._idem == before,
            "duplicate execution returns first result, no second side effect")

    # 8. transient error retried within budget
    w, c = _fresh()
    w.transient_fails_remaining = 2
    r = execute_action(Action("archive_records", {"record_ids": ["rec_4"]}), c, w)
    _assert(r.status == "succeeded", "transient errors retried within budget")

    # 9. transient beyond budget -> fail closed, escalated
    w, c = _fresh()
    w.transient_fails_remaining = 9
    r = execute_action(Action("archive_records", {"record_ids": ["rec_4"]}), c, w)
    _assert(r.status == "failed" and r.reason == "RETRY_BUDGET_EXHAUSTED",
            "exhausted retry budget fails closed and escalates")

    # 10. timeout-with-successful-write -> reconciled, not re-executed
    w, c = _fresh()
    w.timeout_but_succeeds = True
    r = execute_action(Action("archive_records", {"record_ids": ["rec_5"]}), c, w)
    _assert(r.status == "succeeded"
            and any(e["event_type"] == "reconciliation_started" for e in AUDIT_LOG),
            "timeout after a successful write is reconciled, not re-executed")

    # 11. kill switch halts state change immediately
    w, c = _fresh()
    c.kill_switch = True
    r = execute_action(Action("archive_records", {"record_ids": ["rec_1"]}), c, w)
    _assert(r.status == "blocked" and r.reason == "KILL_SWITCH",
            "kill switch refuses state-changing actions immediately")

    # 12. tool-call limit enforced
    w, c = _fresh()
    c.max_tool_calls = 0
    r = execute_action(Action("archive_records", {"record_ids": ["rec_1"]}), c, w)
    _assert(r.status == "blocked" and r.reason == "TOOL_CALL_LIMIT",
            "per-run tool-call limit is enforced")

    # 13. every run emits structured events, and secrets are redacted
    w, c = _fresh()
    c.approvals["send_customer_email"] = {"approvers": ["mgr_1"], "expires_at": time.time() + 999}
    execute_action(Action("send_customer_email", {"to": "a@b.c", "body": "SECRET"}), c, w)
    blob = json.dumps(AUDIT_LOG)
    _assert("SECRET" not in blob and "a@b.c" not in blob,
            "audit events carry no unredacted secret/PII payloads")
    _assert(all("event_type" in e and "run_id" in e for e in AUDIT_LOG),
            "every audit event is structured with type and correlation id")

    print("\nAll executor checks passed.")


if __name__ == "__main__":
    run_tests()
