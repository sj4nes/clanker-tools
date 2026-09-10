#!/usr/bin/env python3
"""Operator checks for the `temporal-data-modeling` skill (stdlib only).

Same known-answer case as checks.bc: a 7-day active-membership + login log with
one team merge, one coverage gap (d6), one field of each semantics.

Checks:
  4. gluing check on a *set-valued* cumulative field (pushout = dedup union)
     passes for a consistent cover and fails when the overlap is double-counted.
  5. a coverage gap scored as `disappear` invents phantom churn that the
     `unobserved` policy suppresses.
  6. a week-resolution property ("weekly-active") evaluated at daily granularity
     disagrees with the restrict-then-check result and with ground truth.
"""

DAYS = ["d1", "d2", "d3", "d4", "d5", "d6", "d7"]

# persistent field: who is active *on* each day. d6 is a coverage gap.
ACTIVE = {
    "d1": {"m1", "m2"},
    "d2": {"m1", "m2", "m3"},
    "d3": {"m1", "m2", "m3"},
    "d4": {"m1", "m3", "m4"},
    "d5": {"m1", "m3", "m4"},
    "d6": None,                       # UNOBSERVED — not {} and not "all gone"
    "d7": {"m1", "m4", "m5"},
}

fail = 0


def observed_days(lo, hi):
    """Day labels in [lo, hi] that actually carry data."""
    i, j = DAYS.index(lo), DAYS.index(hi)
    return [d for d in DAYS[i:j + 1] if ACTIVE[d] is not None]


def cumulative_active(lo, hi):
    """Set-valued cumulative field: everyone active at some point in [lo, hi]."""
    out = set()
    for d in observed_days(lo, hi):
        out |= ACTIVE[d]
    return out


# ---- Check 4: gluing for a set-valued cumulative field --------------------
print("=== Check 4: gluing check, set-valued cumulative field ===")
whole = cumulative_active("d1", "d7")
left = cumulative_active("d1", "d3")
right = cumulative_active("d3", "d7")
overlap = cumulative_active("d3", "d3")
glued = (left | right)                       # pushout: union already dedups d3
# a broken pipeline that keeps *multisets* / counts per half and adds them:
naive_count = len(left) + len(right)         # 3 + 5 = 8, double-counts d3's members
glued_count = len(left | right)              # 5

print(f"  whole [d1,d7]      = {sorted(whole)}")
print(f"  glued (left|right) = {sorted(glued)}")
print(f"  naive count        = {naive_count}   glued count = {glued_count}")
if glued == whole and naive_count != glued_count == len(whole):
    print("  PASS: set pushout reconstructs the whole; count-additive pipeline over-counts\n")
else:
    print("  FAIL\n")
    fail += 1

# order independence
alt = cumulative_active("d1", "d5") | cumulative_active("d5", "d7")
if alt == whole:
    print("  PASS: cut at d5 gives the same reconstruction\n")
else:
    print("  FAIL: reconstruction depends on cut point\n")
    fail += 1


# ---- Check 5: coverage gap as `disappear` vs `unobserved` ----------------
print("=== Check 5: coverage-gap policy and phantom churn ===")


def churn_disappear_policy():
    """Treat the d6 gap as real: everyone active on d5 'disappears' on d6."""
    departures = 0
    arrivals = 0
    prev = ACTIVE["d5"]
    for d in ["d6", "d7"]:
        cur = ACTIVE[d] if ACTIVE[d] is not None else set()   # gap read as empty
        departures += len(prev - cur)
        arrivals += len(cur - prev)
        prev = cur
    return departures, arrivals


def churn_unobserved_policy():
    """Skip the d6 gap; compare the last and next observed days."""
    obs = observed_days("d5", "d7")            # ['d5', 'd7']
    departures = arrivals = 0
    for a, b in zip(obs, obs[1:]):
        departures += len(ACTIVE[a] - ACTIVE[b])
        arrivals += len(ACTIVE[b] - ACTIVE[a])
    return departures, arrivals


dep_bad, arr_bad = churn_disappear_policy()
dep_ok, arr_ok = churn_unobserved_policy()
# ground truth d5 {m1,m3,m4} -> d7 {m1,m4,m5}: m3 leaves, m5 joins.
GROUND_DEP, GROUND_ARR = 1, 1

print(f"  disappear-policy churn : {dep_bad} departures, {arr_bad} arrivals")
print(f"  unobserved-policy churn: {dep_ok} departures, {arr_ok} arrivals")
print(f"  ground truth           : {GROUND_DEP} departure, {GROUND_ARR} arrival")
if (dep_bad, arr_bad) != (dep_ok, arr_ok) and (dep_ok, arr_ok) == (GROUND_DEP, GROUND_ARR):
    print("  PASS: gap-as-disappear invents churn; unobserved policy matches truth\n")
else:
    print("  FAIL\n")
    fail += 1


# ---- Check 6: resolution collapse ---------------------------------------
print("=== Check 6: week-resolution property evaluated at daily granularity ===")
# "weekly-active member" = active on >= 1 day of the week (cumulative @ week res).
ground_truth = cumulative_active("d1", "d7")            # {m1..m5}, 5 members

# restrict-then-check: aggregate to the week, then apply the predicate
restrict_then_check = len(ground_truth)

# naive: evaluate the flag per day from that day's data, take the value at
# week end (a member "is weekly-active" iff active on the last observed day)
last_obs = observed_days("d1", "d7")[-1]                # d7
per_day_then_aggregate = len(ACTIVE[last_obs])          # {m1,m4,m5} -> 3

print(f"  ground truth (weekly-active members) = {sorted(ground_truth)}  -> {len(ground_truth)}")
print(f"  restrict-then-check                  = {restrict_then_check}")
print(f"  per-day flag at week end             = {per_day_then_aggregate}")
if restrict_then_check == len(ground_truth) and per_day_then_aggregate != restrict_then_check:
    print("  PASS: the coarse property must be evaluated at its own resolution\n")
else:
    print("  FAIL\n")
    fail += 1


print("ALL PYTHON CHECKS PASS" if not fail else f"PYTHON CHECKS FAILED: {fail}")
raise SystemExit(1 if fail else 0)
