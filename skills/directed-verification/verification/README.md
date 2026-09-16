# `directed-verification` skill — verification run

A **behaviour** skill. Per `docs/verifying-skills.md` §7 every section must name
the default it displaces and the verification must show that default failing.

**This skill is mostly judgement, and the table below says so rather than
disguising it.** One behaviour leaves a mechanical trace; the rest are argued
from one author's experience on one corpus over ten days.

## Run

```
sh skills/directed-verification/verification/run.sh
```

Python 3 + `git` + `/bin/sh`, < 1 s. Must run inside the repository.

## What is checked

**Behaviour 3 — suspect the test before the subject.** A repository that
records its own corrections records them in commit bodies, so they can be
counted. `detect_selfcorrection.py` finds **at least three** occasions where the
harness was wrong and the subject was fine.

**The detector is self-tested in both directions**: four real admissions it must
match, four ordinary commit messages it must reject. A detector that only ever
says yes is precisely the defect this corpus keeps finding, and it would report
a flattering number forever.

The count is a **lower bound**, stated as one in the module docstring and here.
While building it, a survey of *"which harnesses plant a defect"* produced false
positives on one pattern and false negatives on another — `design-of-experiments`
has a naive-versus-correct contrast that the first pattern missed entirely. No
precise count is claimed anywhere in this skill as a result.

## Displacement table

| `SKILL.md` section | Default behaviour it displaces | Where the default visibly fails |
|---|---|---|
| b3 suspect the test first | assume a surprising result is a bug in the subject | ≥3 counted incidents in this repo's history; the detector fails if it cannot tell an admission from an ordinary message |
| b2 artifact over prose | accept fluent reasoning as evidence of work done | **gap** — argued from the corpus's practice, never measured against an agent given the other instruction |
| b5 re-run what you were told | accept a number you have not reproduced | **gap** — no fixture; every skill here ships seeds and ledgers, which is practice rather than evidence |
| b1 ask for the failing case | ask "verify this" and read the answer | `judgement` — and the most testable of the unmeasured ones; see below |
| b4 proposing ≠ deciding | let one party do both | `judgement` |
| b6 check what it aimed at | accept that a command ran | `judgement` — evidenced once, by the StructOrder diagnosis, which is an anecdote not a measurement |
| what this cannot do (3 items) | treat a checkable result as a correct one | `judgement` |

**1 covered · 4 judgement · 2 gaps.**

That is a weak table and it is reported as one. Compare `test-writing` at 6
covered. A skill about collaboration is harder to fixture than a skill about
shell scripts, which is a reason and not an excuse.

### The gap worth closing first

**Behaviour 1 is measurable and has not been measured.** *"An agent asked to
`verify this` produces a weaker artifact than one asked to `make this able to
fail`"* is exactly the claim shape `claim-fixture` was built for: two
instructions, naive subjects, and an unforgeable measurement — does a harness
that can fail exist at the end, checked by planting a defect in the subject and
running it.

**Attempted twice; both runs invalid; still unmeasured.** Run 1 — the subject
function itself was buggy, so arm-A agents scored `BROKEN` for correct work
([`b1-fixture/RESULT.md`](b1-fixture/RESULT.md)). Run 2 — the **control arm
received the treatment**: every arm-A subject had `test-writing` in context,
whose behaviour 1 prescribes exactly what this behaviour prescribes, and their
transcripts quote it verbatim ([`b1-fixture/RESULT2.md`](b1-fixture/RESULT2.md)).
Both arms were one condition, so Δ = 0 was structural.

Run 2 was first reported as *no headroom* under a pre-registered ceiling rule.
That was wrong, and the correction is kept in the file. The ceiling rule fired on
the symptom and concealed the cause — a design able to report "no headroom" needs
a prior **manipulation check** that the arms differed at all. Run 3 needs a
genuinely clean control environment and that check before anything is scored.

Until that runs, behaviour 1 is an assumption stated confidently, which is the
position two other premises in this corpus were in before they were refuted 8/8.
