# inductive_definition

## Type
primitive  (a root; `constructive_grade: intuitionistic`)

## Statement
A set `S` given by:
- **base clauses**: certain objects are in `S`;
- **closure clauses**: if certain objects are in `S`, so is a specified object
  built from them;
- **extremal clause**: `S` is the **least** (smallest) set closed under the
  above.

The extremal clause yields two principles: **rule induction** (to prove
`∀s ∈ S, P(s)`, show `P` holds of the base and is preserved by each closure
rule) and **recursion** (a function on `S` is determined by base values + one
rule per closure clause).

## Symbols
- `S`: the inductively defined set; a "rule" `(premises) ⟹ conclusion`.

## Prerequisites (tsort edges into this node)
none — **primitive**.

## Why primitive here
The generative mechanism behind every syntactic class: `wff_syntax`,
`term_syntax`, `first_order_wff`, `nd_derivation`, `hilbert_derivation`,
`signature`-generated terms. The capsule takes it primitive (finitistic
metatheory) rather than deriving it from a fixed-point theorem in set theory
(that is the set capsule's job, and would be circular here).

## Constructive grade
`intuitionistic` — the least fixed point of a monotone rule set; when the rules
are finitary and decidable, `S` is decidable and the recursor computes. This
**is** Lean's `inductive` mechanism.

## Lean status
`lean_status: core` (it is the tool). `validation/proof-checks.lean`:
`inductive Wff`, `inductive Deriv`, `inductive H` — each an `inductive_definition`,
each auto-generating its recursor/`induction` principle. `induction d with …`
is rule induction; a recursive `def` is recursion.

## Type / well-formedness check
`well_formed` requires: **at least one base clause** (else `S = ∅` or ill-founded);
each closure rule has **strictly smaller** premises under some measure
(`formula_complexity`-style), so induction/recursion are well-founded; the
**least** fixed point is intended (a *greatest* fixed point is a *co*inductive
definition — streams, bisimilarity — where induction fails and coinduction
applies).

## Specialization / boundary cases
- `ℕ` = inductively defined by `0` and `succ` — `weak_induction` /
  `metatheoretic_induction` is its instance.
- `Wff` — `structural_induction_wff`, `recursion_on_wff`.
- derivations — "rule induction", used by `soundness_prop`, `deduction_theorem`,
  `truth_lemma_*`.
- **finitely many rules, finitely branching**: `S` is recursively enumerable;
  with decidable premises, decidable.
- **schema** (infinitely many rules, one per instance): e.g. the axiom *schemas*
  of `hilbert_system_prop` — still an inductive definition, `S` r.e.

## Hypothesis-dropped counterexamples
- **no base clause**: `S = ∅` (or, with a non-monotone rule, ill-defined).
- **greatest instead of least fixed point**: `S` contains "infinite" objects;
  structural induction is **unsound** (a coinductive stream type).
- **non-monotone rule** (`s ∉ S ⟹ f(s) ∈ S`): no least fixed point;
  induction/recursion undefined.
- **rules not decreasing** any measure: recursion may not terminate.

## Common misuse
Omitting the extremal ("nothing else") clause — then `S` is not the least fixed
point and induction fails; treating a coinductive definition inductively;
assuming an inductively defined set is decidable when the rules are not (it is
only r.e. in general); using recursion with a non-structural recursive call.

## Related nodes (non-prerequisite)
- `provides`: `structural_induction`, and its instances `weak_induction`,
  `structural_induction_wff`; `recursion_on_wff`.
- `builds`: `wff_syntax`, `term_syntax`, `first_order_wff`, `nd_derivation`,
  `hilbert_derivation`.
- `dual`: coinductive definition (out of scope).
- `set_theoretic_version`: least fixed point of a monotone operator
  (`math-sets-functions-cardinality`).

## Sources
[enderton_logic_2e] §1.4; [vandalen_5e] §1.1; Aczel, *An Introduction to
Inductive Definitions* (Handbook of Mathematical Logic, 1977).
