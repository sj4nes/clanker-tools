# clanker-tools

![A robot in a spacecraft lab holding a device labelled "PURPOSE DEVICE" projecting a holographic terrain scan](docs/assets/purpose-device.png)

A catalog of agent skills, compatible with both **Hermes** and **Claude Code**.

## Layout

```
skills/<name>/
  SKILL.md          top-level, YAML frontmatter + instruction body
  references/        linked docs, deep-dive material
  templates/         boilerplate the skill emits (optional)
templates/
  skill-template/    starting point for a new skill
.claude/skills/      symlinks into skills/ so Claude Code discovers them
```

## Skill rules

- Every skill has a top-level `SKILL.md` with valid YAML frontmatter: `name`,
  `description` (required); `version`, `author`, `tags` (optional).
- Each skill is self-contained in its own directory under `skills/`.
- Linked docs go in `references/`; boilerplate goes in `templates/`.
- **Truncation gate:** each `SKILL.md` is capped at 20,000 characters. If a
  skill outgrows that, split it or move depth into `references/`.
- No secrets or runtime state in skill files — skills are procedural memory,
  not config.

## Skills

Each skill packages a disciplined workflow for one command-line tool — how an
agent should use it carefully, what it must never be used for, and how to verify
the result. They all follow the same shape: a `SKILL.md` with the core doctrine
and `references/` holding the deep-dive material.

