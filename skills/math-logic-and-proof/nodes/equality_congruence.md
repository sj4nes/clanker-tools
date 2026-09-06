# equality_congruence

## Type
proposition  (epistemic status: `proved_theorem`; `constructive_grade:
intuitionistic`)

## Statement
In any structure (equality interpreted as identity), `=` is a **congruence**:
if `a₁ = b₁, …, aₙ = bₙ` then for every `n`-ary function symbol `f` and relation
symbol `R`,

    f^𝔄(a₁,…,aₙ) = f^𝔄(b₁,…,bₙ)   and   (a₁,…,aₙ) ∈ R^𝔄 ⟺ (b₁,…,bₙ) ∈ R^𝔄.

Syntactically, the **substitution schema** `x = y → (φ[x/z] → φ[y/z])` is valid
for every `φ`.

## Symbols
- `aᵢ`, `bᵢ`: domain elements with `aᵢ = bᵢ`.

## Prerequisites (tsort edges into this node)
`tarski_satisfaction`, `first_order_logic_with_equality`,
`substitution_lemma_semantic`.

## Proof
**Semantic**: `aᵢ = bᵢ` means they are the *same* element (identity
interpretation), so `f^𝔄` / `R^𝔄` applied to them give the same result —
immediate. **Syntactic** (that the schema is provable / valid): by
`substitution_lemma_semantic` and induction on `φ`.

## Constructive grade
`intuitionistic` — identity substitution is constructively unproblematic (Lean's
`Eq.subst` / `▸`).

## Lean status
`lean_status: core` (the mechanism). Lean's `▸` (`Eq.mpr` / `Eq.subst`) **is**
the substitution schema; `congrArg`, `congrFun` are the function-congruence
instances. `validation/proof-checks.lean` uses these throughout (e.g.
`taut_iff_neg_contra`, the `equiv_*` lemmas). The FOL object-level statement is
`cited`.

## Type / well-formedness check
`well_formed` **given** `first_order_logic_with_equality` (identity
interpretation). The substitution schema `x = y → (φ[x/z] → φ[y/z])` needs `x`,
`y` **free for `z`** in `φ` (`free_for`) — the usual capture guard. This is
exactly the well-definedness obligation for the **`term_model` quotient**
(`t ≈ u` a congruence).

## Specialization / boundary cases
- **reflexivity** `x = x`, **symmetry** `x = y → y = x`, **transitivity**
  `x = y ∧ y = z → x = z` — all instances (symmetry/transitivity from
  reflexivity + the schema).
- congruence for a specific `f`: `x = y → f(x) = f(y)`.
- the `term_model`: `≈` (provable equality) is a congruence **because** the
  equality axioms are in the theory — this is what makes `f^𝔐`, `R^𝔐`
  well-defined.
- **partial equivalence relations** (PERs): drop reflexivity — used in
  realizability, out of scope.

## Hypothesis-dropped counterexamples
- **`=` not identity** (equality-free FOL): `=` is a relation symbol with no
  congruence guarantee; `a = b` need not license replacing `a` by `b` — you must
  *add* congruence axioms, and then work up to the quotient.
- **substitution schema without `free_for`**: capture — the replacement changes
  meaning.
- **no reflexivity axiom**: `x = x` unprovable; the whole equality apparatus
  collapses.

## Common misuse
Assuming congruence in a setting where `=` is not identity; skipping the
`free_for` guard on the substitution schema; using `=` for an equivalence
relation and expecting automatic congruence; forgetting this is what makes the
term-model quotient well-defined.

## Related nodes (non-prerequisite)
- `depends_on`: `first_order_logic_with_equality`, `equality_axioms`.
- `enables`: the `term_model` quotient (`well_defined_on_quotient` analogue).
- `used_by`: `godel_completeness_theorem`, `lowenheim_skolem_down`.
- `related`: PERs (realizability), setoids.

## Sources
[enderton_logic_2e] §2.2; [chiswell_hodges] ch. 5; [hodges_shorter] §1.3.
