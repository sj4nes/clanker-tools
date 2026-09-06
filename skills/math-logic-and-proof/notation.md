# notation.md — master symbol list

| Symbol | Meaning | Type | Area | Node |
|---|---|---|---|---|
| `¬ ∧ ∨ → ↔` | the connectives | `Wff → Wff` (unary/binary) | prop | `wff_syntax` |
| `⊤ ⊥` | verum, falsum | `Wff` | prop | `true_false_constants` |
| `p q r`, `A B C` | propositional atoms / schematic wffs | `Wff` | prop | `wff_syntax` |
| `φ ψ χ` | object wffs (schematic) | `Wff` | both | `wff_syntax` |
| `Γ Δ` | sets of wffs (assumptions / theory) | `Context` / `Theory` | both | `derivability` |
| `v` | truth assignment | `Atom → {T,F}` | prop | `truth_assignment` |
| `v ⊨ φ` | `v` satisfies `φ` | `Prop` | prop | `satisfaction` |
| `⊨ φ` | `φ` is a tautology / valid | `Prop` | both | `tautology`, `validity` |
| `Γ ⊨ φ` | semantic consequence | `Prop` | both | `semantic_consequence` |
| `φ ⊨⊨ ψ`, `φ ≡ ψ` | logically equivalent | `Prop` | both | `logical_equivalence` |
| `Γ ⊢ φ` | `φ` derivable from `Γ` | `Prop` | both | `derivability` |
| `⊢_ND`, `⊢_H` | derivable in ND / Hilbert | `Prop` | both | `nd_derivation`, `hilbert_derivation` |
| `∧I ∧E …` | ND rule names | rule | prop | `nd_rules_propositional` |
| `∀ ∃` | quantifiers | `(Var, Wff) → Wff` | FOL | `quantifier_syntax` |
| `∀x φ`, `∃x φ` | quantified wffs | `Wff` | FOL | `quantifier_syntax` |
| `∃!x φ` | unique existence | `Wff` (abbrev.) | FOL | `uniqueness_proof` |
| `x y z`, `v₀ v₁ …` | object variables | `Var` ⊂ `Term` | FOL | `term_syntax` |
| `c d`, `f g`, `R S` | constant / function / relation symbols | `ℒ`-symbol | FOL | `signature` |
| `t u` | terms | `Term` | FOL | `term_syntax` |
| `FV(φ)` | free variables of `φ` | finite set of `Var` | FOL | `free_bound_variables` |
| `φ[t/x]` | substitution | `Wff` | FOL | `substitution` |
| `t` free for `x` in `φ` | no-capture side condition | `Prop` | FOL | `free_for` |
| `ℒ` | a signature / first-order language | signature | FOL | `signature` |
| `𝔄 𝔅` | structures | `Structure` | FOL | `structure` |
| `\|𝔄\| = A` | domain of `𝔄` | `naive_collection` | FOL | `structure` |
| `c^𝔄, f^𝔄, R^𝔄` | interpretations in `𝔄` | elt / `Aⁿ→A` / `Aⁿ`-rel | FOL | `structure` |
| `s`, `s(x/a)` | variable assignment, update | `Var → A` | FOL | `assignment` |
| `s̄(t)` | value of term `t` under `s` | elt of `A` | FOL | `term_evaluation` |
| `𝔄 ⊨ φ[s]` | `𝔄` satisfies `φ` under `s` | `Prop` | FOL | `tarski_satisfaction` |
| `𝔄 ⊨ σ` | `𝔄` is a model of sentence `σ` | `Prop` | FOL | `model` |
| `Mod(Γ)` | class of models of `Γ` | `naive_collection` | FOL | `model` |
| `Con(Γ)`, `Γ ⊬ ⊥` | `Γ` consistent | `Prop` | both | `consistency` |
| `Th(𝔄)` | the theory of `𝔄` (all sentences true in it) | `Theory` | FOL | `theory` |
| `≅`, `≡` (structures) | isomorphic / elementarily equivalent | `Prop` | FOL | `elementary_equivalence` |
| `\|𝔄\|` (cardinality) | size of the domain | (naive) cardinal | FOL | `lowenheim_skolem_down` |
| `n`-ary | arity | `ℕ` (meta) | both | `signature` |
| `≺` eigenvariable | fresh variable in `∀I` / `∃E` | `Var` | FOL | `eigenvariable_condition` |
| `⊢ φ ⟺ ⊨ φ` | completeness+soundness combined | `metatheorem` | both | `completeness_theorem` |

Overloading of `⊨` and `⊢` is resolved by the type of the left operand — see
`conventions.md`.
