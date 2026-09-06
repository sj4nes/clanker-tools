# functional_completeness

## Type
theorem  (epistemic status: `proved_theorem`; `constructive_grade: intuitionistic`
— the DNF construction is explicit)

## Statement
The connective set `{¬, ∧, ∨}` is **functionally complete**: every Boolean
function `f : {T,F}ⁿ → {T,F}` (every `n`, including `n = 0`) is computed by some
wff over `{¬, ∧, ∨}` in the `n` atoms. Hence so are `{¬, →}`, `{¬, ∧}`,
`{¬, ∨}`, `{↑}` (Sheffer / NAND), `{↓}` (Peirce / NOR).

## Symbols
- `f`: an `n`-ary Boolean function; `n`: arity.
- the wff: `dnf_from_truth_table` of `f`.

## Prerequisites (tsort edges into this node)
`dnf_from_truth_table`.

## Proof
By `dnf_from_truth_table`: the disjunction of the minterms of the `T`-rows of
`f` computes `f`; it uses only `¬` (in literals), `∧` (minterms), `∨` (the
outer). The `n = 0` cases give `⊤`, `⊥`. Then reduce the basis:
`∨` from `{¬, ∧}` by De Morgan; `∧` from `{¬, ∨}`; `→` from `{¬, ∨}`; and
`¬`, `∧`, `∨` each from `{↑}` (`sheffer_stroke`).

## Constructive grade
`intuitionistic` — the wff is **built** from `f`'s table; the correctness proof
is a `Bool` case analysis (decidable). Note: functional completeness is about
**expressing truth functions**, a distinct notion from **deductive**
completeness (`post_completeness_theorem`, proving every tautology) — both hold
for classical propositional logic.

## Lean status
`lean_status: core` (binary case + basis reductions).
`validation/proof-checks.lean`:
- `binary_dnf` — every `f : Bool → Bool → Bool` equals its `{¬,∧,∨}` DNF;
- `not_from_nand`, `and_from_nand`, `or_from_nand` — `{↑}` generates `{¬,∧,∨}`;
- `xor_nf`, `iff_nf`, `imp_nf` — three of the 16 binary connectives in
  `{¬,∧,∨}` form.
The general `n` case (arbitrary arity) is cited (needs a length-`n` literal
list / `Fin n → Bool` enumeration).

## Type / well-formedness check
`well_formed`. "Boolean function" = `{T,F}ⁿ → {T,F}` — a *semantic* object; the
theorem produces a *syntactic* wff realising it. The basis must be checked to
**not** be sub-complete: `{∧, ∨}` (no `¬`) expresses only the **monotone**
functions; `{↔, ¬}` only the **affine** (XOR-of-a-subset ⊕ constant) functions;
`{→}` cannot express `⊥`. **Post's lattice** classifies every clone of Boolean
functions — the five maximal ones (monotone, affine, self-dual,
0-preserving, 1-preserving) are exactly the obstructions.

## Specialization / boundary cases
- `n = 1`: 4 functions (`id`, `¬`, `const ⊤`, `const ⊥`) — all in `{¬}` + `⊤`.
- `n = 2`: all 16 (`binary_boolean_functions_16`).
- **single-connective** complete sets: exactly `{↑}` and `{↓}` (Sheffer 1913).
- **`{if-then-else}`** (the ternary mux) with constants `⊤`, `⊥` is complete.

## Hypothesis-dropped counterexamples (sub-complete bases)
- `{∧, ∨, ⊤, ⊥}`: only monotone functions — cannot express `¬p`.
- `{↔, ¬}` (or `{⊕, ⊤}`): only affine functions — cannot express `∧`.
- `{→}` alone: cannot express `⊥` (every `→`-formula is `T` when all atoms are
  `T`); `{→, ⊥}` **is** complete.
- `{¬}` alone: only `id` and `¬` — unary only.

## Common misuse
Assuming `{∧, ∨}` suffices (misses non-monotone functions); assuming you need
all of `¬, ∧, ∨` (any of the five minimal bases works); confusing functional
with deductive completeness; thinking `{⊕, ∧}` (the "Boolean ring" basis with
`⊤`) is not complete (it is — `{⊕, ∧, ⊤}` = Zhegalkin / algebraic normal form).

## Related nodes (non-prerequisite)
- `proved_via`: `dnf_from_truth_table`.
- `specialised_by`: `sheffer_stroke`, `binary_boolean_functions_16`.
- `contrast`: `post_completeness_theorem` (deductive completeness).
- `related`: Post's lattice / clones; Zhegalkin (algebraic) normal form;
  the mux `{ite, ⊤, ⊥}` basis.

## Sources
[enderton_logic_2e] §1.5; [chiswell_hodges] ch. 3; Post (1941) (the lattice);
Sheffer (1913).
