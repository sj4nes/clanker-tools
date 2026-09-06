# quantifier_negation

## Type
mathematical_identity  (epistemic status: `mathematical_identity`;
**constructive grade is split** — see below)

## Statement
For every `ℒ`-formula `φ` and variable `x`:

    ¬∀x φ   ⊨⊨   ∃x ¬φ                     (constructive grade: needs_LEM)
    ¬∃x φ   ⊨⊨   ∀x ¬φ                     (constructive grade: intuitionistic)

`⊨⊨` is `logical_equivalence_fol`: the two formulas have the same truth value in
every structure under every assignment.

## Symbols
- `φ`: an `ℒ`-formula, `x` possibly free in it.
- `x`: an object variable (`term_syntax`).
- domain of every witnessing structure is **nonempty** (`objects.md`), so
  `∀`/`∃` are genuine duals.

## Prerequisites (tsort edges into this node)
`tarski_satisfaction`, `logical_equivalence_fol`, `de_morgan_prop`.

## Proof
Semantic, from the `∀`/`∃` clauses of `tarski_satisfaction`:
- `¬∃x φ` true ⟺ no `a` makes `φ` true ⟺ every `a` makes `¬φ` true ⟺ `∀x ¬φ`
  true. Each step is a metatheoretic biconditional not using LEM. **Intuitionistic.**
- `¬∀x φ` true ⟺ *not* every `a` makes `φ` true. To get `∃x ¬φ` (some specific
  `a` makes `¬φ` true) from "not all" needs **excluded middle** in the
  metatheory: classically, `¬∀ a. P(a) ⟹ ∃ a. ¬P(a)` by contradiction; this is
  the infinitary De Morgan step (`de_morgan_prop`), which is `needs_LEM`.
- The **converse** `∃x ¬φ ⊨ ¬∀x φ` is intuitionistic in both lines.

## Constructive grade — the split (the capsule's hook)
| direction | grade | Lean |
|---|---|---|
| `¬∃x φ → ∀x ¬φ` | `intuitionistic` | `fun h x hx => h ⟨x, hx⟩` |
| `∀x ¬φ → ¬∃x φ` | `intuitionistic` | `fun h ⟨x, hx⟩ => h x hx` |
| `∃x ¬φ → ¬∀x φ` | `intuitionistic` | `fun ⟨x, hx⟩ h => hx (h x)` |
| `¬∀x φ → ∃x ¬φ` | **`needs_LEM`** | `Classical.not_forall.mp` — irreducibly classical |

So the *node as a whole* is graded `needs_LEM` (its strongest component), with
the three-of-four intuitionistic directions recorded. This mirrors the parallel
propositional facts on `de_morgan_prop` (`¬(p∧q) → ¬p∨¬q` is `needs_LEM`; the
converse is `intuitionistic`).

## Lean status
`lean_status: core`. `validation/proof-checks.lean` — the three intuitionistic
directions are term-mode one-liners; `not_forall_iff` is
`Classical.not_forall`. Also an `instance` check: a 3-element domain with an
explicit predicate, both sides tabulated by `decide`.

## Type / well-formedness check
`well_formed`. `¬∀x φ` and `∃x ¬φ` are both `first_order_wff`; `x` binds the
same occurrences on both sides; no substitution, so no `free_for` obligation.
The equivalence is stated for **formulas** (free variables allowed), evaluated
under an assignment — not only sentences.

## Specialization / boundary cases
- push through an implication: `¬∀x (P x → Q x) ⊨⊨ ∃x (P x ∧ ¬Q x)`.
- **negate an ε–δ statement**: `¬(∀ε>0 ∃δ>0 ∀x, |x−c|<δ → |f x − f c|<ε)`
  `⊨⊨` `∃ε>0 ∀δ>0 ∃x, |x−c|<δ ∧ |f x − f c|≥ε` — this *is* the definition of
  "discontinuous at `c`", and every negated `∀…∃…` in analysis is this node.
- `¬(X countable)` unfolds to "no injection `X → ω`".
- bounded quantifiers: `¬∀x∈A. φ ⊨⊨ ∃x∈A. ¬φ` (same grade).

## Hypothesis-dropped counterexamples
- **drop classical metatheory**: in intuitionistic predicate logic
  `¬∀x (P x ∨ ¬P x)` is refutable, yet `∀x (P x ∨ ¬P x)` is not provable — the
  `¬∀ → ∃¬` direction fails, and with it every "there must be a counterexample"
  argument. (Kripke countermodel: an infinite ascending chain of worlds where
  `P` becomes true later at each node.)
- **drop nonempty domain** (free logic, out of scope): `∀x φ` can be vacuously
  true while `∃x φ` is false, breaking the duality.

## Common misuse
Stopping the negation at the outer quantifier instead of driving it all the way
in. **Swapping quantifier order while negating** — that is `quantifier_order`, a
separate matter: `¬∀x∃y φ` is `∃x∀y ¬φ` (order preserved, each flipped), *not*
`∃y∀x ¬φ`. Claiming the classical direction constructively.

## Related nodes (non-prerequisite)
- `equivalent_to`: `exists_forall_duality` (with `double_negation`).
- `generalises`: `de_morgan_prop` (finite → quantified).
- `used_by`: every counterexample node in `math-real-analysis`,
  `math-number-systems`, `math-sets-functions-cardinality` — each "not
  continuous / not compact / not complete / not countable" is an instance.
  (`edges/cross-capsule.md`: this is the `quantifier_negation` primitive those
  capsules cite.)

## Sources
[enderton_logic_2e] §2.2; [vandalen_5e] §3.1 and ch. 5 (intuitionistic
countermodels); [chiswell_hodges] §5.3.
