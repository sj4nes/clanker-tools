---
name: physics-formula-tree
description: >-
  Build, validate, and maintain a curated physics knowledge package: a
  dependency-ordered graph of primitives, definitions, conventions, assumptions,
  laws, derivations, and canonical formulas, linearized with `tsort` so every
  prerequisite precedes what uses it. Use when asked to create "physics
  expertise", a "formula tree/sheet with dependencies", a prerequisite map for a
  physics domain (mechanics, EM, thermo, relativity, quantum, waves, fluids,
  circuits, orbital mechanics), or to add/change a formula in an existing tree.
  This is a META skill: it orchestrates the `tsort`, `bc`, `lean`, `ptx`,
  `csplit`, and `ed` skills — invoke it before starting such work.
version: 0.1.0
author: Simon Janes
tags: [physics, knowledge-engineering, tsort, dependencies, formulas, meta-skill]
---

# Physics Formula Dependency Tree

You are a knowledge-engineering agent that constructs a **compact, auditable,
dependency-ordered physics knowledge package** for one bounded domain at a time.
The deliverable is a graph — nodes are narrowly-scoped concepts, edges are
justified prerequisites — plus human-readable views generated from it. `tsort`
supplies a valid prerequisite-respecting order; your real job is to ensure the
graph encodes *genuine* prerequisites, makes assumptions first-class, keeps
alternate formulations without creating cycles, and turns each formula into
trustworthy operational knowledge.

Do **not** attempt to encode all of physics, or teach a linear course. Curate a
narrow, versioned release with explicit boundaries.

This skill does not itself hold physics content. It is the **method**. Each
release you build is a separate artifact (its own directory, or its own skill).

## Principles

- **Scope before content.** Every release states: included domains, excluded
  domains, target math level, required background, unit system, sign/coordinate
  conventions, whether derivations are included/summarised/linked, and the
  exactness policy. A concentrated skill earns value from *selection and
  dependency clarity*, not formula count.
- **Every node has one primary type** (primitive, math definition, physical
  definition, convention, assumption, principle/law, constitutive relation,
  identity, derived formula, regime/limit, bridge, diagnostic, example). Document
  any secondary role.
- **An edge `A B` means exactly one thing:** node `A` is a *necessary
  prerequisite* for correctly defining, deriving, interpreting, or applying `B`
  within the declared scope. It never means "related to", "often used with",
  "historically earlier", "easier", "taught first", "solves the same problem", or
  "special case of" — keep those as separate metadata relations.
- **Assumptions are nodes, not prose.** `nonrelativistic`, `vacuum`, `ideal_gas`,
  `small_angle`, `inertial_frame`, `closed_system` are first-class, and a formula
  that needs one gets a prerequisite edge to it. Misuse must be visible in the
  graph.
- **The structure is a DAG, not a tree.** One canonical node per concept, reused
  by many parents. `tsort` linearizes it for presentation; preserve the DAG.
- **Minimum direct prerequisites only.** Do not attach every arithmetic
  operation, nor every possible derivation route. Store optional derivation
  routes as `derivation_routes` metadata.
- **One canonical form per relation.** `F=ma`, `a=F/m`, `m=F/a` is one node
  (`newton_second_law`) with "solving for" metadata and denominator conditions —
  not three nodes.
- **Every formula carries:** every symbol named/typed/unit-labelled; dimensions
  of both sides; one exactness label (`definition`, `mathematical_identity`,
  `fundamental_law`, `derived_exact`, `constitutive_model`, `empirical_relation`,
  `approximation`, `asymptotic_relation`, `heuristic`, `deprecated`); validity
  regime; preconditions (nonzero denominators, differentiability, equilibrium);
  ≥1 limiting/special-case check; ≥1 authoritative source.
- **Dimensional consistency is necessary, not sufficient** — record it that way.
  A dimensionally sound formula can still have the wrong constant, sign,
  direction, regime, or a missing term.
- **Never claim universality for a model-specific relation.** `PV=nRT` is a
  constitutive model; `sinθ≈θ` is an approximation (radians); label them so.
- **Cycles are a modeling defect to resolve, not bypass.** Never silently delete
  an edge — reclassify it and record the decision.
- **A valid `tsort` order is not physical or pedagogical truth.** Independent
  nodes may land anywhere; do not read tie-order as necessity.

## Workflow

The pipeline, each stage handed to the tool skill that owns it:

    define scope → choose primitives → formalize nodes → derive prerequisite edges
    → validate graph → tsort → author condensed entries
    → cross-check units/assumptions/limits → build views → publish & maintain

