# Modelling and identification

A controller choice is premature until there is a model with a stated validity
domain and an uncertainty envelope. This file covers the model charter, the
standard model forms, linearisation, delay, the adequacy checks, and how to
read the controllability / observability tests without over-trusting them.

## The model charter

Write this before choosing a controller.

- **Control objective.** Controlled variables; manipulated variables; measured
  variables; disturbances; required operating envelope; reference / setpoint
  behaviour; hard safety limits; performance targets and acceptable tradeoffs;
  sampling rate and latency budget; operator authority and override rules;
  failure modes and safe states; validation environment and deployment phases.
- **System boundary.** Physical / digital components; sensors, actuators,
  communication links, people, external systems; I/O interfaces and units;
  operating modes; known delays; energy / material / information flows;
  assumptions and exclusions; trust and security boundaries; failure-propagation
  paths.
- **Model source.** First-principles conservation laws; mechanistic / causal
  process models; system identification from input–output data; grey-box
  (theory + data); simulation-derived; reduced-order; data-driven nonlinear
  (with explicit extrapolation limits).

A control-ready objective reads like: *"Maintain reactor temperature at 80 ± 2 °C,
minimise energy, never exceed 90 °C, tolerate a 20 % variation in feed
temperature and a 5 s sensor delay, retain manual emergency shutdown, and enter
a cooling-safe state after sensor failure."* "Keep the reactor stable" is not.

## Standard model forms

Continuous nonlinear state space:

```
xdot = f(x, u, d, theta)
y    = h(x, u, n, theta)
```

Linear time-invariant approximation near an operating point:

```
xdot = A x + B u + E d
y    = C x + D u + F n
```

Sampled (discrete) form, sample period Ts:

```
x[k+1] = Ad x[k] + Bd u[k] + Ed d[k]
y[k]   = Cd x[k] + Dd u[k] + Fd n[k]
```

First-order-plus-dead-time (the workhorse for process loops):

```
G(s) = K / (tau s + 1) * exp(-L s)
```

`K` gain, `tau` time constant, `L` dead time. Second-order:

```
G(s) = wn^2 / (s^2 + 2 zeta wn s + wn^2)
```

`wn` natural frequency, `zeta` damping ratio. `zeta < 1` underdamped (overshoot),
`zeta = 1` critically damped, `zeta > 1` overdamped.

## Linearisation

Around an operating point `(x0, u0)` with `f(x0, u0) = 0`:

```
delta_xdot = (df/dx)|_(x0,u0) delta_x + (df/du)|_(x0,u0) delta_u
```

Record: the operating point, the range of validity, and the trigger for
re-identification / gain scheduling / fallback. A linear controller designed on
this model is only licensed inside that range.

## Delay

Input delay and measurement delay add phase lag that feedback cannot see coming.
Even a small unmodelled `L` relative to `tau` turns an aggressive loop
oscillatory or unstable. Options: include the delay in the model (Padé
approximation or an explicit transport-delay state), detune the controller,
add a Smith predictor when the delay is well known, or switch to MPC with the
delay in the prediction model. Never design as though `L = 0` unless you have
shown `L << tau` and `L` is far below the loop period.

## Model-adequacy checks

Run before trusting the model for design:

- units and dimensional consistency (use the [`bc`](../../bc/SKILL.md) skill;
  lowercase identifiers, no `_` or single uppercase letters);
- conservation laws / invariants hold;
- correct steady-state gain and sign;
- residual diagnostics (no structure left in the errors);
- holdout prediction on data not used to fit;
- response to steps, impulses, ramps, and disturbance changes matches reality;
- parameter identifiability (are the fitted parameters actually constrained by
  the data, or trading off against each other?);
- operating-regime coverage — the data span the envelope the controller will
  see;
- delay and phase accuracy;
- extreme-case behaviour is physical;
- comparison against independent measurements;
- sensitivity of the design conclusion to the uncertain parameters.

A controller must not be more sophisticated than the model evidence justifies.

## Uncertainty register

List, with magnitudes, the uncertainty the design must tolerate:

| Class | Examples |
|---|---|
| Parametric | mass, gain, friction, time constant, reaction rate, service rate |
| Structural | missing dynamics, wrong model class, neglected nonlinearity |
| Disturbance | weather, load, demand, faults, shocks |
| Measurement | sensor noise, latency, bias, dropout, calibration error |
| Actuation | saturation, dead zone, backlash, rate limit, failure |
| Communication | packet loss, jitter, bandwidth, delayed commands |
| Human / organisational | delayed approval, adaptation, non-compliance |
| Implementation | finite precision, scheduling jitter, code error |

This register is the "declared envelope" the robustness analysis must cover.

## Controllability and observability — and how to read them

For `xdot = A x + B u` (n states):

```
Controllability matrix  Cm = [ B  AB  A^2 B  ...  A^(n-1) B ]   -> controllable iff rank(Cm) = n
Observability   matrix  Om = [ C; CA; CA^2; ...; CA^(n-1) ]     -> observable   iff rank(Om) = n
```

These are **nominal and local**. Interpret them:

- A theoretically controllable system can be practically uncontrollable because
  of actuator saturation, delay, cost, safety constraints, or insufficient
  bandwidth.
- A mathematically observable system can be poorly observable because noise
  makes state reconstruction unreliable — check the observability Gramian's
  condition number, not just the rank.
- **Unobservable unstable modes are a stop condition** — you cannot detect the
  divergence, let alone control it.
- Nonlinear systems need local, nonlinear, empirical, or structural reasoning —
  do not blindly apply the linear rank tests.
- Uncontrollable modes are acceptable only if they are stable and you can show
  they stay within the safe envelope on their own.

For multivariable plants, compute the relative gain array (RGA) at the crossover
frequency to see which manipulated variable should drive which controlled
variable and how strong the cross-coupling is; strong coupling points to
decoupling control or MPC rather than independent single loops.
