# Scope — Release 0.1

**Logic and proof — the deepest floor.**

The capsule that develops what
[`math-sets-functions-cardinality`](../math-sets-functions-cardinality/SKILL.md)
(and, transitively, `math-number-systems` and `math-real-analysis`) *cites but
does not build*: propositional and first-order logic — their syntax, semantics,
and deductive calculi — the metatheorems that connect proof to truth
(soundness, Gödel completeness, compactness, Löwenheim–Skolem), and the
catalogue of **proof methods** (contradiction, contrapositive, cases,
induction in its several forms, existence and uniqueness, counterexample) as
first-class nodes with their exact logical content and their constructive cost.

Nothing in this capsule cites a higher capsule. Its only upward promise: it
supplies the nodes `math-sets-functions-cardinality`'s `scope.md` lists under
"Logic floor (cited to a future `math-logic-and-proof`)" —
`proposition_logic`, `predicate_logic`, `quantifier_negation`,
`quantifier_order`, `proof_methods` — as a developed subgraph, so a Release 0.2
of that capsule can replace those five primitives with edges into this one.

## Included

### Propositional logic
- **Syntax**: an alphabet, the inductive definition of a well-formed formula
  (wff), unique readability, the connectives `¬ ∧ ∨ → ↔`, parse trees,
  subformulas, the principle of **structural induction on wffs** and
  **recursion on wff structure** (used to *define* every semantic function).
- **Semantics**: truth assignments, the truth-value recursion, truth tables,
  satisfaction `v ⊨ φ`, tautology, contradiction, satisfiability, logical
  consequence `Γ ⊨ φ`, logical equivalence `φ ⊨⊨ ψ`.
- **The equivalence catalogue**: double negation, commutativity, associativity,
  idempotence, absorption, distributivity, **De Morgan**, `→` as `¬p ∨ q`,
  contraposition, `↔` as a conjunction of implications, exportation,
  the constants `⊤ ⊥`.
- **Normal forms**: NNF, CNF, DNF; existence proofs by recursion; the
  disjunctive-normal-form theorem from the truth table.
- **Expressive completeness**: `{¬, ∧, ∨}` is functionally complete; so are
  `{¬, →}`, `{¬, ∧}`, `{↑}` (Sheffer), `{↓}`; `{∧, ∨}` is not. The 16 binary
  Boolean functions.
- **Deductive calculi** (see *Foundational stance*): a **natural-deduction**
  system (Fitch/Gentzen) as the spine — `∧I ∧E ∨I ∨E →I →E ¬I ¬E ⊥E`, plus
  `RAA`/`DNE` as the classical rule — and a parallel **Hilbert** system
  (three schemas + modus ponens) with an equivalence lemma `⊢_ND φ ⟺ ⊢_H φ`.
  Derivations, discharge of assumptions, the **Deduction Theorem** (a theorem
  for Hilbert, a rule for ND).
- **Propositional metatheory**: consistency, `Γ ⊢ φ` vs `Γ ⊨ φ`,
  **soundness**, **Lindenbaum's lemma**, **Post's completeness theorem**,
  **propositional compactness**, decidability of `⊨ φ` (truth tables) and of
  `Γ ⊢ φ` for finite `Γ`.

### First-order logic
- **Syntax**: a signature (constants, function symbols, relation symbols with
  arities), terms, atomic formulas, wffs, **free and bound variables**,
  **substitution `φ[t/x]`** and the **"`t` is free for `x` in `φ`"** side
  condition, sentences, prenex form.
- **Semantics**: a **structure** (`𝔄` = a domain `A` with interpretations),
  variable assignments, the **term-evaluation recursion**, **Tarski's
  definition of satisfaction** `𝔄 ⊨ φ[s]`, truth of a sentence, models,
  `Γ ⊨ φ`, validity, logical equivalence, the substitution lemma, the
  **coincidence lemma** (truth depends only on the free variables).
- **The quantifier catalogue**: `∀x φ ≡ ¬∃x ¬φ`; **quantifier negation**
  `¬∀x φ ⊨⊨ ∃x ¬φ` and `¬∃x φ ⊨⊨ ∀x ¬φ`; quantifier distribution over `∧`/`∨`
  (and which direction fails); **quantifier order** `∀x∃y` vs `∃y∀x` (one
  entailment, not the other); vacuous quantification; renaming bound variables
  (α-equivalence); **prenex normal form** theorem.
- **First-order calculi**: ND with `∀I ∀E ∃I ∃E` and the **eigenvariable
  (variable-not-free) conditions**; the Hilbert quantifier axioms + generalization;
  first-order logic **with equality** (reflexivity + the substitution schema),
  and equality as a congruence.
