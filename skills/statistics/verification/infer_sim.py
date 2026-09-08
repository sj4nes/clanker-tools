"""Monte Carlo checks for the `statistics` SKILL.

Pure stdlib. Each function independently verifies a claim the SKILL makes about
a prescribed inference step by simulating many datasets and measuring the
realized coverage, error rate, bias, or variance.

Mirrors skills/design-of-experiments/verification/doe_sim.py in spirit: no
external CLI, so verification = exercise the prescribed step on a tractable
case with a known-correct answer.

Reference values it must reproduce:
  - t-interval coverage at n=5, normal data          -> ~0.95   (exact regime)
  - z-interval coverage at n=5                        -> ~0.87   (undercovers)
  - Wald proportion interval near p=0.08, n=40        -> well below 0.95
  - Wilson (score) interval, same case                -> ~0.93-0.95
  - percentile bootstrap for a mean (Exp, n=30)       -> ~0.92-0.95
  - percentile bootstrap for max of Uniform(0,theta)  -> far below 0.95
  - FWER of 20 independent nulls at alpha=0.05        -> ~0.64 unadjusted, <=0.05 Bonferroni
  - Rao-Blackwell: same mean, strictly lower variance
  - normal-variance MLE (/n) at n=4                   -> E ~ 0.75 (biased); /(n-1) ~ 1.0
"""

import math
import random
import statistics

# --- normal quantiles used below (two-sided 95%) ---------------------------
Z_975 = 1.959964
# Student-t 0.975 critical values by df (from tables); only the ones we use.
T_975 = {4: 2.776445, 29: 2.045230}


def _mean_ci_normal_known_shape(xs, crit):
    m = statistics.fmean(xs)
    s = statistics.stdev(xs)
    h = crit * s / math.sqrt(len(xs))
    return m - h, m + h


def t_vs_z_coverage(n, trials, seed):
    """Coverage of the exact t-interval vs the naive z-interval at small n.

    Verifies normal_mean_ci_unknown_variance (regime: exact) against the SKILL's
    'name the regime' principle: substituting the asymptotic z critical value
    at small n undercovers.
    """
    rng = random.Random(seed)
    t_hits = z_hits = 0
    tcrit = T_975[n - 1]
    for _ in range(trials):
        xs = [rng.gauss(0.0, 1.0) for _ in range(n)]
        lo, hi = _mean_ci_normal_known_shape(xs, tcrit)
        if lo <= 0.0 <= hi:
            t_hits += 1
        lo, hi = _mean_ci_normal_known_shape(xs, Z_975)
        if lo <= 0.0 <= hi:
            z_hits += 1
    return t_hits / trials, z_hits / trials


def _wilson(k, n, z=Z_975):
    if n == 0:
        return 0.0, 1.0
    phat = k / n
    denom = 1 + z * z / n
    center = (phat + z * z / (2 * n)) / denom
    half = (z / denom) * math.sqrt(phat * (1 - phat) / n + z * z / (4 * n * n))
    return center - half, center + half


def wald_vs_wilson_proportion(p, n, trials, seed):
    """Coverage of the Wald vs the Wilson interval for a binomial proportion.

    Verifies the wald_interval counterexample: the Wald interval undercovers
    near the boundary; the score (Wilson) interval does not.
    """
    rng = random.Random(seed)
    wald_hits = wilson_hits = 0
    for _ in range(trials):
        k = sum(1 for _ in range(n) if rng.random() < p)
        phat = k / n
        h = Z_975 * math.sqrt(phat * (1 - phat) / n)
        if phat - h <= p <= phat + h:
            wald_hits += 1
        lo, hi = _wilson(k, n)
        if lo <= p <= hi:
            wilson_hits += 1
    return wald_hits / trials, wilson_hits / trials


def _percentile_ci(boot, level=0.95):
    boot = sorted(boot)
    a = (1 - level) / 2
    lo = boot[int(a * len(boot))]
    hi = boot[min(len(boot) - 1, int((1 - a) * len(boot)))]
    return lo, hi


