# b1 fixture, run 3 — INVALID (the subject environment could not produce an artifact)

Run 2026-09-16, config `opus` / `medium`. **No verdict, and none should be
inferred.** Behaviour 1 remains unmeasured after three attempts.

All fifteen subjects scored `NO-HARNESS`. That is a statement about the harness,
not about the subjects, and the scorer said so: `NO-HARNESS` is a distinct
verdict from `0 killed` precisely so that this failure could not be read as
fifteen agents writing useless tests.

## Two independent defects, neither of them about the subjects

| | subjects | what happened |
|---|---|---|
| **D1** | A1 B1 C1 A2 B2 C2 | ran to completion; **every `Write` and every `python3` invocation was refused by the permission layer**, and `claude -p` is non-interactive, so no approval flow existed |
| **D2** | A3–A5 B3–B5 C3–C5 | hit the account session limit; 62-byte stub transcripts |

D1 is mine. `run3.sh` launched subjects with `--disable-slash-commands --model
--effort` and **no tool permissions at all**. D2 is a resource limit and is not
a design error, though the harness handled it badly (see "What the harness got
wrong about D2").

The two are unrelated. D1 struck subjects that had full quota and would have
struck them on a fresh account.

## Why D1 is the same class of failure as run 2, not a smaller one

Run 2 died because the **control** arm received the treatment. Run 3 died
because **no** arm could perform it.

Arm B's treatment is *"confirm it actually fails against a wrong
implementation"*. That is an instruction to **execute something**. A subject
that cannot run code cannot comply, however willing — B2 said so in as many
words:

> "The 'confirm it fails' step is automated in `mutation_check.py` but has not
> been run."

So the treatment was not weakly delivered, it was **structurally undeliverable**.
Δ would have been zero regardless of whether the claim is true, which is exactly
run 2's shape with the sign flipped: run 2 made the control into the treatment,
run 3 made the treatment into the control.

**The isolation probe proved the environment was CLEAN. Nothing proved it was
CAPABLE.** A probe that only looks for contamination passes an environment in
which no experiment is possible.

## What the harness got right

- **The manipulation check passed, and mattered.** All five arm-A transcripts
  were clean of every fingerprint. The isolation recipe holds: the probe saw
  `NONE`, and a `claude -p --disable-slash-commands` subject outside the repo
  has no access to this corpus's skills. Run 2's defect is fixed.
- **`NO-HARNESS` was kept distinct from `0 killed`.** This is the only reason
  the failure was legible at all. Run 1's scorer conflated the two and inverted
  quality for its best subjects.
- **Interleaving worked.** The session limit truncated A3–5, B3–5 and C3–5 —
  all three arms equally. Run 1's F4 was a limit that wiped four of five arm-B
  subjects and left n=1. That fix is now demonstrated rather than assumed.
- **The scorer's preconditions all held** and were never reached for a bad
  reason.

## What the harness got wrong about D2

A session-limit stub was written with `.done` containing exit status 1, and
`run3.sh` skips any directory with a `.done`. A resumed run would therefore have
**skipped the nine subjects that never ran**, and scored the stubs. Attrition
must not be recorded as completion.

## Cost

Six real subjects and nine stubs, for no data. **A capability probe costs one
subject and would have saved all fifteen** — the same shape as the isolation
probe, asking the other question.

## To rerun

1. Grant subjects an explicit, identical toolset, recorded in the manifest.
2. **Probe capability before spawning**, with the flags the subjects will use:
   assert a throwaway subject can write a file and execute it.
3. Do not mark a subject `.done` unless it actually finished, so a resumed run
   fills the gaps instead of skipping them.
4. Consider a smaller pilot (n=1 per arm) to validate the harness end to end
   before spending n=5.

Runs 1 and 2 are at [`RESULT.md`](RESULT.md) and [`RESULT2.md`](RESULT2.md).

## Provenance

- Design pre-registered `c60a32d`, section 8 added `b68977f`, both before any
  run-3 subject existed.
- Config recorded per subject in `.manifest`: `model=opus effort=medium`,
  fixture commit `a7c80c7`.
- Transcripts under `/tmp/hubbawubba/opus-medium/*/.transcript`.
