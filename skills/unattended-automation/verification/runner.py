"""Reference unattended-job runner (standard library only).

Implements the controlled workflow from the skill: validate -> plan -> guards
(kill switch, lock, limits) -> execute unit-at-a-time with bounded retry and
checkpoint -> verify postcondition -> emit one structured audit event.

The job converges an in-memory record store to a desired set (idempotent) and
then performs one external-commit effect (a notification) guarded by an
idempotency key.

Run the suite:  python3 runner.py

Exit-code convention: 0 ok | 1 failure | 2 bad input | 3 skipped
                      | 4 reconcile needed | 5 dependency down
"""
from __future__ import annotations

import json
import time
from dataclasses import dataclass, field
from typing import Any

AUDIT: list[dict] = []


class JobExit(Exception):
    def __init__(self, code: int, outcome: str, reason: str = ""):
        super().__init__(reason or outcome)
        self.code, self.outcome, self.reason = code, outcome, reason


# --------------------------------------------------------------------------- #
# Environment: lock, kill switch, checkpoint, external world
# --------------------------------------------------------------------------- #


@dataclass
class Lock:
    _held: bool = False

    def acquire(self) -> bool:
        if self._held:
            return False
        self._held = True
        return True

    def release(self) -> None:
        self._held = False


class Breaker:
    def __init__(self, threshold: int = 3, cooldown: float = 60.0):
        self.threshold, self.cooldown = threshold, cooldown
        self.failures = 0
        self.opened_at: float | None = None

    def is_open(self) -> bool:
        if self.opened_at is None:
            return False
        return (time.time() - self.opened_at) < self.cooldown

    def record(self, ok: bool) -> None:
        if ok:
            self.failures, self.opened_at = 0, None
        else:
            self.failures += 1
            if self.failures >= self.threshold:
                self.opened_at = time.time()


class World:
    """In-memory target systems + fault injection."""

    def __init__(self) -> None:
        self.records: dict[str, dict] = {}          # internal state store
        self.notifications: list[str] = []           # external-commit sink
        self._notify_idem: set[str] = set()
        # fault injection
        self.transient_fails_remaining = 0
        self.permanent_fail = False
        self.notify_timeout_but_succeeds = False

    def upsert_record(self, key: str, value: dict) -> None:
        if self.permanent_fail:
            raise PermissionError("403 writing record")
        if self.transient_fails_remaining > 0:
            self.transient_fails_remaining -= 1
            raise TimeoutError("connection reset")
        self.records[key] = value

    def send_notification(self, idem_key: str, text: str) -> None:
        if idem_key in self._notify_idem:
            return  # server-side idempotency: no duplicate
        self._notify_idem.add(idem_key)
        self.notifications.append(text)
        if self.notify_timeout_but_succeeds:
            raise TimeoutError("timeout after send")


@dataclass
class Context:
    run_id: str
    desired: dict[str, dict]                 # the input: desired record set
    lock: Lock
    world: World
    breaker: Breaker = field(default_factory=Breaker)
    kill_switch: bool = False
    max_items: int = 100
    stop_after: int | None = None            # simulate SIGTERM after N units
    checkpoint: list[str] = field(default_factory=list)
    dry_run: bool = False


# --------------------------------------------------------------------------- #
# Audit
# --------------------------------------------------------------------------- #


def emit(event_type: str, ctx: Context, **fields: Any) -> None:
    AUDIT.append(
        {
            "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "run_id": ctx.run_id,
            "automation": "reference-sync-job",
            "event_type": event_type,
            **fields,
        }
    )


# --------------------------------------------------------------------------- #
# Bounded retry (transient only)
# --------------------------------------------------------------------------- #


def with_retry(ctx: Context, call_name: str, fn, verify_already_done=None):
    max_attempts, deadline = 3, time.time() + 30
    for attempt in range(1, max_attempts + 1):
        try:
            result = fn()
            ctx.breaker.record(ok=True)
            return result
        except TimeoutError:
            # re-check external state before retrying a write
            if verify_already_done is not None and verify_already_done():
                emit("reconciliation_needed", ctx, retries={"call": call_name,
                     "attempts": attempt, "error_class": "transient_dependency"},
                     note="write landed before timeout; not repeated")
                return None
            ctx.breaker.record(ok=False)
            if attempt == max_attempts or time.time() > deadline:
                raise JobExit(5, "failed", f"{call_name}: retry budget exhausted")
            time.sleep(0)  # placeholder for exponential backoff + jitter
        except (PermissionError, ValueError, KeyError) as exc:
            # permanent: do not retry
            ctx.breaker.record(ok=False)
            raise JobExit(1, "failed", f"{call_name}: permanent error: {exc}")


