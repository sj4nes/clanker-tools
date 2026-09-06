# Conventions and foundational choices — Release 0.1

## Notation conventions (each is a `notation_convention` node where it affects a statement)

| Convention | Choice for this release | Node |
|---|---|---|
| Logic | **Classical** — excluded middle and double-negation elimination are available; so `¬∀x P ⟺ ∃x ¬P` and proof by contradiction are used freely. | `quantifier_negation` |
| Quantifier order | `∀x ∃y` (`y` may depend on `x`) is the default; `∃y ∀x` is the strictly stronger "uniform" form. The two are never silently swapped. | `quantifier_order` |
| `⊆` vs `⊂` | `⊆` allows equality; `⊊` is strict. `⊂` is **not used**. | `subset` |
| `∅` | the empty set; unique by extensionality. | `empty_set` |
| Ordered pair | Kuratowski: `(a,b) := {{a},{a,b}}`. The only property used downstream is `(a,b)=(c,d) ⟺ a=c ∧ b=d`. | `ordered_pair` |
| Function | a set of ordered pairs that is single-valued and total on its domain; `f : X → Y` fixes the codomain `Y` (so surjectivity is a property of the *presentation*). | `function` |
| `f[A]`, `f⁻¹[B]` | image and preimage; `f⁻¹` here is the **preimage operator on sets**, defined for every `f` (not the inverse function). | `image`, `preimage` |
| Indexed family | `{A_i}_{i∈I}` is a function `i ↦ A_i` on an index set `I`; `⋃_{i∈I} A_i`, `⋂_{i∈I} A_i` (the latter needs `I ≠ ∅`). | `indexed_family` |
| `\|X\|` | the cardinality of `X`; `\|X\| = \|Y\|` means "a bijection exists" (`equinumerous`), `\|X\| ≤ \|Y\|` means "an injection exists". Cardinals as *objects* (initial ordinals) appear only in the aleph thread. | `equinumerous`, `cardinal_le` |
| `ℕ` / `ω` | `ω` is the constructed set (smallest inductive), `0 := ∅`, `S x := x ∪ {x}`; **`ω` contains `0`**. `ℕ` and `ω` are used interchangeably after `peano_holds_in_omega`. | `omega_construction` |
| `2^X`, `Y^X` | the set of functions `X → 2` (resp. `X → Y`); `2 := {0,1}`. `𝒫(X) ≅ 2^X` via characteristic functions. | `function_space` |
| `ℵ₀`, `𝔠` | `ℵ₀ := \|ℕ\|`; `𝔠 := 2^ℵ₀ = \|ℝ\| = \|𝒫(ℕ)\|`. | `aleph_hierarchy`, `continuum` |
| "countable" | **injects into `ℕ`** — so every finite set is countable; "countably infinite" = "equinumerous with `ℕ`". | `countable_set` |
| Well-order | a total order in which **every nonempty subset has a least element**. | `well_order` |

## Foundational choices (documented per the method, step 3)

