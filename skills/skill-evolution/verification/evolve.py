#!/usr/bin/env python3
"""Operator checks for the `skill-evolution` skill (stdlib only).

Exercises the two decision procedures SKILL.md prescribes on known-answer
cases, including the negative contrast each guardrail exists to prevent:

  A. the acceptance gate -- target threshold AND protected-metric boundary
  B. the issue-tracker update -- link a recurrence, do not duplicate; reopen
  C. the rejected-candidate log -- a re-proposed dead-end patch is caught
"""

import sys

fails = 0


def check(label, got, want):
    global fails
    ok = got == want
    print(f"  {'OK  ' if ok else 'FAIL'} {label}: got {got!r} want {want!r}")
    if not ok:
        fails += 1


# --------------------------------------------------------------------------
# A. Acceptance gate
# --------------------------------------------------------------------------
def accept(current, candidate, targets, protected, lower_is_better=()):
    """targets: {metric: threshold>0}. protected: {metric: boundary>=0}.
    A metric in `lower_is_better` regresses when it rises; others regress
    when they fall. Accept iff some target improves by >= its threshold
    AND no protected metric regresses by more than its boundary."""
    def regression(m):
        d = candidate[m] - current[m]
        return d if m in lower_is_better else -d
    target_hit = any(regression(m) <= -thr for m, thr in targets.items())
    protected_ok = all(regression(m) <= bound for m, bound in protected.items())
    return target_hit and protected_ok


targets = {"success": 1.0, "constraint_rate": 2.0}
protected = {"cost": 0.0, "safety_pass": 0.0}
lower_is_better = {"cost"}

print("A. acceptance gate")

# Case A1: mean improves, but a protected metric regresses -> REJECT
cur = {"success": 50.0, "constraint_rate": 40.0, "cost": 10.0, "safety_pass": 100.0}
cand = {"success": 55.0, "constraint_rate": 50.0, "cost": 10.8, "safety_pass": 100.0}
check("mean up but cost regresses -> reject", accept(cur, cand, targets, protected, lower_is_better), False)

# Case A2: flat primary, auxiliary target clears, nothing protected regresses -> ACCEPT
cur = {"success": 55.0, "constraint_rate": 50.0, "cost": 10.0, "safety_pass": 100.0}
cand = {"success": 55.0, "constraint_rate": 53.0, "cost": 10.0, "safety_pass": 100.0}
check("flat primary carried by aux target -> accept", accept(cur, cand, targets, protected, lower_is_better), True)

# Case A3: primary clears but safety_pass regresses -> REJECT
cand = {"success": 58.0, "constraint_rate": 53.0, "cost": 10.0, "safety_pass": 98.0}
check("primary up but safety regresses -> reject", accept(cur, cand, targets, protected, lower_is_better), False)


# --------------------------------------------------------------------------
# B. Issue-tracker update
# --------------------------------------------------------------------------
class Issue:
    def __init__(self, iid, pattern, tags, status="open", opened=0):
        self.iid = iid
        self.pattern = pattern
        self.tags = set(tags)
        self.status = status
        self.opened = opened
        self.reopened_round = None
        self.attempts = []


def match_issue(tracker, failure_tags):
    for iss in tracker.values():
        if iss.tags & set(failure_tags):
            return iss
    return None


def update_tracker(tracker, rnd, failure_tags):
    """One failure observed at round `rnd` with `failure_tags`."""
    iss = match_issue(tracker, failure_tags)
    if iss is None:
        nid = f"ISS-{len(tracker) + 1:03d}"
        tracker[nid] = Issue(nid, "new pattern", failure_tags, opened=rnd)
        return nid
    if iss.status == "resolved":
        iss.status = "reopened"
        iss.reopened_round = rnd
    return iss.iid


print("B. issue-tracker update")
tracker = {
    "ISS-001": Issue("ISS-001", "picks cheapest itinerary, ignores the museum constraint",
                     tags=["museum-constraint", "over-optimizes-cost"],
                     status="resolved", opened=1),
}
tracker["ISS-001"].attempts = [
    (2, "add 'satisfy all constraints first'", "partial 2/5"),
    (4, "add explicit constraint checklist", "resolved 5/5"),
]
n_before = len(tracker)

# round 6: the museum-constraint failure recurs (different wording, same tag)
hit = update_tracker(tracker, 6, ["museum-constraint"])
check("recurrence links to existing issue", hit, "ISS-001")
check("no duplicate issue opened", len(tracker), n_before)
check("issue marked reopened", tracker["ISS-001"].status, "reopened")
check("reopen round recorded", tracker["ISS-001"].reopened_round, 6)

# round 7: a genuinely new failure -> new entry
hit = update_tracker(tracker, 7, ["hallucinated-flight-number"])
check("new failure opens a new issue", hit, "ISS-002")
check("tracker grew by one", len(tracker), n_before + 1)


# --------------------------------------------------------------------------
# C. Rejected-candidate log
# --------------------------------------------------------------------------
def is_dead_end(log, signature):
    return any(row["signature"] == signature and row["result"] == "rejected"
              for row in log)


print("C. rejected-candidate log")
log = [
    {"round": 1, "signature": "add-constraint-checklist", "result": "accepted"},
    {"round": 2, "signature": "rewrite-cost-guidance", "result": "rejected"},
]
check("re-proposed rejected patch is caught", is_dead_end(log, "rewrite-cost-guidance"), True)
check("a fresh patch is not flagged", is_dead_end(log, "cap-itinerary-length"), False)
check("an accepted patch is not a dead end", is_dead_end(log, "add-constraint-checklist"), False)


print()
if fails:
    print(f"OPERATOR CHECKS FAILED: {fails}")
    sys.exit(1)
print("ALL OPERATOR CHECKS PASSED")