- **First-order metatheory**: `Γ ⊢ φ` ⟹ `Γ ⊨ φ` (**soundness**);
  consistency; Lindenbaum + **Henkin construction** (constants, witnesses,
  maximal consistent Henkin theory, the **term model**); **Gödel's
  completeness theorem** `Γ ⊨ φ ⟹ Γ ⊢ φ`; **compactness** (as a corollary and
  via the term model); the **downward Löwenheim–Skolem theorem**; upward LS
  (stated, with the Skolem "paradox" as a note); non-categoricity and
  non-finite-axiomatizability examples (infinite models, `(ℝ,<)` vs `(ℚ,<)`).

### Proof methods (a curated block, each a node)
Direct proof; **proof by contrapositive**; **proof by contradiction / RAA**;
**proof by cases** / exhaustive disjunction; biconditional (prove both
directions); **existence** — constructive vs pure-existence (LEM / pigeonhole /
counting) — and **uniqueness** (`∃!`, "assume two, show equal");
**disproof by counterexample** (the working form of `¬∀`); **without loss of
generality**; **weak (ordinary) induction**, **strong (course-of-values)
induction**, **structural induction**, and the **well-ordering principle**, with
the three-way equivalence `weak ⟺ strong ⟺ well-ordering` over `ℕ` proved;
vacuous and trivial proof; the difference between `⟹` and `⟺` in a proof.