- **The ZF(C) axioms are the floor.** `set` is "an element of a model of ZFC".
  The nine ZF axioms + Choice are `axiom` nodes; their mutual consistency is not
  addressed (Gödel's second incompleteness theorem is out of scope). Separation
  and Replacement are **schemas** (one axiom per formula) — recorded as such;
  this capsule uses them only at named instances.
- **Classical logic.** Excluded middle is assumed. This is what makes
  `quantifier_negation` (`¬∀ ⟺ ∃¬`) and proof by contradiction available — both
  are used pervasively downstream (and in `math-real-analysis`, every
  "discontinuous", "not compact", "counterexample" is a `¬∀`).
- **The Axiom of Choice is used, but every use is edged.** Three grades:
  `needs_full_AC` (Zorn, well-ordering, cardinal comparability, `κ·κ = κ`,
  right-inverse-from-surjection), `needs_countable_choice` (countable union of
  countable sets, "not Dedekind-infinite ⟹ finite"), and `choice_free`
  (Cantor–Schröder–Bernstein, Cantor's theorem, Hartogs' number, finite
  pigeonhole, the diagonal argument). `axiom_of_choice`, `countable_choice`,
  `dependent_choice` are first-class nodes.
- **Ordinals** are von Neumann ordinals. Only the spine (`ordinal`,
  `transfinite_induction`, `transfinite_recursion`, `order_type_theorem`) is
  built; ordinal arithmetic and the cumulative hierarchy are out of scope.

## Cycle resolutions (full record; see `edges/cycles.md`)

1. **AC ⟺ Zorn ⟺ well-ordering theorem ⟺ cardinal comparability.** All
   equivalent over ZF; texts prove them in a ring. **Resolution:**
   `axiom_of_choice` is the canonical form and is upstream. `zorn_lemma`,
   `well_ordering_theorem`, and the comparability of cardinals `derive_from` it
   one-directionally; `ac_equivalences` is a summary `theorem` node listing the
   reverse implications, which live as `equivalent_to` rows in
   `edges/relations.tsv` — **not** as graph edges.

2. **cardinal `≤` ⟺ injection ⟺ Cantor–Schröder–Bernstein.** `cardinal_le` is
   *defined* as "an injection exists"; CSB is a theorem about that relation.
   One-directional: `cantor_schroeder_bernstein` `requires` `cardinal_le`.

3. **ordinal ⟺ well-order.** An ordinal is *defined* as a transitive set
   `∈`-well-ordered; `order_type_theorem` ("every well-order is isomorphic to a
   unique ordinal") is the theorem connecting them. `ordinal` `requires`
   `well_order`; `order_type_theorem` `requires` both. No reverse edge.

4. **ℕ ⟺ set.** `ω` is built from `∅` via Infinity + Separation; `finite_set` is
   then defined via the finite ordinals (elements of `ω`). **Resolution:**
   `omega_construction` `requires` `axiom_infinity`, `axiom_separation`;
   `finite_set` `requires` `omega_construction`. The direction is strictly
   set → `ω` → finite. `peano_holds_in_omega` is a theorem *about* the
   construction.

5. **transfinite recursion ⟺ ordinal arithmetic.** Recursion is stated
   abstractly (define `F` on all ordinals from a rule `G`), needing only
   `ordinal` + `transfinite_induction`. Downstream uses (order types, the aleph
   function) `require` it; nothing flows back.

6. **power set ⟺ function space.** `power_set` and `function_space` are defined
   independently; `characteristic_function` and the bijection `𝒫(X) ≅ 2^X` are
   a theorem, not a definitional identification.

7. **quotient before the relation is verified an equivalence.** As in
   `math-number-systems`: `equivalence_partition_correspondence` and the
   equivalence axioms are established for a relation on `X` before `X/∼` is
   formed. `quotient_set` `requires` `equivalence_relation`.

## Distinguishing three orderings

`indexes/tsort-order.txt` is a **prerequisite** order — not historical (Cantor's
cardinality predates the ZF axiomatization by 30 years), not pedagogical, not
the logical order inside a proof. Independent nodes (e.g. `pigeonhole_principle`
and `de_morgan_laws`) may linearize either way.

## The bridge to `math-number-systems` and `math-real-analysis`

- `math-number-systems` takes `set`, `function`, `relation`,
  `equivalence_relation`, `quotient_set`, `cartesian_product`,
  `well_defined_on_quotient`, `axiom_of_choice`, `countable_choice`, and
  `peano_axioms` as primitives/citations. **Every one is a node here**, and
  `peano_holds_in_omega` proves the last. A `math-number-systems` Release 0.2
  would replace those with `requires` edges into this capsule.
- `math-real-analysis` uses `axiom_of_choice` / `countable_choice` and, tacitly,
  the preimage algebra and quotient machinery. `preimage_algebra` here is the
  node its `continuity` / `compact_set` proofs actually stand on.
