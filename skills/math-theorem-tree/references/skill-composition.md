# Composing the companion skills

This meta skill delegates each stage to the tool skill that owns it. Invoke the
companion skill (via the Skill tool) when you reach its stage — do not
reimplement its discipline here.

| Stage (SKILL.md step) | Companion skill | Hand-off — what you give it | What it returns / enforces |
|---|---|---|---|
| 4. Import long source material | **csplit** | a textbook chapter / lecture-note / paper file too large to review whole | reviewable sections in an isolated dir, piece verification, lossless-reconstruction check. You then formalize nodes from the sections. |
| 5. Derive prerequisite edges + 6. sort/cycles | **tsort** | `edges/dependencies.plan` (evidence comment per edge), `nodes/nodes.tsv` | the verbal edge test; commented-plan → clean-edges pattern; BSD-safe cycle detection (stderr, not just exit code); cycle-resolution protocol; "never encode an edge until both endpoints defined"; "never sort nodes within a pair". |
| 7. Proofs, identities, derivations (**primary**) | **lean** | the theorem / lemma / identity a node claims, with its hypotheses; the algebraic or calculus step a proof invokes | a kernel-checked statement, and an explicit split between what Lean verified and what stays cited / assumed (lemmas taken as given, `sorry`s, the informal-to-formal gap). Record `lean_status` (`none` / `cited` / `instance` / `core-arith` / `proved`) in the result YAML and `validation/proof-checks.md` — a per-node field kept *separate* from the epistemic `status_label` so "cited standard proof" and "what this capsule's Lean file checked" are never conflated. **Never upgrade the epistemic label past what a cited checked proof or the kernel supports.** If Mathlib is unavailable there is no `ring` / `linarith` / real-analysis library, and no analytic theorem is even statable over ℝ — but **core Lean has `omega`**, giving *genuine universal* proofs of linear-integer cores (triangle inequality, squeeze / 3-ε patterns, a telescoping sum after one induction, a geometric ratio bound); `omega` cannot divide by a variable. For nonlinear identities fall back to kernel-`decide`d instance checks over `Nat` / `Int` at sample values (label "instance check, not universal proof"; Int `/` truncates, so write `(2*expr)/2` for `½` factors). Upgrade to `by ring` / Mathlib lemmas when present. |
| 7. Specializations, finite cases, numeric instances, counterexample computations | **bc** | the specialization expression (n=1, trivial group, empty set), sample points for an inequality, the arithmetic of a candidate counterexample, error-bound / convergence-rate formulas (applied) | exact decimal arithmetic, explicit precision policy, explicit rounding (bc truncates). Record status in the result YAML `checks.instances` and `validation/instance-checks.md`. **bc has no sets, sequences, or symbolic algebra** — it evaluates *instances*. Every identifier must be lowercase and start with a letter (`Pr`, `_d` fail; `pr`, `dd`, `x_y` are fine). **`n % 2` (and `%` generally) is scale-dependent** — at `scale = 40` it returns a fractional "remainder", not an integer parity; for alternating signs use a sign-flip variable (`sg = 1; … ; sg = -sg`) or drop to `scale = 0` for the modulo only. A passing instance is a sanity check or a counterexample, **never a proof** — state that in the file. |
| 8. Symbol / notation index / KWIC navigation | **ptx** | the curated corpus (`results/*.yaml`, node detail pages, area `.md` views) | a keyword-in-context index (`-W '[A-Za-z0-9_]+'` keeps `sigma_algebra`, `x_0` atomic; `-A` gives `file:line:` provenance). Discovery aid only — confirm every hit with `rg`. Feeds `indexes/symbol-index.md`. **GNU `ptx` 9.x errors (`regular expression has a match of length zero`) on some multi-file `-A -r` invocations** — feed it a single cleaned stream instead (`grep -h -v '^[[:space:]]*$' results/*.yaml notation.md > _corpus.txt`), or run it per-file. |
| 9. Edits to TSV / plan / YAML | **ed** | the specific line-oriented change to a structurally sensitive file | inspect → target → change → verify → validate → write transaction; minimal reviewable diffs instead of file rewrites. |

## The lean / bc division of labour

This is the key shift from the physics method, where `bc` (dimensional analysis)
carried most checks and `lean` handled the occasional algebra step.

- **`lean` is the epistemic gate.** A node may not carry `status_label:
  proved_theorem` (or `proved_lemma` / `proposition` / `corollary`) unless
  either (a) Lean checked it — record `lean_status` and the kernel-vs-cited
  split — or (b) a specific, checked published proof is cited and the capsule
  explicitly marks it `lean_status: cited`. Anything else is at most
  `conjecture` / `heuristic` / `numerical_evidence`.
- **`bc` is the falsification and sanity tool.** Use it to *try to break* a
  statement: drop a hypothesis and compute the candidate counterexample; check a
  claimed inequality at a grid of points; verify the specialization the entry
  claims actually holds numerically. A clean `bc` run raises confidence and
  populates `counterexamples_when_dropped`; it never discharges a proof
  obligation.
- **Applied capsules lean on `bc` more:** truncation-error orders, CFL numbers,
  spectral radii, condition numbers, convergence-rate fits are all `bc`
  worksheets; `lean` still checks the exact identities (a scheme's consistency
  order, an error-propagation recursion).

## Stages this skill owns directly (no companion)

- **1–3. Scope, foundational stance, layout, primitive/axiom selection** —
  judgement calls; see `scope.md` and `conventions.md` discipline in SKILL.md.
- **4. Node formalization** — writing registry rows and detail pages, including
  the type / well-formedness check.
- **8. View generation** other than the symbol index — topic / hypothesis /
  status / counterexample indexes, reverse-dependency index, minimal
  prerequisite paths (from graph structure, not the flat `tsort` list),
  generalization map, equivalent-definitions map, misuse index.
- **10. Versioning and maintenance** — changelog, reverse-dependency impact
  analysis before foundational edits.

## Skills deliberately not used

- **tla-checker** — the tree is not a concurrent / transactional state machine.
  (An exception: a release covering the theory of a *protocol-like* discrete
  system with states and invariants — a distributed algorithm's correctness, a
  automaton — could use it for that sub-model, but that is outside the
  theorem-tree method.)

## Order of invocation in a typical build

```text
csplit   (once, if importing bulk source)
  -> formalize nodes (this skill)
  -> tsort  (edges, validate, sort, resolve cycles)   <-- iterate
  -> lean   (state and check every proved_* node; record kernel-vs-cited)
  -> bc     (specializations, sample points, hypothesis-dropped counterexamples)
  -> ptx    (symbol / KWIC index)
  -> generate remaining views (this skill)
  -> ed     (any subsequent small correction)
```
