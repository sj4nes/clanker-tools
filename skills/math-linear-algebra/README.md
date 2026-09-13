# math-linear-algebra

Linear algebra as a curated, dependency-ordered knowledge capsule.
**Release 0.1** — 198 nodes, 599 edges, acyclic, 0 isolated.

Built with [`math-theorem-tree`](../math-theorem-tree/SKILL.md). Sits **below
`math-statistics`** (whose `linear_algebra_background` node it discharges) and
beside `math-real-analysis`.

Start at [`SKILL.md`](SKILL.md).

## Layout

| path | what |
|---|---|
| `scope.md` | included / excluded, level, foundational stance, the two per-result tags |
| `conventions.md` | notation, `lean_status` vocabulary, the five cycle resolutions, cross-capsule stance |
| `notation.md` | every symbol: one meaning, one type, one scope |
| `objects.md` | the type vocabulary; the shape discipline; the four genuine well-definedness obligations |
| `nodes/nodes.tsv` | the 198-node registry |
| `nodes/<id>.md` | readable detail page per node |
| `results/<id>.yaml` | structured entry per node |
| `edges/dependencies.plan` | the graph, one evidence comment per block |
| `edges/cycles.md` | five would-be cycles, classified and resolved |
| `edges/relations.tsv` | 37 non-prerequisite relations |
| `edges/cross-capsule.md` | the `math-statistics` discharge table |
| `indexes/` | field-scope, hypothesis, status, counterexample, symbol KWIC, prerequisite paths, reverse deps |
| `validation/proof-checks.lean` | Mathlib-free Lean; exit 0, no `sorry`, no warnings |
| `validation/proof-checks.md` | what the kernel verified vs what stays cited |
| `validation/instance-checks.bc` | 12 `bc` sections, all passing |
| `build/all.sh` | full build; fails on any check failure |

## Verification

| check | how | state |
|---|---|---|
| graph | `validation/graph-check.sh` — 2 fields/line, no self-edges, endpoints registered | ok (599 edges, 198 nodes) |
| acyclicity | `tsort` with the **BSD stderr guard** (macOS `tsort` exits 0 on a cycle) + every edge re-checked against the emitted order | ok, 0 isolated |
| YAML ↔ graph | `build/check-consistency.py` — deps match edges, sources known, relations valid | ok |
| Lean refs | `build/check-lean-refs.py` — every `LinAlg.*` named actually exists; no `cited` node names one | ok (55 refs / 87 declarations) |
| proofs | `lean validation/proof-checks.lean` | exit 0, no `sorry`/`axiom`/warnings |
| instances | `bc -l validation/instance-checks.bc`, **output inspected** (bc's `quit` always exits 0) | 12/12 sections pass |

The `bc` harness was negative-contrast tested: corrupting one check makes it
print a `FAIL` line and makes `build/all.sh` exit 1.

## The two tags

**`field_scope`** — which field a result actually needs
(`any_field` / `char_not_2` / `ordered_field` / `real_or_complex` /
`algebraically_closed`). See `indexes/field-scope-index.md`.

**`choice_grade`** — 197 nodes `choice_free`; `basis_existence_general` is
`needs_full_AC` and is the only one.

## Reading warnings

A valid `tsort` order is **not** proof order and **not** teaching order.
`spectral_theorem_symmetric` lands before `characteristic_polynomial` because
this release proves it by the Rayleigh/compactness route, which never mentions
the characteristic polynomial — that is a design decision, recorded in
`edges/cycles.md`, not an error. Likewise `determinant` lands before `basis`
because the determinant genuinely needs no basis theory.
