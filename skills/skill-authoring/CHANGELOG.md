# Changelog — skill-authoring

Versions follow [`docs/skill-versioning.md`](../../docs/skill-versioning.md):
`1.0.0` means "as verified at release"; **MAJOR** = the skill was wrong (re-do
work done under the old text), **MINOR** = a statement changed or grew (re-read
it), **PATCH** = nothing semantic.

    git log -- skills/skill-authoring/

## 1.0.0 — 2026-09-15

First release. Found by building the book's fat outline as a concept dependency
graph: 10 of 23 concepts were backed only by `docs/`, so the standard governing
50 skills was not itself invocable. Adds the organizing idea those docs lack —
**the archetype decides which standard applies** — plus an `archetype:` field
migrated across all 50 skills (behaviour 19, capsule 15, tool-fact 10, meta 6)
and a checker that holds each to its own requirements. First run: 35 failures
across 29 skills, with two of the first corrections going to the checker rather
than to any skill.
