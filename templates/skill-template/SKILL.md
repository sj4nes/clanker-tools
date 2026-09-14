---
name: skill-name
description: >-
  One or two sentences. State what the skill does and, critically, the
  conditions under which an agent should reach for it ("Use when...").
  This text is the only thing matched against a task, so make triggers explicit.
version: 1.0.0
# MAJOR.MINOR.PATCH, per docs/skill-versioning.md.  1.0.0 = as verified at
# release.  Then: MAJOR = the skill was WRONG (the reader must re-do work);
# MINOR = a statement changed or grew (re-read, nothing to re-do); PATCH =
# nothing semantic.  Bump in the SAME COMMIT as the change; `sh
# tools/check-skills.sh` asserts the shape, not the honesty.
author: Your Name
tags: [topic, tool, domain]
---

# Skill Title

Opening paragraph: what role the agent is playing and what outcome it owns.

## Principles

- The non-negotiable rules, most important first.

## Workflow

1. Ordered steps the agent follows.
2. Keep each step verifiable.

## References

Link supporting docs kept in `references/`:

- [`references/example.md`](references/example.md)

## Completion report

What the agent must report back when done.
