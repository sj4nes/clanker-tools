# substitution_of_equivalents

## Type
theorem  (epistemic status: `proved_theorem`; `constructive_grade: intuitionistic`)

## Statement
If `φ ≡ φ'` (`logical_equivalence`) and `ψ'` is obtained from `ψ` by replacing
**some occurrences** of `φ` (as a subformula) by `φ'`, then `ψ ≡ ψ'`.

## Symbols
- `φ`, `φ'`: logically equivalent wffs.
- `ψ`: a wff containing `φ` as a `subformula`; `ψ'`: the result of replacement.

## Prerequisites (tsort edges into this node)
`recursion_on_wff`, `subformula`, `logical_equivalence`.

## Proof
Structural induction on `ψ` (`recursion_on_wff`):
- `ψ = φ` (the whole thing is the replaced subformula): `ψ' = φ'`, and `φ ≡ φ'`
  by hypothesis.
- `ψ` atomic and `≠ φ`: no replacement, `ψ' = ψ`.
- `ψ = ¬χ`: `ψ' = ¬χ'` with `χ ≡ χ'` by IH; then `¬χ ≡ ¬χ'`
  (`equiv_neg`).
- `ψ = χ₁ ∘ χ₂` (`∘ ∈ {∧,∨,→,↔}`): `χᵢ ≡ χᵢ'` by IH; then
  `χ₁ ∘ χ₂ ≡ χ₁' ∘ χ₂'` (`equiv_conj` / `equiv_disj` / `equiv_impl`).
Each connective step is `⟦·⟧` truth-functionality: the value of `ψ` depends only
on the values of its immediate subformulas.

## Constructive grade
`intuitionistic` — pure structural induction with `⟦·⟧` computations; no
classical principle. (An equivalence `φ ≡ φ'` may itself be `needs_LEM` to
*prove*, but the substitution theorem given it is constructive.)

## Lean status
`lean_status: core`. `validation/proof-checks.lean`: the connective-congruence
lemmas `equiv_neg`, `equiv_conj`, `equiv_disj`, `equiv_impl` (each `by intro v;
simp [eval, …]`) are the inductive steps; the full statement is their structural
closure. `equiv_refl/symm/trans` give that `≡` is an equivalence relation.

## Type / well-formedness check
`well_formed`. "Occurrence of `φ` as a subformula" is a position in `ψ`'s parse
tree (`subformula`, well-defined by `wff_unique_readability`). The replacement
must be at genuine subformula boundaries — replacing a *fragment* that is not a
subformula (`p ∧` inside `p ∧ q`) is not licensed. Replacing **some** or **all**
occurrences both work.

## Specialization / boundary cases
- replace **all** occurrences: the common case ("rewrite `¬¬r` to `r`
  everywhere").
- `ψ = φ`: reduces to the hypothesis.
- chained rewriting: apply repeatedly (`≡` transitive) — the mechanism behind
  `negation_normal_form`, CNF/DNF conversion, and simplification.
- schematic: if `φ(p⃗) ≡ φ'(p⃗)` is a `prop_laws` identity, it can be applied to
  any substitution instance inside any `ψ`.

## Hypothesis-dropped counterexamples
- **`φ ≢ φ'`** (merely materially equivalent under the current assignment, not
  logically): replacing changes `ψ`'s truth value under other assignments.
- **replace a non-subformula fragment**: `ψ = (p → q) → r`, "replace `p → q`"
  is fine (it is a subformula), but "replace `q → r`" is **not** a subformula
  here (the parse is `(p→q) → r`, not `p → (q→r)`) — a `wff_unique_readability`
  trap.
- **opaque context** (modal/provability/quotation): substitution of equivalents
  **fails** — `□(p ∧ q) ≢ □(q ∧ p)`? actually that one holds, but
  `Prov(⌜φ⌝) ≢ Prov(⌜ψ⌝)` for `φ ≡ ψ`. Out of scope; noted because it is where
  the theorem stops.

## Common misuse
Replacing a fragment that is not a subformula (misparsing); using material
(assignment-specific) equivalence; applying it inside intensional contexts;
forgetting it is "some occurrences" — you need not replace all.

## Related nodes (non-prerequisite)
- `uses`: `logical_equivalence` (congruence property), `recursion_on_wff`,
  `subformula`.
- `enables`: `negation_normal_form`, `conjunctive_normal_form`,
  `disjunctive_normal_form`, simplification via `prop_laws`.
- `stops_at`: intensional / non-truth-functional contexts.

## Sources
[enderton_logic_2e] §1.2 (the replacement lemma); [vandalen_5e] §1.2;
[chiswell_hodges] §2.4.
