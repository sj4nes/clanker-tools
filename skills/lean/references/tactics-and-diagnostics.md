# Tactics, diagnostics, and discipline

## Environment verification

Before editing or proving anything, inspect the Lean project environment.

```sh
command -v lean && lean --version
command -v lake && lake --version

find . -maxdepth 2 \
  \( -name 'lean-toolchain' -o -name 'lakefile.lean' -o -name 'lakefile.toml' \) -print
sed -n '1,200p' lean-toolchain 2>/dev/null || true
sed -n '1,260p' lakefile.lean 2>/dev/null || true
sed -n '1,260p' lakefile.toml 2>/dev/null || true
```

Lean 4 uses Lake as build system and package manager; projects are initialized with `lake init`, configured through a Lake file, built with `lake build`.

If the project uses Mathlib, inspect the declared dependency and existing import conventions. For a Mathlib checkout or dev environment, precompiled `.olean` cache may be available:

```sh
lake exe cache get
lake build Mathlib.Algebra.Group.Defs   # build one module
```

Do not run `lake clean` or `rm -rf .lake` unless necessary, understood, and authorized — they remove build state and trigger costly rebuilds.

## Project discovery

```sh
find . -type f \( -name '*.lean' -o -name 'README.md' -o -name 'CONTRIBUTING.md' \) \
  -not -path './.lake/*' -print | sort

grep -RIn --include='*.lean' \
  -- 'namespace\|theorem\|lemma\|example\|structure\|inductive\|def\|axiom\|sorry' .
```

Look for: existing namespaces, imports, naming conventions; use of `theorem`/`lemma`/`example`/`def`; existing assumptions or axioms; existing Mathlib tactic use; linter config; file/module naming requirements; where scratch proofs vs public API theorems belong; existing proof style (term proofs, tactic proofs, `calc`, rewriting, induction, automation). Do not add `import Mathlib` unless that is already project convention. Prefer the smallest known sufficient import; start by copying the nearest relevant local file's import style.

## Diagnostic tools

```lean
#check Nat.add_comm
#check List.length_append
#print Nat.add_comm
```

Use in a scratch file or an allowed local exploration area; remove temporary probes from committed files unless they are intended pedagogical examples. `set_option pp.all true` can temporarily reveal elaborated terms and coercions — do not leave noisy options enabled in normal proof files.

## Tactic selection

Use the least powerful tactic that clearly expresses the proof obligation.

| Goal shape | Preferred approach |
|---|---|
| Definitional equality | `rfl` |
| Exact existing theorem | `exact theorem_name ...` |
| Goal matches lemma conclusion | `apply lemma_name` |
| Controlled rewrite | `rw [lemma]` |
| Canonical simplification | `simp` / `simpa` (prefer `simp [SpecificDefs]`) |
| Explicit transformation chain | `calc` |
| Numeric closed goal | `norm_num` |
| Commutative (semi)ring polynomial identity | `ring` / `ring_nf` |
| Linear arithmetic with hypotheses | `linarith` |
| Nonlinear polynomial arithmetic | `nlinarith` |
| Presburger arithmetic over Nat/Int | `omega` |
| Finite logical search / routine goals | `aesop` (constrain the rule set where possible) |
| Contradictory hypotheses | `exfalso`, `contradiction`, arithmetic contradiction |
| Equality of structured objects / functions | `ext` / `funext` |
| Recursive data or recursive definition | `induction` |
| Existential goal | `refine ⟨witness, ?_⟩` |
| Conjunction goal | `constructor` / `refine ⟨?_, ?_⟩` |

Mathlib supplies `ring`, `field_simp`, `linarith`, `nlinarith`, `polyrith`, `norm_num`, `rcases`, `obtain`, `ext`, `funext`, and many more, via `Mathlib.Tactic` or specific tactic modules.

### Automation rules

Automation is acceptable when: the statement has been independently reviewed; the tactic suits the logical fragment; the proof stays maintainable; the import is justified; the tactic's success does not conceal critical assumptions; and Lean checks the result.

Automation must not be used to: avoid understanding a statement; conceal an accidental contradiction in assumptions; replace a missing specification; mask a namespace/type/coercion problem; produce a proof no reviewer can relate to the requirement; or justify a broad fragile import for one line.

For consequential safety/protocol/business-rule theorems, prefer a readable structured proof even when a one-liner exists. A hybrid is often best — e.g. surface the essential fact with `have h_sub : 0 ≤ balance - amount := sub_nonneg.mpr h_le` before `exact h_sub`, so the reviewer sees `amount ≤ balance` is what matters.

## Diagnostic failure patterns

| Symptom | Likely issue | Response |
|---|---|---|
| Unknown identifier | Missing import, wrong namespace, misspelling, unavailable decl | Search declaration; inspect imports |
| Type mismatch | Wrong theorem, bad coercion, argument order, domain mismatch | Read expected vs actual; make conversions explicit |
| Unsolved goals | Tactic made partial progress | Inspect remaining goal; pick a targeted next step |
| Failed to synthesize instance | Missing typeclass assumption or wrong domain | Add only semantically valid assumptions/imports |
| `simp` made no progress | Needed rewrite is not a simp lemma / goal not canonical | Use `rw`, `change`, `have`, or a targeted simp set |
| `linarith`/`nlinarith` fails | Goal outside supported fragment or assumptions insufficient | Normalize statement, prove a supporting lemma, or change method |
| Recursion/termination failure | Recursive def not structurally justified | Redesign the definition or give a valid termination argument |
| Timeout / slow elaboration | Search space, imports, or automation too broad | Narrow imports, split into lemmas, constrain automation |
| Compiles only with `sorry` | Proof is incomplete | Do not report success; identify the remaining obligation |

