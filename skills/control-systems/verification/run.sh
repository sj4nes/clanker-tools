#!/bin/sh
# Verification run for the `control-systems` skill: exercises the prescribed
# workflow on a second-order mass-spring-damper plant with known closed forms.
#
#   1. analytic checks: poles, pole placement, Routh-Hurwitz, ctrl/obs dets  (bc)
#   2. structural feasibility: controllability / observability rank           (py)
#   3. nominal stability: placed continuous closed-loop poles have Re < 0     (py)
#   4. PID step response: integral action drives steady-state error -> 0      (py)
#   5. loop-rate guardrail: same PID diverges when Ts is made too large       (py)
#   6. anti-windup: bounded actuator + large setpoint, with vs without AW     (py)
#   7. robustness: Monte-Carlo plant-gain sweep, fraction still stable        (py)
set -e
cd "$(dirname "$0")"
PY=python3

echo "=== 1. analytic checks (bc) ==="
bc -q -l checks.bc
echo

echo "=== 2-7. workflow checks (python, stdlib only) ==="
$PY - <<'EOF'
import random
from plant import (controllability_2x2, observability_2x2,
                   closed_loop_poles_state_fb, simulate_pid)

fail = 0

# --- 2. structural feasibility ---------------------------------------------
dc = controllability_2x2()
do = observability_2x2()
print(f"2. controllability det = {dc:+.4f}   observability det = {do:+.4f}")
ok = abs(dc) > 1e-9 and abs(do) > 1e-9
print(f"   both nonzero -> controllable AND observable : {'PASS' if ok else 'FAIL'}")
fail += (not ok)

# --- 3. nominal stability of the placed state-feedback loop ---------------
# K placed for wn_cl = 2.0, zeta_cl = 0.8  (see checks.bc)
k1, k2 = 3.0, 2.8
re, im = closed_loop_poles_state_fb(k1, k2)
print(f"3. closed-loop poles: {re[0]:+.3f}{im[0]:+.3f}j , {re[1]:+.3f}{im[1]:+.3f}j")
ok = max(re) < 0
print(f"   all Re < 0 -> nominally asymptotically stable : {'PASS' if ok else 'FAIL'}")
fail += (not ok)

# --- 4. PID step response, integral action removes offset -----------------
_, _, m = simulate_pid(setpoint=1.0, kp=4.0, ki=3.0, kd=1.5, ts=0.05, t_end=40.0)
print(f"4. PID step: overshoot {m['overshoot_pct']:.1f}%  settle {m['settling_time']:.2f}s  "
      f"steady-state error {m['steady_state_error']:.2e}")
ok = (not m['diverged']) and m['steady_state_error'] < 1e-3 and m['settling_time'] < 15
print(f"   converges with ~zero steady-state error : {'PASS' if ok else 'FAIL'}")
fail += (not ok)

# proportional-only leaves a visible offset (contrast case)
_, _, mp = simulate_pid(setpoint=1.0, kp=4.0, ki=0.0, kd=1.5, ts=0.05, t_end=40.0)
print(f"   P+D only (ki=0): steady-state error {mp['steady_state_error']:.3f}  "
      f"(offset expected, integral is what removes it)")
fail += (not (mp['steady_state_error'] > 0.05))

# --- 5. loop-rate guardrail ---------------------------------------------------
_, _, mfast = simulate_pid(kp=4.0, ki=3.0, kd=1.5, ts=0.05, t_end=30.0)
_, ys_slow, mslow = simulate_pid(kp=4.0, ki=3.0, kd=1.5, ts=0.8, t_end=30.0)
print(f"5. same PID  Ts=0.05 -> settle {mfast['settling_time']:.2f}s, diverged={mfast['diverged']}")
print(f"             Ts=0.80 -> |y| max {max(abs(v) for v in ys_slow):.1e}, "
      f"diverged={mslow['diverged']}")
ok = (not mfast['diverged']) and mslow['diverged']
print(f"   too-slow sampling destabilises an otherwise-stable loop : {'PASS' if ok else 'FAIL'}")
fail += (not ok)

# --- 6. anti-windup ---------------------------------------------------------
# transient error saturates the actuator -> integrator winds up before recovery
kw = dict(setpoint=1.0, kp=4.0, ki=4.0, kd=1.0, ts=0.05, t_end=60.0,
          u_min=-1.0, u_max=1.0)
_, _, m_no = simulate_pid(anti_windup=False, **kw)
_, _, m_aw = simulate_pid(anti_windup=True, **kw)
print(f"6. actuator limited to +/-1.0, setpoint 1.0")
print(f"   no anti-windup : overshoot {m_no['overshoot_pct']:.0f}%  settle {m_no['settling_time']:.1f}s")
print(f"   anti-windup    : overshoot {m_aw['overshoot_pct']:.0f}%  settle {m_aw['settling_time']:.1f}s")
ok = m_aw['overshoot_pct'] < m_no['overshoot_pct'] and m_aw['settling_time'] <= m_no['settling_time']
print(f"   anti-windup reduces overshoot and settling : {'PASS' if ok else 'FAIL'}")
fail += (not ok)

# --- 7. robustness Monte-Carlo over plant gain ---------------------------------
rng = random.Random(20260906)
n, stable = 400, 0
worst_settle = 0.0
for _ in range(n):
    g = rng.uniform(0.7, 1.3)          # +/-30% gain uncertainty envelope
    _, _, mm = simulate_pid(setpoint=1.0, kp=4.0, ki=3.0, kd=1.5, ts=0.05,
                            t_end=40.0, g=g)
    if (not mm['diverged']) and mm['steady_state_error'] < 1e-2 and mm['settling_time'] < 20:
        stable += 1
        worst_settle = max(worst_settle, mm['settling_time'])
frac = stable / n
print(f"7. plant gain ~ U[0.7, 1.3], {n} runs: {frac*100:.1f}% stable & settled<20s, "
      f"worst settle {worst_settle:.1f}s")
ok = frac > 0.98
print(f"   robust across the declared +/-30% gain envelope : {'PASS' if ok else 'FAIL'}")
fail += (not ok)

print()
print("ALL CHECKS PASS" if fail == 0 else f"{fail} CHECK(S) FAILED")
raise SystemExit(1 if fail else 0)
EOF
