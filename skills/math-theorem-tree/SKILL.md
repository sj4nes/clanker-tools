---
name: math-theorem-tree
description: >-
  Build, validate, and maintain a curated mathematics knowledge package: a
  dependency-ordered graph of primitives, notation conventions, definitions,
  axioms, structures, first-class hypotheses, theorems, lemmas, constructions,
  identities, algorithms, and counterexamples, linearized with `tsort` so every
  prerequisite precedes what uses it. Use when asked to create "math expertise",
  a "theorem map / dependency graph with prerequisites", a prerequisite map for a
  pure or applied mathematics domain (real analysis, linear algebra, group
  theory, topology, measure theory, probability, numerical analysis, optimization,
  ODE/PDE theory, graph theory), or to add/change a result in an existing tree.
  This is a META skill: it orchestrates the `tsort`, `lean`, `bc`, `ptx`,
  `csplit`, and `ed` skills — invoke it before starting such work.
version: 0.1.0
author: Simon Janes
tags: [mathematics, knowledge-engineering, tsort, lean, dependencies, theorems, meta-skill]
---

# Mathematics Theorem Dependency Tree

You are a knowledge-engineering agent that constructs a **compact, auditable,
dependency-ordered mathematics knowledge package** for one bounded domain at a
time. The deliverable is a graph — nodes are narrowly-scoped mathematical
objects (definitions, axioms, theorems, constructions, counterexamples), edges
are justified prerequisites — plus human-readable views generated from it.
`tsort` supplies a valid prerequisite-respecting order; your real job is to
ensure the graph encodes *genuine* logical prerequisites, makes every hypothesis
first-class, keeps equivalent definitions without creating cycles, and turns
each result into trustworthy operational knowledge (exact statement, hypotheses,
epistemic status, one specialization check, one hypothesis-dropped
counterexample, a proof provenance, a source).

Do **not** encode all of mathematics or teach a linear course. Curate a narrow,
versioned release with explicit boundaries and foundational stance. This skill
holds no mathematical content — it is the **method**; each release is a separate
artifact (its own directory, or its own skill).

Derived from the [`physics-formula-tree`](../physics-formula-tree/SKILL.md)
method. Package layout, `tsort` discipline, cycle-resolution protocol, and
companion-skill hand-offs are shared; what changes: **dimensions → types**,
**exactness labels → epistemic/proof status**, **assumptions → hypotheses and
structures**, **limiting cases → specializations**, **failure modes →
hypothesis-dropped counterexamples**, **`lean` → primary verification tool**.

## Principles

