# Gaps the fat outline found

The outline was built as a concept dependency graph (`concepts.tsv`, `deps.txt`)
and linearised with `tsort`, per the `nonfiction-book` skill's step 13: no term
may be used before it is defined. Every concept was then traced to whatever
backs it.

    gap = 4      docs-only = 10      skill-backed = 6

That was the count when the outline was built (3890836, 2026-09-15). The
sections below are kept as that record.

## Status, 2026-09-17: two of three gaps built, one of them weak

| gap | now | backs | state |
|---|---|---|---|
| the standard is not a skill | `skills/skill-authoring` 1.1.0 (197b313; stale statements fixed b3ad6e6) | II.7, and the ten docs-only concepts | harness passes; its checker's gates are each broken alone. **II.7 drafted 2026-09-17**; drafting found two stale statements in the skill and that its proposed harness-first check is silent for 17 of 21 skills (ledger C-II-56..59). |
| the collaboration | `skills/directed-verification` 1.3.0 (6fbfac2; evidence fixed 8097530) | II.6 (`directing-verification`, `agent-as-collaborator`) | built, and **reported weak**: 1 covered, 4 judgement, 2 gaps. **II.6 drafted 2026-09-17.** |
| `source-authority` | — | II.3's open problem; `directed-verification` behaviour 6 | still backlogged, still unbuilt |

"Built" is not "backed", and drafting II.6 is how that showed:

- **Behaviour 1 is unmeasured after three fixture runs**, all invalid (ledger
  C-II-20..22). The concept the book calls its differentiator rests on a skill
  whose most testable claim has never produced a result.
- **The one covered row overcounted** (C-II-47). The self-correction detector
  reported 5; two were false positives, one of them the skill's own release
  commit. The "at least three" shipped at release rested on two real matches.
  The claim is true by hand; the instrument did not show it. **Fixed in
  directed-verification 1.3.0 (8097530)**: the claim now rests on three
  hand-read commits, which a history check holds the detector to.
- **The clean evidence points the other way.** The two premise fixtures that
  did produce results found agents doing the expensive work unprompted, 8/8
  twice. So II.6 argues for directing verification on the skill's narrower
  boundary — it changes what the director can check — not on agents cutting
  corners.

So the collaboration gap is closed as a *document* and open as *evidence*. The
next thing it needs is not more prose but a fourth b1 run that clears
`claim-fixture`'s pre-flight gates. (The other need, a detector tested on the
repository's own sentences, was met in 8097530.)

## The headline: the standard governing 50 skills is not itself a skill

**Ten of the book's twenty-three concepts — the entire core of the standard —
exist only in `docs/`.** A human reading the repository can find them. An agent
working in it cannot invoke them.

| concept | lives in |
|---|---|
| default-behaviour, displacement-claim, displacement-table, judgement-row, skill-taxonomy | `docs/verifying-skills.md` §7 |
| harness | `docs/verifying-skills.md` §2 |
| negative-contrast, guard-isolation | `docs/verifying-skills.md` §8 |
| version-as-wrongness, changelog | `docs/skill-versioning.md` |

889 lines of standard, governing 50 skills, and only three skills so much as
cite it. There is a meta-skill for building a physics capsule, a math capsule,
and a tutorial from a capsule — and none for **authoring a skill to the
standard this corpus holds every skill to**.

That is the gap to take. Call it `skill-authoring`. It absorbs the ten
docs-only concepts, it is the synthesis node the dependency graph already puts
at position 21 of 23 (it depends on nearly everything), and its absence is why
the standard has to be re-explained by hand every time.

## The second gap is the book's own differentiator

Three concepts have no source at all, and they cluster:

- **agent-as-collaborator** — the agent as a participant in quality, not a
  producer of text
- **directing-verification** — how to get an agent to build the harness, plant
  the defect, run the fixture, and report what it found against you
- **authoring-to-the-standard** — the synthesis of both with the ten above

The positioning brief names the collaboration as half the book's unique angle.
**Nothing in the corpus backs it.** Fifty skills, and not one about working with
an agent to produce a verified artifact — despite every skill in the corpus
having been produced exactly that way.

This is the same shape as the premise refutations: the thing most relied upon
was the thing never written down.

## The third is already known

**source-authority** — declaring which sources are authoritative and warning
when a step reads one older than the artifact it describes. Already in
`BACKLOG.md`, from the StructOrder diagnosis where every gathered fact was true
and the conclusion was wrong. The outline independently rediscovered it as a
dependency of `independent-oracle`, which is mild corroboration that it belongs.

## What to build, in order

+ **`skill-authoring`** — **built 2026-09-15.** The standard, invocable. Largest payoff, clears ten
  concepts, and makes the book's Part II a description of a skill rather than a
  re-derivation of it.
+ **The collaboration content** — **built 2026-09-15 as its own skill,
  `directed-verification`; weak, see Status.** Either a section of `skill-authoring` or its
  own skill. Decide by whether it is a distinct *workflow* or a chapter of one.
+ **`source-authority`** — already specified in the backlog. **Still open.**

None of these are book work. They are corpus work the book surfaced, which is
the outline doing its job.
