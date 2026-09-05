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

## Verification

The runnable examples were exercised on macOS (BSD userland: `ed`, `tsort`,
`csplit`) with GNU `bc` 7.x, GNU `ptx` 9.11, and `tla` 0.6.11. Every skill has now
been run against its real tool. Findings folded back into the skills:

| Skill | Status | Notes |
|---|---|---|
| `ed` | verified | All `SKILL.md` and `references/` examples run as written on BSD `ed`. |
| `bc` | verified, **fixed** | The `x / 1` truncation idiom does **not** truncate on the macOS/FreeBSD `bc`; rounding helpers rewritten to drop to `scale = 0` for the division only. Base-conversion example corrected — after `ibase = 16`, `obase = 10` means base-16 ten, so set `obase` first or use `obase = A`. |
| `tsort` | verified, **fixed** | BSD `tsort` exits `0` on a cycle (writes `cycle in data` to stderr); cycle detection now checks stderr, not just exit status. |
| `csplit` | verified, **fixed** | BSD/macOS `csplit` lacks `{*}`, `-b`, `--`, `--suppress-matched`, `-z`, `--version`. Added a GNU-vs-BSD table and a portable numeric-split recipe (`grep -n` → line-number args); transactional template rewritten to run on both. |
| `ptx` | verified, **fixed** | Checked against GNU coreutils `ptx` 9.11. Confirmed the central caveat concretely: the default keyword regex is letters-only, so `cache_key` → `cache` + `key`, `retry-policy` → `retry` + `policy`, CamelCase stays whole, matching is case-sensitive. Added `-W '[A-Za-z0-9_]+'` to index identifiers atomically and `ptx -A` for free `file:line:` provenance; both verified. |
| `tla-checker` | verified, **fixed** | Checked against `tla 0.6.11`. `Counter` reaches a deadlock at `x = Limit` — example now uses `--allow-deadlock` and explains why. `Lease` was missing an `epoch < MaxEpoch` guard (immediate `TypeOK` violation) and `EXTENDS FiniteSets` for `Cardinality`; both fixed, now 13 states clean. `RetryCharge` produces the claimed duplicate-charge counterexample. Added `--validate`, `--list-invariants`, `--trace-json` / `--save-counterexample` / `--replay`; version corrected from 0.3.11; verified JSON shape documented. |

## Adding a skill

1. `cp -r templates/skill-template skills/<name>`
2. Fill in `SKILL.md` frontmatter and body; add `references/` as needed.
3. `ln -s ../../skills/<name> .claude/skills/<name>` for Claude Code discovery.
4. Add a row to the table above.
