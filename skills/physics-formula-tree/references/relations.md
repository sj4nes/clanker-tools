# Relation types, cycles, bridges, approximation ladders

## Which relations become `tsort` edges

`tsort` needs a directed **acyclic** prerequisite graph. Physics knowledge is
richer, so store relation types separately.

| Relationship | Meaning | `tsort` edge? | Stored in |
|---|---|---|---|
| `requires` | necessary prerequisite for correct use/derivation | **yes** | `edges/dependencies.plan` |
| `defines` | one node formally introduces another | usually yes | `edges/dependencies.plan` |
| `derives_from` | a derivation needs a prior law/definition | **yes** | `edges/dependencies.plan` |
| `valid_when` | assumption/regime required for use | **yes** | `edges/dependencies.plan` |
| `generalizes` | one theory/formula extends another | no | `edges/relations.tsv` |
| `special_case_of` | constrained case of a more general relation | no (reverse pedagogical pressure) | `edges/relations.tsv` |
| `equivalent_to` | alternative but equal formulation | no | `edges/relations.tsv` |
| `contrasts_with` | distinguishes models/limits | no | `edges/relations.tsv` |
| `approximates` | approximation relationship | no (store regime + error) | `edges/relations.tsv` |
| `supersedes_in_regime` | more general theory applies under stated conditions | no | `edges/relations.tsv` |
| `historically_precedes` | historical sequence | no | `edges/relations.tsv` |
| `commonly_confused_with` | frequent misuse pair | no | `edges/relations.tsv` |
| `tested_by` | example/problem validates comprehension | no | `edges/relations.tsv` |

`edges/relations.tsv`: `type<TAB>source_id<TAB>target_id<TAB>note`.

Forcing all of these into `tsort` edges creates artificial cycles and destroys
the meaning of the dependency order. Do not do it.

## The edge test

For every candidate `tsort` edge `A B`, first write the plain-language claim in a
`#` comment in `dependencies.plan`, then check:

> "Can I truthfully say **A must be understood/introduced before B can be
> correctly defined, derived, interpreted, or applied** — within this release's
> scope?"

If no, it is not a `tsort` edge. Never reverse direction: if kinetic energy is
derived from the work-energy theorem, and the release introduces KE first, the
edge is `kinetic_energy work_energy_theorem`.

Prefer the **minimum direct prerequisite set**. Do not attach `addition`,
`multiplication`, `division`, `one_half` to every formula; work at a consistent
abstraction level (`scalar_multiplication`, `squaring`). Do not make every
possible derivation route a mandatory prerequisite — put alternates in the node's
`derivation_routes` metadata.

## Cycle patterns and resolutions

`tsort` on a cyclic graph: GNU exits non-zero; **BSD/macOS prints
`tsort: cycle in data` to stderr, emits a meaningless order, and exits 0** —
always check stderr (this is the `tsort` skill's rule).

Protocol when a cycle is reported: stop publication; preserve the edge list and
diagnostics; name the cycle nodes; translate every cycle edge to plain language;
classify each as true-prerequisite / operational-measurement / derivation /
explanatory / equivalence / historical / duplicate; move non-prerequisites to
`edges/relations.tsv`; if a genuine foundational choice remains, declare one
concept primitive for this scope; re-run `build-tree.sh`; record in
`edges/cycles.md`.

| Observed cycle | Underlying issue | Resolution |
|---|---|---|
| `force → acceleration`, `acceleration → force` | force defined via `a`, `a` measured via force | acceleration is **kinematic** (from position/time); force is **dynamical** via `F=ma`. Keep `force → acceleration` only if the release predicts `a` dynamically; store the reverse as an operational-measurement note. |
| mass ↔ force | operational mass measurement uses `F=ma` | mass is primitive for the release; the measurement procedure is a note, not an edge. |
| energy ↔ work | energy introduced via work; work uses force·displacement | pick one as the entry point; the other `derives_from` it one-directionally. |
| new app schema ↔ old app (analogous in staged physics models) | missing intermediate | add the intermediate regime/bridge node. |

Record every resolution in `edges/cycles.md`: the cycle, each edge's
classification, what was moved or made primitive, and why.

## Cross-domain bridges (high-value nodes)

Bridges reduce isolated formula clusters. Each is a node with fully audited
assumptions and a convention link.

| Bridge | Connects | Assumption to make explicit |
|---|---|---|
| work-energy theorem | dynamics ↔ energy | constant mass, net work |
| impulse-momentum theorem | force ↔ momentum | — |
| `F = -grad U` | force ↔ potential energy | **conservative force only**, formulation-dependent |
| `P = dE/dt` | energy ↔ rate/process | — |
| `E = h f` | waves ↔ quantum | photon, stated interpretation |
| `p = hbar k` | momentum ↔ wave vector | — |
| `E = m c^2` | mass ↔ energy | special relativity, rest frame |
| `c = 1/sqrt(mu0 eps0)` | EM ↔ wave propagation | vacuum |
| de Broglie `lambda = h/p` | classical momentum ↔ quantum wavelength | — |

Never present a bridge as universally applicable — link its regime nodes as
`tsort` prerequisites.

## Approximation ladders

Stored in `edges/relations.tsv` as `approximates`, **not** as `tsort` edges (an
approximation must not be forced to precede the theory it approximates). For each
`approximates` pair record: approximation formula, more general formula,
small parameter / regime, leading-correction term or error behaviour if the
source gives it, failure threshold, physical consequence of failure.

```text
approximates  newtonian_kinetic_energy   relativistic_kinetic_energy   v/c << 1; K = 1/2 m v^2 + 3/8 m v^4/c^2 + ...
approximates  small_angle_sine           sine_function                 theta in rad, theta << 1; error ~ theta^3/6
approximates  ideal_gas_law              real_gas_eos                  low density / high T; fails near condensation
approximates  geometric_optics           wave_optics                   lambda << feature size
approximates  electrostatic_limit        maxwell_equations             d/dt -> 0
```

Distinguish the **mathematical** limit from the **physical** validity limit:
`PV=nRT ⇒ P→∞` as `V→0+` is a valid math limit, but the ideal-gas model is
physically unreliable long before that.
