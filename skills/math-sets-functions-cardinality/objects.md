# Type vocabulary and well-formedness rules — Release 0.1

Everything is a **set** in ZFC; the "types" below are the useful working
distinctions, and the well-formedness rules are the traps this pass exists to
catch (an ill-scoped quantifier, an `⋂` of an empty family, a "function" that is
not total, a choice used without acknowledgement).

## Object kinds

| Kind | What it is | Formed by | Typical predicates |
|---|---|---|---|
| `set` | a set (element of a ZFC universe) | the ZF axioms | `empty, nonempty, transitive, inductive, finite, countable` |
| `class` | `{x : φ(x)}` — a **proper class** unless proven a set | a formula `φ` | `is a set (via Separation/Replacement)` |
| `relation` | `R ⊆ X × Y` | `cartesian_product` + `separation` | `reflexive, symmetric, antisymmetric, transitive, connex, well-founded` |
| `equiv` | an equivalence relation on `X` | `relation` | — |
| `partition` | a set of nonempty pairwise-disjoint sets covering `X` | `power_set` + `separation` | — |
| `function` | `f ⊆ X × Y`, single-valued and **total on `X`** | `relation` | `injective, surjective, bijective, order-preserving` |
| `family` | a function `i ↦ A_i` on an index set `I` | `function` | `disjoint, increasing` |
| `order` | a reflexive antisymmetric transitive relation | `relation` | `total, well-order, dense, complete` |
| `ordinal` | a transitive set well-ordered by `∈` | `axiom_foundation` + `separation` | `successor, limit, zero` |
| `cardinal` | (as an object) an initial ordinal; (as a predicate) an equinumerosity class | `ordinal` + AC | `finite, aleph, regular` |

## Well-formedness rules (checked in `validation/type-checks.md`)

1. **`{x : φ(x)}` is a class, not automatically a set.** Writing it as a set
   asserts a Separation instance (`{x ∈ X : φ}` for a known set `X`) or a
   Replacement instance. Russell's `{x : x ∉ x}` is the standing counterexample
   — it is a proper class, and treating it as a set is the classic type error.
2. **`⋂ 𝓕` requires `𝓕 ≠ ∅`.** `⋂ ∅` would be "everything" — a proper class.
   Every statement with an indexed `⋂_{i∈I}` carries `I ≠ ∅`.
3. **A function is total.** `f : X → Y` asserts `∀x∈X ∃!y∈Y, (x,y)∈f`. A
   "partially defined" rule is a function on a *subdomain*, and its domain must
   be named. `f⁻¹` as a *function* is well-formed only when `f` is a bijection
   (rule via `inverse_iff_bijective`); `f⁻¹` as the **preimage operator on
   sets** is always well-formed.
4. **Codomain is part of the data.** `f : X → Y` and `f : X → f[X]` are
   *different functions*; surjectivity is a statement about the presentation.
   The image laws (`f[A∪B] = f[A]∪f[B]`) do not depend on the codomain; the
   preimage laws are stated for subsets of the codomain.
5. **Quantifier order is load-bearing.** `∀x ∃y P(x,y)` and `∃y ∀x P(x,y)`
   differ; a statement's type check records which. The "uniform" upgrades
   (uniform continuity, uniform convergence, a *single* choice function for a
   whole family) all move a `∀` left of an `∃`.
6. **`¬∀` unfolds to `∃¬` (classical).** Every counterexample construction is
   the classical equivalence `¬(∀x, P x) ⟺ ∃x, ¬P x` applied once; the negated
   inner statement must itself be pushed through (`¬(A ⟹ B) ⟺ A ∧ ¬B`,
   `¬(∀ε ∃δ …) ⟺ ∃ε ∀δ ¬…`). `quantifier_negation` is the node.
7. **Choice must be acknowledged.** Any proof that selects one element from each
   of infinitely many nonempty sets uses `axiom_of_choice` (or a weak form).
   The result carries an edge to `axiom_of_choice` / `countable_choice` /
   `dependent_choice`, and a `choice_grade` field. A "canonical" choice (a
   definable selector — least element of a well-order, the unique element of a
   singleton) is **not** a use of AC and is noted as such.
8. **Cardinality claims need a witness.** `|X| = |Y|` asserts an *exhibited or
   proven* bijection; `|X| ≤ |Y|` an injection; `|X| < |Y|` additionally
   `¬∃` bijection (a `¬∀`, rule 6). `|X| < |𝒫(X)|`'s proof
   (`cantor_theorem`) must produce, from any `f : X → 𝒫(X)`, the explicit
   missing set `{x : x ∉ f(x)}`.

## The "is it a set, is the function total, is choice used" signature check

For a quick pass: (a) every `{x : …}` is bounded by a known set or justified by
Replacement; (b) every `⋂` over a family has a nonempty index; (c) every
`f : X → Y` is total and `Y` is fixed; (d) every "∀…∃…" records whether the
witness is uniform; (e) every "for each `i`, pick …" over an infinite family is
tagged with its choice grade. This is the analog of summing dimension
exponents.