### Boundary nodes (stated, never proved — they mark the ceiling)
`decidability` and `undecidability`; the **Church–Turing thesis** (`heuristic`);
**undecidability of first-order validity** (Church/Turing); **Gödel's first and
second incompleteness theorems**; **Tarski's undefinability of truth**; the
**halting problem**; a one-line statement that PA and ZFC, if consistent, are
incomplete. Each carries a full statement, its hypotheses (e.g. "consistent,
recursively axiomatized, interprets Robinson arithmetic"), sources, and epistemic
status `stated_not_proved` (or `heuristic` for Church–Turing) — and **no proof
obligation**.

## Excluded (out of scope for 0.1)

- **Proofs of the boundary nodes**: the arithmetization of syntax, the fixed-point
  lemma, the construction of Turing machines / recursive functions, Rosser's
  trick, provability logic. Incompleteness is *stated and cited*, never derived.
- **Sequent calculus proof theory**: Gentzen's `LK`/`LJ`, cut elimination,
  the subformula property, ordinal analysis, `ε₀`, proof mining. (Sequent
  calculus is *mentioned* as an alternative calculus via a relation, not built.)
- **Model theory proper**: elementary embeddings, types and the omitting-types
  theorem, saturation, quantifier elimination, Ehrenfeucht–Fraïssé games,
  ultraproducts and Łoś's theorem, categoricity theorems (Morley),
  o-minimality, stability. Only the LS theorems and bare non-categoricity are
  in scope.
- **Higher-order and non-classical logic**: second-/higher-order logic beyond a
  contrast note, `ω`-logic, infinitary logic `L_{κλ}`; modal, temporal,
  intuitionistic, linear, many-valued, and relevance logic as *systems* — though
  **intuitionistic validity is tracked per node** as the constructive grade
  (see below), the intuitionistic *calculus* itself is not developed.
- **Set theory**: the ZF(C) axioms, cardinal/ordinal arithmetic — that is the
  capsule above. This capsule uses only naive finite/countable collection talk
  in its metatheory (see *Foundational stance*).
- **Computability as a subject**: the theory of recursive functions,
  reducibility, the arithmetical hierarchy, complexity. Only the named boundary
  facts appear.
- **Automated deduction**: resolution, unification, DPLL/CDCL, tableaux as
  algorithms, SMT. (Tableaux/resolution may appear as a *mentioned* alternative
  refutation method, not as built algorithms.)

## Level and audience

A first course in mathematical logic, taken alongside or just after a
"transition to proof" course. Primary texts: Enderton, *A Mathematical
Introduction to Logic* (2e); van Dalen, *Logic and Structure* (5e); Chiswell &
Hodges, *Mathematical Logic*; Mendelson, *Introduction to Mathematical Logic*
(6e). For the proof-method block: Velleman, *How to Prove It* (3e); Hammack,
*Book of Proof*. For the boundary nodes: Boolos, Burgess & Jeffrey,
*Computability and Logic* (5e); Smith, *An Introduction to Gödel's Theorems*.
The reader can already read quantifier notation and follow an induction.

## Foundational stance

- **Syntax is the true floor.** Formulas are finite strings over a countable
  alphabet, defined inductively; derivations are finite trees / finite
  sequences of strings. This combinatorial layer — finite strings, finite
  sequences, induction and recursion **on the natural numbers and on wff
  structure** — is taken as primitive **finitistic metatheory**. The nodes
  `symbol`, `string`, `inductive_definition`, `metatheoretic_induction`,
  `finite_sequence` are the roots. Metatheoretic `ℕ` is primitive here; it is
  *not* imported from `math-number-systems` (that would be circular — that
  capsule's proofs are, in principle, objects this capsule talks about).
- **The metatheory of semantics uses naive collections.** A structure has a
  domain "set"; completeness quantifies over "all models". The capsule is
  honest that this talk is exactly what `math-sets-functions-cardinality`
  axiomatizes, and that the two floors are **mutually referential**: proof
  theory grounds set theory's logic; set theory's collections ground model
  theory's semantics. The resolution recorded in `conventions.md`: the
  **syntactic/proof-theoretic development is self-contained and primitive**;
  every **semantic** node (satisfaction, models, soundness, completeness,
  compactness, LS) is tagged `metatheory: naive_collections` and depends on the
  node `naive_collection` — a primitive here, discharged *from above* by the
  set capsule, exactly mirroring how that capsule's `proposition_logic`
  primitive is discharged from here. Neither capsule's `tsort` graph contains a
  cycle; the loop is a documented cross-capsule `grounds` relation, not an edge.
- **Classical logic is the object logic** for the headline metatheorems
  (completeness, compactness, LS are stated for classical first-order logic).
- **Excluded middle is available in the metatheory** but its use is *tracked*:
  Lindenbaum's lemma / the maximal-consistent-set step is `needs_LEM` (or
  weak König / ultrafilter in the infinite case — recorded), and this is called
  out, mirroring the set capsule's choice bookkeeping.
- **`⊢` is calculus-independent.** ND is the spine; the Hilbert system is built
  in parallel and `nd_hilbert_equivalence` is a proved lemma, so no headline
  result depends on the choice of calculus.

## Proof policy

Proofs are sketched per node. The finitary cores are checked with the `lean`
skill, and Lean's own `Prop` *is* intuitionistic natural deduction, which the
capsule exploits:

- **Propositional fragment — proved outright.** Every equivalence in the
  catalogue, functional completeness, NNF/CNF/DNF existence, **soundness**, and
  **Post's completeness theorem** for a finite language go through in plain
  Lean 4 (truth assignments as `String → Bool`, wffs as an inductive type,
  `decide` for the finite tautology checks). The ND ⟺ Hilbert equivalence is
  formalized.
- **First-order fragment — full proof attempt.** Terms, formulas, substitution
  with the capture condition, structures, and Tarski satisfaction are
  formalized as inductive types with their recursions. **Soundness** is proved.
  The **Henkin construction and Gödel completeness** are formalized as far as
  feasible: where Mathlib's `FirstOrder.Language` and its completeness theorem
  are available they are cited and connected; where not, the construction is
  carried in plain Lean with every remaining gap (`sorry`, cited lemma,
  informal-to-formal step) recorded explicitly in
  `validation/proof-checks.md`. **Compactness** and **downward LS** are then
  derived from whatever completeness we actually have. The release ships with
  `lean_status` honest per node — `core`, `mathlib_cited`, `partial`, or
  `stated` — and never upgrades an epistemic label past the kernel.
- **Boundary nodes** carry `lean_status: none` and epistemic status
  `stated_not_proved` / `heuristic` by policy.
- **`bc`** enumerates truth tables (`2^n` rows), counts tautologies and the 16
  binary connectives, checks Sheffer/Peirce functional completeness by
  exhaustion, and runs small finite-model checks (a 2- or 3-element structure
  satisfying / refuting a sentence, `∀x∃y` vs `∃y∀x` on a concrete relation).

## Epistemic-status policy

Labels: `primitive`, `notation_convention`, `definition`, `axiom` (a calculus
schema or an equality axiom), `mathematical_identity` (a logical equivalence),
`proved_theorem`, `proved_lemma`, `proposition`, `corollary`,
`metatheorem` (soundness / completeness / compactness / LS — a claim *about* the
calculus and semantics), `constructive_result`, `nonconstructive_result`,
`stated_not_proved` (the incompleteness / undecidability boundary),
`heuristic` (Church–Turing), `counterexample`, `deprecated`.

`lean_status` per node: `core` (genuine plain-Lean proof), `mathlib_cited`
(connected to a Mathlib result, that result trusted), `partial` (formalized with
recorded gaps), `stated` (statement only), `instance` (`decide` sample),
`none`.

**Constructive grade** — the per-node hook, one of:
`intuitionistic` (derivable in minimal/intuitionistic ND, i.e. Lean without
`Classical`), `needs_LEM` (excluded middle / `∨` with its negation),
`needs_DNE` (double-negation elimination / `by_contra` / RAA),
`needs_full_classical` (LEM + choice-flavoured metatheory, e.g. completeness via
an arbitrary maximal extension). Examples: `¬∃x φ ⟺ ∀x ¬φ` is `intuitionistic`;
`¬∀x φ ⟺ ∃x ¬φ` is `needs_LEM`; `¬¬φ → φ` and proof by contradiction are
`needs_DNE`; De Morgan `¬(p ∧ q) → (¬p ∨ ¬q)` is `needs_LEM` (the converse is
`intuitionistic`); Post/Gödel completeness is `needs_full_classical`.
