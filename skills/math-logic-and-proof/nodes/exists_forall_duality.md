# exists_forall_duality

## Type
mathematical_identity  (epistemic status: `mathematical_identity`; **split**:
`∃x φ → ¬∀x ¬φ` intuitionistic, `¬∀x ¬φ → ∃x φ` `needs_LEM`)

## Statement
`∃x φ ≡ ¬∀x ¬φ`  (and dually `∀x φ ≡ ¬∃x ¬φ`).

## Symbols
- `φ`: a first-order formula, `x` possibly free.

## Prerequisites (tsort edges into this node)
`quantifier_syntax`, `logical_equivalence_fol`, `quantifier_negation`.

## Content
The quantifier analogue of `implication_as_disjunction` / the `∀`/`∃`
interdefinability. Both quantifiers are given **primitive** formation rules
(`quantifier_syntax`, avoiding the definitional cycle), and this identity is a
**theorem** — so a treatment taking only `∀` primitive can *define* `∃x φ :=
¬∀x ¬φ`, and a constructive treatment keeps both primitive with only the
intuitionistic half.

## Constructive grade
**split** — `∃x φ → ¬∀x ¬φ` is `intuitionistic` (`fun ⟨a, ha⟩ h => h a ha`);
`∀x φ → ¬∃x ¬φ` is `intuitionistic`; `¬∃x ¬φ → ∀x φ` and `¬∀x ¬φ → ∃x φ` are
`needs_LEM` (they are `quantifier_negation`'s classical direction wrapped in a
negation). Node graded `needs_LEM` overall; the `∃`-from-`∀` reading is the
classical one.

## Lean status
`lean_status: core`. `validation/proof-checks.lean`: `not_exists_iff`
(`¬∃ ↔ ∀¬`, intuitionistic) and `not_forall_iff` (`¬∀ ↔ ∃¬`, `Classical`);
compose with `dni`/`dne` (`double_negation`) to get this identity.

## Type / well-formedness check
`well_formed`. Nonempty domain (`objects.md`); `x` binds the same occurrences on
both sides. `¬∀x ¬φ` and `∃x φ` are both `first_order_wff`.

## Specialization / boundary cases
- `φ` **decidable** (a decidable predicate over the domain): the whole identity
  is intuitionistically valid.
- domain **finite** `{a₁, …, aₙ}`: `∃x φ ≡ φ(a₁) ∨ … ∨ φ(aₙ)` and
  `¬∀x ¬φ ≡ ¬(¬φ(a₁) ∧ …)` — reduces to finite De Morgan.
- `¬¬∃x φ → ∃x φ` is `needs_LEM` even though `¬¬(∃x φ ∨ ¬∃x φ)` is
  intuitionistic — the constructive existence property is strictly stronger.

## Hypothesis-dropped counterexamples
- **intuitionistic logic**: `¬∀x ¬φ → ∃x φ` fails — Kripke countermodel: an
  infinite forcing chain where `∀x ¬φ` is refutable at the root (so `¬∀x¬φ`
  holds) yet no single world provides a witness for `∃x φ`. This is the "there
  is no constructive existence from a double negation" phenomenon.
- **empty domain**: `∃x φ` false, `¬∀x ¬φ` = `¬⊤` = `⊥` — happen to agree, but
  `∀x φ ≡ ¬∃x ¬φ` breaks (`∀x φ` vacuously true, `¬∃x ¬φ` = `¬⊥` = `⊤` — ok
  actually; the real empty-domain breakage is `∃x(x=x)`).

## Common misuse
Using the `∃`-from-`¬∀¬` direction constructively; assuming a double-negated
existence gives a witness; treating `∀`/`∃` as *definitionally* one from the
other in a constructive setting; empty-domain instincts.

## Related nodes (non-prerequisite)
- `equivalent_to`: `quantifier_negation` (with `double_negation`).
- `analogue`: `implication_as_disjunction`, `de_morgan_prop` (the propositional
  interdefinabilities).
- `enables`: taking `∀` primitive and defining `∃` (classical treatments).

## Sources
[enderton_logic_2e] §2.2; [vandalen_5e] §3.1, ch. 5; [chiswell_hodges] §5.3.
