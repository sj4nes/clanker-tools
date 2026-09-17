---
name: skill-authoring
description: >-
  Author a new agent skill, or bring an existing one up to standard, so that it
  makes a claim something could disagree with. Use when writing a SKILL.md,
  reviewing one, deciding whether a draft is ready to ship, or auditing a
  corpus of them. Six behaviours: declare the archetype, because it decides
  which standard applies; name the default the skill displaces, or declare
  there is none; build the harness before the prose; break each guard on its
  own; measure the premise before building on it; and version a mistake as a
  mistake. NOT a guide to prompt phrasing, NOT a way to make an agent more
  capable, and not applicable to a document nobody will maintain — the whole
  standard is about what happens to a skill on its second reading.
version: 1.2.0
archetype: behaviour
author: Simon Janes
tags: [skills, authoring, verification, standard, corpus, meta]
---

# Authoring a skill that can be wrong

A skill is not prose about a topic. It is a **claim**: that some default
behaviour exists, that it is worse than the alternative, and that this document
moves an agent from one to the other. Written that way it can be checked.
Written as prose about a topic it cannot, and it will read beautifully either
way.

This skill is short because the detail is elsewhere and should stay there:
[`docs/verifying-skills.md`](../../docs/verifying-skills.md) is the harness
contract, [`docs/skill-versioning.md`](../../docs/skill-versioning.md) is the
version contract. What was missing — and what this adds — is the thing that
decides **which parts of those apply to the skill in front of you.**

## The six behaviours

1. **Declare the archetype. It decides the standard.** Four kinds, and holding
   one to another's standard is how a rule gets a reputation for being
   bureaucratic:

   | `archetype:` | the agent's prior | what it owes |
   |---|---|---|
   | `behaviour` | has a default, and it is wrong | a harness **and** a displacement table |
   | `tool-fact` | genuinely empty | reference material; a displacement table would be meaningless |
   | `capsule` | — | `build/` and `validation/`, not `verification/` |
   | `meta` | — | must name the skills it orchestrates |

   Undeclared, nothing can check anything, because every requirement above is
   conditional. This corpus ran 50 skills for ten days with no archetype field,
   and the first run of the checker found **35 conformance failures across 29
   of them** — not because standards had slipped, but because no gate could
   tell which standard to apply.

2. **Name the default you displace — or declare `tool-fact` and stop.** Write
   the displacement table before the prose: section → default displaced → where
   that default visibly fails. A row with an empty third cell is advice. A row
   no fixture can falsify is marked `judgement`, and naming those honestly is
   the point rather than a loophole. If you cannot name a default for any
   section, you are writing `tool-fact` and should say so.

3. **Build the harness before the prose.** Fixture-first, and not as a matter
   of taste: prose written first becomes the thing the fixture is bent to
   confirm. Build the failing case, watch it fail, and then write the document
   that quotes it. Every number in a skill body should be one the harness
   produced. **Commit the harness on its own, before the prose.** A commit
   records what was finished, not what was written first: of this corpus's 21
   behaviour skills, 17 landed harness and prose in one commit, so their history
   cannot show which came first — this skill's included. A separate commit is
   the only trace the order leaves, the same way `claim-fixture` proves a scorer
   preceded its results.

4. **Break each guard on its own.** A harness typically has three signals — a
   tool's exit status, a pass banner, a failure marker — and they mask each
   other. Plant a defect that trips exactly one, leaving the others intact. A
   guard only ever seen to fail *alongside* another has not been tested, which
   is how a dead marker grep survived in eight of nine harnesses here.

5. **Measure the premise before building on it.** Behaviour 2 asks you to name
   a default. This asks whether it is real. Use
   [`claim-fixture`](../claim-fixture/SKILL.md): split the claim, naive
   subjects, unforgeable measurement, pre-registration in its own commit. Two
   premises in this corpus were asserted confidently, built on for a day, and
   struck after fixtures took minutes — one refuted 8/8, the other with only
   3 of 8 subjects' execution proven, because its scorer accepted strings the
   repository's own docs held.

6. **Version a mistake as a mistake.** `MAJOR` means *the skill was wrong* —
   re-do work done under the old text. So `MAJOR − 1` counts the times this
   document has been wrong, and it should be a number you are reluctant to
   increment and unwilling to fudge. A version bump with no changelog entry is
   a number nobody can read.

## What this cannot do for you

- **Decide whether the skill is worth writing.** A perfectly conformant skill
  for a problem nobody has is still shelfware. Nothing here measures demand.
- **Judge whether the default you named is the *interesting* default.** The
  standard checks that you named one and that it is real, never that it was the
  one worth displacing.
- **Tell you the skill helps.** It tells you the skill makes a checkable claim
  and that the check can fail. The caution is Luu's eval, which `test-writing`
  cites: a test skill from a widely starred collection scored almost as well as
  no instructions overall, and worse than no instructions on the runs it
  actually influenced. Only reading the runs showed it. Nothing in this standard
  measures that; conformance says nothing about effect.

## Before you ship it

- [ ] `archetype:` declared, and the requirements for that archetype met.
- [ ] Every frontmatter field present; the description states a **boundary**.
- [ ] A displacement table with no empty cells (`behaviour` only), with the
      covered / judgement / gap counts reported.
- [ ] The harness was written before the prose, and has been **seen to fail**.
- [ ] Each guard has been broken in isolation.
- [ ] The premise is measured, or explicitly recorded as unmeasured.
- [ ] Version and changelog agree, and the bump level matches what changed.
- [ ] `sh tools/check-skills.sh` and this skill's checker both pass.

## Verification

[`verification/`](verification/) runs the archetype standard over **every skill
in the corpus** — the fixture is 50 real skills, not a toy — and mutation-tests
the checker itself. `sh verification/run.sh`.

The first run found 35 failures across 29 skills, and **two of the first
corrections were to the checker rather than to a skill**: its boundary pattern
accepted only the word "NOT", and flagged `chemistry-foundations` ("Excludes
kinetics…") and `ptx` ("no conclusion may rest on `ptx` output alone"), both of
which state a real boundary. That is the expected yield of building a gate.

## Related skills

- **`claim-fixture`** — behaviour 5, in full.
- **`test-writing`** — behaviours 3 and 4 at the level of a single test; its
  independent-oracle rule is what makes a harness evidence rather than an echo.
- **`skill-evolution`** — improving one skill against an evaluator once it
  exists. This skill is how it comes to exist.
- **`experience-library`** — when the corpus itself grows past the point where
  adding a skill reliably helps.
- **`docs/verifying-skills.md`**, **`docs/skill-versioning.md`** — the contracts
  this skill decides the applicability of.

## Completion report

State, briefly: the archetype and why; the default named, or that it is
`tool-fact`; that the harness preceded the prose and was seen to fail; which
guards were broken alone; whether the premise was measured; the displacement
counts; and what you did **not** verify.
