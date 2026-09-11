# Why Heat Engines Have a Ceiling

> Generated from the `physics-thermodynamics` capsule (Release 0.1) with the
> `formula-tree-tutorial` skill. The physics, the prerequisite order, and
> every calculation come from that capsule.

## How to run this

Install `upmd` (https://upmd.dev), then run
`upmd why-heat-engines-have-a-ceiling.md` for the interactive walk, or
`upmd --ci --all why-heat-engines-have-a-ceiling.md` to run every
calculation top to bottom. Each section ends with a code block you run
yourself; blocks depend on earlier ones, so
`upmd --ci -b capstone why-heat-engines-have-a-ceiling.md` runs the full
chain.

## What you need first

SI units and ordinary algebra — no other capsule tutorial is assumed. The
full path from `zeroth_law` to `carnot_efficiency` in
`physics-thermodynamics` has 42 prerequisites; this tutorial keeps the ones
that carry the actual argument and quietly assumes the bare math/SI-unit
floor (`real_numbers`, `length`, `mass`, `time`, `function`, `derivative`,
`integral`) a reader already has.

---

## 0. Setup

```bash [name:setup]
export t_c=300   # K, a cold reservoir
export t_h=600   # K, a hot reservoir -- exactly 2x the cold one, for round numbers
echo "cold reservoir: $t_c K, hot reservoir: $t_h K"
```

## 1. The zeroth law: why "temperature" is even a well-defined number

Before anything about heat or work, thermodynamics needs "temperature" to
mean something consistent. The **zeroth law** states: if system A is in
thermal equilibrium with system C, and B is also in thermal equilibrium
with C, then A and B are in thermal equilibrium with each other
(`A~C and B~C => A~B`). That transitivity is what lets you define a single
number — **temperature** — such that "same temperature" and "thermal
equilibrium" mean the same thing, and compare any two systems' temperatures
using a thermometer as the common "C." Without it, "hot" and "cold" would
only be pairwise comparisons, not a scale.

## 2. The first law: energy bookkeeping

The **first law**, `dU = dQ - dW`, says a system's internal energy changes
by exactly the heat added minus the work done *by* the system — energy is
conserved, full stop. **Heat** itself is defined through this law
(`dQ = dU + dW`): it's whatever energy transfer isn't accounted for by
mechanical work. This is the accounting system every later result in this
tutorial has to balance against — a heat engine can't produce more work
than the energy that flows into it, no matter how it's built.

## 3. Reversible, isothermal, adiabatic: the building blocks of a cycle

Three process types matter for what's next:

- **Reversible**: a process with no net entropy generation
  (`dS_univ = 0`) — an idealization no real process quite reaches, but the
  ceiling every real process is measured against.
- **Isothermal**: temperature held constant (`T = const`) while heat flows.
- **Adiabatic**: no heat exchanged at all (`dQ = 0`) — compression and
  expansion happen "too fast" for heat to flow in or out.

## 4. Cycles, engines, and refrigerators

A **thermodynamic cycle** returns a system to its starting state
(`cyclic integral dU = 0` — no net energy stored after one loop). Run one
between a hot and a cold reservoir, extracting net work, and you have a
**heat engine**, with efficiency `eta = |W| / |Q_h|` — work out divided by
heat *in* from the hot side. Run the same cycle backward, using work *in*
to move heat from cold to hot, and you have a **refrigerator** (or heat
pump), with `COP = |Q| / |W|`. Every steam turbine, car engine, and
refrigerator is one of these two, in disguise.

## 5. The second law, two ways

The first law alone doesn't rule out a "perfect" engine that turns 100% of
heat into work with no cold reservoir at all — that would still conserve
energy. The **second law** is the extra rule that forbids it, in two
apparently different but *provably equivalent* forms:

- **Kelvin–Planck**: no cyclic engine can take heat from a single reservoir
  and convert all of it to work — some heat must always be dumped
  somewhere colder.
- **Clausius**: heat never spontaneously flows from cold to hot on its
  own — a refrigerator only works because you put work in.

`second_law_equivalence` is the capsule's `bridge` node connecting them:
each statement can be shown to imply the other (violate one, and you can
build a device that violates the other). Either one is "the" second law;
this tutorial doesn't re-derive the equivalence proof, just uses the
result.

## 6. The Carnot cycle: the best-case engine

The **Carnot cycle** is one specific, idealized cycle: two isothermal legs
(heat absorbed at `T_h`, rejected at `T_c`) and two adiabatic legs
connecting them, run **reversibly**. It's not the only possible engine
cycle — it's the *theoretical best case*, built entirely from the
reversible building blocks in section 3.

## 7. Carnot's theorem: no engine beats it

**Carnot's theorem** is the actual "ceiling" claim: `eta_rev >= eta_any` —
no engine operating between two given reservoirs can be more efficient than
a reversible engine operating between the same two reservoirs, and *every*
reversible engine between those two reservoirs has exactly the same
efficiency, regardless of the working substance or the details of the
cycle. This follows from the second law by a proof-by-contradiction: pair
a hypothetical better-than-Carnot engine with a Carnot refrigerator running
backward, and the combination would violate Kelvin–Planck or Clausius.

## 8. The thermodynamic temperature scale

Because every reversible engine between two reservoirs has the *same*
efficiency, that efficiency can only depend on the two reservoir
temperatures — which is exactly what licenses **defining** temperature
itself by the heat ratio a reversible engine exchanges:
**`Q_h / Q_c = T_h / T_c`**. This is the capsule's
`thermodynamic_temperature_scale` node, and it's the temperature scale
that's actually independent of any particular thermometer substance
(unlike, say, "how much does mercury expand").

## 9. Carnot efficiency: the formula

Combine `thermodynamic_temperature_scale` with the heat-engine definition
`eta = |W|/|Q_h|` and energy conservation (`|W| = |Q_h| - |Q_c|`), and the
heat ratio becomes a temperature ratio directly:

**`eta = 1 - T_c / T_h`**

— the maximum possible efficiency of *any* heat engine running between a
hot reservoir at `T_h` and a cold reservoir at `T_c`, full stop, no matter
how cleverly it's engineered.

```bash [name:chk_carnot_efficiency, deps:setup]
echo "scale=4; 1 - $t_c / $t_h" | bc -l
echo "(want .5, for Tc=300K, Th=600K -- an exact 2:1 reservoir ratio)"
```

This is the same numeric case
`physics-thermodynamics/validation/dimensional-checks.bc` already runs and
labels `(want .5)`.

---

## Capstone: the ceiling for a real power plant

A typical coal-fired steam plant runs its boiler around `T_h ≈ 838 K`
(~565°C superheated steam) and rejects heat to the environment around
`T_c ≈ 298 K` (~25°C, roughly room temperature). Plug those into the same
formula:

```bash [name:capstone, deps:chk_carnot_efficiency]
t_h_plant=838   # K, typical superheated-steam boiler temperature
t_c_plant=298   # K, ambient cooling-water/air temperature
echo "Carnot ceiling for Th=$t_h_plant K, Tc=$t_c_plant K:"
echo "scale=4; 1 - $t_c_plant / $t_h_plant" | bc -l
echo ""
echo "real coal plants typically achieve 35-40% thermal efficiency --"
echo "well below this theoretical ceiling. The gap is entropy generation"
echo "from every real irreversibility (friction, turbulent mixing, finite"
echo "temperature-difference heat transfer) that carnot_theorem's eta_rev"
echo ">= eta_any already told you no real engine can close."
```

The ceiling comes out around 64% — and every real steam plant falls well
short of it. That gap isn't an engineering failure waiting to be fixed
away; `carnot_theorem` says a **perfectly reversible** engine is the only
way to reach the ceiling, and perfectly reversible processes are an
idealization no real, finite-time process achieves.

## Where to go next

- The full `physics-thermodynamics` capsule: `skills/physics-thermodynamics/`
  — entropy, the thermodynamic potentials, the Maxwell relations, and the
  ideal-gas specializations this tutorial skipped.
- Not covered here: `clausius_inequality`, `entropy` and its ideal-gas
  form, `refrigerator`/`COP` worked numerically (this tutorial only
  computed the engine case), and the third law — all in the capsule, none
  yet in a tutorial.
- `physics-acoustics/tutorial/how-fast-does-sound-travel.md` is this
  capsule's sibling: a different physics-formula-tree capsule, same
  "minimal path to one satisfying number" tutorial shape.
