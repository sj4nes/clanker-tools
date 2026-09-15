# Worked example: a real diagnose run

`structorder-drift.ledger.json` is the first run of any deck in this skill
against a real question in a codebase that did not produce the skill.

    python3 run_deck.py log    --ledger examples/structorder-drift.ledger.json
    python3 run_deck.py verify --ledger examples/structorder-drift.ledger.json

**The question.** StructOrder (`~/work26/twim`) is an authoring tool whose
premise is detecting drift in novels. Its product brief carried, as that
round's Open Question: *"Is the current mental model of what we provide users
actually correct, or has it drifted from what's been built?"* — the founder's
own question, not one invented for the exercise.

**The run.** 10 plays, spend 11/11, all seven roles worn, three instruments
invoked, one reroll, ledger verified. Seed 20260915.

**What it got right.** Story 5-1 "assemble a Direction" — labelled backlog and
called the signature differentiator — is built: canon-aware through injected
repositories, 46 test assertions across three modules, reachable through three
tested API routes, with commits six weeks past the brief's snapshot.

**What it got wrong, and why the file is kept.** The run concluded *"the
tracker is stale, update it."* Wrong: the project had already abandoned that
tracker for `kata`. The WHITE hat had gathered `sprint-status.yaml` (last
touched a month before the code it described, commit message *"wip lots of
weird lol"*) and a build-state block from the brief — both fossils of a dead
process. **Every fact gathered was true and the conclusion was wrong.**

Grounding worked perfectly and was worthless: it proves a command *ran*, never
that it was aimed at something alive. That is the skill's own "a command is not
the right command" limitation, which had been filed as a mild caveat about
relevance and is not mild. Two `BACKLOG.md` items come from this run.

One thing did hold. **The ledger does not lie about what was done** — it
records exactly which sources were read, so the error was diagnosable in
seconds rather than mysterious. An audit trail that only looks good when
nothing went wrong is decoration; this is the case it exists for.

## Why this is not wired into `verification/`

A ledger is bound to its deck version by design — `verify` reports a problem
when they diverge, which is correct behaviour and makes an archived ledger
useless as a version-independent regression test. It would fail on the next
legitimate edit to `decks/diagnose.json` and teach nothing. It is a **record**,
not a test.

**This has since happened, which is the point.** The ledger was written against
diagnose `0.7.0`; the deck is now `0.8.0` (`candidates` gained a `min_items`
rule), so `verify` reports:

    *** FAIL ledger was written against deck version 0.7.0, deck is now 0.8.0

That is the check working, not the example rotting. The run it records is still
exactly what happened on 2026-09-15 under 0.7.0, and the version mismatch is
the ledger refusing to pretend otherwise. Had this been wired into
`verification/`, the suite would now be red for no defect at all.
