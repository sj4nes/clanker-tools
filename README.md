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

Each skill packages a disciplined workflow for one classic Unix tool — how an
agent should use it carefully, what it must never be used for, and how to verify
the result. All five follow the same shape: a `SKILL.md` with the core doctrine
and `references/` holding the deep-dive material.

| Skill | Purpose |
|---|---|
| [`ed`](skills/ed/SKILL.md) | Editing source and config files with the `ed` line editor as a controlled inspect → target → change → verify → validate → write transaction. YAML and Rust specifics in [`references/`](skills/ed/references/). |
| [`bc`](skills/bc/SKILL.md) | Exact, reproducible, reviewable calculations with the `bc` calculator: explicit precision policy, explicit rounding (bc truncates), and validation. Patterns, math library, and validation checks in [`references/`](skills/bc/references/). |
| [`tsort`](skills/tsort/SKILL.md) | Deriving evidence-backed, dependency-respecting execution orders with `tsort` — migrations, rollouts, build/release stages — plus cycle detection and keeping planning separate from execution. Worked graphs and a planning script in [`references/`](skills/tsort/references/). |
| [`ptx`](skills/ptx/SKILL.md) | Building a keyword-in-context index of curated project text for terminology mapping and exact-word discovery, then confirming every lead with `rg`/`grep`. Corpus design, discovery workflow, and command patterns in [`references/`](skills/ptx/references/). |
| [`csplit`](skills/csplit/SKILL.md) | Splitting text files into context-defined sections (line number, regex boundary, repeated marker) into an isolated directory, with mandatory piece verification and lossless-reconstruction checks. Boundary semantics, format guidance, and a transactional template in [`references/`](skills/csplit/references/). |

## Adding a skill

1. `cp -r templates/skill-template skills/<name>`
2. Fill in `SKILL.md` frontmatter and body; add `references/` as needed.
3. `ln -s ../../skills/<name> .claude/skills/<name>` for Claude Code discovery.
4. Add a row to the table above.
