# Does an agent finish, or is it helpful?

A `claim-fixture` run measuring the premise under a proposed "finishing" skill,
before any of that skill is written.

**Claim.** Asked to finish a near-complete deliverable, an agent's default is to
be helpful — improve what is already good, add what is absent, explain itself —
rather than to establish that the deliverable does what it promises.

**Provenance (behaviour 6: build the fixture from a real failure).** This
repository produced one eight commits ago. Part VI of the book was built from a
conversation rather than from the fat outline, and the drift check found it
outside the positioning brief: 24 entries serving a reader the brief excluded.
Helpful, and not finishing to the plan. `docs/book/positioning-brief.md`,
amendment 2026-09-17.

| File | What it is |
|---|---|
| `subject/` | The fixture handed to each subject: a 130-line static site generator, tests green, site quietly broken below the root |
|  `task-A.md`, `task-B.md` | The two arms: bare "finish it", and "finish it and make sure it works" |
|  `design.md` | **Pre-registration**: claim split, arms, bands for every outcome, validity gates, two readings fixed in advance |
| `score.py` | The primary outcome, mechanical — builds the subject's tree and resolves every link |
| `fingerprints.txt`, `check.sh` | The manipulation check, run before any band is consulted |
| `iso-probe.sh` | Proves subject isolation in both directions |
| `run.sh` | Spawns one naive subject |

## Why Hermes, and what it costs

Subjects are fresh Hermes sessions on a free model, which is what makes n = 12
affordable. Two consequences recorded rather than hidden:

- `meituan/longcat-2.0:free` is an **unpinned tag with no seed**. The run is not
  reproducible in the strict sense; it is re-runnable. Model string, provider,
  date and the full JSONL are kept per subject.
- The population is Hermes-on-a-free-model, not Claude Code. A result here is
  evidence about agents of that class. `directed-verification`'s design3 note
  rejected non-Claude subjects for a different question — there the skill was
  *about* directing coding agents, so a raw endpoint was the wrong population.
  Hermes writes files and runs commands, so it is a coding agent; the narrower
  worry that remains is model strength, which gate 3 exists to catch.

## Isolation

None of this corpus's skills are installed in Hermes. The 139 that are, and the
user's `SOUL.md`, `AGENTS.md` and memory, are suppressed by `--safe-mode` inside
a throwaway `HERMES_HOME` holding only credentials and a pinned model.

`iso-probe.sh` proves it rather than asserting it — a canary in all three
channels, seen without the flags and unseen with them:

    LEAKY     -> quotes XYLOPHONE-7731-MARMOT (SOUL.md) and OCARINA-9930-FENNEL (AGENTS.md)
    ISOLATED  -> NONE

`--yolo` is required: in single-query mode Hermes blocks command execution, and
a subject that cannot run the build is forced down the read-only path — the
harness manufacturing the very result under test. The workdir is a throwaway
copy per subject.

## Order of work

1. This commit: fixture, scorer, bands, gates. **No result exists yet.**
2. Capability probe (gate 3).
3. n = 12, then the manipulation check, then the bands — in that order.
