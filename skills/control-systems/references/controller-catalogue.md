# Controller catalogue

Classical and state-space controllers: when to use each, the control law, and
the checks that must accompany it. Climb this ladder only as far as the model
evidence and the constraint set force you.

## On-off / bang-bang

```
u = umax             if e >  h
u = umin             if e < -h
u = u_previous       if |e| <= h        (h = hysteresis band)
```

Use when simplicity and cost dominate and cycling is tolerable: thermostats,
level control, basic interlocks. Always include hysteresis to bound the switch
rate. Avoid when actuator wear, precision, energy use, overshoot, or a hard
limit make cycling unacceptable. Report the limit-cycle amplitude and period.

## PID

Continuous:

```
u(t) = Kp e(t) + Ki integral(e dt) + Kd de/dt
```

Discrete, with the parts that make it real:

```
u[k] = Kp e[k] + Ki sum(e_i) Ts + Kd (e[k] - e[k-1]) / Ts
```

- **Proportional** — acts on current error; alone leaves a steady-state offset.
- **Integral** — removes offset; causes windup and slow oscillation if
  unmanaged.
- **Derivative** — adds damping and anticipation; amplifies measurement noise.

Every deployed PID needs:

- actuator saturation modelled;
- **anti-windup** — clamp or back-calculate the integrator when the output
  saturates (conditional integration, or `integral += (u_sat - u_unsat)/Kp` per
  step);
- **derivative filtering** or **derivative-on-measurement** (`-Kd d y/dt`) so a
  setpoint step does not produce a derivative kick and so noise is not
  differentiated raw;
- **bumpless transfer** between manual and automatic — initialise the
  integrator so `u` is continuous at the switch;
- output rate limiting where the actuator has a slew limit;
- defined sensor-failure behaviour (hold last good, ramp to safe, hand to
  operator);
- **gain scheduling** where the plant gain / time constant changes materially
  across the operating range — with tested transitions between schedules;
- a stated tuning method (Ziegler–Nichols / relay / lambda / IMC / model-based)
  and the validation tests run afterwards.

PID is not a safe default for large dead time (`L/tau` above ~1), strong
nonlinearity, unstable multivariable plants, hard constraints, or plants where
unmodelled dynamics make aggressive feedback dangerous.

## Lead-lag and loop shaping

Use when a frequency response is available or meaningful.

- **Lead** compensation adds phase margin and speeds the response.
- **Lag** compensation improves low-frequency tracking / steady-state accuracy.
- **Notch** filters suppress a known resonance.
- **Low-pass** filters cut noise sensitivity at the cost of phase.

Compute or estimate: gain margin, phase margin, crossover frequency, closed-loop
bandwidth, the sensitivity function `S = (I + L)^-1` and complementary
sensitivity `T = L (I + L)^-1` where `L = G C`. `S + T = I`: you cannot make
both small everywhere. High bandwidth buys fast tracking but magnifies noise,
excites unmodelled modes, demands more actuator effort, and erodes robustness.
Target phase margin ~45–60°, gain margin ~6 dB or more unless a tighter design
is justified and tested.

## State feedback and observers

For `xdot = A x + B u`:

```
u = -K x + N r        ->      xdot = (A - BK) x + B N r
```

`K` places the closed-loop eigenvalues of `A - BK`; `N` sets the DC gain so `y`
tracks `r`. When not all states are measured, run an observer:

```
xhat_dot = A xhat + B u + L (y - C xhat)
```

`L` sets the estimation-error dynamics (eigenvalues of `A - LC`), typically
2–5× faster than the controller poles but slow enough not to amplify noise.

Design routes:

- **pole placement** — direct eigenvalue assignment; fine for low order and a
  clear target, but arbitrary fast poles cost actuator effort and robustness;
- **LQR** — minimise `J = integral(x' Q x + u' R u) dt`; systematic tradeoff of
  state deviation vs control effort; guaranteed gain margin (−6 dB, +inf) and
  60° phase margin *for the full-state-feedback loop only*;
- **Kalman filter** — the optimal linear state estimate under stated process
  and measurement noise covariances `Qk`, `Rk`;
- **LQG** — LQR + Kalman. The separation principle lets you design them
  independently for *nominal* performance, but LQG has **no guaranteed
  robustness margins** — check `S`, `T`, and the loop transfer at the plant
  input and output explicitly, or apply loop-transfer recovery.

State feedback assumes the model, the sensing, and the timing are good. Budget
for model error, estimator lag, and computational / communication delay before
trusting placed poles.

## Model predictive control

Solve, every step, over a horizon `N`:

```
min  sum_{k=0}^{N-1} [ (x_k - r_k)' Q (x_k - r_k) + u_k' R u_k ]
                     + (x_N - r_N)' Qf (x_N - r_N)
s.t. x_{k+1} = f(x_k, u_k, d_k)
     x_k in X,  u_k in U,  delta_u_k in dU
```

Apply `u_0`, measure, re-solve (receding horizon). Use MPC when inputs / states
have hard limits, several coupled variables must be balanced, future setpoints
or disturbances are known or forecastable, the model is adequately identified,
and the optimisation reliably meets the real-time deadline.

Mandatory tests:

- feasibility under the worst-case disturbance;
- solver deadline compliance at worst case, and a defined fallback if the solve
  is infeasible or late (last feasible plan, a backup PID, a safe hold);
- behaviour under model mismatch;
- stability — terminal cost / terminal constraint set / sufficiently long
  horizon, or an explicit stability argument;
- prediction- and control-horizon sensitivity;
- warm-start and numerical robustness;
- a safe action bound enforced **independently of** optimiser correctness.
