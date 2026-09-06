#!/bin/sh
# Verification run for the `simulation` skill: exercises the prescribed
# workflow on a tractable M/M/1 model with a known closed form.
#
#   1. analytic benchmark + dimensional / Little's-law check   (bc)
#   2. validation: simulated L vs analytic L, inside a 95% CI   (DES)
#   3. solver/horizon convergence: longer horizon tightens toward analytic
#   4. degenerate case: zero arrivals -> queue stays empty
#   5. stochastic discipline: one run is not evidence (wide spread shown)
#   6. common random numbers sharpen a paired config comparison
set -e
cd "$(dirname "$0")"
PY=python3

echo "=== 1. analytic benchmark + dimensional check (bc) ==="
bc -q checks.bc
echo

echo "=== 2. validation: simulated L vs analytic (rho=0.8, 40 reps) ==="
$PY mm1_des.py --lam 0.8 --mu 1.0 --reps 40 --seed 1
echo

echo "=== 3. horizon convergence (rho=0.8) ==="
for H in 5000 20000 80000; do
  $PY mm1_des.py --lam 0.8 --mu 1.0 --horizon "$H" --warmup 2000 --reps 30 --seed 2 \
    | sed -n '2p'
done
echo

echo "=== 4. degenerate case: lam = 0 -> L must be 0 ==="
$PY mm1_des.py --lam 0.0 --mu 1.0 --reps 5 --seed 3 | sed -n '2p'
echo

echo "=== 5. one run is not evidence (per-rep spread, rho=0.9) ==="
$PY - <<'EOF'
from mm1_des import replicate
ys = [replicate(0.9, 1.0, 20000, 2000, 100+i, 500+i) for i in range(8)]
print("  8 single runs :", ", ".join(f"{y:.2f}" for y in ys))
print(f"  min..max      : {min(ys):.2f} .. {max(ys):.2f}   analytic L = 9.00")
EOF
echo

echo "=== 6. common random numbers: paired (rho=0.7) vs (rho=0.75) ==="
$PY - <<'EOF'
import statistics, math
from mm1_des import replicate
def paired(crn):
    d=[]
    for i in range(60):
        if crn:
            a,s = 1_000_003+i, 2_000_029+i
        else:
            import random
            a = random.Random(7+i).randrange(2**31)
            s = random.Random(13+i).randrange(2**31)
        la = replicate(0.70,1.0,20000,2000,a,s)
        lb = replicate(0.75,1.0,20000,2000,a if crn else a+1,s if crn else s+1)
        d.append(lb-la)
    m=statistics.fmean(d); sd=statistics.stdev(d)
    return m, 1.96*sd/math.sqrt(len(d))
for crn in (False, True):
    m,h = paired(crn)
    print(f"  crn={crn!s:5}  mean delta L = {m:+.3f}  95% CI half-width = {h:.3f}")
print("  analytic delta L = 3.000 - 2.333 = 0.667")
EOF
