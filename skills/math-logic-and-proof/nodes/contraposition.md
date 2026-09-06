# contraposition

## Type
mathematical_identity  (epistemic status: `mathematical_identity`; **split**:
`(p→q) → (¬q→¬p)` intuitionistic, the converse `needs_DNE`)

## Statement
`(p → q) ⊨⊨ (¬q → ¬p)` — an implication and its contrapositive are logically
equivalent.

## Symbols
- `p` (antecedent), `q` (consequent): wffs.

## Prerequisites (tsort edges into this node)
`logical_equivalence`, `double_negation`.

## Proof
- `(p → q) → (¬q → ¬p)`: **intuitionistic** — `fun h hnq hp => hnq (h hp)`.
- `(¬q → ¬p) → (p → q)`: **needs DNE** — from `¬q → ¬p` and `p` get `¬¬q`
  (assume `¬q`, then `¬p`, contradiction with `p`), then `double_negation`
  (`¬¬q → q`).

## Constructive grade
`needs_DNE` for the node overall. The forward half is `intuitionistic`
(`contrapose_weak`). The dependence on `double_negation` in the edge list is
exactly for the converse.

## Lean status
`lean_status: core`. `validation/proof-checks.lean`:
`contrapose_weak : (p → q) → (¬q → ¬p)` (term-mode), and
`contrapose_iff : (p → q) ↔ (¬q → ¬p)` (the `←` via `dne`).

## Type / well-formedness check
`well_formed`, schematic in `p`, `q`. The **contrapositive** `¬q → ¬p` is the
equivalent transform. Distinguish:
- **converse** `q → p` — *not* equivalent;
- **inverse** `¬p → ¬q` — *not* equivalent (it is the contrapositive of the
  converse).
Only `¬q → ¬p` is equivalent to `p → q`.

## Specialization / boundary cases
- `q = ⊥`: contrapositive of `p → ⊥` is `⊤ → ¬p` ≡ `¬p` — proving `¬p` directly.
- `p`, `q` **decidable**: intuitionistically equivalent, no DNE needed.
- quantified: `(∀x (P x → Q x)) ⊨⊨ (∀x (¬Q x → ¬P x))` — the quantifier stays
  out front and is **not** touched (contrast `disproof_by_counterexample`).

## Hypothesis-dropped counterexamples
- **drop classical logic**: `(¬q → ¬p) → (p → q)` fails. Take `p = ⊤`, `q` an
  undecided atom: `¬q → ¬⊤` is `¬q → ⊥` i.e. `¬¬q`; from `¬¬q` you cannot
  intuitionistically get `q`, so you cannot get `⊤ → q` i.e. `q`.
- the forward direction survives constructively.

## Common misuse
Proving the **converse** or **inverse** and claiming the original; negating the
quantifier along with the matrix (conflates with counterexample-disproof);
believing a contrapositive proof is constructive; iterating carelessly —
"contrapositive of the contrapositive" is the original, but "contrapositive of
the converse" is the inverse.

## Related nodes (non-prerequisite)
- `equivalent_to`: `proof_by_contrapositive` uses this as its licence.
- `commonly_confused_with`: converse, inverse.
- `uses`: `double_negation` (converse direction).
- `related`: `implication_as_disjunction` (`¬q → ¬p ⊨⊨ ¬¬q ∨ ¬p ⊨⊨ q ∨ ¬p`
  classically).

## Sources
[velleman_3e] §3.2; [enderton_logic_2e] §1.2; [hammack_bop] ch. 5.
