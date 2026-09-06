# vacuous_quantification

## Type
mathematical_identity  (epistemic status: `mathematical_identity`;
`constructive_grade: intuitionistic`, given a nonempty domain)

## Statement
If `x ∉ FV(φ)` then `∀x φ ≡ φ` and `∃x φ ≡ φ` (nonempty domain). Quantifying a
variable that does not occur free changes nothing.

## Symbols
- `φ`: a formula with `x ∉ FV(φ)`.

## Prerequisites (tsort edges into this node)
`free_bound_variables`, `logical_equivalence_fol`.

## Content
Two moves it licenses: (i) **drop** a vacuous quantifier; (ii) **add** one
(useful in `prenex_normal_form` to make prefixes line up, and to α-rename). The
**nonempty domain** assumption (`objects.md`) is essential: over an empty
domain `∀x φ` is vacuously true and `∃x φ` false, so `∃x φ ≡ φ` fails when `φ`
is true.

## Constructive grade
`intuitionistic` given a nonempty domain: `∀x φ → φ` is
`fun h => h (some element)`; `φ → ∀x φ` is `fun hφ x => hφ`; `∃`-side similar
(needs a domain element for `∃x φ → φ` — hence nonemptiness).

## Lean status
`lean_status: cited`. `fun h => h (Classical.arbitrary _)` / `fun h _ => h` in
Lean, requiring `[Nonempty α]` for the `∃` direction. Not named in
`validation/proof-checks.lean`.

## Type / well-formedness check
`well_formed` **iff** `x ∉ FV(φ)` (checked via `free_bound_variables`) **and**
the domain is nonempty. `∀x φ` and `∃x φ` are still `first_order_wff`s; `x` is
bound but does not occur.

## Specialization / boundary cases
- `φ` a **sentence**: `∀x φ ≡ φ ≡ ∃x φ` for any `x`.
- adding `∀x` before a formula to match a prefix: `∀x∀y P(y) ≡ ∀y P(y)`.
- **shadowing**: `∀x ∀x φ` — the inner `∀x` makes `x` not free in its scope for
  the outer, so the outer is vacuous: `∀x ∀x φ ≡ ∀x φ`.
- bounded: `∀x ∈ A, φ` with `x ∉ FV(φ)` is `(∃y ∈ A) → φ` roughly — the
  nonemptiness of `A` matters, mirroring the domain condition.

## Hypothesis-dropped counterexamples
- **empty domain**: take `φ = ⊤`. `∀x ⊤ ≡ ⊤` (fine), but `∃x ⊤ ≡ ⊥ ≢ ⊤` — so
  `∃x φ ≡ φ` **fails**. This is a headline reason the capsule fixes nonempty
  domains.
- **`x ∈ FV(φ)`**: `∀x P(x) ≢ P(x)` — the free `x` on the right is unbound.

## Common misuse
Dropping/adding a quantifier over a variable that *does* occur free; assuming
`∃x φ ≡ φ` over a possibly-empty domain; forgetting shadowing makes an outer
quantifier vacuous; using it in a free-logic setting.

## Related nodes (non-prerequisite)
- `requires`: nonempty domain (`objects.md`), `x ∉ FV(φ)`.
- `used_by`: `prenex_normal_form`, `vacuous_trivial_proof` (its propositional
  cousin), α-renaming setup.
- `related`: shadowing; bounded quantification over a possibly-empty set.

## Sources
[enderton_logic_2e] §2.2; [vandalen_5e] §3.1; [chiswell_hodges] ch. 7.
