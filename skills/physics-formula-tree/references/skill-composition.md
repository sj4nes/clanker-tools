# Composing the companion skills

This meta skill delegates each stage to the tool skill that owns it. Invoke the
companion skill (via the Skill tool) when you reach its stage — do not
reimplement its discipline here.

| Stage (SKILL.md step) | Companion skill | Hand-off — what you give it | What it returns / enforces |
|---|---|---|---|
| 4. Import long source material | **csplit** | a textbook chapter / lecture-note file too large to review whole | reviewable sections in an isolated dir, piece verification, lossless-reconstruction check. You then formalize nodes from the sections. |
| 5. Derive prerequisite edges + 6. sort/cycles | **tsort** | `edges/dependencies.plan` (evidence comment per edge), `nodes/nodes.tsv` | the verbal edge test; commented-plan → clean-edges pattern; BSD-safe cycle detection (stderr, not just exit code); cycle-resolution protocol; "never encode an edge until both endpoints defined"; "never sort nodes within a pair". |
| 7. Dimensional checks + limiting cases | **bc** | dimension exponents of LHS/RHS; limiting-case expressions (`v=0`, `v/c→0`, leading corrections) | exact decimal arithmetic, explicit precision policy, explicit rounding (bc truncates). Record status in the formula YAML `dimension_check_status` and `validation/dimensional-checks.md`. **bc has no vectors, and every identifier must be lowercase and start with a letter** (`Pr`, `_d` both fail; `pr`, `dd`, `x_y` are fine) — represent each quantity as one lowercase scalar per base-dimension exponent (`<q>m <q>l <q>t`, plus `<q>h` for `Θ` when temperature is in the basis) and let each check print all-zeros for LHS−RHS. A single non-zero component is a real inconsistency (or a typo in the check — the zero-gate catches both). For a 4-exponent basis a `define p4(a,b,c,d)` print helper keeps the checks readable; call it as `dd = p4(...)` so bc does not echo the return value. |
| 7. Derivation / identity verification | **lean** | the algebraic or calculus step a node's `derivation status` claims ("K derived exactly from work-energy theorem", `sin²+cos²=1`, constant-`a` integration → kinematics set) | a kernel-checked statement, and an explicit split between what Lean verified (the math step) and what stays assumed (regime, physical premises). Never claim Lean validated the physics. Record in `validation/derivation-checks.md`. **If Mathlib is unavailable** there is no `ring`/`nlinarith`/`linarith` over the reals — fall back to kernel-`decide`d instance checks over `Int` at sample values (label them "instance check, not universal proof"; note that Int `/` truncates, so write `(2*expr)/2` to keep `½` factors exact). Upgrade to `by ring` when Mathlib is present. |
| 8. Symbol index / KWIC navigation | **ptx** | the curated formula corpus (`formulas/*.yaml`, domain `.md` views) | a keyword-in-context index (`-W '[A-Za-z0-9_]+'` keeps `v_0`, `mu_0` atomic; `-A` gives `file:line:` provenance). Discovery aid only — confirm every hit with `rg`. Feeds `indexes/symbol-index.md`. |
| 9. Edits to TSV / plan / YAML | **ed** | the specific line-oriented change to a structurally sensitive file | inspect → target → change → verify → validate → write transaction; minimal reviewable diffs instead of file rewrites. |

## Stages this skill owns directly (no companion)

- **1–3. Scope, layout, primitive selection** — judgement calls; see `scope.md`
  discipline in SKILL.md.
- **4. Node formalization** — writing registry rows and detail pages.
- **8. View generation** other than the symbol index — topic/assumption/formula
  indexes, reverse-dependency index, minimal prerequisite paths (from graph
  structure, not the flat `tsort` list), generalization map, misuse index.
- **10. Versioning and maintenance** — changelog, reverse-dependency impact
  analysis before foundational edits.

## Skills deliberately not used

- **tla-checker** — the tree is not a concurrent/transactional state machine.
  (An exception: if a release models a *protocol-like* physical process with
  discrete states and invariants, that specific sub-model could use it — but that
  is outside the formula-tree method.)

## Order of invocation in a typical build

```text
csplit   (once, if importing bulk source)
  -> formalize nodes (this skill)
  -> tsort  (edges, validate, sort, resolve cycles)   <-- iterate
  -> bc     (dimensional + limiting-case checks per formula)
  -> lean   (derivation steps that claim exactness)
  -> ptx    (symbol / KWIC index)
  -> generate remaining views (this skill)
  -> ed     (any subsequent small correction)
```
