# objects.md — the type vocabulary

Every symbol in every node's statement inhabits one of these. The
well-formedness (type) check for a node confirms each symbol's type and that
every operation's domain/codomain line up.

## Syntactic types (the finitary floor — no collections)

| Type | What it is | Notes |
|---|---|---|
| `Symbol` | an element of the fixed countable alphabet | connectives, quantifiers, punctuation, variables `v₀ v₁ …`, and — for FOL — the `ℒ`-symbols |
| `String` | a finite sequence of `Symbol` | wffs are distinguished strings |
| `Term` (FOL) | inductive: a variable, a constant, or `f t₁…tₙ` for an `n`-ary function symbol `f` | closed term = no variables |
| `Wff` | inductive: propositional (atoms + `¬ ∧ ∨ → ↔`) or first-order (atomic `R t₁…tₙ`, `t₁ = t₂`, plus `∀x ∃x`) | **unique readability** licenses recursion |
| `Occurrence` | a position in a wff's parse tree | free vs bound is a predicate on variable occurrences |
| `Context` / `Γ` | a **finite** set (propositional ND) or a set (metatheory) of wffs | finite where derivations are concerned; arbitrary in compactness/completeness statements — flagged |
| `NDDerivation` | a finite tree of wffs with discharge annotations | conclusion `type: Wff`, open assumptions `type: finite set of Wff` |
| `HilbertDerivation` | a finite sequence of wffs, each an axiom or an MP consequence | |
| `Substitution` | a map `Var → Term` (usually single `[t/x]`) | only applied under `free_for` |

## Semantic types (depend on `naive_collection`)

| Type | What it is | Notes |
|---|---|---|
| `TruthAssignment` | a function `Atom → {T, F}` (propositional) | often `2^Atom`; finite-support where a wff is finite |
| `Structure` / `𝔄` | a nonempty domain `A` (a `naive_collection`) + interpretations: `c^𝔄 ∈ A`, `f^𝔄 : Aⁿ → A`, `R^𝔄 ⊆ Aⁿ` | equality always interpreted as identity on `A` |
| `Assignment` / `s` | a function `Var → A` | `s(x/a)` = `s` updated at `x` to `a` |
| `TermValue` | `s̄(t) ∈ A`, by recursion on `t` | |
| `TruthValue` | `T` or `F` (or `Bool`) | `⟦φ⟧_{𝔄,s}` by recursion on `φ` |
| `Model` (of `Γ`) | a `Structure` with `𝔄 ⊨ σ` for every `σ ∈ Γ` | class of models is a `naive_collection` of structures |
| `Theory` | a `naive_collection` of sentences | consistent / complete / Henkin are predicates on it |

## Meta types

| Type | What it is |
|---|---|
| `ℕ` (meta) | metatheoretic natural numbers — formula length, height, symbol indices, induction |
| `BooleanFunction` | `{T,F}ⁿ → {T,F}` — the target of *functional completeness* |
| `Prop` (meta) | a metatheoretic proposition; the metalogic is classical, LEM-use tracked |
| `ConstructiveGrade` | `intuitionistic` \| `needs_LEM` \| `needs_DNE` \| `needs_full_classical` |

## Well-formedness rules used

- **Recursion on `Wff`** is licensed only by unique readability
  (`wff_unique_readability`); every semantic function (`⟦·⟧`, free-variable set,
  substitution, quantifier rank) is defined this way.
- **`φ[t/x]` is only well-formed to *use*** when `free_for(t, x, φ)` holds; a
  node stating `φ[t/x]` without it is ill-formed (this is a common-misuse trap,
  e.g. in `∀E` and `∃I`).
- **`𝔄 ⊨ φ[s]`** requires `s` defined on every free variable of `φ`
  (`coincidence_lemma` says only those matter).
- **`Γ ⊢ φ`** requires `Γ` and `φ` in the *same* language `ℒ`.
- **A quantifier rule's eigenvariable** must not occur free in the conclusion or
  any open assumption — an explicit side condition, checked per use.
- **Domain nonempty**: `∃x (x = x)` is valid in this capsule; free-logic
  variants are out of scope.