# --------------------------------------------------------------------------- #
# The controlled workflow
# --------------------------------------------------------------------------- #


def run_job(ctx: Context) -> int:
    emit("run_started", ctx, trigger={"type": "cron", "source": "test"})
    try:
        # 1. validate inputs (untrusted)
        if not isinstance(ctx.desired, dict):
            raise JobExit(2, "rejected", "desired set is not a mapping")
        if len(ctx.desired) == 0:
            raise JobExit(2, "rejected", "desired set is empty (likely upstream failure)")
        for k, v in ctx.desired.items():
            if not isinstance(k, str) or not isinstance(v, dict) or "status" not in v:
                raise JobExit(2, "rejected", f"malformed desired entry: {k!r}")
        emit("input_validated", ctx, inputs=[{"name": "desired", "row_count": len(ctx.desired)}])

        # 2. plan (converge: which records need writing)
        plan = [k for k, v in ctx.desired.items() if ctx.world.records.get(k) != v]
        emit("plan", ctx, plan={"planned_items": len(plan), "dry_run": ctx.dry_run})
        if len(plan) > ctx.max_items:
            raise JobExit(4, "reconciliation_needed",
                          f"plan {len(plan)} exceeds max_items {ctx.max_items}")

        # 3. guards
        if ctx.kill_switch:
            raise JobExit(3, "skipped_kill_switch", "kill switch set")
        if ctx.breaker.is_open():
            raise JobExit(5, "failed", "circuit breaker open")
        if not ctx.lock.acquire():
            raise JobExit(3, "skipped_locked", "another instance holds the lock")

        try:
            if ctx.dry_run:
                emit("done", ctx, outcome="dry_run", plan={"planned_items": len(plan)})
                return 0

            # 4. execute one unit at a time, retry transient, checkpoint
            processed = 0
            for key in plan:
                if ctx.stop_after is not None and processed >= ctx.stop_after:
                    emit("stopped", ctx, checkpoint={"processed_count": processed,
                         "last_processed": ctx.checkpoint[-1] if ctx.checkpoint else None,
                         "resumable": True})
                    raise JobExit(0, "stopped", "SIGTERM: checkpoint written")
                if ctx.kill_switch:  # re-check between units
                    raise JobExit(3, "skipped_kill_switch", "kill switch set mid-run")
                val = ctx.desired[key]
                with_retry(ctx, "upsert_record",
                           lambda k=key, v=val: ctx.world.upsert_record(k, v),
                           verify_already_done=lambda k=key, v=val: ctx.world.records.get(k) == v)
                ctx.checkpoint.append(key)
                processed += 1
                emit("unit_processed", ctx, changes={"updated": 1, "resource_ids": [key]})

            # external-commit effect, idempotency-keyed
            idem = f"{ctx.run_id}:notify:{sorted(ctx.desired)}"
            with_retry(ctx, "send_notification",
                       lambda: ctx.world.send_notification(idem, f"synced {len(ctx.desired)} records"),
                       verify_already_done=lambda: idem in ctx.world._notify_idem)

            # 5. verify postcondition
            verified = all(ctx.world.records.get(k) == v for k, v in ctx.desired.items())
            emit("postcondition_verified" if verified else "postcondition_failed", ctx,
                 postcondition={"method": "read_after_write", "verified": verified})
            if not verified:
                raise JobExit(4, "reconciliation_needed", "records do not match desired set")

            emit("done", ctx, outcome="success",
                 changes={"updated": processed, "sent": 1},
                 metrics={"items_processed": processed})
            return 0
        finally:
            ctx.lock.release()

    except JobExit as e:
        if e.outcome not in ("stopped",):
            emit("error" if e.code not in (0, 3) else "skipped", ctx,
                 outcome=e.outcome, exit_code=e.code,
                 error={"message_redacted": e.reason, "alerted": e.code not in (0, 3)})
        else:
            emit("done", ctx, outcome=e.outcome, exit_code=e.code)
        return e.code


# --------------------------------------------------------------------------- #
# Test suite
# --------------------------------------------------------------------------- #

DESIRED = {f"rec_{i}": {"status": "active"} for i in range(1, 6)}


def _fresh(**kw) -> Context:
    AUDIT.clear()
    base = dict(run_id="run_1", desired=dict(DESIRED), lock=Lock(), world=World())
    base.update(kw)
    return Context(**base)


