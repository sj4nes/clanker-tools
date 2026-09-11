# lowenheim_skolem_down

## Type
metatheorem  (epistemic status: `metatheorem`; `constructive_grade:
needs_full_classical` term-model version / `needs_full_AC` the
elementary-substructure version)

## Statement
- **(term-model form)** A consistent theory `T` in a **countable** language has
  a model of cardinality `≤ ℵ₀`. If `T` has an infinite model, it has a
  countably infinite one.
- **(elementary-substructure form)** If `𝔄 ⊨ T` and `X ⊆ |𝔄|` with
  `|X| ≤ κ` for `max(ℵ₀, |ℒ|) ≤ κ ≤ |𝔄|`, there is `𝔅 ≼ 𝔄` (elementary
  substructure) with `X ⊆ |𝔅|` and `|𝔅| = κ`.

## Symbols
- `ℒ`: a first-order language, `|ℒ|` its cardinality.
- `T`: a satisfiable set of `ℒ`-sentences.
- `𝔅 ≼ 𝔄`: `𝔅` is a substructure and every formula with parameters from `𝔅`
  has the same truth value in `𝔅` and `𝔄`.

## Prerequisites (tsort edges into this node)
`godel_completeness_theorem`, `term_model`, `signature`.

## Proof
- **term-model form**: the model built in `godel_completeness_theorem` has
  domain a quotient of the **closed terms of `ℒ⁺`**, and `ℒ⁺` = `ℒ` + countably
  many Henkin constants is countable when `ℒ` is; a quotient of a countable set
  is countable. So the model already produced is `≤ ℵ₀`.
- **elementary-substructure form**: close `X` under **Skolem functions** for
  every formula `∃y φ(x̄, y)` (pick a witness — this is where **choice** enters);
  the closure is an elementary substructure (Tarski–Vaught test) of size `κ`.

## Constructive grade
- term-model form: `needs_full_classical` (inherits from completeness /
  Lindenbaum); **choice-free** given the countable-language completeness proof.
- elementary-substructure form: `needs_full_AC` (dependent choice suffices for
  countable `κ`; full AC for the general downward theorem).

## Lean status
`lean_status: cited` (corrected from `partial` — audited 2026-09-11; see
`BACKLOG.md`). Inherits the status of `godel_completeness_theorem`, itself
corrected to `cited` — the term-model-countability argument this node
needs is not formalised. Cited: [enderton_logic_2e] Thm 25.19. Mathlib:
`FirstOrder.Language.exists_elementarySubstructure_card_eq` / the downward
LS development, not connected here.

## Type / well-formedness check
`well_formed`. "Countable" = `|ℒ| ≤ ℵ₀` **and** `|model| ≤ ℵ₀` — cardinality is
imported as `naive_collection` talk (the arithmetic lives in
`math-sets-functions-cardinality`). The elementary-substructure form needs
`𝔅` to be a genuine substructure (closed under the functions of `ℒ`) *and*
elementary — the second is the content.

## Specialization / boundary cases
- **ZFC (if consistent) has a countable model** — `skolem_paradox`.
- the theory of **real closed fields** has a countable model: the real algebraic
  numbers.
- **any consistent finitely axiomatised theory** has a finite or countable
  model.
- combined with `lowenheim_skolem_up`: a first-order theory with an infinite
  model has models of **every** infinite cardinality (`non_categoricity`).

## Hypothesis-dropped counterexamples
- **drop countable language**: `ℒ` with `ℵ₁` constants `{cᵢ}` and axioms
  `cᵢ ≠ cⱼ` — every model has `≥ ℵ₁` elements; no countable model. (The bound
  is `max(ℵ₀, |ℒ|)`.)
- **drop satisfiability**: an inconsistent theory has no model at all.
- **second-order logic**: SOL with standard semantics has **no** downward LS —
  `(ℕ, +, ·, <)` is categorical, so its second-order theory has only models of
  size `ℵ₀`... actually the point: second-order Peano has *only* the standard
  model up to iso, and the *reals* second-order-axiomatised have only
  `2^ℵ₀`-sized models — no countable one. First-order-ness is essential.

## Common misuse
The **Skolem "paradox"**: concluding set theory is inconsistent because a
countable model contains sets the model believes are uncountable — "uncountable"
is **not absolute**; the bijection witnessing countability exists *outside* the
model (`skolem_paradox`). Also: thinking a theory with only infinite models can
be "pinned down" (LS says it cannot be pinned to one cardinality); confusing the
two forms; forgetting `|ℒ|` in the cardinality bound.

## Related nodes (non-prerequisite)
- `companion`: `lowenheim_skolem_up`.
- `proved_using`: `godel_completeness_theorem` (term-model form).
- `illustrated_by`: `skolem_paradox`.
- `implies`: `non_categoricity` (with upward LS).

## Sources
[enderton_logic_2e] §2.6; [chiswell_hodges] ch. 6; [hodges_shorter] §3.1;
[vandalen_5e] §3.2.