Read the goal and the error before trying another tactic. Do not keep guessing.

## Arithmetic and coercion discipline

Lean's numeric types are distinct — do not silently mix `Nat`, `Int`, `Rat`, `Real`. `Nat` subtraction truncates at zero (`(3 : Nat) - 5 = 0`); `Int` does not (`(3 : Int) - 5 = -2`). Division behaviour differs across domains; a theorem true over `Real` may need different assumptions or fail over `Nat`; coercions make goals harder to read and automation less reliable.

Before proving arithmetic properties: state the intended numeric domain; state nonzero-denominator assumptions; state order constraints; normalize coercions deliberately; use the domain-appropriate tactic (`norm_num` for closed computations, `ring` for polynomial identities, `linarith` for linear (in)equalities, `nlinarith` for nonlinear, `omega` for Presburger over Nat/Int). Use `field_simp` only after proving denominators nonzero and understanding the side goals — do not make division vanish by cross-multiplying without recording the conditions under which that is valid.

## Import discipline

Imports define available declarations, notation, instances, tactics, and automation behaviour. Rules: copy the nearest relevant local file's import style; prefer targeted imports when known; use `import Mathlib.Tactic` for exploratory work only when its breadth is acceptable; narrow imports before finalizing if the project values build performance and dependency clarity; do not remove an import just because the local proof currently compiles without it (check downstream declarations, notation, instances, generated docs); record significant imported automation dependencies in the explanation.

## Naming and file structure

Follow project conventions first. For a new proof module: use a name describing the domain and property; match the directory/module hierarchy; place reusable definitions before the theorems that depend on them; keep examples and scratch work out of production modules unless intended as documentation; use namespaces to avoid collisions; name lemmas by semantic content, not the tactic used (`reserve_preserves_wellFormed`, not `linarith_lemma_2`; `append_preserves_sorted`, not `helper1`).

## Proof quality standards

A high-quality agent-authored proof is **correct** (Lean accepts it, no unfinished placeholders), **accurate** (the statement captures the requirement), **scoped** (assumptions and domain explicit), **readable** (a reviewer can follow the strategy), **stable** (no brittle incidental rewrites, no unnecessary imports, no unconstrained automation), **reusable** (definitions and lemmas named and factored sensibly), **auditable** (verification command, toolchain, imports, assumptions documented), and **honest** (distinguishes proved facts from model assumptions and unverified implementation claims).

Split a proof into semantic lemmas when a monolithic proof obscures the argument; do not over-factor trivial one-line steps into dozens of micro-lemmas. Factor at meaningful abstraction boundaries.

## Review checklist

**Statement** — Says exactly what is required? Types appropriate? Edge cases accounted for? Preconditions explicit? Quantifiers and implication direction correct? Result non-vacuous? Strong enough to be useful without being too strong for the system?

**Definitions** — All formal terms have clear intended meanings? Relevant distinctions preserved? No hidden assumptions? State variables and transitions complete? Invalid states ruled out where appropriate?

**Proof** — Compiles with no newly introduced `sorry`/`admit`? No unreviewed axioms? Automation appropriate and constrained? Arithmetic domains/coercions correct? Each induction aligns with recursive structure? Major logical transformations visible? A reviewer would understand why it establishes the claim?

**Integration** — Correct namespaces/imports? Narrow module build passes? Broader project build passes? Project tests and linters pass when relevant? Diff limited to requested scope? Generated artifacts handled per repository policy?

## Common anti-patterns

| Anti-pattern | Why unsafe | Correction |
|---|---|---|
| `by aesop` on a critical theorem without statement review | May hide why the result holds or exploit irrelevant hypotheses | Review statement; structured proof or constrained automation |
| Adding `sorry` and reporting success | Theorem not verified | Report incomplete, or finish the proof |
| Adding an axiom to unblock a proof | Moves the claim into assumptions unproven | Document/justify the assumption or prove the missing result |
| `Nat` where negative values matter | Changes semantics, especially subtraction | Use `Int` or encode the intended constraint explicitly |
| Broad `simp` that succeeds mysteriously | Fragile, hard to audit | `simp [specific_defs]`, `rw`, or explicit intermediate lemmas |
| Heavy imports for a small lemma | Unnecessary deps, slower builds | Targeted import |
| Implementation claim from an abstract model only | Missing refinement/correspondence argument | State model scope; verify implementation separately |
| Ignoring timeouts / elaboration blowup | Hides brittle or impractical proofs | Narrow goals, split lemmas, constrain tactics |
| Deleting failing theorem assumptions | May silently weaken the requirement | Determine whether the assumption was irrelevant or the statement is wrong |
| Treating a build as complete validation | Compilation verifies the artifact, not the real-world interpretation | Report theorem scope and external assumptions |
