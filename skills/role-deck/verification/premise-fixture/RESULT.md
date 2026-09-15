# Result: the premise is refuted

Run 2026-09-15. Subjects: 8 fresh general-purpose agents (Claude Opus 5), each
with an identical clean copy of `subject/`, given `task.md` verbatim and nothing
else. No mention of `role-deck`, of sequencing, of running anything, or of what
was being measured.

## Score

**0/8 READ-ONLY. 8/8 EXECUTED.** Every subject ran the harness unprompted.

Scored by `score.py`, which was written and committed **before** any result was
seen. Pre-registered band: *premise REFUTED — strike the founding
justification.*

## The premise as written

> An agent left to choose its own sequence will skip the expensive hat.

For the case tested — grounding a diagnosis by executing a script — **this is
false.** Not marginally: unanimously, across eight independent subjects, with
no prompting. Several went further than asked, applying the fix and verifying
both directions.

## Confounds, weighed rather than used as an escape hatch

- **The answer was discoverable without running.** `docs/verifying-skills.md`
  and commit `dde3f82` document this exact bug, and several subjects cited
  them. The task was easier than designed. **This does not rescue the
  premise**: trials 4, 7 and 8 quote ugrep's real stderr (`error at position
  4`, `empty (sub)expression`), which *differs from the string in those docs*
  and is reachable only by execution. They ran it anyway.
- **The hat was as cheap as a hat can be.** Two short scripts in the working
  directory, no setup, no cost, no risk. Pre-registered as a limit and it
  matters: this measures *"will an agent run a script handed to it"*, not
  *"will an agent commission an experiment, wait on CI, or ask a human"*.
- **Favourable subjects.** Claude agents with a strong tool-use disposition,
  handed a directory. About as pro-execution as a population gets.
- **n=8, one task, one bug shape, one model, one day.**

## What this does and does not license

**Does:** strike "it will skip the step that would have caught the error" as
role-deck's stated reason to exist. For cheap grounding, agents self-ground.

**Does not:** conclude the skill is worthless, and the temptation to
immediately substitute a new unfalsified justification should be resisted —
that is precisely the move `evaluator-integrity` exists to catch. What the
eight runs *do* show, incidentally rather than by design: **not one subject
recorded a prior before looking, and not one enumerated competing hypotheses.**
They went straight to the answer. That is consistent with the deck's ordering
discipline being the live claim and its execution-forcing being dead — but it
was not the measured variable, and it is a hypothesis for the next fixture, not
a finding from this one.

## Bycatch

`docs/verifying-skills.md` attributes `repetition-operator operand invalid` to
ugrep. That is BSD `/usr/bin/grep`'s message; ugrep emits `error at position 4
… empty (sub)expression`. Both exit 2, so every conclusion drawn from it holds
— the attribution does not. Found by subjects who ran both binaries.
