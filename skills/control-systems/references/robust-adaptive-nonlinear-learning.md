# Robust, adaptive, nonlinear, and learning control

Methods above the classical / LQG ladder. Each buys something specific and
carries a specific failure mode. None of them removes the need for an
independent safety layer.

## Stability categories

Name which one you are claiming:

- **Lyapunov** — small perturbations stay small.
- **Asymptotic** — the state returns to equilibrium.
- **Exponential** — with a rate.
- **BIBO** — bounded input gives bounded output.
- **Marginal** — bounded oscillation, no decay (fragile; usually unacceptable).
- **Input-to-state (ISS)** — bounded disturbance gives a bounded state response.
- **Practical** — the state enters and stays in an acceptable neighbourhood.
- **Robust** — stability persists across the declared model-uncertainty set.

LTI stability: continuous — all eigenvalues of `A_cl` have `Re(lambda) < 0`;
discrete — all `|lambda| < 1`. Evaluate with Routh–Hurwitz / root locus /
Nyquist, and always alongside the bandwidth and loop-rate budget.

## The uncertainty envelope

"Robust" is meaningless without a declared set. Before using any robust method,
write the envelope from the uncertainty register in
[`modeling-and-identification.md`](modeling-and-identification.md): parameter
ranges, an additive or multiplicative dynamic-uncertainty weight `W(s)`, the
disturbance spectrum / bound, the measurement-noise model, and the actuation and
communication limits. The guarantee only covers what you declared.

## Method map

| Method | Use when | Primary risk |
|---|---|---|
| H-infinity, mu-synthesis, robust loop shaping | Uncertainty and disturbance attenuation are central | Weight / model selection is hard; guarantees cover only the declared uncertainty |
| Gain scheduling | The plant changes predictably across regimes | Unsafe transitions; poor interpolation between scheduled models; hidden instability between grid points |
| Adaptive control (MRAC, self-tuning) | Parameters vary online but the structure is known | Unmodelled dynamics + insufficient excitation can destabilise the adaptation; needs a projection / dead-zone / robust modification |
| Sliding-mode | Strong robustness to matched uncertainty is required | Chattering, actuator wear, excitation of unmodelled high-frequency modes; use a boundary layer or higher-order SMC |
| Feedback linearisation | The nonlinear structure is known and invertible in the region of interest | Fragile to model mismatch; singularities; ignores actuator constraints |
| Nonlinear MPC | Nonlinear dynamics / constraints materially matter | Computational burden; local minima; weak global guarantees; solver reliability |
| Reinforcement-learning control | No usable model, and a safe training rig exists | Unsafe exploration; distribution shift; poor interpretability; constraint violation |
| Safe / constrained RL | Learning is necessary and constraints are formalised | Safety claims depend on the constraint model, the monitor, and the OOD detector being right |
| Hybrid / switched control | Modes, switching, logic, or contact dominate | Zeno behaviour; mode-transition errors; verification complexity |

## Gain scheduling — the discipline

- Choose scheduling variables that are measured, slowly varying relative to the
  loop, and that actually parameterise the dynamics change.
- Design and verify a controller at each operating point.
- Verify stability *between* grid points (interpolated plant + interpolated
  controller), not only at them.
- Bound the scheduling-variable rate; a fast traverse can destabilise a set of
  individually stable designs.
- Test every transition, including reversals and the boundaries.

## Learning-enabled control — default gates

If a learned component is in the loop, default to: offline evaluation first;
simulation with a validated plant model; conservative hard constraints; shadow
mode (recommendations logged, not applied); supervised deployment; explicit
out-of-distribution detection with a defined fallback; rollback capability; and
an **independent safety filter** (control-barrier function, reachability-based
supervisor, or interlock) that the learned policy cannot override.

Never treat reward maximisation as equivalent to safety or mission success, and
never present average episode return as evidence of worst-case behaviour.

## Safety filters and barrier functions

A safety filter sits between the nominal controller and the actuator:

```
u_applied = argmin || u - u_nominal ||^2   s.t.  u keeps the state in the safe set
```

Control-barrier-function (`h(x) >= 0` defines the safe set, enforce
`hdot >= -alpha(h)`) and reachability-based filters give a minimally invasive
override: the nominal controller runs freely until it would leave the safe set,
then the filter corrects only as much as needed. The filter must depend on its
own sensing / model path where consequences justify the independence.
