#!/bin/sh
# Verification run for the `design-of-experiments` skill. The skill is
# methodology-only (no bespoke CLI), so verification means: exercise the
# prescribed steps on tractable cases with known-correct answers, and confirm
# each prescribed check behaves as the SKILL claims.
#
#   1. sample-size + adjustment arithmetic                        (bc)
#   2. realized power at the prescribed n                         (Monte Carlo)
#   3. empirical design effect vs 1 + (m-1)*rho                   (Monte Carlo)
#   4. pseudoreplication: obs-level vs cluster-level FPR          (Monte Carlo)
#   5. ANCOVA covariate adjustment shrinks the SE by ~sqrt(1-R^2) (Monte Carlo)
#   6. fractional-factorial alias structure, two independent ways (exact)
set -e
cd "$(dirname "$0")"
PY=python3

echo "=== 1. sample-size + adjustment arithmetic (bc) ==="
bc -q checks.bc
echo

echo "=== 2. realized power at the prescribed n (sigma=20, delta=5, n=252/arm) ==="
$PY - <<'EOF'
from doe_sim import power_two_arm
p = power_two_arm(252, 20.0, 5.0, 10000, 1)
print(f"  realized power = {p:.3f}   target = 0.800   {'PASS' if 0.77 <= p <= 0.83 else 'FAIL'}")
EOF
echo

echo "=== 3. empirical design effect (m=50, rho=0.05; want 3.45) ==="
$PY - <<'EOF'
from doe_sim import design_effect_empirical
de = design_effect_empirical(20, 50, 0.05, 4000, 7)
print(f"  empirical DE = {de:.2f}   analytic 1+(m-1)rho = 3.45   "
      f"{'PASS' if 3.1 <= de <= 3.8 else 'FAIL'}")
EOF
echo

echo "=== 4. pseudoreplication: false-positive rate of a NULL cluster trial ==="
$PY - <<'EOF'
from doe_sim import cluster_fpr
naive, correct = cluster_fpr(20, 50, 0.05, 2500, 11)
print(f"  obs-level analysis (wrong unit)  FPR = {naive:.3f}   (nominal 0.05)")
print(f"  cluster-level analysis (correct) FPR = {correct:.3f}")
ok = naive > 0.15 and 0.03 <= correct <= 0.08
print(f"  {'PASS' if ok else 'FAIL'}  -- obs-level analysis inflates the error rate ~{naive/0.05:.0f}x")
EOF
echo

echo "=== 5. ANCOVA: SE ratio vs sqrt(1 - R^2), R^2 = 0.36 ==="
$PY - <<'EOF'
import math
from doe_sim import ancova_se_ratio
ratio = ancova_se_ratio(400, 0.36, 4000, 23)
want = math.sqrt(1 - 0.36)
print(f"  empirical SE ratio = {ratio:.3f}   sqrt(1-R^2) = {want:.3f}   "
      f"{'PASS' if abs(ratio - want) < 0.03 else 'FAIL'}")
EOF
echo

echo "=== 6. fractional factorial 2^(4-1), D=ABC: alias structure ==="
$PY alias.py
