# Cycles found and how they were resolved

`tsort` on `edges/dependencies.edges` is **acyclic** (BSD-safe stderr check, see
`validation/tsort-errors.txt` — empty). The following five conceptual loops were
recognised while building the graph and designed out *before* any edge was
written, by choosing a canonical entry point for each. None required deleting an
edge after the fact.

## 1. temperature ↔ zeroth law

*Loop:* "temperature is what thermometers measure" ↔ "a thermometer works
because temperature exists".
*Resolution:* the **zeroth law** (transitivity of thermal equilibrium) is the
entry point; `temperature` is the label it licenses. Edge: `zeroth_law →
temperature`. Thermometry (a substance whose property tracks `T`) is an
operational note on the `temperature` node, not an edge back to it.

## 2. temperature ↔ thermodynamic (absolute) scale

*Loop:* the Carnot efficiency `1 − T_c/T_h` needs absolute `T`; the absolute
scale `Q_h/Q_c = T_h/T_c` is defined *using* a Carnot engine.
*Resolution:* **empirical** `temperature` (from the zeroth law) comes first and
is enough to state the second law and construct a Carnot engine. The
**absolute scale** is a later node,
`carnot_theorem → thermodynamic_temperature_scale`, that *fixes the ratio
scale* — it does not redefine the thing the second law was stated with. That
the ideal-gas scale coincides with the absolute scale is a theorem, noted on the
`thermodynamic_temperature_scale` node.

## 3. internal energy ↔ first law

*Loop:* `U` is "the thing the first law conserves"; the first law is "`dU =
δQ − δW`".
*Resolution:* `internal_energy` is introduced as the state function whose
*existence* the first law asserts (`energy → internal_energy →
first_law_thermodynamics`). Its numerical values come only from measured `δQ`
and `δW` along paths — an operational note, not an edge.

## 4. heat ↔ first law

*Loop:* heat is defined via the first law; the first law contains `δQ`.
*Resolution:* the first law is stated in terms of `dU` and `δW` (both
independently grounded — `U` as a state function, `δW = P dV` from mechanics),
and **`heat` is then *defined* by it** as `δQ ≡ dU + δW`. Edge:
`first_law_thermodynamics → heat`. `temperature → heat` also holds (heat is the
transfer driven by a temperature difference).

## 5. entropy ↔ second law

*Loop:* the entropy-increase principle *is* a statement of the second law;
`entropy` is defined using the second law.
*Resolution:* the chain is
`carnot_theorem → clausius_inequality → entropy → entropy_increase_principle`.
The **Clausius inequality** (`∮ δQ/T ≤ 0`, proved from Carnot's theorem) comes
first; its **equality case** for reversible cycles makes `∮ δQ_rev/T = 0`, hence
`δQ_rev/T` is an exact differential, hence `entropy` exists as a state function.
The **entropy-increase principle** is then a separate downstream node that
`derives_from` `entropy` + `irreversible` + `isolated_system`.

## Non-prerequisite relations kept out of `tsort`

Stored as prose in the node entries / `conventions.md`, never as `tsort` edges:

- `helmholtz_free_energy`, `gibbs_free_energy`, `enthalpy` are **Legendre
  transforms** of `internal_energy` (`transform_of`) — but their prerequisite is
  `fundamental_relation_u`, not each other.
- `kelvin_planck_statement` `equivalent_to` `clausius_statement` (captured by the
  `second_law_equivalence` bridge node, which *does* have prerequisite edges from
  both).
- `ideal_gas_law` `approximated_by` real-gas equations (`superseded_in_regime`)
  — out of scope, named on the node.
