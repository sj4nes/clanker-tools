#!/usr/bin/env python3
"""Verification for the `unknown-discovery` skill.

Exercises the quantitative methods the skill prescribes on cases with known
answers, stdlib only:

  1. Calibration: a calibrated forecaster's Brier score approaches the
     irreducible p(1-p) floor; an overconfident one scores worse.
  2. Analysis of competing hypotheses: diagnostic evidence separates two
     hypotheses that non-diagnostic (confirming) evidence cannot.
  3. Residual / regime shift: a hidden variable is caught by clustered
     residuals while the aggregate mean residual hides it.
  4. Triage score P = I*U*(1-R)*D: monotonic in each component, and the
     components are retained (two equal scores, different drivers).
"""
import math
import random

fail = 0


def check(name, ok, detail=""):
    global fail
    print(f"   {name:<52} {'PASS' if ok else 'FAIL'}   {detail}")
    fail += (not ok)


# --- 1. calibration ---------------------------------------------------------
print("1. calibration — Brier score vs the irreducible p(1-p) floor")
rng = random.Random(20260906)
n = 40000
floor_sum = cal_sum = over_sum = 0.0
# calibration buckets for the calibrated forecaster
buckets = {i: [0, 0] for i in range(10)}          # bucket -> [n, hits]
for _ in range(n):
    q = rng.random()                              # true probability of this event
    o = 1 if rng.random() < q else 0
    p_cal = q                                     # calibrated: reports the truth
    # overconfident: push toward 0/1 around the midpoint
    p_over = min(1.0, max(0.0, 0.5 + (q - 0.5) * 3.0))
    floor_sum += q * (1 - q)
    cal_sum += (p_cal - o) ** 2
    over_sum += (p_over - o) ** 2
    b = min(9, int(p_cal * 10))
    buckets[b][0] += 1
    buckets[b][1] += o

floor = floor_sum / n
brier_cal = cal_sum / n
brier_over = over_sum / n
print(f"   irreducible floor mean p(1-p) = {floor:.4f}")
print(f"   calibrated forecaster Brier   = {brier_cal:.4f}")
print(f"   overconfident forecaster Brier= {brier_over:.4f}")
check("calibrated Brier ~ floor (within 0.01)", abs(brier_cal - floor) < 0.01,
      f"|{brier_cal:.4f}-{floor:.4f}|")
check("overconfident Brier > floor + 0.02", brier_over > floor + 0.02,
      f"{brier_over:.4f} > {floor + 0.02:.4f}")
# calibration curve: stated midpoint ~ observed frequency in every populated bucket
gaps = [abs((b + 0.5) / 10 - hits / cnt)
        for b, (cnt, hits) in buckets.items() if cnt > 50]
max_gap = max(gaps)
check("calibrated: stated prob ~ observed freq per bucket", max_gap < 0.03,
      f"max gap {max_gap:.3f}")

# --- 2. analysis of competing hypotheses ----------------------------------
print("\n2. competing hypotheses — diagnosticity")
prior = {"h1": 0.5, "h2": 0.5}


def update(post, like):
    z = sum(post[h] * like[h] for h in post)
    return {h: post[h] * like[h] / z for h in post}


# non-diagnostic evidence: both hypotheses predict it strongly
after_confirm = update(prior, {"h1": 0.90, "h2": 0.85})
# diagnostic evidence: expected under h1, unexpected under h2
after_diag = update(prior, {"h1": 0.90, "h2": 0.20})
print(f"   prior P(h1)                = {prior['h1']:.3f}")
print(f"   after non-diagnostic evid. = {after_confirm['h1']:.3f}")
print(f"   after diagnostic evidence  = {after_diag['h1']:.3f}")
check("non-diagnostic evidence barely moves posterior",
      abs(after_confirm["h1"] - 0.5) < 0.05, f"{after_confirm['h1']:.3f}")
check("diagnostic evidence moves posterior decisively",
      after_diag["h1"] > 0.80, f"{after_diag['h1']:.3f}")

# --- 3. residual / regime shift -----------------------------------------
print("\n3. residuals — a hidden regime shift the aggregate mean hides")
rng = random.Random(11)
rows = []                                          # (x, cat, late, y)
for i in range(4000):
    x = rng.uniform(0, 10)
    cat = rng.choice(["a", "b"])
    late = i > 2000
    y = 2.0 * x + rng.gauss(0, 1.0)
    if late and cat == "b":                        # hidden +4 in one cell only
        y += 4.0
    rows.append((x, cat, late, y))

# fit y ~ b0 + b1 x  by ordinary least squares
n_ = len(rows)
sx = sum(r[0] for r in rows)
sy = sum(r[3] for r in rows)
sxx = sum(r[0] ** 2 for r in rows)
sxy = sum(r[0] * r[3] for r in rows)
b1 = (n_ * sxy - sx * sy) / (n_ * sxx - sx * sx)
b0 = (sy - b1 * sx) / n_
resid = [(r, r[3] - (b0 + b1 * r[0])) for r in rows]

overall_mean = sum(e for _, e in resid) / n_
cell = [e for (r, e) in resid if r[2] and r[1] == "b"]
rest = [e for (r, e) in resid if not (r[2] and r[1] == "b")]
cell_mean = sum(cell) / len(cell)
rest_mean = sum(rest) / len(rest)
se_cell = (sum((e - cell_mean) ** 2 for e in cell) / len(cell)) ** 0.5 / math.sqrt(len(cell))
print(f"   overall mean residual          = {overall_mean:+.3f}")
print(f"   mean residual (late & cat b)    = {cell_mean:+.3f}  (se {se_cell:.3f})")
print(f"   mean residual (everything else) = {rest_mean:+.3f}")
check("aggregate mean residual looks clean", abs(overall_mean) < 0.15,
      f"{overall_mean:+.3f}")
check("disaggregated cell residual is many SE from zero",
      cell_mean / se_cell > 8, f"{cell_mean / se_cell:.1f} se")

# --- 4. triage score P = I*U*(1-R)*D -----------------------------------
print("\n4. triage score  P = I * U * (1 - R) * D")


def p_score(i, u, r, d):
    return i * u * (1 - r) * d


base = p_score(0.6, 0.6, 0.3, 3)
check("monotone increasing in impact", p_score(0.9, 0.6, 0.3, 3) > base)
check("monotone increasing in uncertainty", p_score(0.6, 0.9, 0.3, 3) > base)
check("monotone decreasing in reversibility", p_score(0.6, 0.6, 0.8, 3) < base)
check("monotone increasing in dependency centrality", p_score(0.6, 0.6, 0.3, 6) > base)
# two assumptions, equal score, different drivers -> components must be kept
a = dict(i=0.8, u=0.5, r=0.2, d=4)      # impact-driven
b = dict(i=0.4, u=1.0, r=0.2, d=4)      # uncertainty-driven
pa, pb = p_score(**a), p_score(**b)
check("equal score reachable from different components", abs(pa - pb) < 1e-9,
      f"{pa:.3f} == {pb:.3f}")
check("the components differ (score alone would lose this)", a["i"] != b["i"],
      "impact 0.8 vs 0.4 -> different probe")

print()
print("ALL CHECKS PASS" if fail == 0 else f"{fail} CHECK(S) FAILED")
raise SystemExit(1 if fail else 0)
