# Conventions and foundational choices

## Notation

- `d` — exact differential of a **state function** (`dU`, `dS`, `dV`, `dT`):
  `∮ dX = 0` around any cycle.
- `δ` — a path-dependent infinitesimal of a **path function** (`δQ`, `δW`):
  `∮ δX` is generally nonzero.
- `Δ` — a finite change between two equilibrium states, never an uncertainty.
- Subscripts on partial derivatives name the held variable:
  `(∂U/∂T)_V` holds `V` fixed.
- Lowercase `u, h, s, c_v, c_p` are **molar** (per mole); uppercase `U, H, S, C`
  are **extensive**. `X = n x`.
- `T` is **thermodynamic (absolute) temperature in kelvin** everywhere except
  where a node explicitly says "empirical temperature".
- SI base dimensions used: `M, L, T, Θ, N` (see [`units.md`](units.md)).

## The sign convention (load-bearing)

**This release fixes the first law as**

```
dU = δQ − δW ,   δW = P dV   (quasi-static)
```

so **heat added to the system is positive** and **work done by the system is
positive**. A gas expanding against a piston does positive `δW` and, with no
heat, loses internal energy.

The common alternative — `dU = δQ + δW` with `δW` the work done *on* the system —
gives identical physics with every `W` sign flipped. It is **not** used here.
Any formula imported from a source that uses the other convention has been
rewritten to this one; see each formula's source note.

## Other conventions

- **Entropy zero point.** Only entropy *differences* are used, except where the
  third law fixes `S → 0` as `T → 0` for a perfect crystal.
- **Reservoir / reservoir temperatures.** `T_h > T_c > 0` denote the hot and
  cold reservoir temperatures; reservoirs are idealised as infinite (constant
  `T` despite heat exchange).
- **Efficiency and COP are magnitudes.** `η = |W|/|Q_h|`, `COP = |Q|/|W|`, all
  computed from magnitudes of the cycle's heat and work transfers.
- **Molar heat capacities of ideal gases are quoted, not derived** (that needs
  kinetic theory / equipartition, which is out of scope): monatomic
  `c_v = 3R/2`, diatomic `c_v = 5R/2` near room temperature.

## Foundational primitive choices

Accepted as **primitive for Release 0.1** (documented, not defined here):

| Node | Why primitive here | Omitted alternative |
|---|---|---|
| `real_numbers`, `function`, `derivative`, `partial_derivative`, `integral`, `exact_differential` | multivariable calculus assumed known | construction from first principles |
| `mass`, `length`, `time` | dimensional basis imported from mechanics | operational redefinition |
| `energy` | the mechanical work/energy concept `[M L^2 T^-2]`, imported | deriving thermal energy from microscopic motion |
| `pressure` | intensive state variable, operationally a gauge reading; `= F/A` in mechanics | deriving `P` from momentum flux (kinetic theory) |
| `amount_of_substance` | SI base quantity (mole) | particle count `N` and Avogadro's number |

A term is primitive here because Release 0.1 draws its boundary *above* the
level that would define it — not because it is intrinsically undefinable.

## Cycle-resolution decisions

Recorded in full in [`edges/cycles.md`](edges/cycles.md). Summary:

- **temperature ↔ zeroth law.** The zeroth law (transitivity of thermal
  equilibrium) is the entry point; `temperature` is the label the law licenses
  (`zeroth_law → temperature`). Thermometry (measuring `T` with a substance whose
  property varies) is an operational note on `temperature`, not a prerequisite
  edge back to it.
- **temperature ↔ second law (absolute scale).** `temperature` (empirical, from
  the zeroth law) comes first and is enough to *state* the second law and build a
  Carnot engine. The **thermodynamic (absolute) scale** — `Q_h/Q_c = T_h/T_c`
  for a reversible engine — is a *later* node
  (`carnot_theorem → thermodynamic_temperature_scale`), not a redefinition that
  loops back.
- **entropy ↔ second law.** The Clausius inequality (`∮ δQ/T ≤ 0`, proved from
  Carnot's theorem) comes first; `entropy` is defined as the state function
  whose differential is `δQ_rev/T` because the equality case makes `∮ δQ_rev/T`
  path-independent. Edge: `clausius_inequality → entropy`. The
  entropy-increase principle then `derives_from` `entropy` + `irreversible`.
- **internal energy ↔ first law.** `internal_energy` is introduced as the state
  function whose existence the first law asserts; `heat` is then *defined* by the
  first law as `δQ = dU + δW`. Edges run `energy → internal_energy`,
  `internal_energy → first_law_thermodynamics`, `first_law_thermodynamics → heat`.
- **work ↔ pressure/volume.** `work_thermodynamic` (`δW = P dV`) requires
  `pressure`, `volume`, `integral`, `quasistatic`; there is no edge back from
  work to pressure.

## Model vs law labels

- `zeroth_law`, `first_law_thermodynamics`, `kelvin_planck_statement`,
  `clausius_statement`, `carnot_theorem`, `clausius_inequality`,
  `entropy_increase_principle`, `third_law_thermodynamics` →
  `fundamental_law` **of classical thermodynamics** (each node states its scope).
- `ideal_gas_law` → `constitutive_model` (dilute-gas limit; each real gas
  deviates — the node names the correction).
- `carnot_efficiency`, `carnot_cop`, `mayer_relation`, `heat_capacity_ratio`,
  `enthalpy`, `adiabatic_reversible_ideal_gas`, `entropy_ideal_gas`,
  `tds_relations`, `fundamental_relation_u`, `maxwell_relations` →
  `derived_exact` **within their stated assumptions**.
- Ideal-gas molar `c_v`, `c_p` numeric values → `empirical_relation` (quoted from
  measurement / kinetic theory, not derived here).

## Changing a convention node

`work_sign_convention` and `extensive_intensive` are broad semantic nodes.
Editing either forces revalidation of **every** downstream formula's signs — do
it only with a changelog entry and a full re-audit.
