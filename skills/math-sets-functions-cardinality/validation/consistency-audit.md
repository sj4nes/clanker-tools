# Consistency audit — Release 0.1

Run everything: `sh build/all.sh`

## Graph (`build/build-tree.sh`)

- **106** registered nodes, **263** prerequisite edges after `sort -u`.
- Every edge line has exactly 2 fields; no self-edges (`graph-check.sh`).
- Every edge endpoint exists in `nodes/nodes.tsv`
  (`build/unknown-edge-nodes.txt` empty).
- `tsort`: **empty stderr**, 106-node order emitted → **acyclic** (BSD-safe
  check).
- Every one of the 263 edges satisfied by `indexes/tsort-order.txt`.
- **0 isolated nodes.**
- **1 root node**: `proposition_logic`. Everything else is derived, except the
  twelve assumed `axiom`-typed nodes (the nine ZF axioms + AC + DC + CC), each
  of which *has* a prerequisite (`predicate_logic` / `axiom_extensionality` /
  `axiom_of_choice`) so is not a root. The capsule bottoms out at propositional
  logic.

## Nodes by type

| type | count |
|---|---|
| definition | 52 |
| theorem | 24 |
| axiom | 12 |
| proposition | 6 |
| principle_law | 3 |
| primitive | 3 |
| construction | 2 |
| structure | 2 |
| regime | 1 |
| notation_convention | 1 |
| **total** | **106** |

Areas: cardinality 21, functions 19, sets 15, axioms 14, orders 11,
equivalence 8, logic 5, relations 5, naturals 4, ordinals 4. (Definition-heavy,
as a vocabulary-building foundational capsule should be.)

## Cycles

None in the committed graph. Seven would-be cycles designed out
(`edges/cycles.md`): AC ⟺ Zorn ⟺ well-ordering ⟺ comparability; `cardinal_le`
⟺ CSB; ordinal ⟺ well-order; ℕ ⟺ set; transfinite recursion ⟺ ordinal
arithmetic; power set ⟺ function space; the quotient before the relation is
verified an equivalence. The completeness-style node here is
`continuum_hypothesis`, resolved a third way: `independent_of_ZFC`.

## Type / well-formedness checks (`validation/type-checks.md`)

14 headline nodes, all **well_formed**. Recurring obligations forced into the
entries: (1) every `{x : φ}` is bounded or Replacement-justified; (2) `⋂` over a
family carries `I ≠ ∅`; (3) every "function" is total, codomain fixed;
(4) quantifier order is recorded; (5) **every use of choice is graded and
edged** (`choice_free` / `needs_countable_choice` / `needs_full_AC`), with
CSB / Cantor / Hartogs / finite-pigeonhole explicitly flagged choice-free.

## Lean proof-core checks (`validation/proof-checks.lean`, `.md`)

- Lean **4.33.1, no Mathlib**. `lean validation/proof-checks.lean` → **exit 0**,
  no `sorry`, 11 checked items.
- **Genuine universal proofs** (in plain Lean, sets as `X → Prop`): the
  **preimage algebra** (`f⁻¹` commutes with `⋃`, `⋂`, complement — `rfl`), the
  image laws (`f[A∪B] = f[A]∪f[B]` by `funext`+`propext`; `f[A∩B] ⊆` only),
  composition preserving injectivity/surjectivity, classical quantifier negation
  (`Classical.not_forall`, `not_exists`), the equivalence-class identity
  `[x] = [y] ⟺ x ∼ y`, and **Cantor's diagonal theorem** (2 lines, no Mathlib).
- **Instance check (`decide`):** pigeonhole for `Fin 5 → Fin 4`, function
  spelled out (`Fintype` is Mathlib).
- No epistemic label rests on this file; `lean_status` per YAML is `core` /
  `instance` / `cited` / `none`.

## bc instance checks (`validation/instance-checks.bc`)

`bc -q -l` → clean run (`build/instance-checks.out`). Covers: the Cantor pairing
tabulated as a bijection `ω×ω → ω` and its inverse (`ℚ⁺` enumeration); `ℤ`
countable by interleaving; the diagonal argument executed on a 5-row list of
binary sequences; `|𝒫(X)| = 2^{|X|}`; Cantor's theorem worked for `X = {0,1,2,3}`
with the missing set `D` exhibited; `ℵ₀ + ℵ₀ = ℵ₀` by interleaving;
pigeonhole 5→4.

`bc` note: `k % 2` at `scale = 0` is honest integer parity and is used
deliberately for the `ℤ`-interleaving (the `scale = 20` fractional-remainder
trap from `math-number-systems` is avoided by keeping the whole file at
`scale = 0`).

## Coverage of the deliverable

- `results/*.yaml`: 15 headline nodes. Remaining nodes covered by
  `nodes/nodes.tsv` + `edges/dependencies.plan` + the indexes.
- `nodes/*.md` detail pages: 3 exemplars.
- Every headline node has a type check, ≥1 specialization, ≥1
  hypothesis-dropped counterexample, a proof provenance with `lean_status` and a
  `choice_grade`, and ≥1 source.

## The bridge downstream

`conventions.md` records it. This capsule discharges the primitives/citations of
`math-number-systems`: `set`, `function`, `relation`, `equivalence_relation`,
`quotient_set`, `cartesian_product`, `well_defined_on_quotient`,
`axiom_of_choice`, `countable_choice` are all **nodes here**, and
`peano_holds_in_omega` + `recursion_theorem` provide the `peano_axioms` /
`recursion_theorem` that `math-number-systems` cites to Enderton. It also
provides `preimage_algebra` — the node `math-real-analysis`'s continuity and
compactness proofs actually stand on. A Release 0.2 of either capsule would edge
into this one.

## Standing limitations

A curated dependency graph, not a full development. The nine ZF axioms + Choice
are the floor; their consistency is not addressed (Gödel's second incompleteness
theorem is out of scope). The logic floor (`proposition_logic`,
`predicate_logic`) is used, not developed — that is a future
`math-logic-and-proof`. Zorn's lemma, the ordinal spine,
Cantor–Schröder–Bernstein, and the infinite-cardinal arithmetic are set-level
and not formalised in this Mathlib-free environment — they rest on [enderton],
[jech_set_theory], [halmos]. `continuum_hypothesis` is genuinely independent of
ZFC; the proofs (L, forcing) are cited only. A passing type check and passing
`bc`/`decide` instances are not proofs.
