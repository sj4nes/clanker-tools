# Conventions and foundational choices — Release 0.1

## Notation conventions (each is a `notation_convention` node where it affects a statement)

| Convention | Choice for this release | Node |
|---|---|---|
| Connectives | `¬ ∧ ∨ → ↔`, binding tightest-to-loosest in that order; `→` right-associative; outer parentheses dropped. | `wff_syntax` |
| `⊨` overloaded | `v ⊨ φ` (assignment satisfies), `𝔄 ⊨ φ[s]` (structure+assignment), `𝔄 ⊨ σ` (structure models a sentence), `Γ ⊨ φ` (semantic consequence). Disambiguated by the type of the left side. | `satisfaction`, `semantic_consequence` |
| `⊢` overloaded | `Γ ⊢ φ` (derivable). Subscript `⊢_ND`, `⊢_H` only where the calculus matters; `nd_hilbert_equivalence` licenses dropping it elsewhere. | `derivability` |
| `⊨⊨` | logical equivalence: `φ ⊨⊨ ψ` iff `φ ⊨ ψ` and `ψ ⊨ φ`. Written `≡` in prose. | `logical_equivalence` |
| `φ[t/x]` | substitute term `t` for every **free** occurrence of `x` in `φ`; only performed when **`t` is free for `x` in `φ`** (no capture). The side condition is a first-class node. | `substitution`, `free_for` |
| Signature / language | `ℒ` = (constant symbols, function symbols with arity, relation symbols with arity). Equality `=` is **logical**, always present, always interpreted as identity (FOL *with equality* is the default). | `signature`, `first_order_logic_with_equality` |
| Structure | `𝔄 = (A, ·^𝔄)`; domain `A` is **nonempty** by convention. Written with fraktur; domain `|𝔄| = A`. | `structure` |
| `ℕ` (metatheory) | the metatheoretic natural numbers `{0,1,2,…}`, **contains 0**, used to index symbols, measure formula length/height, and drive induction. **Primitive here**, not imported. | `metatheoretic_induction` |
| "consistent" | `Γ` is consistent iff `Γ ⊬ ⊥` (equivalently, for some `φ`, `Γ ⊬ φ`). | `consistency` |
| "theory" | a set of sentences closed under `⊢`, or (loosely) any set of sentences (its axioms). Closure meant when ambiguous. | `theory` |
| Derivation | ND: a finite tree with discharged assumptions (Gentzen) — Fitch boxes are the same object. Hilbert: a finite sequence of wffs. | `nd_derivation`, `hilbert_derivation` |
| `⊤ ⊥` | `⊤ := (p → p)`, `⊥` primitive with `⊥E` (ex falso). Ex falso is `intuitionistic`; RAA/`⊥`-classical is separate. | `true_false_constants` |
| Constructive grade | every logical-law and proof-method node carries one of `intuitionistic` / `needs_LEM` / `needs_DNE` / `needs_full_classical` — see `scope.md`. | (field on every such node) |

## Foundational choices (documented per the method, step 3)

