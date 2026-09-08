#!/bin/sh
# Verification run for the `statistics` skill. The skill is methodology-only
# (no bespoke CLI), so verification means: exercise the prescribed inference
# steps on tractable cases with known-correct answers, and confirm each
# prescribed check behaves as the SKILL claims. Every claim maps to a
# math-statistics node.
#
#   1. CRLB efficiency + multiplicity arithmetic                     (bc)
#   2. exact t-interval vs naive z-interval coverage at n=5          (Monte Carlo)
#   3. Wald vs Wilson proportion-interval coverage near p=0.08       (Monte Carlo)
#   4. bootstrap coverage: smooth mean vs non-regular maximum        (Monte Carlo)
#   5. family-wise error rate: unadjusted vs Bonferroni             (Monte Carlo)
#   6. Rao-Blackwell: same mean, strictly lower variance            (Monte Carlo)
#   7. normal-variance MLE bias at n=4                              (Monte Carlo)
set -e
cd "$(dirname "$0")"
PY=python3

echo "=== 1. CRLB efficiency + multiplicity arithmetic (bc) ==="
bc -lq checks.bc
echo

echo "=== 2. t-interval vs z-interval coverage, n=5 normal (want t~0.95, z<0.90) ==="
$PY - <<'EOF'
from infer_sim import t_vs_z_coverage
t, z = t_vs_z_coverage(5, 40000, 7)
print(f"  t-interval (exact regime)   coverage = {t:.3f}   target 0.950")
print(f"  z-interval (wrong regime)   coverage = {z:.3f}   undercovers")
ok = 0.94 <= t <= 0.96 and z < 0.90
print(f"  {'PASS' if ok else 'FAIL'}  -- normal_mean_ci_unknown_variance needs the t critical value")
EOF
echo

echo "=== 3. Wald vs Wilson interval for a proportion, p=0.08 n=40 ==="
$PY - <<'EOF'
from infer_sim import wald_vs_wilson_proportion
wald, wil = wald_vs_wilson_proportion(0.08, 40, 40000, 11)
print(f"  Wald interval   coverage = {wald:.3f}   (nominal 0.95 -- undercovers)")
print(f"  Wilson interval coverage = {wil:.3f}")
ok = wald < 0.92 and wil >= 0.92
print(f"  {'PASS' if ok else 'FAIL'}  -- the wald_interval counterexample near the boundary")
EOF
echo

echo "=== 4. percentile bootstrap: smooth mean vs non-regular maximum ==="
$PY - <<'EOF'
from infer_sim import bootstrap_regular_vs_not
m, mx = bootstrap_regular_vs_not(3000, 800, 23)
print(f"  mean of Exp(1), n=30      coverage = {m:.3f}   (~nominal: smooth functional)")
print(f"  max of Uniform(0,1), n=30 coverage = {mx:.3f}   (fails: estimand at edge of support)")
ok = m >= 0.90 and mx < 0.80
print(f"  {'PASS' if ok else 'FAIL'}  -- bootstrap_consistency needs the smoothness hypothesis")
EOF
echo

echo "=== 5. family-wise error rate: 20 independent nulls at alpha=0.05 ==="
$PY - <<'EOF'
from infer_sim import fwer_multiplicity
raw, bonf = fwer_multiplicity(20, 0.05, 20000, 29)
print(f"  unadjusted FWER = {raw:.3f}   (analytic 1-(1-.05)^20 = 0.642)")
print(f"  Bonferroni FWER = {bonf:.3f}   (<= 0.05)")
ok = 0.60 <= raw <= 0.68 and bonf <= 0.055
print(f"  {'PASS' if ok else 'FAIL'}  -- multiple_testing_fwer / bonferroni_correction")
EOF
echo

echo "=== 6. Rao-Blackwell: crude 1{X1=0} vs E[.|sum X] for e^{-lam}, Poisson ==="
$PY - <<'EOF'
from infer_sim import rao_blackwell_poisson
cm, cv, rm, rv, truth = rao_blackwell_poisson(1.0, 10, 40000, 31)
print(f"  target e^-1                 = {truth:.4f}")
print(f"  crude   mean={cm:.4f}  var={cv:.5f}")
print(f"  Rao-Blackwell mean={rm:.4f}  var={rv:.5f}")
ok = abs(cm - truth) < 0.01 and abs(rm - truth) < 0.01 and rv < cv * 0.5
print(f"  {'PASS' if ok else 'FAIL'}  -- rao_blackwell_theorem: same mean, strictly lower variance")
EOF
echo

echo "=== 7. normal-variance MLE bias at n=4 (want MLE~0.75, unbiased~1.0) ==="
$PY - <<'EOF'
from infer_sim import variance_mle_bias
mle, unb = variance_mle_bias(4, 80000, 37)
print(f"  MLE (/n)      mean = {mle:.3f}   (biased low; true = 1.000)")
print(f"  unbiased (/n-1) mean = {unb:.3f}")
ok = abs(mle - 0.75) < 0.02 and abs(unb - 1.0) < 0.02
print(f"  {'PASS' if ok else 'FAIL'}  -- mle_asymptotic_normality is an n->inf statement")
EOF
