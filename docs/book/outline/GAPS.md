# Gaps the fat outline found

The outline was built as a concept dependency graph (`concepts.tsv`, `deps.txt`)
and linearised with `tsort`, per the `nonfiction-book` skill's step 13: no term
may be used before it is defined. Every concept was then traced to whatever
backs it.

    gap = 4      docs-only = 10      skill-backed = 6

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

+ **`skill-authoring`** — the standard, invocable. Largest payoff, clears ten
  concepts, and makes the book's Part II a description of a skill rather than a
  re-derivation of it.
+ **The collaboration content** — either a section of `skill-authoring` or its
  own skill. Decide by whether it is a distinct *workflow* or a chapter of one.
+ **`source-authority`** — already specified in the backlog.

None of these are book work. They are corpus work the book surfaced, which is
the outline doing its job.
