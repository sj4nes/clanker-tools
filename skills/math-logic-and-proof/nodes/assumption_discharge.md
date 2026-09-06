# assumption_discharge

## Type
definition  (epistemic status: `definition`; `constructive_grade: intuitionistic`)

## Statement
In natural deduction, a temporarily assumed wff `φ` is **discharged** by a later
rule application, after which `φ` no longer counts as an open assumption. The
`→I` rule is the paradigm: a sub-derivation of `ψ` under assumption `φ` yields
`φ → ψ` with `φ` discharged.

    [φ]¹
     ⋮
     ψ
    ─────  →I, discharging ¹
    φ → ψ

`∨E`, `¬I`, and `RAA` also discharge.

## Symbols
- `[φ]ⁱ`: an assumption occurrence, labelled `i`, to be discharged.
- the discharging step: `→I` (label `i`), `∨E`, `¬I`, or `RAA`.

## Prerequisites (tsort edges into this node)
`nd_rules_propositional`, `nd_derivation`.

## Content
Discharge is what makes natural deduction *natural*: you reason "suppose `φ` …"
and later "so, if `φ` then `ψ`", closing the supposition. It is the
proof-theoretic form of the **deduction theorem** (`deduction_theorem`): `→I`
turns `Γ, φ ⊢ ψ` into `Γ ⊢ φ → ψ`. In the Hilbert calculus there is no
discharge rule — the deduction theorem is a **metatheorem** simulating it, and
that gap is the substantive case of `nd_hilbert_equivalence`.

Under Curry–Howard, discharge is **λ-abstraction**: `→I` binds the variable
standing for the assumption.

## Constructive grade
`intuitionistic` — `→I` is minimal logic; abstraction. (The *discharging rule*
`RAA` is classical, but the discharge *mechanism* is not.)

## Lean status
`lean_status: core`. `Deriv.impI : Deriv (p :: Γ) q → Deriv Γ (Wff.impl p q)` in
`validation/proof-checks.lean` — the assumption `p` sits in the context `p :: Γ`
of the sub-derivation and is removed on the conclusion. In Lean's own logic,
`intro h` makes an assumption and the closing `fun h => …` discharges it.

## Type / well-formedness check
`well_formed`. A discharging step closes **exactly** the assumptions bearing its
label — closing more is unsound (smuggles away a real premise), closing fewer
leaves them open (they belong in `Γ`). Multiple occurrences of the same
assumption may share a label and all discharge at once (or `→I` may discharge
**zero** occurrences — vacuous, giving `φ → ψ` from `ψ` alone).

## Specialization / boundary cases
- discharge **zero** occurrences: `ψ ⊢ φ → ψ` (weakening / `vacuous_trivial_proof`).
- discharge **all** occurrences of a multiply-used assumption in one step.
- `∨E`: discharges one assumption in **each** branch.
- `RAA`: discharges `¬φ` from a sub-derivation of `⊥`.
- iterated `→I`: `Γ, φ₁, …, φₙ ⊢ ψ` becomes `Γ ⊢ φ₁ → … → φₙ → ψ`.

## Hypothesis-dropped counterexamples
- **discharge an assumption that was never made**: nonsense — no such leaf.
- **fail to discharge**: the "theorem" `⊢ φ → ψ` is actually `φ ⊢ ψ` — an open
  assumption.
- **over-discharge in `RAA`** (close `¬φ` *and* some `γ ∈ Γ`): "proves" a
  stronger statement than licensed.
- **share a label across independent assumptions**: closes both when only one
  was intended.

## Common misuse
Forgetting to discharge (leaving the proof conditional); discharging an
assumption used outside the intended sub-derivation; in Fitch notation, citing a
line from a closed box; assuming Hilbert systems have discharge (they simulate
it via `deduction_theorem`).

## Related nodes (non-prerequisite)
- `is`: the mechanism of `→I`, `∨E`, `¬I`, `RAA` in `nd_rules_propositional`.
- `metatheoretic_counterpart`: `deduction_theorem`.
- `curry_howard`: λ-abstraction.
- `feeds`: `direct_proof`, `proof_by_contradiction`, `nd_hilbert_equivalence`.

## Sources
[vandalen_5e] ch. 2; [chiswell_hodges] ch. 4; Prawitz (1965).
