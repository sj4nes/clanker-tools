# lindenbaum_lemma_prop

## Type
proved_lemma  (epistemic status: `proved_lemma`; `constructive_grade: needs_LEM`
for a countable atom set, `needs_full_classical` for an arbitrary one)

## Statement
Every `consistency`-consistent set of wffs `Γ` extends to a **maximal
consistent** set `Δ ⊇ Γ` (`maximal_consistent_set`) in the same language.

## Symbols
- `Γ`: a consistent set; `Δ`: its maximal consistent extension.

## Prerequisites (tsort edges into this node)
`maximal_consistent_set`, `consistency`, `metatheoretic_induction`,
`derivability`.

## Proof
**Countable atom set.** Enumerate the wffs `φ₀, φ₁, …`. `Δ₀ = Γ`; given `Δₙ`
consistent, set `Δₙ₊₁ = Δₙ ∪ {φₙ}` if consistent, else `Δₙ ∪ {¬φₙ}` (one always
is — `consistency`). `Δ = ⋃ₙ Δₙ`. Each `Δₙ` consistent (`metatheoretic_induction`);
`Δ` consistent by **finite character** of consistency; `Δ` maximal by
construction.

**Uncountable atom set.** Apply **Zorn's lemma** to the poset of consistent
extensions of `Γ` under `⊆` (every chain has a consistent upper bound, by finite
character).

## Constructive grade
- countable: **`needs_LEM`** — "is `Δₙ ∪ {φₙ}` consistent?" is decided by
  excluded middle at each stage; **no choice** (the enumeration is given,
  `metatheoretic_induction` drives it).
- uncountable: **`needs_full_classical`** — Zorn's lemma ≡ AC. Over ZF, the
  Boolean prime ideal theorem (weaker than AC) suffices.

This is the sole classical/choice-flavoured step in the propositional
completeness proof — the analogue of the set capsule's choice bookkeeping and of
`lindenbaum_lemma_fol`.

## Lean status
`lean_status: cited`. `validation/proof-checks.lean` does not build the
propositional completeness proof; a plain-Lean version for a countable atom set
(enumerate wffs, decide each) is feasible (LEM + `Nat`-recursion, no choice) and
would be the natural next Lean addition.

## Type / well-formedness check
`well_formed`. `Δ` stays in the **same language** — Lindenbaum adds no symbols
(contrast `henkin_constants`). "Maximal consistent" here means maximal among
consistent **sets of wffs**; deductive closure is a consequence.

## Specialization / boundary cases
- `Γ` already complete and consistent: `Δ` = its deductive closure.
- `Γ = ∅`: `Δ` is a "random" complete consistent theory, path-dependent on the
  enumeration.
- `Γ` decidable, countable atoms: `Δ` is still generally **not** decidable (the
  per-stage consistency check is undecidable).
- first-order: `lindenbaum_lemma_fol`, same argument.

## Hypothesis-dropped counterexamples
- **`Γ` inconsistent**: no consistent extension exists — `Δ` does not exist.
- **drop LEM** (constructive metatheory): "one of `Δₙ ∪ {φₙ}`, `Δₙ ∪ {¬φₙ}` is
  consistent" is not decidable; there is **no constructive Lindenbaum lemma**,
  and propositional completeness genuinely fails constructively (intuitionistic
  logic is complete only for Kripke semantics).
- **stop the construction early**: `Δ` is consistent but not maximal —
  `truth_lemma_prop` breaks at `¬`/`∨`.

## Common misuse
Assuming `Δ` is unique (enumeration- / Zorn-dependent); assuming `Δ` is
decidable/definable; using the uncountable case without acknowledging the choice
principle; confusing "maximal consistent set" (syntactic) with "theory of a
model" (semantic — though they coincide via `truth_lemma_prop`).

## Related nodes (non-prerequisite)
- `produces`: `maximal_consistent_set`.
- `feeds`: `post_completeness_theorem`.
- `first_order`: `lindenbaum_lemma_fol` (+ `henkin_theory`).
- `uses` (uncountable): `zorn_lemma` / BPIT (`math-sets-functions-cardinality`).

## Sources
[enderton_logic_2e] §1.7 / §2.5; [vandalen_5e] §1.5; [chiswell_hodges] §3.3;
[jech_set_theory] ch. 2 (BPIT vs AC).
