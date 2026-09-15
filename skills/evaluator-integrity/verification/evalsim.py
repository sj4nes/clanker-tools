#!/usr/bin/env python3
"""Monte Carlo half of the `evaluator-integrity` verification.

Standard library only; every RNG stream is seeded from an argument.

Four sections:

  1. budget confound   -- draws pass@k rather than computing the complement,
                          so it is an INDEPENDENT oracle for checks.bc §1
  2. selection gap     -- the reported score of the best-of-C candidates on
                          the set used to choose them, versus their true
                          ability; swept over C to show the gap grow with
                          the number of looks
  3. evaluator swap    -- a run whose true ability DECLINES every round but
                          whose score table rises, because the judge was
                          replaced halfway and the old rounds were not
                          re-scored
  4. leniency          -- draws the score/agreement curves rather than
                          integrating them: an independent oracle for
                          checks.bc §5

Each section prints PASS/FAIL lines and the script exits 1 if any failed.
"""

import random
import statistics

FAIL = []


def check(name, ok, detail=""):
    print(f"   [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
    if not ok:
        FAIL.append(name)


# --------------------------------------------------------------------------
# 1. BUDGET CONFOUND -- an independent oracle for the closed form in checks.bc
# --------------------------------------------------------------------------
def passatk_mc(p, k, trials, seed):
    """Fraction of trials in which at least one of k independent attempts
    succeeds. Drawn, not computed from 1-(1-p)^k -- that is the point."""
    rng = random.Random(seed)
    hits = 0
    for _ in range(trials):
        for _ in range(k):
            if rng.random() < p:
                hits += 1
                break
    return hits / trials


def section_budget(seed=20260914):
    print("=== 1. budget confound: pass@k at fixed ability ===")
    p, trials = 0.35, 200_000

    for k, closed in ((1, 0.35), (4, 0.82149375)):
        mc = passatk_mc(p, k, trials, seed + k)
        # 3 sd of a binomial proportion at n=200k is under 0.004
        check(
            f"pass@{k} Monte Carlo agrees with the closed form",
            abs(mc - closed) < 0.005,
            f"mc={mc:.5f} closed={closed:.5f}",
        )

    mc1 = passatk_mc(p, 1, trials, seed + 1)
    mc4 = passatk_mc(p, 4, trials, seed + 4)
    print("   ability p is IDENTICAL in both rows; only the budget changed")
    print(f"   reported: pass@1 = {mc1:.4f}  ->  pass@4 = {mc4:.4f}"
          f"   (+{100*(mc4-mc1):.1f} points)")

    # The naive default: read the delta as improvement.
    check(
        "an unmatched-budget comparison reports a large gain from nothing",
        (mc4 - mc1) > 0.40,
        f"apparent gain {100*(mc4-mc1):.1f} points at unchanged ability",
    )

    # The prescribed correction: match k, and the gain vanishes.
    mc4_again = passatk_mc(p, 4, trials, seed + 404)
    check(
        "matching the budget collapses the apparent gain to noise",
        abs(mc4_again - mc4) < 0.005,
        f"{100*abs(mc4_again-mc4):.2f} points, both at k=4",
    )
    print()


# --------------------------------------------------------------------------
# 2. SELECTION GAP -- choosing on the set you report on
# --------------------------------------------------------------------------
def selection_gap(n_candidates, true_ability, n_items, trials, seed):
    """Every candidate has the SAME true ability. Score each on a shared
    eval set of n_items, keep the best, and report that score. Also score
    the winner on a fresh held-out set.

    Returns (mean reported score, mean held-out score)."""
    rng = random.Random(seed)
    reported, heldout = [], []
    for _ in range(trials):
        scores = [
            sum(rng.random() < true_ability for _ in range(n_items)) / n_items
            for _ in range(n_candidates)
        ]
        best = max(scores)
        reported.append(best)
        # the winner's ability is still true_ability; a fresh set says so
        fresh = sum(rng.random() < true_ability for _ in range(n_items)) / n_items
        heldout.append(fresh)
    return statistics.fmean(reported), statistics.fmean(heldout)


def section_selection(seed=20260914):
    print("=== 2. selection gap: the set that steers must not be the set that reports ===")
    true_ability, n_items, trials = 0.60, 100, 400

    print(f"   {trials} runs; every candidate has true ability "
          f"{true_ability:.2f}; eval set = {n_items} items")
    print("   looks    reported (chosen-on set)    held-out    gap")

    gaps = []
    for c in (1, 5, 20, 100):
        rep, held = selection_gap(c, true_ability, n_items, trials, seed + c)
        gaps.append((c, rep, held))
        print(f"   {c:>5}    {rep:>20.4f}    {held:>8.4f}    "
              f"{100*(rep-held):>+5.1f} pts")

    g1 = gaps[0][1] - gaps[0][2]
    g100 = gaps[3][1] - gaps[3][2]

    check(
        "with one look the reported score is honest",
        abs(g1) < 0.02,
        f"gap {100*g1:+.1f} points",
    )
    check(
        "the gap grows with the number of looks at the same set",
        g100 > g1 + 0.04,
        f"{100*g1:+.1f} -> {100*g100:+.1f} points",
    )
    check(
        "every held-out score recovers the true ability",
        all(abs(h - true_ability) < 0.02 for _, _, h in gaps),
        f"held-out mean stays at {true_ability:.2f} regardless of looks",
    )
    # The default this displaces: report the best number you saw.
    check(
        "reporting the best-of-100 score overstates ability by a visible margin",
        gaps[3][1] - true_ability > 0.04,
        f"reported {gaps[3][1]:.4f} vs true {true_ability:.2f}",
    )
    print()


# --------------------------------------------------------------------------
# 3. EVALUATOR SWAP -- a rising table over a falling capability
# --------------------------------------------------------------------------
def score_round(ability, threshold, n, rng):
    """A judge admits a candidate when its observed quality clears
    `threshold`. Quality is the round's ability plus uniform noise."""
    passed = 0
    for _ in range(n):
        q = ability + rng.uniform(-0.30, 0.30)
        if q >= threshold:
            passed += 1
    return passed / n


def section_swap(seed=20260914):
    print("=== 3. evaluator swap: a rising table over a falling capability ===")
    rng = random.Random(seed)
    n = 20_000

    abilities = [0.60, 0.57, 0.54, 0.51, 0.48, 0.45]   # monotonically DOWN
    strict, lenient = 0.55, 0.35                        # judge v1, judge v2

    # what actually happened: v1 for rounds 1-3, v2 for rounds 4-6,
    # and the earlier rounds were never re-scored
    as_reported = []
    for i, a in enumerate(abilities):
        t = strict if i < 3 else lenient
        as_reported.append(score_round(a, t, n, rng))

    # the prescribed correction: re-score every round under ONE evaluator
    rescored = [score_round(a, strict, n, rng) for a in abilities]

    print("   round   true ability   judge   as reported   re-scored under v1")
    for i, a in enumerate(abilities):
        v = "v1" if i < 3 else "v2"
        print(f"   {i+1:>5}   {a:>12.2f}   {v:>5}   {as_reported[i]:>11.4f}   "
              f"{rescored[i]:>18.4f}")

    rep_delta = as_reported[-1] - as_reported[0]
    res_delta = rescored[-1] - rescored[0]
    print(f"   reported trend  {100*rep_delta:+.1f} points   "
          f"re-scored trend {100*res_delta:+.1f} points")

    check(
        "true ability declined every round",
        all(abilities[i + 1] < abilities[i] for i in range(len(abilities) - 1)),
    )
    check(
        "the as-reported table shows a NET GAIN over that decline",
        rep_delta > 0.05,
        f"{100*rep_delta:+.1f} points, entirely from the judge swap",
    )
    check(
        "re-scoring under one evaluator recovers the decline",
        res_delta < -0.15,
        f"{100*res_delta:+.1f} points",
    )
    check(
        "the two readings disagree in SIGN, not just magnitude",
        rep_delta > 0 > res_delta,
    )
    print()


# --------------------------------------------------------------------------
# 4. LENIENCY -- independent oracle for checks.bc §5
# --------------------------------------------------------------------------
def judge_curve(threshold, anchor, trials, seed):
    """Candidate quality ~ U(0,1). The judge admits at `threshold`; the
    anchor's truth is `anchor`. Returns (reported score, agreement)."""
    rng = random.Random(seed)
    passed = agree = 0
    for _ in range(trials):
        q = rng.random()
        j = q >= threshold
        a = q >= anchor
        passed += j
        agree += (j == a)
    return passed / trials, agree / trials


def section_leniency(seed=20260914):
    print("=== 4. leniency: score and accuracy move apart ===")
    anchor, trials = 0.50, 200_000

    print("   threshold   reported score   agreement with anchor")
    rows = []
    for t in (0.50, 0.35, 0.20, 0.00):
        s, a = judge_curve(t, anchor, trials, seed + int(t * 100))
        rows.append((t, s, a))
        print(f"   {t:>9.2f}   {s:>14.4f}   {a:>21.4f}")

    for t, s, a in rows:
        check(
            f"t={t:.2f}: score matches the closed form 1-t",
            abs(s - (1 - t)) < 0.005,
            f"mc={s:.4f} closed={1-t:.4f}",
        )
        check(
            f"t={t:.2f}: agreement matches the closed form 1-|t-0.5|",
            abs(a - (1 - abs(t - anchor))) < 0.005,
            f"mc={a:.4f} closed={1-abs(t-anchor):.4f}",
        )

    scores = [s for _, s, _ in rows]
    agrees = [a for _, _, a in rows]
    check(
        "score-selection is MONOTONE in leniency -- it has no interior optimum",
        scores == sorted(scores),
        "so 'adopt the judge that scores higher' never stops",
    )
    check(
        "the score-selected judge is the LEAST accurate one",
        agrees[scores.index(max(scores))] == min(agrees),
        f"picks agreement {min(agrees):.2f}, a coin flip",
    )
    check(
        "anchor-selection picks the judge at the truth",
        rows[agrees.index(max(agrees))][0] == anchor,
    )
    print()


if __name__ == "__main__":
    section_budget()
    section_selection()
    section_swap()
    section_leniency()

    if FAIL:
        print(f"*** {len(FAIL)} SIMULATION CHECK(S) FAILED: {', '.join(FAIL)}")
        raise SystemExit(1)
    print("ALL SIMULATION CHECKS PASSED")
    raise SystemExit(0)
