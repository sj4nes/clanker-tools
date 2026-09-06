# true_false_constants

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
- `⊥` (**falsum**, bottom) — a primitive wff constant. Semantically `⟦⊥⟧_v = F`
  for every `v`; proof-theoretically it is the premise of `⊥`-elimination
  (`explosion_ex_falso`) and the target of `¬`-elimination.
- `⊤` (**verum**, top) — defined `⊤ := (p → p)` for a fixed atom `p` (or
  primitive with `⟦⊤⟧_v = T`). Any tautology serves.
- `¬φ` is often taken as an abbreviation for `φ → ⊥`.

## Symbols
- `⊥`, `⊤`: the constant wffs.

## Prerequisites (tsort edges into this node)
`wff_syntax`.

## Content
The `0`-ary connectives / lattice bounds. In the Lindenbaum–Tarski Boolean
algebra (`logical_equivalence`), `[⊥]` is the bottom element and `[⊤]` the top;
they are the identities for `∨` and `∧` respectively (`⊥ ∨ φ ≡ φ`, `⊤ ∧ φ ≡ φ`)
and the annihilators for the other (`⊤ ∨ φ ≡ ⊤`, `⊥ ∧ φ ≡ ⊥`).
Choosing `⊥` primitive (rather than `⊤`) is standard because `¬`, `→`, and the
`⊥E`/`¬E` rules are stated with it, and it distinguishes **minimal** logic
(no `⊥E`), **intuitionistic** (with `⊥E`), and **classical** (with `RAA`).

## Constructive grade
`intuitionistic` — the constants and their rules (`⊥E` aside — that is
`explosion_ex_falso`, still intuitionistic). `⊤` is a theorem of even minimal
logic.

## Lean status
`lean_status: core` (`⊥`). `Wff.fls` is a constructor in
`validation/proof-checks.lean`; `eval v fls = false` by `rfl`; the `falseE`
constructor of `Deriv` is `⊥E`; `⊤` would be `Wff.impl (atom 0) (atom 0)` with
`eval v ⊤ = true` by `cases`.

## Type / well-formedness check
`well_formed`. If `⊤` is *defined* as `p → p`, its value is provably constant
(`eval` computation); if primitive, its clause is added to
`truth_value_recursion`. `¬φ` as `φ → ⊥` must be consistent with any primitive
`¬` clause. `empty ∨ = ⊥`, `empty ∧ = ⊤` (`notation.md`) — the empty
disjunction/conjunction conventions.

## Specialization / boundary cases
- `¬⊥ ≡ ⊤`, `¬⊤ ≡ ⊥`.
- `φ → ⊥ ≡ ¬φ`; `⊥ → φ ≡ ⊤` (`vacuous_trivial_proof`, intuitionistic);
  `⊤ → φ ≡ φ`; `φ → ⊤ ≡ ⊤`.
- `φ ∨ ⊥ ≡ φ`, `φ ∧ ⊤ ≡ φ` (identities); `φ ∨ ⊤ ≡ ⊤`, `φ ∧ ⊥ ≡ ⊥`
  (annihilators).
- in a **fixed** finite atom set with `n ≥ 1`, `⊤`/`⊥` add nothing expressible;
  with `n = 0` they are the only wffs up to equivalence.

## Hypothesis-dropped counterexamples
- **minimal logic** (drop `⊥E`): `⊥` is still a wff and `¬` still works, but
  `⊥ → φ` fails for general `φ` — `⊥` loses its "explosive" force.
- **no `⊥` at all** (positive logic): `¬` is not definable; you lose all of
  negation.
- **`⊤` as a fresh atom**: then `⟦⊤⟧_v` depends on `v` — wrong; `⊤` must be a
  tautology.

## Common misuse
Treating `⊤` as an atom; assuming `⊥ → φ` in minimal logic; forgetting the empty
`⋁`/`⋀` conventions when a normal form has zero clauses; conflating `¬φ`
(as `φ → ⊥`) with a primitive `¬` if both are in play.

## Related nodes (non-prerequisite)
- `feeds`: `explosion_ex_falso` (`⊥E`), `raa_rule` (`RAA` targets `⊥`),
  `consistency` (`Γ ⊬ ⊥`), `duality_principle` (`⊤ ↔ ⊥` swap).
- `algebra`: bottom / top of the Lindenbaum–Tarski Boolean algebra.
- `separates`: minimal / intuitionistic / classical logic.

## Sources
[vandalen_5e] §1.1, §2.3; [enderton_logic_2e] §1.1; [chiswell_hodges] ch. 2.