def _assert(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)
    print(f"  ok: {msg}")


def _last_outcome() -> str:
    for e in reversed(AUDIT):
        if "outcome" in e:
            return e["outcome"]
    return "<none>"


def run_tests() -> None:
    print("unattended-automation runner verification")

    # 1. bad input -> abort, no side effect
    ctx = _fresh(desired="not a dict")
    code = run_job(ctx)
    _assert(code == 2 and ctx.world.records == {} and ctx.world.notifications == [],
            "invalid input aborts (exit 2) with no side effect")

    # 2. empty input -> abort
    ctx = _fresh(desired={})
    _assert(run_job(ctx) == 2 and _last_outcome() == "rejected",
            "empty input is rejected, not processed as zero work")

    # 3. happy path
    ctx = _fresh()
    code = run_job(ctx)
    _assert(code == 0 and ctx.world.records == DESIRED and ctx.world.notifications == [
            "synced 5 records"], "happy path converges the store and sends one notification")

    # 4. duplicate run -> idempotent, no duplicate external commit
    ctx.run_id = "run_1"
    n_before = list(ctx.world.notifications)
    code = run_job(ctx)
    _assert(code == 0 and ctx.world.notifications == n_before,
            "re-run is idempotent: no records rewritten, no duplicate notification")

    # 5. concurrent run -> lock held -> skip
    ctx = _fresh()
    ctx.lock.acquire()  # someone else holds it
    _assert(run_job(ctx) == 3 and _last_outcome() == "skipped_locked",
            "second concurrent run bails on the lock (exit 3)")

    # 6. transient error -> retried -> success
    ctx = _fresh()
    ctx.world.transient_fails_remaining = 2
    _assert(run_job(ctx) == 0 and ctx.world.records == DESIRED,
            "transient dependency error is retried and the run succeeds")

    # 7. permanent error -> no retry -> fail closed
    ctx = _fresh()
    ctx.world.permanent_fail = True
    code = run_job(ctx)
    _assert(code == 1 and _last_outcome() == "failed"
            and any(e["event_type"] == "error" for e in AUDIT),
            "permanent error fails closed (exit 1), not retried")

    # 8. timeout after successful write -> reconciled, not repeated
    ctx = _fresh()
    ctx.world.notify_timeout_but_succeeds = True
    code = run_job(ctx)
    _assert(code == 0 and ctx.world.notifications == ["synced 5 records"]
            and any(e["event_type"] == "reconciliation_needed" for e in AUDIT),
            "timeout after a successful commit is reconciled, effect not repeated")

    # 9. resource limit -> abort before execution
    ctx = _fresh(max_items=2)
    code = run_job(ctx)
    _assert(code == 4 and ctx.world.records == {},
            "plan exceeding max_items aborts before any write (exit 4)")

    # 10. kill switch -> skip, no effect
    ctx = _fresh(kill_switch=True)
    _assert(run_job(ctx) == 3 and ctx.world.records == {}
            and _last_outcome() == "skipped_kill_switch",
            "kill switch stops the run (exit 3) with no side effect")

    # 11. SIGTERM mid-run -> resumable checkpoint, lock released
    ctx = _fresh(stop_after=2)
    code = run_job(ctx)
    _assert(code == 0 and _last_outcome() == "stopped" and len(ctx.checkpoint) == 2
            and ctx.lock.acquire() is True,
            "SIGTERM mid-run writes a resumable checkpoint and releases the lock")
    # resume: same context, no stop -> finishes the rest
    ctx.lock.release()
    ctx.stop_after = None
    code = run_job(ctx)
    _assert(code == 0 and ctx.world.records == DESIRED,
            "resumed run completes the remaining units (checkpoint honored via converge)")

    # 12. circuit breaker open -> fast fail
    ctx = _fresh()
    ctx.breaker.failures = 3
    ctx.breaker.opened_at = time.time()
    _assert(run_job(ctx) == 5 and ctx.world.records == {},
            "open circuit breaker fails fast (exit 5) without touching the world")

    # 13. every run emits a structured terminal event with an outcome
    ctx = _fresh()
    run_job(ctx)
    _assert(all("event_type" in e and "run_id" in e for e in AUDIT)
            and any("outcome" in e for e in AUDIT)
            and "SECRET" not in json.dumps(AUDIT),
            "every path emits structured events with a terminal outcome")

    print("\nAll runner checks passed.")


if __name__ == "__main__":
    run_tests()
