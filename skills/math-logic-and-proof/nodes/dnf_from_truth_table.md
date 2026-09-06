# dnf_from_truth_table

## Type
theorem  (epistemic status: `proved_theorem` / `constructive_result`;
`constructive_grade: intuitionistic` given the completed table)

## Statement
Given the `truth_table` of a wff `φ` over atoms `p₁, …, pₙ`, an explicit
equivalent DNF is

    φ  ≡  ⋁ { m_v : v a row with ⟦φ⟧_v = T },      m_v = ⋀ᵢ ℓᵢ,
    ℓᵢ = pᵢ if v(pᵢ) = T, else ¬pᵢ.

Each `m_v` (a **minterm**) is true under exactly the one assignment `v`. If no
row is `T`, `φ ≡ ⊥`.

## Symbols
- `v`: a row of the table; `m_v`: its minterm (a full conjunction of literals,
  one per atom).

## Prerequisites (tsort edges into this node)
`truth_table`, `disjunctive_normal_form`.

## Proof
`m_v` is `T` under `w` iff `w = v` (each literal pins one atom). So
`⋁_{⟦φ⟧_v = T} m_v` is `T` under `w` iff `w` is one of the `T`-rows iff
`⟦φ⟧_w = T`. Same truth table as `φ` ⟹ `≡`.

## Constructive grade
`intuitionistic` **given** the completed table — the construction reads off the
`T`-rows and emits a formula, a finite computation. Building the table uses `LEM`
at each atom (each `v(pᵢ)` is `T` or `F`), but for the finitely many atoms of a
wff this is decidable, so effectively constructive.

## Lean status
`lean_status: core` (binary case). `validation/proof-checks.lean`:
`binary_dnf (f : Bool → Bool → Bool) (a b : Bool) : f a b = (f tt tt && (a && b))
|| (f tt ff && (a && !b)) || (f ff tt && (!a && b)) || (f ff ff && (!a && !b))`
— proved for all 4 `(a,b)` by `cases … <;> simp`. This **is**
`dnf_from_truth_table` for `n = 2`, at the Boolean-function level, and directly
witnesses `functional_completeness`.

## Type / well-formedness check
`well_formed`. Each minterm is a **full** conjunction (every atom appears,
positive or negated) — this makes the DNF **canonical** (unique up to order),
unlike a general `disjunctive_normal_form`. The number of minterms = number of
`T`-rows ≤ `2ⁿ`.

## Specialization / boundary cases
- `φ` a **tautology**: all `2ⁿ` minterms — the full DNF is a disjunction of
  every minterm.
- `φ` a **contradiction**: empty disjunction `= ⊥`.
- `φ` true on exactly one row: `φ ≡` that single minterm.
- **dual**: the `F`-rows give the canonical **CNF** (one **maxterm** per `F`-row).
- **minimisation**: merge minterms differing in one literal
  (`absorption`/`distributivity_prop`) → Karnaugh / Quine–McCluskey; the
  *minimal* DNF is generally **not** canonical.

## Hypothesis-dropped counterexamples
- **partial table**: minterms only from *some* `T`-rows ⟹ a formula strictly
  weaker than `φ` (misses models).
- **non-full minterms** (omit an atom): the "minterm" is true on ≥ 2
  assignments ⟹ the DNF may over-shoot (be true where `φ` is false).
- **read the `F`-rows as minterms**: gives `¬φ`'s DNF, not `φ`'s.

## Common misuse
Using only some `T`-rows; dropping atoms from minterms; reading off the wrong
rows; presenting the canonical DNF as *minimal* (it usually is not); assuming
this makes tautology-checking cheap (it is still `2ⁿ`).

## Related nodes (non-prerequisite)
- `special_case_of`: `disjunctive_normal_form` (the canonical one).
- `reads_from`: `truth_table`.
- `witnesses`: `functional_completeness`.
- `dual`: canonical CNF from the `F`-rows (maxterms).
- `related`: Karnaugh maps, Quine–McCluskey, minterm/maxterm terminology.

## Sources
[enderton_logic_2e] §1.5; [chiswell_hodges] ch. 3; any digital-logic text
(minterm expansion).
