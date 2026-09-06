# godel_incompleteness_first

## Type
theorem  (epistemic status: **`stated_not_proved`**; `constructive_grade: n/a`
— it is a boundary node, cited not derived)

## Statement
Let `T` be a first-order theory such that
1. `T` is **consistent** (`consistency_fol`),
2. `T` is **recursively axiomatised** (the set of axioms is decidable —
   `decidability` / `church_turing_thesis`),
3. `T` **interprets Robinson arithmetic `Q`** (a modest amount of arithmetic is
   provable in `T`).

Then there is a sentence `G_T` in the language of `T` such that
`T ⊬ G_T` and `T ⊬ ¬G_T` — `T` is **incomplete**. Moreover `G_T` is *true* in
the standard model `ℕ` (it asserts its own unprovability). With
ω-consistency (Gödel) or just consistency (Rosser's refinement), the undecided
sentence exists.

## Symbols
- `T`: a theory (`Theory`) — the intended instances are `PA`, `ZFC`, `Q`.
- `G_T`: the Gödel sentence; via the diagonal lemma, `T ⊢ G_T ↔ ¬Prov_T(⌜G_T⌝)`.
- `⌜·⌝`: Gödel numbering — the arithmetisation of syntax (**out of scope**).

## Prerequisites (tsort edges into this node)
`decidability`, `derivability_fol`, `consistency_fol`, `church_turing_thesis`.

## Why it is stated, not proved (scope)
The proof needs the **arithmetisation of syntax** (Gödel numbering of terms,
formulas, proofs; the primitive-recursive `Prov_T` predicate) and the
**diagonal / fixed-point lemma**. Both are squarely in the excluded territory
(`scope.md`: "proofs of the boundary nodes … the fixed-point lemma"). This
capsule states the theorem with its exact hypotheses and cites a checked
treatment; it carries **no proof obligation** and `lean_status: none`.

## Relation to the completeness theorem (the confusion this node exists to kill)
- `godel_completeness_theorem`: the **logic** is complete — every semantic
  consequence is derivable. About `⊨` vs `⊢`.
- `godel_incompleteness_first`: a sufficiently strong **theory** is incomplete —
  some sentence is neither proved nor refuted. About `T ⊢ φ` vs `T ⊢ ¬φ`.

No contradiction: completeness says `T ⊬ G_T` implies `T ∪ {¬G_T}` has a model
(a **non-standard** model of arithmetic, where `G_T` is false). Incompleteness
just says that model and the standard one disagree on `G_T`.

## Type / well-formedness check
`well_formed` as a *schema over theories*. Each hypothesis is a predicate on
`T`: consistency (`consistency_fol`), "axiom set decidable"
(`decidability` — informal primitive), "interprets `Q`" (a provability
condition). The conclusion quantifies over sentences of `T`'s language.

## Specialization / boundary cases
- `T = PA`: `PA ⊬ Con(PA)` (that is `godel_incompleteness_second`);
  Goodstein's theorem and the Paris–Harrington principle are *natural*
  `PA`-independent statements.
- `T = ZFC`: incomplete if consistent (`incompleteness_of_PA_ZFC`); `CH`,
  large-cardinal axioms are independent (different mechanism — forcing — but
  same headline).
- `T = Q` (Robinson arithmetic): incomplete, and moreover **essentially
  undecidable**.
- **`T` = true arithmetic `Th(ℕ)`**: complete (it is a complete theory by
  definition) but **not recursively axiomatisable** — hypothesis 2 fails. This
  is the tight boundary: you can have completeness *or* a decidable axiom set,
  not both, for arithmetic.
- **`T` = real closed fields / `(ℝ,+,·,<)`**: complete *and* decidable
  (Tarski) — hypothesis 3 fails, RCF does not interpret `ℕ`. Shows the
  arithmetic hypothesis is essential.

## Hypothesis-dropped counterexamples
- **drop consistency**: an inconsistent `T` proves every sentence — trivially
  "complete".
- **drop recursive axiomatisation**: `Th(ℕ)` is complete.
- **drop "interprets `Q`"**: the theory of dense linear orders without
  endpoints, Presburger arithmetic `(ℕ,+)`, and RCF are all complete and
  decidable.

## Common misuse
"Gödel showed mathematics is inconsistent / unknowable"; applying it to
theories that do not interpret arithmetic (group theory, `(ℝ,+,·,<)`); reading
`G_T` as "true but unprovable" without noting *true in `ℕ`*, provable in
stronger theories (`PA + Con(PA) ⊢ G_PA`); conflating with the completeness
theorem.

## Related nodes (non-prerequisite)
- `commonly_confused_with`: `godel_completeness_theorem`.
- `strengthened_by`: `godel_incompleteness_second`, Rosser's theorem.
- `proved_using` (shared machinery, out of scope): the diagonal lemma, also
  behind `tarski_undefinability`.
- `historically_precedes`: Gödel 1931.

## Sources
[smith_godel_2e] (the reference treatment); [bbj_5e] ch. 17–18;
[enderton_logic_2e] §3.5 (statement and discussion).
