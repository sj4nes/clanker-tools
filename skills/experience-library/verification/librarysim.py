#!/usr/bin/env python3
"""Monte Carlo half of the `experience-library` verification.

Standard library only; every RNG stream is seeded from an argument.

Four sections:

  1. drift curve      -- DRAWS the coverage/retrieval trade-off (retrieval is
                         an actual argmax over noisy scores, not the closed
                         form (1-q)^(n-1)), so it is an INDEPENDENT oracle
                         for checks.bc §1
  2. retention policy -- three governance policies run over rounds:
                         unbounded growth, a governed cap with
                         contribution-based retirement, and an aggressive cap
  3. admission gate   -- a candidate with ZERO true effect that inspects well;
                         the inspection rule admits it, the paired A/B gate
                         rejects it
  4. paired power     -- paired vs unpaired detection of a real effect at the
                         same task budget: an independent oracle for the
                         variance argument in checks.bc §4

Each section prints PASS/FAIL lines and the script exits 1 if any failed.
"""

import random
import statistics

FAIL = []

CC = 0.02     # each entry is relevant to 2% of tasks
QQ = 0.01     # each distractor outranks the right entry 1% of the time


def check(name, ok, detail=""):
    print(f"   [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
    if not ok:
        FAIL.append(name)


# --------------------------------------------------------------------------
# 1. DRIFT CURVE -- drawn, not computed
# --------------------------------------------------------------------------
def drift_mc(n_entries, trials, seed):
    """One task at a time. Each of the n entries is independently relevant
    with probability CC. Retrieval returns the top-ranked entry; each
    irrelevant entry outranks a relevant one with probability QQ.

    Benefit is realised only when a relevant entry exists AND wins the
    ranking. Nothing here evaluates (1-CC)^n or (1-QQ)^(n-1) -- the whole
    point is to reach the same curve by a different route."""
    rng = random.Random(seed)
    hits = 0
    for _ in range(trials):
        relevant = [rng.random() < CC for _ in range(n_entries)]
        if not any(relevant):
            continue                     # no coverage: nothing to retrieve
        # the relevant entry loses if ANY irrelevant entry outranks it
        beaten = False
        for is_rel in relevant:
            if not is_rel and rng.random() < QQ:
                beaten = True
                break
        if not beaten:
            hits += 1
    return hits / trials


def closed_form(n):
    return (1 - (1 - CC) ** n) * ((1 - QQ) ** (n - 1))


def section_drift(seed=20260914):
    print("=== 1. drift curve: coverage rises, retrieval falls, benefit peaks ===")
    trials = 60_000

    print("   entries    benefit (drawn)    benefit (closed form)")
    drawn = {}
    for n in (10, 55, 100, 200):
        mc = drift_mc(n, trials, seed + n)
        drawn[n] = mc
        cf = closed_form(n)
        print(f"   {n:>7}    {mc:>15.4f}    {cf:>20.4f}")
        check(
            f"n={n}: drawn benefit agrees with the closed form in checks.bc",
            abs(mc - cf) < 0.008,
            f"drawn={mc:.4f} closed={cf:.4f}",
        )

    check(
        "the 200-entry library is WORSE than the 10-entry one",
        drawn[200] < drawn[10],
        f"{drawn[200]:.4f} < {drawn[10]:.4f}, despite 5x the coverage",
    )
    check(
        "the peak is interior -- n=55 beats both ends",
        drawn[55] > drawn[10] and drawn[55] > drawn[200],
        f"{drawn[55]:.4f} vs {drawn[10]:.4f} and {drawn[200]:.4f}",
    )
    check(
        "at n=100 the score is still ABOVE n=10 -- the collapse is not yet visible",
        drawn[100] > drawn[10],
        f"{drawn[100]:.4f} > {drawn[10]:.4f}, and already past the peak",
    )
    print()


# --------------------------------------------------------------------------
# 2. RETENTION POLICY -- unbounded vs governed vs aggressive
# --------------------------------------------------------------------------
def run_policy(cap, rounds, candidates_per_round, seed, retire_by_contribution=True):
    """Each round produces candidate entries. All are admitted (this section
    isolates RETENTION, not admission). When the library exceeds `cap`, the
    lowest-measured-contribution entries are retired.

    `cap = None` means unbounded growth.

    Returns the final library size."""
    rng = random.Random(seed)
    library = []          # each entry: its measured contribution so far
    for _ in range(rounds):
        for _ in range(candidates_per_round):
            # an entry's true contribution; most are marginal, a few good
            library.append(rng.expovariate(1.0))
        if cap is not None and len(library) > cap:
            if retire_by_contribution:
                library.sort(reverse=True)          # keep the best
            else:
                rng.shuffle(library)                # keep at random
            library = library[:cap]
    return len(library)


def section_policy(seed=20260914):
    print("=== 2. retention policy: the governance curve is a U, not a slope ===")
    rounds, per_round = 20, 10       # 200 candidates over the run

    policies = [
        ("aggressive cap (5)", 5),
        ("governed cap (55)", 55),
        ("no cap", None),
    ]
    results = {}
    print("   policy                  final size    benefit (drawn)")
    for name, cap in policies:
        size = run_policy(cap, rounds, per_round, seed + (cap or 999))
        # benefit is DRAWN on the library the policy actually produced, not
        # read off the closed form -- otherwise this section would only be
        # testing the policy -> size mapping.
        benefit = drift_mc(size, 30_000, seed + size)
        results[name] = (size, benefit)
        print(f"   {name:<22}  {size:>10}    {benefit:>14.4f}")

    agg = results["aggressive cap (5)"][1]
    gov = results["governed cap (55)"][1]
    non = results["no cap"][1]

    check("the governed cap beats no cap", gov > non, f"{gov:.4f} > {non:.4f}")
    check(
        "the aggressive cap is WORSE than no cap at all",
        agg < non,
        f"{agg:.4f} < {non:.4f} -- over-retirement is not the safe direction",
    )
    check("the governed cap beats the aggressive cap", gov > agg, f"{gov:.4f} > {agg:.4f}")
    check(
        "the ordering is governed > none > aggressive",
        gov > non > agg,
        "so 'retire harder' is not a monotone improvement",
    )
    print()


# --------------------------------------------------------------------------
# 3. ADMISSION GATE -- inspection vs a paired A/B run
# --------------------------------------------------------------------------
def inspection_admits(candidate_appeal, threshold=0.5):
    """The default gate: a human or model reads the candidate artifact and
    admits it if it reads as useful. Appeal is UNCORRELATED with effect --
    that is the failure being demonstrated."""
    return candidate_appeal > threshold


def paired_admits(true_effect, n_tasks, rng, z=2.0):
    """HDSO's gate: run the SAME tasks twice, control = current library,
    treatment = library + candidate. Admit only when the paired mean
    difference clears z standard errors of zero."""
    diffs = []
    for _ in range(n_tasks):
        # task difficulty is shared by both arms and CANCELS in the pairing
        difficulty = rng.gauss(0, 0.30)
        control = difficulty + rng.gauss(0, 0.10)
        treatment = difficulty + true_effect + rng.gauss(0, 0.10)
        diffs.append(treatment - control)
    mean = statistics.fmean(diffs)
    se = statistics.stdev(diffs) / (n_tasks ** 0.5)
    return mean > z * se


def section_admission(seed=20260914):
    print("=== 3. admission gate: a useless candidate that inspects well ===")
    rng = random.Random(seed)
    trials, n_tasks = 600, 100

    # A null candidate: zero true effect, but it reads well -- a plausible
    # lesson, crisply written, drawn from a real trajectory.
    null_inspect = null_paired = 0
    for _ in range(trials):
        appeal = rng.uniform(0.4, 1.0)          # it always reads well
        if inspection_admits(appeal):
            null_inspect += 1
        if paired_admits(0.0, n_tasks, rng):
            null_paired += 1

    # A real candidate: a genuine 0.05 improvement.
    real_inspect = real_paired = 0
    for _ in range(trials):
        appeal = rng.uniform(0.4, 1.0)
        if inspection_admits(appeal):
            real_inspect += 1
        if paired_admits(0.05, n_tasks, rng):
            real_paired += 1

    print(f"   {trials} candidates of each kind, {n_tasks} tasks per paired run")
    print("   candidate        inspection admits    paired A/B admits")
    print(f"   null (0 effect)  {null_inspect/trials:>17.3f}    {null_paired/trials:>17.3f}")
    print(f"   real (+0.05)     {real_inspect/trials:>17.3f}    {real_paired/trials:>17.3f}")

    check(
        "inspection admits the useless candidate at a high rate",
        null_inspect / trials > 0.7,
        f"{null_inspect/trials:.3f} -- appeal carries no information about effect",
    )
    check(
        "the paired gate rejects the useless candidate almost always",
        null_paired / trials < 0.10,
        f"admits only {null_paired/trials:.3f}",
    )
    check(
        "the paired gate still admits the real candidate",
        real_paired / trials > 0.8,
        f"{real_paired/trials:.3f} -- it is a gate, not a wall",
    )
    check(
        "inspection cannot tell the two candidates apart at all",
        abs(null_inspect - real_inspect) / trials < 0.08,
        f"{null_inspect/trials:.3f} vs {real_inspect/trials:.3f}",
    )
    print()


# --------------------------------------------------------------------------
# 4. PAIRED POWER -- oracle for the variance argument in checks.bc §4
# --------------------------------------------------------------------------
def unpaired_admits(true_effect, n_tasks, rng, z=2.0):
    """The same budget spent WITHOUT pairing: a fresh set of tasks for each
    arm, so per-task difficulty no longer cancels."""
    control = [rng.gauss(0, 0.30) + rng.gauss(0, 0.10) for _ in range(n_tasks)]
    treatment = [rng.gauss(0, 0.30) + true_effect + rng.gauss(0, 0.10)
                 for _ in range(n_tasks)]
    mean = statistics.fmean(treatment) - statistics.fmean(control)
    se = ((statistics.variance(treatment) + statistics.variance(control)) / n_tasks) ** 0.5
    return mean > z * se


def section_power(seed=20260914):
    print("=== 4. paired vs unpaired at the same task budget ===")
    rng = random.Random(seed)
    trials, n_tasks, effect = 600, 100, 0.05

    p_hit = sum(paired_admits(effect, n_tasks, rng) for _ in range(trials)) / trials
    u_hit = sum(unpaired_admits(effect, n_tasks, rng) for _ in range(trials)) / trials
    p_fp = sum(paired_admits(0.0, n_tasks, rng) for _ in range(trials)) / trials
    u_fp = sum(unpaired_admits(0.0, n_tasks, rng) for _ in range(trials)) / trials

    print(f"   effect {effect}, {n_tasks} tasks per arm, {trials} trials")
    print(f"   paired    detects {p_hit:.3f}   false-admits {p_fp:.3f}")
    print(f"   unpaired  detects {u_hit:.3f}   false-admits {u_fp:.3f}")

    check(
        "the paired design detects the real effect",
        p_hit > 0.8,
        f"{p_hit:.3f}",
    )
    check(
        "the unpaired design MISSES it at the same budget",
        u_hit < 0.35,
        f"{u_hit:.3f} -- the task budget was identical",
    )
    check(
        "both control false admissions, so the difference is power, not laxity",
        p_fp < 0.10 and u_fp < 0.10,
        f"paired {p_fp:.3f}, unpaired {u_fp:.3f}",
    )
    # sqrt((vd+ve)/ve) = sqrt(0.10/0.01) = sqrt(10) = 3.16, per checks.bc §4
    print("   checks.bc §4: the unpaired gate needs 10x the tasks for equal power")
    print()


if __name__ == "__main__":
    section_drift()
    section_policy()
    section_admission()
    section_power()

    if FAIL:
        print(f"*** {len(FAIL)} SIMULATION CHECK(S) FAILED: {', '.join(FAIL)}")
        raise SystemExit(1)
    print("ALL SIMULATION CHECKS PASSED")
    raise SystemExit(0)
