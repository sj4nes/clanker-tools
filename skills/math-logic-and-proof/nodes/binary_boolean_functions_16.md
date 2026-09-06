# binary_boolean_functions_16

## Type
example  (epistemic status: `example` / `mathematical_identity`;
`constructive_grade: intuitionistic`)

## Statement
There are exactly **`2^(2²) = 16`** functions `{T,F}² → {T,F}` — the binary
Boolean connectives. Each is named, and each is expressible in `{¬, ∧, ∨}`.

| function | name | `{¬,∧,∨}` form |
|---|---|---|
| `const F` | `⊥` / contradiction | `p ∧ ¬p` |
| `p ∧ q` | AND | `p ∧ q` |
| `p ∧ ¬q` | nonimplication | `p ∧ ¬q` |
| `p` | left projection | `p` |
| `¬p ∧ q` | converse nonimpl. | `¬p ∧ q` |
| `q` | right projection | `q` |
| `p ⊕ q` | XOR | `(p ∨ q) ∧ ¬(p ∧ q)` |
| `p ∨ q` | OR | `p ∨ q` |
| `¬(p ∨ q)` | NOR `↓` | `¬p ∧ ¬q` |
| `p ↔ q` | XNOR / iff | `(p ∧ q) ∨ (¬p ∧ ¬q)` |
| `¬q` | right negation | `¬q` |
| `q → p` | converse impl. | `q → p` |
| `¬p` | left negation | `¬p` |
| `p → q` | implication | `¬p ∨ q` |
| `¬(p ∧ q)` | NAND `↑` | `¬p ∨ ¬q` |
| `const T` | `⊤` / tautology | `p ∨ ¬p` |

## Symbols
- a binary Boolean function `f : {T,F}² → {T,F}` — determined by its 4-bit truth
  column.

## Prerequisites (tsort edges into this node)
`truth_table`.

## Content
Counting: a function on `{T,F}²` is fixed by its value on each of the `2² = 4`
input pairs, so `2⁴ = 16` functions. More generally `2^(2ⁿ)` `n`-ary functions
(4 unary, 256 ternary). Structure: 2 constants, 4 that ignore an input
(projections + their negations), and 10 "genuinely binary". Of the 16, exactly
**2** (`↑`, `↓`) are complete singletons (`sheffer_stroke`); the **monotone**
ones are `⊥, ∧, p, q, ∨, ⊤` (6); the **affine** ones are
`⊥, ⊤, p, q, ¬p, ¬q, ⊕, ↔` (8).

## Constructive grade
`intuitionistic` — a finite enumeration; each `{¬,∧,∨}` form is verified by a
2-atom truth table (`by cases <;> rfl`).

## Lean status
`lean_status: core` (the count + normal forms). `validation/proof-checks.lean`:
`binary_dnf` proves **every** `f : Bool → Bool → Bool` equals its 4-minterm DNF
(so all 16 have a `{¬,∧,∨}` form); `xor_nf`, `iff_nf`, `imp_nf` spell out three;
`nand`, `not/and/or_from_nand` handle `↑`. The literal count `2^(2^2) = 16` is a
`#eval` / `bc` fact (`bc validation/instance-checks.bc` prints it).

## Type / well-formedness check
`well_formed`. "16" counts *functions*, not *wffs* — infinitely many wffs
compute each function (they are the `⊨⊨`-equivalence classes of 2-atom wffs:
`Wff({p,q}) / ≡` has exactly `2^(2^2) = 16` elements — the free Boolean algebra
on 2 generators).

## Specialization / boundary cases
- `n = 0`: 2 functions (`⊤`, `⊥`).
- `n = 1`: 4 (`id`, `¬`, `⊤`, `⊥`).
- `n = 3`: 256; includes the ternary **majority** and **mux (if-then-else)**.
- the 16 form a **Boolean algebra** under pointwise operations (it is `2^4`), and
  a **group** of order 16 under `⊕` (it is `(ℤ/2)⁴`).

## Hypothesis-dropped counterexamples
- **count wffs instead of functions**: infinite — the point of the
  `⊨⊨`-quotient.
- **assume all 16 are "connectives" in a logic**: only a functionally complete
  *subset* is taken primitive; the rest are defined.
- **`n`-ary count as `2ⁿ`**: it is `2^(2ⁿ)` — the arguments range over `2ⁿ`
  input tuples.

## Common misuse
Confusing `2^(2ⁿ)` (functions) with `2ⁿ` (input rows) or with `n` (atoms);
counting equivalent wffs as distinct functions; treating XOR/XNOR as "not real
connectives"; forgetting `→` and `←` (converse) are two different functions.

## Related nodes (non-prerequisite)
- `counted_by`: `truth_table` (`2ⁿ` rows ⟹ `2^(2ⁿ)` functions).
- `specialises`: `functional_completeness`, `sheffer_stroke`.
- `algebra`: the free Boolean algebra on 2 generators = `2^4`; `(ℤ/2)⁴` under
  `⊕`; Post's lattice restricted to arity 2.

## Sources
[enderton_logic_2e] §1.5; [chiswell_hodges] ch. 3; Post (1941).
