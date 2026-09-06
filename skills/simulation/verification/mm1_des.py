#!/usr/bin/env python3
"""Minimal discrete-event simulation of an M/M/1 queue.

Exercises the machinery the `simulation` skill prescribes:
  - an explicit event calendar (heap), time advancing event-to-event
  - seeded, independent random-number streams
  - a warm-up period discarded from steady-state statistics
  - independent replications -> a mean with a confidence interval
  - support for common random numbers (CRN) across configurations

Model (conceptual -> mathematical -> computational, kept separable):
  entities  : jobs
  resource  : one server, capacity 1
  queue     : FIFO, unbounded
  events    : arrival, departure
  arrivals  : Poisson process, rate lam           (inter-arrival ~ Exp(lam))
  service   : exponential, rate mu                 (service time  ~ Exp(mu))
  state     : number in system n(t)
  metric    : time-average number in system L  (Little: L = lam * W)

Analytic benchmark (rho = lam/mu < 1):
  L  = rho / (1 - rho)
  Lq = rho^2 / (1 - rho)
  W  = 1 / (mu - lam)
"""
from __future__ import annotations

import argparse
import heapq
import math
import random
import statistics


def replicate(lam: float, mu: float, horizon: float, warmup: float,
              arr_seed: int, svc_seed: int) -> float:
    """One independent run. Returns the time-average number in system
    over (warmup, horizon]. Arrival and service randomness draw from
    separate streams so CRN can hold one fixed while varying the other."""
    arr_rng = random.Random(arr_seed)
    svc_rng = random.Random(svc_seed)

    clock = 0.0
    n_in_system = 0            # state
    area = 0.0                 # integral of n(t) dt over the measured window
    last_t = 0.0
    measure_start = warmup

    # event calendar: (time, seq, kind); seq breaks ties deterministically
    cal: list[tuple[float, int, str]] = []
    seq = 0

    def schedule(t: float, kind: str) -> None:
        nonlocal seq
        heapq.heappush(cal, (t, seq, kind))
        seq += 1

    if lam > 0.0:
        schedule(arr_rng.expovariate(lam), "arrival")

    while cal:
        t, _, kind = heapq.heappop(cal)
        if t > horizon:
            break

        # accumulate area under n(t) for the portion inside the measure window
        seg_lo = max(last_t, measure_start)
        seg_hi = max(t, measure_start)
        if seg_hi > seg_lo:
            area += n_in_system * (seg_hi - seg_lo)
        last_t = t
        clock = t

        if kind == "arrival":
            n_in_system += 1
            if n_in_system == 1:  # server was idle -> start service now
                schedule(clock + svc_rng.expovariate(mu), "departure")
            schedule(clock + arr_rng.expovariate(lam), "arrival")
        else:  # departure
            n_in_system -= 1
            if n_in_system > 0:
                schedule(clock + svc_rng.expovariate(mu), "departure")

    span = horizon - measure_start
    return area / span if span > 0 else 0.0


def run(lam: float, mu: float, horizon: float, warmup: float,
        reps: int, base_seed: int, crn: bool) -> dict:
    ys = []
    for i in range(reps):
        if crn:
            # same arrival stream every rep-index across configs; only the
            # config (lam, mu) differs. Service stream also fixed per rep.
            arr_seed = base_seed * 1_000_003 + i
            svc_seed = base_seed * 2_000_029 + i
        else:
            arr_seed = random.Random(base_seed * 7 + i).randrange(2**31)
            svc_seed = random.Random(base_seed * 13 + i).randrange(2**31)
        ys.append(replicate(lam, mu, horizon, warmup, arr_seed, svc_seed))

    mean = statistics.fmean(ys)
    if reps > 1:
        sd = statistics.stdev(ys)
        half = 1.96 * sd / math.sqrt(reps)   # normal approx, reps large
    else:
        sd = float("nan")
        half = float("nan")
    return {"mean": mean, "sd": sd, "ci_half": half, "n": reps, "ys": ys}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--lam", type=float, default=0.8)
    p.add_argument("--mu", type=float, default=1.0)
    p.add_argument("--horizon", type=float, default=50_000.0)
    p.add_argument("--warmup", type=float, default=5_000.0)
    p.add_argument("--reps", type=int, default=40)
    p.add_argument("--seed", type=int, default=1)
    p.add_argument("--crn", action="store_true")
    a = p.parse_args()

    r = run(a.lam, a.mu, a.horizon, a.warmup, a.reps, a.seed, a.crn)
    rho = a.lam / a.mu
    analytic = rho / (1 - rho) if rho < 1 else float("inf")
    print(f"lam={a.lam} mu={a.mu} rho={rho:.4f} reps={a.reps} "
          f"horizon={a.horizon:g} warmup={a.warmup:g} crn={a.crn}")
    print(f"  simulated L = {r['mean']:.4f}  (95% CI +/- {r['ci_half']:.4f})")
    print(f"  analytic  L = {analytic:.4f}")
    if math.isfinite(analytic):
        inside = abs(r["mean"] - analytic) <= r["ci_half"]
        print(f"  analytic within simulated 95% CI: {inside}")


if __name__ == "__main__":
    main()
