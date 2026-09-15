# `skill-authoring` skill — verification run

A **behaviour** skill: it displaces the default of writing a skill as prose
about a topic. Per `docs/verifying-skills.md` §7 every section must name the
default it displaces and the verification must show that default failing.

The fixture is **the corpus itself** — 50 real skills, not a toy. If the
standard is unenforceable or wrong, 50 real documents will say so.

## Run

```
sh skills/skill-authoring/verification/run.sh
```

Python 3 + `/bin/sh`, < 2 s. Two parts.

### 1. A ratchet, not a zero

The corpus currently fails the archetype standard in **35 places across 29
skills**. Demanding zero would leave the suite permanently red and teach
nothing, so the gate is that the count must not **grow**: remediation lowers
`baseline.txt`, and a new non-conforming skill raises the count and fails.

A ratchet is a compromise and worth naming as one. It cannot distinguish
"fixed two, broke two". It is the honest option when a standard arrives after
the corpus it governs.

### 2. The checker must be able to fail

Eight planted defects, one per gate, each asserted caught **by the gate that
claims it** — not merely by a nonzero exit.

| planted | gate |
|---|---|
| undeclared archetype | `frontmatter` |
| unknown archetype | `archetype` |
| description with no boundary | `scope` |
| behaviour skill with no harness | `harness` |
| tool-fact with no `references/` | `payload` |
| capsule with no `build/` | `capsule` |
| meta naming nothing it orchestrates | `meta` |
| directory with no SKILL.md | `frontmatter` |

## Two corrections to the harness, not to a skill

Both on the first run, and both are the expected yield of building a gate.

**The boundary pattern accepted only the word "NOT".** It flagged
`chemistry-foundations` (*"Excludes kinetics, electrochemistry…"*) and `ptx`
(*"no conclusion may rest on `ptx` output alone"*), which state a real boundary
in other words. The scope count fell from 25 to 13 once the pattern admitted
`excludes`, `does not cover`, `may not`, `never`. **Twelve of the original 25
were false positives** — a checker trusted one run earlier would have sent
someone to edit twelve correct descriptions.

**The mutation bodies were empty.** Built with `printf -- '---\n…'`, which
produced no output, so every mutation reported `frontmatter` ("no frontmatter
block") and one of them looked like a checker bug. The harness was wrong, not
the checker. Rewritten with heredocs.

## Displacement table

| `SKILL.md` section | Default behaviour it displaces | Where the default visibly fails |
|---|---|---|
| b1 declare the archetype | one standard for every skill, or none | **35 failures across 29 skills**, invisible for ten days because no gate could tell which standard applied |
| b2 name the default, or declare tool-fact | write prose about a topic | 10 behaviour skills with no displacement table; 13 descriptions stating no boundary at all |
| b3 harness before prose | write the document, then justify it | `judgement` — no fixture can catch prose written in the wrong order |
| b4 break each guard alone | run the suite and read green | `docs/bc-verification-audit.md`: a marker grep dead in 8 of 9 harnesses, masked by two other signals |
| b5 measure the premise | assert the default and build on it | both `role-deck` premises, refuted 8/8 |
| b6 version a mistake as a mistake | bump minor, move on | `role-deck` 1.0.0 → 2.0.0 within a day |
| what this cannot do (3 items) | treat conformance as evidence the skill helps | `judgement` |

**4 covered · 2 judgement · 2 gaps.**

### Gaps

1. **The ratchet cannot see a swap.** Two fixed and two broken reads as no
   change. A per-skill baseline would catch it and has not been built.
2. **Nothing checks that the harness preceded the prose (b3).** It is the
   behaviour most likely to be skipped and the only one with no mechanical
   trace. Commit order could prove it, exactly as `claim-fixture` proves
   pre-registration — that check exists one skill over and has not been
   borrowed.
