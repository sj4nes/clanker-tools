# axiom_of_choice

## Type
axiom  (epistemic status: `axiom`; `choice_grade: needs_full_AC`)

## Statement
For every family `{A_i}_{i∈I}` of nonempty sets there is a **choice function**
`c` with `c(i) ∈ A_i` for all `i`.

## Prerequisites (tsort edges into this node)
`predicate_logic`. (AC is an axiom; it has no mathematical prerequisite beyond
being a well-formed sentence.)

## Independence
- **Gödel (1938):** `L`, the constructible universe, models `ZFC` — so ZF cannot
  *refute* AC. `Con(ZF) → Con(ZFC)`.
- **Cohen (1963):** forcing builds a model of `ZF + ¬AC` — so ZF cannot *prove*
  AC. `Con(ZF) → Con(ZF + ¬AC)`.

AC is therefore a genuine choice of axiom, not a theorem and not refutable.

## The three grades this capsule uses
Every downstream result carries a `choice_grade`:

| grade | meaning | examples |
|---|---|---|
| `choice_free` | provable in ZF | **Cantor–Schröder–Bernstein**, **Cantor's theorem**, **Hartogs' number**, the **finite pigeonhole**, `preimage_algebra`, `equivalence_partition_correspondence`, `omega_construction`, `recursion_theorem` |
| `needs_countable_choice` | needs CC (one choice per `n ∈ ℕ`) | `countable_closure_properties` (union clause), `finite_iff_not_dedekind_infinite` |
| `needs_full_AC` | needs AC / equivalent | `zorn_lemma`, `well_ordering_theorem`, `cardinal_comparability`, `infinite_cardinal_arithmetic` (`κ·κ=κ`), `right_inverse_iff_surjective`, `aleph_hierarchy` |

## Equivalent forms (`edges/relations.tsv`, not graph edges)
Zorn's lemma; the well-ordering theorem; comparability of cardinals; every
surjection splits; every vector space has a basis; every product of nonempty
sets is nonempty; Tychonoff's theorem.

## Weak forms (`countable_choice`, `dependent_choice`)
`AC ⟹ DC ⟹ CC`. **DC** suffices for essentially all sequential arguments in
analysis (building a sequence one term at a time). **CC** suffices for "a
countable union of countable sets is countable".

## Type / well-formedness check
`well_formed`. Recorded: a **definable** selector (least element of a
well-order; the element of a singleton; a canonical lowest-terms representative)
is **not** a use of AC (`objects.md` rule 7).

## Specialization / boundary cases
- a **finite** family — choice is provable in ZF by induction; AC only concerns
  infinite families.
- a family of nonempty subsets of a **well-ordered** set — pick the least
  element, no AC.
- a family of nonempty sets of **reals** — still needs AC in general.

## Hypothesis-dropped counterexamples (drop full AC)
Consistent with ZF that: `ℝ` is a countable union of countable sets; an infinite
set has no countably infinite subset (an *amorphous* set); a vector space has no
basis; `ℝ` cannot be well-ordered; there is a set that is neither finite nor
Dedekind-infinite.

## Common misuse
"Pick an element from each `A_i`" over an infinite family without acknowledging
AC; assuming CSB / Cantor's theorem / the finite pigeonhole need it; treating a
choice function as canonical.

## Related nodes (non-prerequisite)
- `equivalent_to`: `zorn_lemma`, `well_ordering_theorem`,
  `cardinal_comparability`
- `weakened_by`: `dependent_choice`, `countable_choice`

## Sources
[zermelo_1904]; [jech_set_theory] ch. 5; [herrlich_axiom_of_choice];
[enderton] ch. 6.
