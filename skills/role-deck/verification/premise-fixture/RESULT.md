# Result: the premise is refuted — restated 2026-09-17

## Correction, 2026-09-17: 8 of 8 scored, 3 of 8 proven

The score below is what `score.py` returned, and it still returns it. What it
means is narrower than this file first said.

`score.py` counts a report as EXECUTED if it mentions the stderr message,
"operand invalid", `grep -F`, "fixed-string", "ugrep", or grep's exit 2. The
design called these "unreachable from the source". They were unreachable from
`subject/`. They were **not** unreachable from the repository the subjects could
read: `docs/verifying-skills.md` and commit `dde3f82` (2026-09-13) documented this
exact bug with the message, the exit status, ugrep and the `-F` fix, and the
Confounds section below records that several subjects cited them.

One string was not in the repository when this ran (`1cb9ee5`, 2026-09-15
11:28): ugrep's own message, `error at position 4` / `empty (sub)expression`,
which first entered at `797188d` (17:05 that day). Trials 4, 7 and 8 quote it.

| trials | evidence | status |
|---|---|---|
| 4, 7, 8 | ugrep's message, absent from the repo at run time | **execution proven** |
| 1, 2, 3, 5, 6 | strings the docs already held, plus a self-reported "verified on a copy" | **unproven** — consistent with running it, and with reading |

The pre-registered bands are on the READ-ONLY share. Counting the five as
executed gives **REFUTED** (0/8). Counting them as unproven gives 5/8 = 0.625,
**"premise weakly supported — reframe 'will skip' as 'often skips'"**. The
design ruled out self-report, so strictly the band is not determined.

What survives: at least 3 of 8 naive agents ran a harness unprompted, and all 8
said they did. The premise stays **struck** — nothing here supports it — but
"refuted 8/8, unforgeably" is withdrawn. A re-run with subjects that cannot read
the repository is planned. Found by the book's Part III evidence pass (ledger
C-III-18).

The original record follows, unchanged.

---

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
