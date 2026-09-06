"""Monte Carlo checks for the design-of-experiments SKILL.

Pure stdlib. Each function independently verifies a claim the SKILL makes about
a prescribed design step, by simulating many experiments and measuring the
realized error rate or power.

Reference values it must reproduce:
  - power at the SKILL's sample size (sigma=20, delta=5)         -> ~0.80
  - design effect for m=50, rho=0.05                             -> 3.45
  - naive obs-level analysis of a cluster-randomized trial       -> FPR >> 0.05
  - cluster-level analysis of the same data                      -> FPR ~ 0.05
  - ANCOVA with a covariate at R^2=0.36 shrinks the SE by ~sqrt(0.64)
"""

import math
import random
import statistics

Z_CRIT = 1.959964  # two-sided 5%, normal approx (n is large in every case here)


def _mean_sd(xs):
    return statistics.fmean(xs), statistics.pstdev(xs)


def two_sample_z(a, b):
    """Two-sample z statistic assuming independent observations."""
    ma, sa = statistics.fmean(a), statistics.stdev(a)
    mb, sb = statistics.fmean(b), statistics.stdev(b)
    se = math.sqrt(sa * sa / len(a) + sb * sb / len(b))
    return (mb - ma) / se


def power_two_arm(n_per_arm, sigma, delta, trials, seed):
    """Realized power of a two-arm mean comparison at n_per_arm.

    Verifies references/power-and-sample-size.md: the prescribed n should give
    the target power (0.80) for an effect of size delta.
    """
    rng = random.Random(seed)
    hits = 0
    for _ in range(trials):
        a = [rng.gauss(0.0, sigma) for _ in range(n_per_arm)]
        b = [rng.gauss(delta, sigma) for _ in range(n_per_arm)]
        if abs(two_sample_z(a, b)) > Z_CRIT:
            hits += 1
    return hits / trials


def _cluster_arm(rng, n_clusters, m, tau, sigma_e, shift):
    """One arm: n_clusters clusters of size m, with a cluster random effect."""
    obs = []
    for _ in range(n_clusters):
        u = rng.gauss(0.0, tau)
        for _ in range(m):
            obs.append(shift + u + rng.gauss(0.0, sigma_e))
    return obs


def _cluster_means(rng, n_clusters, m, tau, sigma_e, shift):
    out = []
    for _ in range(n_clusters):
        u = rng.gauss(0.0, tau)
        out.append(shift + u + statistics.fmean(rng.gauss(0.0, sigma_e) for _ in range(m)))
    return out


def cluster_fpr(n_clusters, m, icc, trials, seed):
    """False-positive rate of two analyses of a *null* cluster-randomized trial.

    Verifies the SKILL's central guardrail: analyzing at the observation level
    when randomization was at the cluster level is pseudoreplication and inflates
    the false-positive rate far above the nominal 5%. Cluster-level analysis
    (the prescribed unit) restores it.
    """
    total_var = 1.0
    tau = math.sqrt(icc * total_var)
    sigma_e = math.sqrt((1.0 - icc) * total_var)
    rng = random.Random(seed)
    naive_hits = 0
    correct_hits = 0
    for _ in range(trials):
        a_obs = _cluster_arm(rng, n_clusters, m, tau, sigma_e, 0.0)
        b_obs = _cluster_arm(rng, n_clusters, m, tau, sigma_e, 0.0)  # no effect
        if abs(two_sample_z(a_obs, b_obs)) > Z_CRIT:
            naive_hits += 1
        a_cl = _cluster_means(rng, n_clusters, m, tau, sigma_e, 0.0)
        b_cl = _cluster_means(rng, n_clusters, m, tau, sigma_e, 0.0)
        if abs(two_sample_z(a_cl, b_cl)) > Z_CRIT:
            correct_hits += 1
    return naive_hits / trials, correct_hits / trials


def design_effect_empirical(n_clusters, m, icc, trials, seed):
    """Empirical design effect: Var(cluster-randomized mean) / Var(iid mean).

    Verifies DE = 1 + (m-1)*rho from references/power-and-sample-size.md.
    """
    total_var = 1.0
    tau = math.sqrt(icc * total_var)
    sigma_e = math.sqrt((1.0 - icc) * total_var)
    rng = random.Random(seed)
    clustered_means = []
    iid_means = []
    n = n_clusters * m
    for _ in range(trials):
        clustered_means.append(statistics.fmean(_cluster_arm(rng, n_clusters, m, tau, sigma_e, 0.0)))
        iid_means.append(statistics.fmean(rng.gauss(0.0, 1.0) for _ in range(n)))
    return statistics.pvariance(clustered_means) / statistics.pvariance(iid_means)


def ancova_se_ratio(n_per_arm, rsq, trials, seed):
    """Ratio of the ANCOVA-adjusted treatment-effect SE to the unadjusted SE.

    Verifies references/power-and-sample-size.md: adjusting for a pre-treatment
    covariate with outcome-correlation R multiplies the effective variance by
    (1 - R^2), i.e. the SE ratio is ~sqrt(1 - R^2).
    """
    rng = random.Random(seed)
    r = math.sqrt(rsq)
    unadj = []
    adj = []
    for _ in range(trials):
        # one experiment: covariate x, outcome y = r*x + sqrt(1-r^2)*e (+ 0 effect)
        def arm():
            xs = [rng.gauss(0.0, 1.0) for _ in range(n_per_arm)]
            ys = [r * x + math.sqrt(1 - rsq) * rng.gauss(0.0, 1.0) for x in xs]
            return xs, ys
        xa, ya = arm()
        xb, yb = arm()
        # unadjusted: difference in y means
        unadj.append(statistics.fmean(yb) - statistics.fmean(ya))
        # adjusted: residualize y on pooled x slope, then difference
        allx = xa + xb
        ally = ya + yb
        mx = statistics.fmean(allx)
        my = statistics.fmean(ally)
        sxx = sum((x - mx) ** 2 for x in allx)
        sxy = sum((x - mx) * (y - my) for x, y in zip(allx, ally))
        beta = sxy / sxx
        ra = [y - beta * x for x, y in zip(xa, ya)]
        rb = [y - beta * x for x, y in zip(xb, yb)]
        adj.append(statistics.fmean(rb) - statistics.fmean(ra))
    return statistics.pstdev(adj) / statistics.pstdev(unadj)


if __name__ == "__main__":
    print("smoke:", power_two_arm(252, 20.0, 5.0, 2000, 1))