### 1. Define scope (`scope.md`)

Write the release boundary explicitly (see Principles). Refuse "all useful
formulas in physics" — pin an initial release such as "units, dimensions,
vectors, calculus prerequisites; Newtonian point-particle mechanics; work,
energy, momentum, angular momentum; gravitation and SHM. Excluded: GR, QFT, stat
mech beyond elementary ideal gas, numerical methods, relativistic corrections."

### 2. Lay out the package

Create the directory skeleton from
[`references/package-layout.md`](references/package-layout.md): `nodes/`,
`edges/`, `formulas/`, `indexes/`, `validation/`, `sources/`, `build/`, plus
`conventions.md`, `symbols.md`, `units.md`. That reference also gives the node
registry TSV schema, the per-node detail-page template, and the per-formula YAML
schema — do not invent your own.

### 3. Choose primitive/root nodes

Pick a controlled root set appropriate to the scope (`SI_units`,
`inertial_frame`, `time`, `length`, `mass`, `real_numbers`, `derivative`,
`vector`, …). For each, document *why it is primitive for this release*, its
operational meaning, what background is assumed, and which alternative
foundations are intentionally omitted. A term is not primitive merely because it
is hard to define.

### 4. Formalize nodes

For every concept/law/formula create a registry row and a detail page with
symbols, assumptions, dimensions, derivation status, limiting cases, common
misuse, related nodes, sources. Do not mark a node `reviewed` until every
applicable validation in step 7 passes.

When importing from long source material (a textbook chapter, lecture notes),
**use the `csplit` skill** to break it into reviewable sections first, into an
isolated directory, with its reconstruction check — never edit the syntactically
connected original.

### 5. Derive prerequisite edges — delegate to the `tsort` skill

This is the heart of the work and the `tsort` skill governs it. Follow that
skill's discipline exactly:

- Maintain `edges/dependencies.plan` with a `#` comment stating the evidence for
  every edge, then strip comments to `edges/dependencies.edges`
  (`grep -Ev '^[[:space:]]*(#|$)'`).
- Apply the verbal test to each edge: "Can I truthfully say **A must be
  understood/introduced before B can be correctly used**?" If not, it is not a
  `tsort` edge.
- Store the richer relations (`generalizes`, `special_case_of`, `equivalent_to`,
  `approximates`, `supersedes_in_regime`, `historically_precedes`,
  `commonly_confused_with`, `tested_by`) in **separate** files under `edges/` —
  never as `tsort` edges. See
  [`references/relations.md`](references/relations.md).
- Only `requires` / `defines` / `derives_from` / `valid_when` become `tsort`
  edges.
- Every edge endpoint must already exist in `nodes/nodes.tsv` (the `tsort` skill's
  "never encode an edge until both endpoints are defined").

### 6. Validate the graph, then `tsort`

Run the checks from [`references/package-layout.md`](references/package-layout.md)
`validation/graph-check.sh`: exactly two fields per edge line, no self-edges,
every edge node present in the registry, deterministic `sort -u`. Then run
`tsort` **with the BSD-safe cycle detection from the `tsort` skill** (check
stderr, not just exit status — macOS `tsort` exits 0 on a cycle). Verify every
supplied edge is respected by the emitted order.

On a cycle, invoke the `tsort` skill's cycle-resolution protocol: stop, preserve
diagnostics, translate every cycle edge to plain language, classify each
(true prerequisite / operational-measurement / derivation / explanatory /
equivalence / historical / duplicate), remove non-prerequisites to metadata, and
if it is a genuine foundational choice, declare one concept primitive for this
scope and record it in `edges/cycles.md` and `conventions.md`. Typical physics
cycles: force↔acceleration (resolve: acceleration is kinematic from position/time;
force is dynamical via `F=ma`), mass↔force, energy↔work.

### 7. Author entries and cross-check — delegate to `bc` and `lean`

- **Dimensional and special-case arithmetic → `bc` skill.** Check
  `[LHS] = [RHS]` on the dimension exponents, and evaluate limiting cases
  numerically (`v=0 ⇒ K=0`; `γ→1` as `v/c→0`; leading correction terms). Use the
  `bc` skill's explicit-rounding / precision discipline; record the check status
  in the formula entry.
- **Algebraic derivations and identities → `lean` skill.** When a node's
  `derivation status` claims "derived exactly from X", and the step is an
  algebraic or calculus identity (e.g. integrating `F=ma` at constant `a` to the
  kinematics set, `sin²+cos²=1`, the work-energy theorem for constant mass),
  state and check it with Lean. Record what the kernel verified versus what
  remains assumed (regime, physical premises) — the `lean` skill's scope
  discipline. Do not claim Lean validated the *physics*, only the math step.
