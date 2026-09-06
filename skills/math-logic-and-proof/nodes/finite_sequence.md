# finite_sequence

## Type
primitive  (a root; `constructive_grade: intuitionistic`)

## Statement
A **finite sequence** (list) of objects of one type `A`: `⟨a₀, …, a_{n−1}⟩`,
`n ≥ 0`. Operations: length, indexed access, `cons`/`append`, membership.

## Symbols
- `⟨a₀, …, a_{n−1}⟩`; the empty sequence `⟨⟩`; `n` the length.

## Prerequisites (tsort edges into this node)
none — **primitive**.

## Why primitive here
Finite sequences are the second finitistic primitive (`conventions.md`), used
for: `string`s (sequences of `symbol`s), **Hilbert derivations** (sequences of
wffs), **assumption lists / contexts** `Γ` in the propositional calculus, tuples
`⟨t₁, …, tₙ⟩` feeding an `n`-ary relation/function symbol, and the
finite-support facts (every wff has finitely many atoms; every derivation cites
finitely many premises → `compactness_prop`).

## Constructive grade
`intuitionistic` — an inductive type (`nil`, `cons`); all operations computable.

## Lean status
`lean_status: core`. `validation/proof-checks.lean` uses `List Wff` for the
context (`abbrev Ctx := List Wff`); `p :: Γ` is `cons` (the discharge slot in
`Deriv.impI`); `List.mem_cons` drives the `ax` cases of `soundness` / `deduction`.

## Type / well-formedness check
`well_formed`. A finite sequence is **finite** and **ordered** (contrast a
finite *set* — order and multiplicity forgotten). Where a context `Γ` is treated
as a **set** (`derivability`), that is a deliberate abstraction licensed by
`commutativity_associativity_idempotence` of `∧` (reorder/dedup premises freely).

## Specialization / boundary cases
- `n = 0`: `⟨⟩` — the empty context (`∅ ⊢ φ` is "φ is a theorem"); the empty
  premise list of a derivation.
- sequence of length `n` over a 2-element type ↔ a subset of `{0,…,n−1}` ↔ a row
  of a `truth_table`.
- **derivation as a sequence**: `hilbert_derivation` is exactly a finite
  sequence of wffs with a justification per position.
- nested: a finite sequence of finite sequences (a finite tree, bounded depth) —
  `nd_derivation`.

## Hypothesis-dropped counterexamples
- **infinite sequence**: not a finite sequence; an `ω`-sequence of wffs is not a
  derivation, and infinitary rules break `compactness_prop`.
- **treat a sequence as a set when order matters**: in a *sequent calculus* the
  structural rules (exchange, contraction, weakening) are exactly what may be
  dropped in substructural logics — order/multiplicity then matter.

## Common misuse
Allowing infinite sequences; forgetting sequences are ordered when that matters
(sequent calculus); conflating a finite sequence with a finite set without the
`∧`-idempotence/commutativity justification.

## Related nodes (non-prerequisite)
- `builds`: `string` (over `symbol`), `hilbert_derivation`, contexts `Γ`,
  argument tuples.
- `abstracted_to_a_set`: contexts in `derivability` (via `∧` comm/assoc/idem).
- `related`: sequent-calculus structural rules; substructural logics.

## Sources
[enderton_logic_2e] §1.1; [chiswell_hodges] ch. 2.