- **Roots.** Five primitive nodes, all finitary-combinatorial:
  `symbol` (an element of a fixed countable alphabet),
  `string` (a finite sequence of symbols),
  `finite_sequence` (finite lists, over any node type — used for derivations),
  `inductive_definition` (a set given by a base clause + closure clauses, with
  its induction and recursion principles),
  `metatheoretic_induction` (ordinary + strong induction and recursion on the
  metatheoretic `ℕ`).
  Two further roots that are not in the finitary five:
  `first_order_logic_with_equality` — an `axiom` node ("`=` is a logical symbol,
  interpreted as identity on every domain"), a root in the manner of the set
  capsule's ZF axioms; and `decidability` — an informal primitive for the
  **boundary block only** ("membership settled by an always-halting effective
  procedure"), left undischarged because computability theory is explicitly out
  of scope. Only `tautology_decidable` and the boundary nodes touch it.

  Plus one primitive discharged **from above**: `naive_collection` — informal
  "set of" talk used only in semantic nodes; see the mutual-grounding note
  below. Every semantic node depends on it; no syntactic node does.

- **Why `ℕ` is primitive here and not imported.** `math-number-systems`
  constructs `ℕ` and proves things about it *using logic*. Its derivations are,
  in principle, among the finite objects this capsule quantifies over. Importing
  its `ℕ` would make the floor rest on something two storeys up. So the
  metatheoretic `ℕ` — used only to count symbols and license induction on
  finite syntactic structure — is declared primitive, with the Peano-style
  induction/recursion rules as the `metatheoretic_induction` node. This is
  finitistic and uncontroversial; it is *not* a claim that `ℕ` needs no
  construction, only that this capsule is not the place for it.

- **The syntax/semantics grounding loop is documented, not encoded.**
  - Syntactic development (`symbol` → wffs → ND/Hilbert → `⊢` → Deduction
    Theorem → propositional consistency) is **self-contained**: every edge is
    finitary, the subgraph is acyclic, and `tsort` orders it with no appeal to
    collections.
  - Semantic development (truth assignments → satisfaction → `⊨` → soundness →
    Henkin → completeness → compactness → LS) depends on `naive_collection`.
  - `naive_collection` is primitive **in this capsule** and discharged **by**
    `math-sets-functions-cardinality` (its ZF axioms). That capsule's
    `proposition_logic` / `predicate_logic` / `proof_methods` primitives are
    discharged **by this capsule**.
  - Net: a `grounds` relation runs both ways *between* the capsules
    (`edges/cross-capsule.md`), but **neither capsule's `tsort` graph has a
    cycle**. The circularity is real and is the honest state of the
    foundations; it is recorded, not hidden, and not linearised.

- **Classical object logic.** Completeness, compactness, and LS are stated for
  classical first-order logic with equality, nonempty domains.

- **Metatheory LEM is tracked.** The step "extend a consistent set to a maximal
  consistent set" (Lindenbaum) uses excluded middle at each stage and, for an
  uncountable language, a choice-flavoured principle (Zorn / an ultrafilter).
  Recorded on `lindenbaum_lemma` as `needs_full_classical`, with a note that the
  countable-language case needs only LEM + `metatheoretic_induction` (no choice).

- **Calculus independence.** `nd_derivation` is the spine. `hilbert_derivation`
  is a parallel subgraph. `nd_hilbert_equivalence` (`proved_lemma`) licenses
  every downstream `⊢` statement to be read in either calculus.

## Cycle resolutions

| Apparent cycle | Resolution | Recorded in |
|---|---|---|
| `⊢` ↔ `⊨` (soundness needs both; completeness needs both) | Not a cycle: `derivability` and `semantic_consequence` are independent nodes; `soundness` and `completeness` are theorems with edges *into* them from both. No edge between `⊢` and `⊨`. | `edges/cycles.md` |
| truth ↔ satisfaction | One node `satisfaction`, defined by recursion on wff structure (`recursion` clause supplied by `inductive_definition`). | `edges/cycles.md` |
| weak induction ↔ strong induction ↔ well-ordering | All three over metatheoretic `ℕ`; `metatheoretic_induction` supplies weak induction as primitive; `induction_equivalence` proves the other two equivalent to it. No cycle. | `edges/cycles.md` |
| syntax (this capsule) ↔ collections (set capsule) | Cross-capsule `grounds`, both directions, documented; `naive_collection` primitive here, `proposition_logic` primitive there. Neither `tsort` graph contains the loop. | `conventions.md` (above), `edges/cross-capsule.md` |
| `∀` ↔ `∃` (each defined from the other) | `∀` primitive in the syntax; `∃x φ := ¬∀x ¬φ` **classically**, but both are given primitive formation rules in the wff grammar and `exists_forall_duality` is a proved equivalence (so the intuitionistic reading is available too). | `edges/cycles.md` |