def bootstrap_regular_vs_not(trials, boots, seed):
    """Percentile-bootstrap coverage for a smooth functional vs a non-regular one.

    Verifies bootstrap_consistency's hypothesis: consistent for the mean of
    exponential data; inconsistent for the maximum of Uniform(0, theta) (the
    estimand sits at the edge of the support).
    """
    rng = random.Random(seed)
    n = 30
    mean_hits = max_hits = 0
    true_mean = 1.0      # Exp(rate=1)
    theta = 1.0          # Uniform(0, 1)
    for _ in range(trials):
        xs = [rng.expovariate(1.0) for _ in range(n)]
        bmeans = [statistics.fmean(rng.choices(xs, k=n)) for _ in range(boots)]
        lo, hi = _percentile_ci(bmeans)
        if lo <= true_mean <= hi:
            mean_hits += 1

        ys = [rng.uniform(0.0, theta) for _ in range(n)]
        bmax = [max(rng.choices(ys, k=n)) for _ in range(boots)]
        lo, hi = _percentile_ci(bmax)
        if lo <= theta <= hi:
            max_hits += 1
    return mean_hits / trials, max_hits / trials


def fwer_multiplicity(m, alpha, trials, seed):
    """Realized family-wise error rate of m independent true nulls.

    Verifies multiple_testing_fwer and bonferroni_correction: unadjusted FWER
    ~ 1-(1-alpha)^m; Bonferroni (per-test alpha/m) pulls it back under alpha.
    BH controls the FDR, which here (all nulls) equals the FWER, so with all
    nulls BH behaves like Bonferroni-ish -- we only assert unadjusted vs Bonf.
    """
    rng = random.Random(seed)
    raw_any = bonf_any = 0
    for _ in range(trials):
        pvals = [rng.random() for _ in range(m)]  # p ~ Uniform(0,1) under the null
        if any(p < alpha for p in pvals):
            raw_any += 1
        if any(p < alpha / m for p in pvals):
            bonf_any += 1
    return raw_any / trials, bonf_any / trials


def rao_blackwell_poisson(lam, n, trials, seed):
    """Crude estimator of e^{-lam}=P(X=0) vs its Rao-Blackwellization.

    delta = 1{X_1 = 0} is unbiased for e^{-lam}. Its conditional expectation
    given the complete sufficient statistic T = sum X_i is ((n-1)/n)^T
    (rao_blackwell_theorem / lehmann_scheffe_theorem -> the UMVUE). Same mean,
    lower variance.
    """
    rng = random.Random(seed)

    def pois(mu):
        # Knuth
        el = math.exp(-mu)
        k = 0
        pr = 1.0
        while True:
            pr *= rng.random()
            if pr <= el:
                return k
            k += 1

    crude = []
    rb = []
    for _ in range(trials):
        sample = [pois(lam) for _ in range(n)]
        crude.append(1.0 if sample[0] == 0 else 0.0)
        t = sum(sample)
        rb.append(((n - 1) / n) ** t)
    return (
        statistics.fmean(crude), statistics.pvariance(crude),
        statistics.fmean(rb), statistics.pvariance(rb),
        math.exp(-lam),
    )


def variance_mle_bias(n, trials, seed):
    """MLE of a normal variance (divide by n) vs the unbiased estimator (n-1).

    Verifies the SKILL's 'MLE guarantees are asymptotic' principle: at n=4 the
    MLE is visibly biased downward; mle_asymptotic_normality is an n->inf claim.
    """
    rng = random.Random(seed)
    mle = []
    unb = []
    for _ in range(trials):
        xs = [rng.gauss(0.0, 1.0) for _ in range(n)]
        m = statistics.fmean(xs)
        ss = sum((x - m) ** 2 for x in xs)
        mle.append(ss / n)
        unb.append(ss / (n - 1))
    return statistics.fmean(mle), statistics.fmean(unb)


if __name__ == "__main__":
    print("smoke t/z:", t_vs_z_coverage(5, 3000, 1))