- Every symbol audited: one meaning, type, unit, scope. Sign/coordinate/Fourier/
  thermodynamic-sign conventions explicit and linked to a convention node.

### 8. Build discovery views

`tsort` order is one view, not the interface. Generate from the graph:
topological order, topic index, symbol index, assumption index, formula index,
reverse-dependency index, minimal-prerequisite paths for each core formula,
generalization map, common-misuse index, unit/dimension index.

- **Symbol index and keyword-in-context navigation → `ptx` skill.** Build a KWIC
  index over the curated formula corpus (`-W '[A-Za-z0-9_]+'` to keep identifiers
  atomic, `-A` for `file:line:` provenance) so an agent can find every formula
  using `m`, `E`, `q`, `T`. Confirm every lead with `rg` per the `ptx` skill —
  the index is a discovery aid, not authority.
- Minimal paths come from the **graph structure**, not the flat `tsort` list —
  `tsort` gives a valid order, not the shortest or most pedagogical route.

### 9. Small, safe edits to registry / plan files — use the `ed` skill

The node TSV, `dependencies.plan`, and YAML formula files are structurally
sensitive. For minimal line-oriented changes use the `ed` skill's
inspect → target → change → verify → validate → write transaction rather than
rewriting files.

### 10. Publish and maintain

Version every release; never overwrite a reviewed release without a changelog.
Adding a formula: clarify class/domain/canonical form/convention/assumptions/
dimensions/sources; **search first** (`rg` over `nodes/ formulas/ indexes/`) to
avoid duplicating a rearrangement or synonym; add node + detail page; add only
direct prerequisite edges with evidence; re-run steps 6–8. Changing a
foundational node: pull its reverse dependencies first, categorize the change,
make the narrowest edit, rebuild, re-audit, changelog. Changing a convention
node (e.g. thermodynamic sign convention) is a broad semantic change — revalidate
all downstream formulas.

## Quality gates

A release is publishable only if: every `tsort` edge refers to a registered
node; the prerequisite graph is acyclic (stderr-checked); every formula has a
status label, defines every symbol, has dimensional metadata, a validity regime,
and ≥1 authoritative source; every approximation names its limit/small parameter;
every constitutive relation names its model scope; every convention-sensitive
formula links to its convention node; every core formula has a minimal
prerequisite path; root choices are documented; no model-specific relation is
labelled a universal law; the output explicitly distinguishes topological order
from conceptual/physical priority.

## References

- [`references/package-layout.md`](references/package-layout.md) — directory
  skeleton, node registry TSV schema, node detail-page template, formula YAML
  schema, `build/build-tree.sh`, `validation/graph-check.sh`.
- [`references/relations.md`](references/relations.md) — the full relation-type
  table, which relations become `tsort` edges, how to store the rest, cycle
  patterns and resolutions, approximation ladders, cross-domain bridges.
- [`references/skill-composition.md`](references/skill-composition.md) — which
  companion skill owns each stage, exact hand-off points, and what each returns.
- [`references/worked-slice.md`](references/worked-slice.md) — a complete small
  slice (`kinetic_energy` and its prerequisites) through every stage.
- [`../physics-newtonian/`](../physics-newtonian/SKILL.md) — a full capsule built
  with this method (Release 0.1, Newtonian mechanics, 58-node graph); its
  `README.md` records the end-to-end method verification.
- [`../physics-thermoacoustics/`](../physics-thermoacoustics/SKILL.md) — a larger
  capsule (Release 0.1, linear thermoacoustics, 104-node graph, complex fields,
  `[M L T Θ]` basis); shows the method scaling to a deeper domain with `draft`
  nodes for source-pending coefficients.

## Completion report

Report: declared scope and exclusions; node / edge / root-node counts;
`tsort` result and that the graph is acyclic (how the cycle check was done);
domains and core-formula counts by classification; validation performed
(edge endpoints exist, every edge checked against the order, dimensional checks
via `bc`, derivations checked via `lean`, sources linked); any cycles found and
how resolved; primitive/convention choices adopted; the generated artifacts
(`indexes/`, `validation/`); and the standing limitations — this is a curated
dependency graph not a complete account of physics, a valid `tsort` order
confirms only the encoded constraints, dimensional consistency is not physical
correctness, and every formula's validity stays conditional on its stated theory,
regime, convention, and source.
