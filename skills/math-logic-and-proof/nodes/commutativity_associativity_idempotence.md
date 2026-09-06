# commutativity_associativity_idempotence

## Type
mathematical_identity  (epistemic status: `mathematical_identity`;
`constructive_grade: intuitionistic`)

## Statement
For `∧` and for `∨`:
- **commutativity**: `p ∧ q ⊨⊨ q ∧ p`;  `p ∨ q ⊨⊨ q ∨ p`.
- **associativity**: `(p ∧ q) ∧ r ⊨⊨ p ∧ (q ∧ r)`;  likewise `∨`.
- **idempotence**: `p ∧ p ⊨⊨ p`;  `p ∨ p ⊨⊨ p`.

Together with `distributivity_prop`, `de_morgan_prop`, `absorption`, and the
`⊤`/`⊥` identities, these are the **Boolean-algebra axioms** realised in
propositional logic (`Wff / ⊨⊨` is the Lindenbaum–Tarski algebra).

## Symbols
- `p`, `q`, `r`: wffs / atoms.

## Prerequisites (tsort edges into this node)
`logical_equivalence`.

## Proof
Term-mode, all `intuitionistic`:
- comm: `fun ⟨a, b⟩ => ⟨b, a⟩` (and the `Or.elim`/`Or.inr`,`Or.inl` version);
- assoc: `fun ⟨⟨a, b⟩, c⟩ => ⟨a, b, c⟩`;
- idem: `fun ⟨a, _⟩ => a` / `fun a => ⟨a, a⟩`.

## Constructive grade
`intuitionistic` — hold in every Heyting algebra. No classical content.

## Lean status
`lean_status: core`. `validation/proof-checks.lean`: `and_comm'`, `and_assoc'`,
`and_idem'` (term-mode, no axioms). The `∨` versions are the exact duals; Lean
core also has `And.comm`, `and_assoc`, `and_self`, `Or.comm`, `or_assoc`,
`or_self`.

## Type / well-formedness check
`well_formed`, schematic. Associativity is what licenses writing
`p ∧ q ∧ r` and `p ∨ q ∨ r` **without parentheses** as far as *truth value*
goes — but the parser still fixes an association (`conventions.md`:
`→` right-assoc; `∧`, `∨` conventionally left-assoc), so the *wff* `(p∧q)∧r` and
`p∧(q∧r)` are distinct objects that happen to be logically equivalent (relevant
for `wff_unique_readability` and `subformula`).

## Specialization / boundary cases
- **idempotence fails for `→` and `↔`**: `p → p ⊨⊨ ⊤` (not `p`);
  `p ↔ p ⊨⊨ ⊤`. Only `∧`, `∨` are idempotent.
- **`→` is not commutative or associative**: `p → q ⊭⊨ q → p`;
  `(p → q) → r ⊭⊨ p → (q → r)` (the latter *is* `exportation`'s shape only when
  the left is `p ∧ q`).
- `n`-fold: `⋀` and `⋁` over a finite multiset are well-defined up to `⊨⊨`
  regardless of order/repetition — the basis for treating `Γ` as a set in
  `Γ ⊢ φ`.
- empty case: `⋀ ∅ = ⊤`, `⋁ ∅ = ⊥` (`notation.md` / `true_false_constants`).

## Hypothesis-dropped counterexamples
Equivalences, both directions — nothing to drop. The instructive failures are
the **connectives these laws do not apply to**: `→` (neither comm nor assoc nor
idem), `↔` (comm and assoc, but not idem in the `p` sense), `⊕` (comm, assoc,
not idem — `p ⊕ p ⊨⊨ ⊥`).

## Common misuse
Assuming `→` is associative or commutative; treating `p ∧ q ∧ r` as a single
3-ary connective (it is a *wff* with a fixed parse, equivalent to the other
association); using idempotence for `→`/`↔`; reordering `Γ` in a *sequent
calculus* where structural rules matter (in substructural logics
comm/contraction/weakening are exactly the rules that may be dropped — out of
scope).

## Related nodes (non-prerequisite)
- `feeds`: `absorption`, `negation_normal_form`, `conjunctive_normal_form`
  (clause dedup / reorder).
- `related`: the Lindenbaum–Tarski Boolean algebra of `Wff / ⊨⊨`; substructural
  logics (where these are the droppable structural rules).

## Sources
[enderton_logic_2e] §1.2; [vandalen_5e] §1.2; [chiswell_hodges] §2.4;
[halmos_boolean] (the algebra).