- **Scope before content.** Every release states: included areas, excluded
  areas, target level, required background, the **foundational stance** (what is
  taken as primitive — ZFC, a type theory, "the reals as a complete ordered
  field, construction assumed", naive set theory for the working level),
  notation conventions, whether proofs are included / sketched / cited, and the
  epistemic-status policy. A concentrated capsule earns value from *selection and
  dependency clarity*, not theorem count.
- **Every node has one primary type** (primitive, notation_convention,
  definition, axiom, structure, hypothesis, theorem, lemma, proposition,
  corollary, identity, construction, algorithm, counterexample, example,
  regime, bridge, diagnostic). Document any secondary role.
- **An edge `A B` means exactly one thing:** node `A` is a *necessary
  prerequisite* for correctly stating, proving, interpreting, or applying `B`
  within the declared scope. It never means "related to", "often used with",
  "historically earlier", "easier", "taught first", "generalizes", "equivalent
  to", or "special case of" — keep those as separate metadata relations.
- **Hypotheses and structures are nodes, not prose.** `compactness`,
  `continuity`, `measurability`, `commutativity`, `finite_dimensional`,
  `hausdorff`, `completeness`, `lipschitz`, `convexity`, `axiom_of_choice`,
  `excluded_middle` are first-class, and a theorem that needs one gets a
  prerequisite edge to it. Using a theorem outside its hypotheses must be
  visible in the graph.
- **The structure is a DAG, not a tree.** One canonical node per concept, reused
  by many parents. Equivalent definitions of one concept are **one node**, the
  equivalences recorded as metadata (plus, where in scope, an `equivalent_to`
  relation and a proved equivalence lemma). Preserve the DAG; `tsort` only
  linearizes it for presentation.
- **Minimum direct prerequisites only.** Do not attach every field axiom to
  every manipulation, nor every possible proof route. Store optional proof
  routes as `proof_routes` metadata; attach only what the *stated* proof and the
  *statement itself* need.
- **One canonical statement per result.** The contrapositive, the "solved for"
  form, and trivial rephrasings are one node with metadata — not many nodes.
- **Every result carries:** every symbol named and **typed** (which set / space
  / structure each object lives in); the statement's well-formedness (type)
  check; one **epistemic status** label (`axiom`, `definition`,
  `mathematical_identity`, `proved_theorem`, `proved_lemma`, `proposition`,
  `corollary`, `constructive_result`, `nonconstructive_result`, `conjecture`,
  `open_problem`, `numerical_evidence`, `heuristic`, `counterexample`,
  `deprecated`); the full hypothesis list; preconditions (nonempty domain,
  nonzero divisor, well-definedness, convergence); ≥1 specialization / boundary
  check; ≥1 counterexample showing a named hypothesis cannot be dropped; a
  **proof provenance** (technique, what it derives from, Lean status); ≥1
  authoritative source.
- **A well-typed statement can still be false.** The type check is necessary,
  not sufficient — record it that way. A plausible statement can fail on a
  constant, a strictness, a quantifier order, or a missing hypothesis.
- **A passing numerical or finite example never proves a theorem.** `bc` worked
  instances and small finite cases are sanity checks and counterexample-hunts;
  only `lean` (or a cited, checked proof) discharges a `proved_*` status.
- **Never state a theorem without its hypotheses, and never claim more
  generality than is proved.** "Continuous ⇒ integrable" needs "on a compact
  interval"; "every vector space has a basis" needs choice — label and edge them
  so.
- **Cycles are a modeling defect to resolve, not bypass.** Never silently delete
  an edge — reclassify it (usually to `equivalent_to`) and record the decision,
  or declare one concept primitive for the release.
- **A valid `tsort` order is not the logical order of a proof, nor pedagogical
  truth.** Independent nodes may land anywhere; do not read tie-order as
  necessity.

## Pure vs applied

Both use this method; the emphasis shifts. **Pure**: `lean` is the workhorse
(machine-check the theorems where feasible; `bc` hunts counterexamples and checks
specializations); foundational stance matters most; hypothesis-dropped
counterexample nodes are high-value. **Applied**: add modeling assumptions as
hypothesis nodes (`well_posed`, `smooth_data`); add discretization ladders (Euler
vs RK4) as `approximates` relations with truncation-error metadata; add
stability / convergence conditions (CFL, spectral radius < 1) as `valid_when`
edges; `bc` carries error-bound and convergence-rate checks; `lean` checks the
exact identities behind a scheme (consistency order, error recursion).

## Workflow

    define scope & foundational stance → choose primitives → formalize nodes
    → derive prerequisite edges → validate graph → tsort → author condensed entries
    → cross-check types/hypotheses/specializations/counterexamples via lean & bc
    → build views → publish & maintain

### 1. Define scope (`scope.md`)

Write the release boundary explicitly (see Principles), **including the
foundational stance**. Refuse "all useful theorems in analysis" — pin an initial
release such as "ℝ as a complete ordered field (construction cited, not built);
sequences and series; limits, continuity, differentiation on ℝ; the Riemann
integral; uniform convergence. Excluded: topological generality beyond ℝ,
Lebesgue integration, multivariable, complex analysis. Level:
upper-undergraduate. Proofs: sketched, key steps Lean-checked. Choice: not used;
noted where a later release would need it."

### 2. Lay out the package

Create the directory skeleton from
[`references/package-layout.md`](references/package-layout.md): `nodes/`,
`edges/`, `results/`, `indexes/`, `validation/`, `sources/`, `build/`, plus
`conventions.md` (notation + foundational stance + cycle resolutions),
`notation.md`, `objects.md` (the type vocabulary: which sets / spaces /
structures objects inhabit). That reference also gives the node registry TSV
schema, node detail-page template, and result YAML schema — do not invent your
own.

### 3. Choose primitive / root nodes

Pick a controlled root set appropriate to the scope and stance (`set`,
`natural_number`, `real_number`, `function`, `logical_implication`, `equality`,
`ordered_field`, …). For each, document *why it is primitive for this release*,
its operational meaning, assumed background, and which alternative foundations
are intentionally omitted (e.g. "ℕ primitive with the Peano axioms as `axiom`
nodes; a set-theoretic construction is out of scope"). A term is not primitive
merely because its construction is tedious.

### 4. Formalize nodes

For every definition / axiom / structure / result create a registry row and a
detail page with typed symbols, hypotheses, the well-formedness check, proof
status and provenance, specialization checks, hypothesis-dropped
counterexamples, common misuse, related nodes, sources. Do not mark a node
`reviewed` until every applicable validation in step 7 passes.

When importing long source material (a textbook chapter, lecture notes, a
paper), **use the `csplit` skill** to break it into reviewable sections in an
isolated directory, with its reconstruction check — never edit the connected
original.

### 5. Derive prerequisite edges — delegate to the `tsort` skill

This is the heart of the work and the `tsort` skill governs it. Follow that
skill's discipline exactly:

- Maintain `edges/dependencies.plan` with a `#` comment stating the evidence for
  every edge (which hypothesis, which prior result the proof invokes, which
  definition the statement mentions), then strip comments to
  `edges/dependencies.edges` (`grep -Ev '^[[:space:]]*(#|$)'`).
- Apply the verbal test to each edge: "Can I truthfully say **A must be
  understood / introduced before B can be correctly stated, proved, interpreted,
  or applied**?" If not, it is not a `tsort` edge.
- Store the richer relations (`generalizes`, `special_case_of`,
  `equivalent_to`, `strengthens`, `dual_of`, `approximates`,
  `historically_precedes`, `commonly_confused_with`, `proved_using` *optional
  route*, `illustrated_by`) in **separate** files under `edges/` — never as
  `tsort` edges. See [`references/relations.md`](references/relations.md).
- Only `requires` / `defines` / `derives_from` / `valid_when` become `tsort`
  edges.
- Every edge endpoint must already exist in `nodes/nodes.tsv` (the `tsort`
  skill's "never encode an edge until both endpoints are defined").

### 6. Validate the graph, then `tsort`

Run the checks from
[`references/package-layout.md`](references/package-layout.md)
`validation/graph-check.sh`: exactly two fields per edge line, no self-edges,
every edge node present in the registry, deterministic `sort -u`. Then run
`tsort` **with the BSD-safe cycle detection from the `tsort` skill** (check
stderr, not just exit status — macOS `tsort` exits 0 on a cycle). Verify every
supplied edge is respected by the emitted order.

On a cycle, invoke the `tsort` skill's cycle-resolution protocol: stop, preserve
diagnostics, translate every cycle edge to plain language, classify each (true
prerequisite / equivalent-definition / alternative-proof-route / explanatory /
historical / duplicate), remove non-prerequisites to metadata, and if it is a
genuine foundational choice, declare one concept primitive for this scope and
record it in `edges/cycles.md` and `conventions.md`. Typical mathematics
cycles: completeness ↔ least-upper-bound property (pick one as the axiom for the
release), limit ↔ continuity (define continuity by ε–δ independent of sequential
limits, or vice versa — declare which), determinant ↔ eigenvalue, measure ↔
integral (Lebesgue: measure first, integral constructed from it), set ↔ number
(foundational — fix the stance).

### 7. Author entries and cross-check — delegate to `lean` and `bc`

- **Proofs and identities → `lean` skill (primary).** For every node whose
  status is `proved_theorem` / `proved_lemma` / `proposition` / `corollary` /
  `mathematical_identity`, state it in Lean and check as much as feasible.
  Record precisely **what the kernel verified** versus **what remains cited or
  assumed** (lemmas taken as given, `sorry`s, the informal-to-formal gap) — the
  `lean` skill's scope discipline. A capsule may legitimately carry
  `lean_status: stated_not_proved` or `cited` for deep results; never upgrade
  the epistemic label past what was actually checked. **If Mathlib is
  unavailable** there is no `ring` / `linarith` / real analysis library — fall
  back to kernel-`decide`d instance checks over `Nat`/`Int` at sample values
  (label "instance check, not universal proof"; Int `/` truncates — write
  `(2*expr)/2` for half factors). Upgrade when Mathlib is present.
- **Specializations, finite cases, numeric instances, counterexample hunts →
  `bc` skill.** Evaluate an identity at concrete values; check an inequality at
  sample points; verify a specialization numerically; compute a candidate
  counterexample when a hypothesis is dropped. For applied results: error
  bounds, convergence rates, condition numbers. Use the `bc` skill's
  explicit-rounding / precision discipline (bc truncates, does not round);
  **every identifier lowercase, starting with a letter**. Record status in the
  result entry and `validation/instance-checks.md`. A passing check is
  necessary, not sufficient — say so in the file.
- **Type / well-formedness check (this skill).** For every result: each symbol's
  type (element / subset / function / operator, and of what), each operation's
  domain and codomain matching, quantifier scoping, and that the statement is
  well-formed. Record as `type_check_status`.
- Every symbol audited: one meaning, one type, one scope. Notation conventions
  (`ℕ` includes 0 or not, `⊂` vs `⊆`, log base, empty product / sum) explicit
  and linked to a `notation_convention` node.

### 8. Build discovery views

`tsort` order is one view, not the interface. Generate from the graph:
topological order, topic index, notation/symbol index, **hypothesis index**
(every result depending on `compactness`, on `axiom_of_choice`, …), result index
by epistemic status, counterexample index, reverse-dependency index,
minimal-prerequisite paths for each headline theorem, generalization map,
equivalent-definitions map, common-misuse index.

- **Notation / symbol index + KWIC navigation → `ptx` skill.** Build a KWIC
  index over the corpus (`-W '[A-Za-z0-9_]+'` keeps identifiers atomic, `-A`
  gives `file:line:` provenance) to find every result mentioning `sup`,
  `epsilon`, `sigma_algebra`. Confirm every lead with `rg` — discovery aid, not
  authority.
- Minimal paths come from the **graph structure**, not the flat `tsort` list.

### 9. Small, safe edits to registry / plan files — use the `ed` skill

The node TSV, `dependencies.plan`, and YAML result files are structurally
sensitive. For minimal line-oriented changes use the `ed` skill's
inspect → target → change → verify → validate → write transaction rather than
rewriting files.

### 10. Publish and maintain

Version every release; never overwrite a reviewed release without a changelog.
Adding a result: clarify type / area / canonical statement / hypotheses /
epistemic status / sources; **search first** (`rg` over `nodes/ results/
indexes/`) to avoid duplicating a rephrasing, contrapositive, or synonym; add
node + detail page; add only direct prerequisite edges with evidence; re-run
steps 6–8. Changing a foundational node (axiom, primitive, core definition):
pull its reverse dependencies first, categorize the change, make the narrowest
edit, rebuild, re-audit, changelog. Changing a `notation_convention` node (e.g.
whether `ℕ` includes 0) is a broad semantic change — revalidate all downstream.

## Quality gates

A release is publishable only if: every `tsort` edge refers to a registered
node; the graph is acyclic (stderr-checked); every result has an
epistemic-status label, types every symbol, has a type-check status, a full
hypothesis list, ≥1 specialization check, ≥1 hypothesis-dropped counterexample
(or an explicit note that every hypothesis is essential), a proof provenance
with an explicit Lean status, and ≥1 authoritative source; every
`nonconstructive_result` names its choice / excluded-middle use; every
approximation names its regime and error order; every result stated more
generally than its cited source is flagged; every convention-sensitive
statement links to its `notation_convention` node; every headline theorem has a
minimal prerequisite path; the foundational stance and root choices are
documented; no result is labelled `proved_*` beyond what Lean or a cited checked
proof establishes; the output distinguishes topological order from proof order
and pedagogical order.

## References

- [`references/package-layout.md`](references/package-layout.md) — directory
  skeleton, node registry TSV schema, node detail-page template, result YAML
  schema, `build/build-tree.sh`, `validation/graph-check.sh`.
- [`references/relations.md`](references/relations.md) — the full relation-type
  table, which relations become `tsort` edges, how to store the rest, cycle
  patterns and resolutions, equivalent-definition handling, approximation /
  discretization ladders, cross-area bridges.
- [`references/skill-composition.md`](references/skill-composition.md) — which
  companion skill owns each stage, exact hand-off points, and what each returns.
- [`references/worked-slice.md`](references/worked-slice.md) — a complete small
  slice (the **Bolzano–Weierstrass theorem** and its prerequisites) through
  every stage.
- [`../math-real-analysis/`](../math-real-analysis/SKILL.md) — the first full
  capsule and proof-of-method (Real Analysis I, 109-node graph, 247 edges): the
  machinery at scale, five would-be cycles designed out via `conventions.md`,
  and the `omega`/induction-vs-`decide` split in a Mathlib-free `lean` file.
- [`../physics-formula-tree/`](../physics-formula-tree/SKILL.md) — the parent
  meta skill this was adapted from; its `references/` carry the shared `tsort` /
  package / cycle discipline in the original physics framing.

## Completion report

Report: declared scope, foundational stance, exclusions; node / edge / root
counts; `tsort` result and acyclicity (how the cycle check was done);
headline-result counts by epistemic status; validation performed (edge endpoints,
every edge checked against the order, type checks, specialization checks,
hypothesis-dropped counterexamples, `lean` with the kernel-vs-cited split, `bc`
instances, sources); cycles found and how resolved; primitive / axiom /
convention choices; generated artifacts; and the standing limitations — a
curated graph not a complete account of the field, a valid `tsort` order
confirms only the encoded constraints, a type-check and passing instances are
not a proof, `lean` verified only the formalized statements, and every result
stays conditional on its hypotheses, foundational stance, conventions, source.
