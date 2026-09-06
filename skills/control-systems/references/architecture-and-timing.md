# Architecture and timing

The controller law is a small part of a deployable system. This file covers the
layering, the multi-rate structure, sampling hazards, hybrid-mode handling, and
fault detection.

## Layered control

A robust real system has independent layers, each separately inspectable:

1. **Physical process** — plant and environment.
2. **Sensors / estimation** — filtering, fault detection, state estimation.
3. **Fast local loop** — current / torque, temperature, pressure, position,
   voltage, rate control.
4. **Supervisory loop** — setpoints, scheduling, optimisation, mode selection.
5. **Safety layer** — independent limits, interlocks, emergency stop, safe-state
   logic. Must not be bypassable by the optimiser or a learned policy.
6. **Human authority** — approval, override, escalation, maintenance.
7. **Monitoring and audit** — telemetry, alarms, incidents, controller / model
   version tracking.
8. **Security layer** — segmentation, authentication, authorisation, secure
   update, anomaly response.

Common composite control law:

```
u = u_feedforward(d, r) + u_feedback(r - y)
u_applied = safety_filter( saturate( u ) )
```

## Multi-rate control

Loops run at different rates:

| Loop | Typical rate |
|---|---|
| Current / torque | very fast (kHz) |
| Velocity | fast |
| Position | slower |
| Path planner / MPC | slower |
| Mission / operations planner | slow |
| Human strategic review | slowest |

Document, per loop: sample and update rate; sensor timestamp quality;
computation time; communication jitter; hold behaviour (zero-order hold, last
value, extrapolation); synchronisation between loops; data age at the moment of
decision; and the buffering / dropout policy. A controller designed as though
every signal is instantaneous and synchronous is not deployment-ready.

## Sampling and aliasing

- The loop rate should be several times (rule of thumb 10–20×) the desired
  closed-loop bandwidth for smooth, robust motion; a servo needs more where
  stability margins are tight.
- Anti-alias filter every analogue measurement below the Nyquist frequency
  before sampling — aliased noise cannot be removed digitally.
- Account for the sample-and-hold half-period of phase lag in the stability
  analysis; it is not free.
- Re-verify discrete closed-loop stability at the *actual* `Ts`, including
  worst-case scheduling jitter, not the nominal one. (The verification harness
  in this skill shows an otherwise-stable loop diverging when `Ts` is made too
  large.)

## Hybrid systems

Continuous dynamics plus discrete modes: thermostat on/off, aircraft modes,
robot contact, gear shifts, safety shutdown, traffic-signal states,
threshold-triggered policies.

Represent with hybrid automata: modes, continuous dynamics per mode, guard
conditions, reset maps, and explicit transition priorities. Test every
transition, including race conditions, simultaneous events, chattering across a
guard, and every recovery path. Watch for Zeno behaviour (infinitely many
transitions in finite time) — add hysteresis or dwell-time constraints. A
bounded state-machine core can be checked with the
[`tla-checker`](../../tla-checker/SKILL.md) skill.

## Fault detection, isolation, and recovery (FDIR)

- **Detection** — residual between measured and predicted output crosses a
  threshold; sensor range / rate / cross-check violations; actuator
  command-vs-response mismatch; watchdog timeout.
- **Isolation** — structured residuals or parity relations to identify which
  sensor / actuator / component failed.
- **Recovery** — reconfigure to redundant hardware; fall back to a degraded
  controller; hold last safe output; ramp to the safe state; hand to the
  operator. Define which for each fault, and the alarm priority.
- **Graceful degradation** — a defined sequence of reduced-capability modes
  rather than a binary works / fails, each with its own safe envelope.

Every fault path needs a test in the scenario matrix, including simultaneous
faults and a fault during a mode transition.
