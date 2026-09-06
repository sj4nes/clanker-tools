# `control-systems` skill — verification run

The `control-systems` skill is methodology-only (no bespoke CLI), so
verification means: exercise the workflow the skill prescribes end-to-end on a
plant with a known closed form, and confirm each prescribed check behaves as
claimed.

**Model.** A normalised second-order mass–spring–damper (`wn = 1.0`,
`zeta = 0.2`), integrated with RK4 and driven by a discrete PID (derivative on
measurement, back-calculation anti-windup) or by placed state feedback. Chosen
because its poles, DC gain, controllability / observability, and pole-placement
gains are all exact by hand.

## Run

```
sh skills/control-systems/verification/run.sh
```

Tooling: `bc` 7.x (`-l`), Python 3 (stdlib only), macOS. ~2 s wall.

## What each step demonstrates (SKILL.md workflow step → result)

| Step | Prescribed check | Result |
|---|---|---|
| 2 model / units | `bc` reproduces open-loop poles `-0.2 ± j…`, the pole-placement gains `K = [3.0, 2.8]` for `wn_cl = 2, zeta_cl = 0.8`, Routh–Hurwitz `a1,a0 > 0`, and the ctrl/obs determinants | all consistent — **pass** |
| 3 structural feasibility | controllability det `-1.0`, observability det `+1.0` — both nonzero | controllable **and** observable — **pass** |
| 5 controller — nominal stability | placed closed-loop poles `-1.6 ± 1.2j`, `Re < 0` | nominally asymptotically stable — **pass** |
| 6 test campaign — tracking | PID step: steady-state error `~1.7e-11`; `ki = 0` (P+D only) leaves a `0.20` offset | integral action is what removes the offset — **pass** |
| 4 model / sampling guardrail | same PID at `Ts = 0.05 s` settles in `6.6 s`; at `Ts = 0.80 s` the output blows up to `~1e5` | too slow a loop rate destabilises an otherwise-stable loop (the Principles "model sampling explicitly" guardrail) — **pass** |
| 5 controller — anti-windup | actuator limited to `±1.0`, setpoint `1.0`: no anti-windup → `52 %` overshoot, `19.6 s` settle; with back-calculation → `1 %` overshoot, `9.1 s` settle | anti-windup is not optional on a saturating loop — **pass** |
| 6 test campaign — robustness | plant gain `~ U[0.7, 1.3]` (±30 % declared envelope), 400 runs | `100 %` stable & settled `< 20 s`, worst settle `9.2 s` — robust across the declared envelope — **pass** |

## Findings folded back into the skill

- `bc` needs `-l` for the (unused-here but conventional) math library and prints
  a leading-zero-less `.40`; identifiers kept lowercase and letters-only per the
  [`bc`](../../bc/SKILL.md) skill's rules — already reflected in the SKILL's
  step-2 unit-check guidance.
- The anti-windup contrast only appears when the steady-state actuator demand is
  *inside* the limit but the transient saturates: an unreachable setpoint
  (`u_ss > u_max`) makes both variants sit at the limit forever and hides the
  effect. This is the concrete reason the skill lists "saturation modelled"
  *and* "anti-windup" as separate mandatory elements — folded into
  `references/controller-catalogue.md`.

Nothing in `SKILL.md` or the reference files needed a correctness fix; the
prescribed workflow produced the right calls and the right conclusions. (The
demo PID is deliberately left loosely tuned — `37 %` overshoot on the nominal
step — so the anti-windup and loop-rate contrasts are visible; a real design
would tune it and re-run the campaign.)
