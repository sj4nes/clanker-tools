# lindenbaum_lemma_fol

## Type
proved_lemma  (epistemic status: `proved_lemma`; `constructive_grade:
needs_LEM` for a countable language, `needs_full_classical` for an arbitrary
one)

## Statement
Every consistent set of `ℒ`-sentences `T` extends to a **maximal consistent**
set `T* ⊇ T` in the same language `ℒ`: `T*` is consistent, and for every
`ℒ`-sentence `σ`, either `σ ∈ T*` or `¬σ ∈ T*`.

## Symbols
- `T`: a consistent set of `ℒ`-sentences (`consistency_fol`).
- `T*`: the maximal consistent extension.
- `ℒ`: the language — its cardinality controls the proof method.

## Prerequisites (tsort edges into this node)
`consistency_fol`, `maximal_consistent_set`, `metatheoretic_induction`,
`derivability_fol`.

## Proof
**Countable `ℒ`.** Enumerate the `ℒ`-sentences `σ₀, σ₁, …`. Set `T₀ = T`; given
`Tₙ` consistent, let `Tₙ₊₁ = Tₙ ∪ {σₙ}` if that is consistent, else
`Tₙ ∪ {¬σₙ}` (one of the two always is — `consistency_fol`). `T* = ⋃ₙ Tₙ`. Each
`Tₙ` is consistent; `T*` is consistent because any derivation of `⊥` uses
finitely many premises, all in some `Tₙ`. `T*` is maximal by construction. This
is `metatheoretic_induction` + `proof_by_cases` at each step.

**Uncountable `ℒ`.** The chain has length `> ω`; use **Zorn's lemma** on the
poset of consistent extensions of `T` ordered by `⊆` (every chain has a
consistent upper bound, again by finite character), or a maximal filter /
ultrafilter argument.

## Constructive grade
- countable `ℒ`: **`needs_LEM`** — "is `Tₙ ∪ {σₙ}` consistent?" is a
  yes/no decided by excluded middle at each stage; no choice, no enumeration
  problem beyond `metatheoretic_induction`.
- uncountable `ℒ`: **`needs_full_classical`** — Zorn's lemma is equivalent to
  the Axiom of Choice (`math-sets-functions-cardinality`, `zorn_lemma`).

This is the single choice-flavoured step in the whole completeness proof, and
the analogue of the set capsule's choice bookkeeping.

## Lean status
`lean_status: cited` (FOL). The propositional analogue `lindenbaum_lemma_prop`
is `cited` too; a Mathlib release connects to
`FirstOrder.Language.Theory.exists_maximal…` / the `Complete` predicate.
`validation/proof-checks.lean` does not build it (no FOL calculus without
Mathlib).

## Type / well-formedness check
`well_formed`. `T*` stays in `ℒ` — Lindenbaum adds **no new symbols** (contrast
`henkin_constants`, which does). "Maximal consistent" here means maximal *among
subsets of `Sent(ℒ)`*, not deductively closed a priori (though a maximal
consistent set **is** deductively closed as a consequence).

## Specialization / boundary cases
- `T` already complete and consistent: `T* = ` the deductive closure of `T`.
- `T = ∅`: `T*` is a complete consistent theory in `ℒ` — a "random" one, path-
  dependent on the enumeration.
- propositional: `lindenbaum_lemma_prop`, same argument over
  `truth_assignment`s.
- `T` decidable and `ℒ` countable: `T*` is still generally **not** decidable
  (the consistency check at each stage is undecidable) — even a constructive-
  looking countable Lindenbaum yields a non-computable theory.

## Hypothesis-dropped counterexamples
- **drop consistency of `T`**: an inconsistent `T` has no consistent extension
  at all — `T*` does not exist.
- **drop LEM** (constructive metatheory): the "one of `Tₙ ∪ {σₙ}`,
  `Tₙ ∪ {¬σₙ}` is consistent" step fails to be decidable; there is no
  constructive Lindenbaum lemma, and completeness fails constructively
  (this is why intuitionistic logic is complete only for Kripke semantics).
- **`T*` not maximal** (stop the construction early): the truth lemma's `¬`/`∨`
  clauses break — `truth_lemma_fol` needs `σ ∈ T*` **or** `¬σ ∈ T*`.

## Common misuse
Assuming `T*` is unique (it depends on the enumeration / the Zorn choices);
assuming `T*` is decidable / definable; using it for an uncountable language
without acknowledging the choice principle; confusing "maximal consistent"
(syntactic) with "the theory of a model" (semantic — though every maximal
consistent Henkin theory *is* the theory of its term model, that is
`truth_lemma_fol`, a theorem).

## Related nodes (non-prerequisite)
- `specialises`: `lindenbaum_lemma_prop`.
- `feeds`: `henkin_theory`, `godel_completeness_theorem`.
- `uses` (uncountable case): `zorn_lemma` (`math-sets-functions-cardinality`).
- `equivalent_to` (uncountable case, over ZF): the Boolean prime ideal theorem
  is enough — full AC is not strictly needed, only BPIT.

## Sources
[enderton_logic_2e] §2.5; [vandalen_5e] §3.1; [chiswell_hodges] §5.3;
[jech_set_theory] ch. 2 (BPIT vs AC).