| Skill | Purpose |
|---|---|
| [`ed`](skills/ed/SKILL.md) | Editing source and config files with the `ed` line editor as a controlled inspect → target → change → verify → validate → write transaction. YAML and Rust specifics in [`references/`](skills/ed/references/). |
| [`bc`](skills/bc/SKILL.md) | Exact, reproducible, reviewable calculations with the `bc` calculator: explicit precision policy, explicit rounding (bc truncates), and validation. Patterns, math library, and validation checks in [`references/`](skills/bc/references/). |
| [`tsort`](skills/tsort/SKILL.md) | Deriving evidence-backed, dependency-respecting execution orders with `tsort` — migrations, rollouts, build/release stages — plus cycle detection and keeping planning separate from execution. Worked graphs and a planning script in [`references/`](skills/tsort/references/). |
| [`ptx`](skills/ptx/SKILL.md) | Building a keyword-in-context index of curated project text for terminology mapping and exact-word discovery, then confirming every lead with `rg`/`grep`. Corpus design, discovery workflow, and command patterns in [`references/`](skills/ptx/references/). |
| [`csplit`](skills/csplit/SKILL.md) | Splitting text files into context-defined sections (line number, regex boundary, repeated marker) into an isolated directory, with mandatory piece verification and lossless-reconstruction checks. Boundary semantics, format guidance, and a transactional template in [`references/`](skills/csplit/references/). |
| [`tla-checker`](skills/tla-checker/SKILL.md) | Modelling bounded concurrent/distributed/transactional systems in a TLA+ subset with `tla-checker` — exhaustive state exploration, safety invariants, deadlock and bounded-liveness checks, and counterexample traces as debugging evidence. Analytics/modes and modeling guidance with worked examples in [`references/`](skills/tla-checker/references/). |
| [`lean`](skills/lean/SKILL.md) | Stating, developing, and checking machine-verified proofs with Lean 4 / Lake / Mathlib — clarify claim, formalize definitions, search existing results, prove incrementally, check narrowly, report scope. Distinguishes what the kernel verified from what remains to establish about the real system. Tactic/diagnostic discipline and stateful-modeling examples in [`references/`](skills/lean/references/). |
| [`physics-formula-tree`](skills/physics-formula-tree/SKILL.md) | **Meta skill.** Building a curated, dependency-ordered physics knowledge package for one bounded domain — a DAG of primitives, conventions, first-class assumptions, laws, derivations, and canonical formulas linearized with `tsort`. Orchestrates the `tsort`, `bc`, `lean`, `ptx`, `csplit`, and `ed` skills. Package layout, schemas, relation types, cycle handling, skill hand-offs, and a full worked slice in [`references/`](skills/physics-formula-tree/references/). |
| [`physics-newtonian`](skills/physics-newtonian/SKILL.md) | **Knowledge capsule** (built with `physics-formula-tree`). Newtonian point-particle mechanics as a 58-node dependency graph: kinematics, Newton's laws, work/energy, momentum, SHM, gravitation — each formula with symbols, SI units, `[M L T]` dimensions, exactness label, first-class assumptions, a limiting-case check, failure modes, and a source. Graph/formulas/indexes and a full verification run in the skill directory. |
| [`physics-thermoacoustics`](skills/physics-thermoacoustics/SKILL.md) | **Knowledge capsule** (built with `physics-formula-tree`). Linear thermoacoustics as a 104-node graph: ideal-gas + thermodynamic + transport prerequisites, linear acoustics, thermal/viscous penetration depths, Rott's wave equation with the complex `f`-functions, Swift's short-stack results, standing-wave vs traveling-wave (Stirling) device analysis, the Carnot limit. `[M L T Θ]` basis, complex phasor fields; 10 nodes at `draft` pending source reconciliation. |
| [`math-theorem-tree`](skills/math-theorem-tree/SKILL.md) | **Meta skill** (adapted from `physics-formula-tree` — first cross-field adaptation). Building a curated, dependency-ordered pure- or applied-mathematics knowledge package for one bounded domain — a DAG of primitives, notation conventions, definitions, axioms, structures, first-class hypotheses, theorems, constructions, and counterexamples linearized with `tsort`. Dimensions become types, exactness labels become epistemic/proof status, assumptions become hypotheses, limiting cases become specializations, failure modes become hypothesis-dropped counterexamples, and `lean` becomes the primary verification tool. Orchestrates `tsort`, `lean`, `bc`, `ptx`, `csplit`, `ed`. Package layout, schemas, relation types, cycle handling, and a full worked slice (Bolzano–Weierstrass) in [`references/`](skills/math-theorem-tree/references/). |
| [`math-real-analysis`](skills/math-real-analysis/SKILL.md) | **Knowledge capsule** (built with `math-theorem-tree`; its proof-of-method). Real Analysis I as a 109-node dependency graph: ℝ as a complete ordered field, sequences and series, the topology of ℝ, continuity, differentiation, Riemann integration, uniform convergence. Every result carries typed symbols, a well-formedness check, an epistemic/proof status (`proved_theorem` / `nonconstructive_result` / …), its full hypothesis list, a specialization, a hypothesis-dropped counterexample, a proof provenance with explicit Lean status, and a source. 247 edges, acyclic; 12 kernel-checked algebraic cores (`omega`/induction + `decide` instances, no Mathlib); `bc` counterexample worksheets. |
| [`formula-tree-tutorial`](skills/formula-tree-tutorial/SKILL.md) | **Meta skill.** Turn a `physics-formula-tree` capsule into a tutorial for people — a plain-Markdown document that runs under [`upmd`](https://upmd.dev) so the reader executes each formula's dimensional check, limiting case, and worked example interactively in a real terminal. Linearizes the capsule's `tsort` order into a lesson, one runnable `bc` block per concept wired by `deps:`, verified by `upmd --ci --all`. upmd mechanics, node→section authoring, and the document skeleton in [`references/`](skills/formula-tree-tutorial/references/). |

## Verification

The runnable examples were exercised on macOS (BSD userland: `ed`, `tsort`,
`csplit`) with GNU `bc` 7.x, GNU `ptx` 9.11, `tla` 0.6.11, and Lean 4.33.1. Every
skill has now been run against its real tool. Findings folded back into the skills:

| Skill | Status | Notes |
|---|---|---|
| `ed` | verified | All `SKILL.md` and `references/` examples run as written on BSD `ed`. |
| `bc` | verified, **fixed** | The `x / 1` truncation idiom does **not** truncate on the macOS/FreeBSD `bc`; rounding helpers rewritten to drop to `scale = 0` for the division only. Base-conversion example corrected — after `ibase = 16`, `obase = 10` means base-16 ten, so set `obase` first or use `obase = A`. |
| `tsort` | verified, **fixed** | BSD `tsort` exits `0` on a cycle (writes `cycle in data` to stderr); cycle detection now checks stderr, not just exit status. |
| `csplit` | verified, **fixed** | BSD/macOS `csplit` lacks `{*}`, `-b`, `--`, `--suppress-matched`, `-z`, `--version`. Added a GNU-vs-BSD table and a portable numeric-split recipe (`grep -n` → line-number args); transactional template rewritten to run on both. |
| `ptx` | verified, **fixed** | Checked against GNU coreutils `ptx` 9.11. Confirmed the central caveat concretely: the default keyword regex is letters-only, so `cache_key` → `cache` + `key`, `retry-policy` → `retry` + `policy`, CamelCase stays whole, matching is case-sensitive. Added `-W '[A-Za-z0-9_]+'` to index identifiers atomically and `ptx -A` for free `file:line:` provenance; both verified. |
| `lean` | verified, **fixed** | Checked against Lean 4.33.1 / Lake 5.0.0 (no Mathlib available). Plain-Lean snippets run as written. `List.length_append` `cons` case needed `Nat.add_right_comm` without Mathlib (bare `simp [ih]` leaves an arithmetic goal); `debit_nonnegative` uses `Int.sub_nonneg` — the general `sub_nonneg` is Mathlib-only. Mathlib-dependent examples (`example ... import Mathlib`, the `reserve_preserves_wellFormed` script) are labelled as requiring Mathlib and shape-not-literal. |
| `physics-formula-tree` | verified via two capsules | Method exercised end-to-end building the 58-node Newtonian and 104-node thermoacoustics capsules. Fixes folded back: `bc` identifiers must be lowercase and start with a letter (`Pr`, `_d` fail); Lean without Mathlib has no `ring`/complex, so fall back to kernel-`decide`d `Int` instance checks (complex as `(re,im)` pairs) and record what stays unproven; BSD `tsort` cycle check (from the `tsort` skill) confirmed necessary; derive view-generator inputs from the node registry, not hard-coded lists. |
| `physics-newtonian` | verified, **fixed** | `build/build-tree.sh`: 58 nodes, 145 edges, `tsort` acyclic, every edge respected. `bc` 7.0.3: 13/13 formulas dimensionally consistent (one check sign-typo caught by the `0 0 0` gate, then fixed). Lean 4.33.1 (no Mathlib): 5/5 `Int` instance checks pass after rewriting `½` factors as `(2·expr)/2` to survive integer division. `ptx` 9.11 used as a discovery pass with whole-token confirmation. |
| `physics-thermoacoustics` | verified, **fixed** | `build/build-tree.sh`: 104 nodes, 253 edges, `tsort` acyclic, every edge respected; one isolated assumption node caught by the coverage step and edged. `bc` 7.0.3: 19/19 checks consistent on the `[M L T Θ]` basis (`Pr`→`pr`, `_d`→`dd` name fixes). Lean 4.33.1 (no Mathlib): 13/13 `Int` instance checks, complex fields as `(re,im)` pairs. `gen-assumption-index.sh` rewritten to read the node registry. 10 nodes at `draft` (Rott/Swift coefficient forms pending a line-by-line source pass). |
| `math-theorem-tree` | verified via `math-real-analysis` | Adapted from `physics-formula-tree` for pure/applied mathematics; exercised end-to-end building the 109-node real-analysis capsule. Adaptations confirmed: node types → definition/axiom/structure/hypothesis/theorem/counterexample; exactness label → epistemic status (`proved_theorem` / `nonconstructive_result` / …) with a separate per-node `lean_status`; dimensional check → type/well-formedness check; limiting case → specialization; failure modes → hypothesis-dropped counterexamples (computed with `bc`); `lean` as the epistemic gate. Fixes folded back into `references/`: `bc`'s `n % 2` is scale-dependent (use a sign-flip variable); `ptx -A -r` errors on multi-file input (feed one cleaned stream); `omega` proves linear ℤ cores universally but not division by a variable; equivalent definitions collapse to one node to pre-empt definitional cycles. |
| `math-real-analysis` | verified, **fixed** | `build/build-tree.sh`: 109 nodes, 247 edges, BSD `tsort` **acyclic** (stderr-checked), every edge respected, 0 isolated, 5 roots = declared primitives. 5 would-be cycles (completeness pentagon, limit⟺continuity, derivative⟺continuity, compact⟺seq-compact, IVT route) designed out in advance. `lean` 4.33.1 (no Mathlib): `validation/proof-checks.lean` exit 0 — genuine `omega`/induction proofs of the triangle/squeeze/telescope/ratio-bound cores, `decide` instances for the nonlinear identities. `bc` 7.0.3: clean run; √2 recursion exact to 40 places and shown to fail in ℚ; `x^n` sup 1 on `[0,1]` vs → 0 on `[0,0.9]`. **Fixes:** `bc` `n % 2` sign-flip; `ptx` multi-file → single-stream; IVT edge to `connected_iff_interval` dropped (canonical proof is the direct `lub_axiom` argument). |
| `formula-tree-tutorial` | verified via `pendulum.md` | Built `skills/physics-newtonian/tutorial/pendulum.md` (9 blocks, `newton_second_law` → `simple_pendulum`) and ran it: `upmd 0.2.3 --ci --all` → all 9 blocks exit 0, no `failed to start`; `--ci -b chk_simple_pendulum` pulls the correct dep chain; capstone predicts `T = 2.006 s` for a 1 m pendulum and `PASS`es. Fixes folded back: upmd runs *every* fenced block, so formulas go inline not in `text`/indented fences; `bc` uppercase-name rule reconfirmed (`A`→`amp`); standalone run is `upmd --ci -b NAME FILE`, not `-b NAME --yes` (which needs a TTY). |
| `tla-checker` | verified, **fixed** | Checked against `tla 0.6.11`. `Counter` reaches a deadlock at `x = Limit` — example now uses `--allow-deadlock` and explains why. `Lease` was missing an `epoch < MaxEpoch` guard (immediate `TypeOK` violation) and `EXTENDS FiniteSets` for `Cardinality`; both fixed, now 13 states clean. `RetryCharge` produces the claimed duplicate-charge counterexample. Added `--validate`, `--list-invariants`, `--trace-json` / `--save-counterexample` / `--replay`; version corrected from 0.3.11; verified JSON shape documented. |

## Adding a skill

1. `cp -r templates/skill-template skills/<name>`
2. Fill in `SKILL.md` frontmatter and body; add `references/` as needed.
3. `ln -s ../../skills/<name> .claude/skills/<name>` for Claude Code discovery.
4. Add a row to the table above.
