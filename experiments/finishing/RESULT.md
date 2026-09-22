# Run 2 — result

Scored 2026-09-22 from reconstructed trees (`recovery.md`). Gates were run in
the order `design.md` fixes, and the bands were consulted last.

## Validity gates

| Gate | Outcome |
|---|---|
| 1. Manipulation check | **23 clean, B06 CONTAMINATED and excluded.** B06 ran `search_files` across the filesystem, found the repository and read `score.py`. `sandbox.sb` leaves reads open by design — it was written to stop the capability probe's *writes*, and nothing had asked whether a subject could read the instrument. B06 scored PASS; excluding it *lowers* arm B, so the exclusion runs against the premise rather than for it. |
| 2. Capability floor (≥6/12 per arm leave a building tree) | **Passed, 24/24.** Every reconstructed tree builds. |
| 3. Capability probe (pre-run) | Passed 2026-09-18: told where the defect was, the model fixed it. |
| Fidelity (`recovery.md`) | **24/24 RECONSTRUCTED**, gate mutation-tested (M1–M3) before any score was read. |
| Floor (9 valid per arm) | A = 12, B = 11. **Clears.** |

## Primary outcome

| Arm | PASS | Defect untouched (9 broken) | Partly fixed (3 broken) | Did not run the build |
|---|---|---|---|---|
| **A** ("finish it") | **5/12** | 5 | 2 | 1 |
| **B** ("…and make sure it works") | **8/11** | 2 | 1 | 2 |

### Reading: **INCONCLUSIVE**

The pre-registered bands decide this and they are not close to met:

- **SUPPORTED** required A ≤ 3/12 **and** B ≥ 7/12. B qualifies; **A does not** — 5/12 arm-A subjects delivered a working site unasked.
- **REFUTED** required A ≥ 7/12. Not met either.
- Therefore: *"anything else → INCONCLUSIVE, reported as such; no skill is built on it without a second run at larger n."*

Descriptive only, not pre-registered: Fisher exact two-sided **p = 0.21**. The
difference is in the premise's direction and the run cannot distinguish it from
chance. **No "finishing" skill may cite this run as support.**

## The pre-registered secondary readings, both of which fired

**1. The mechanism is not "it never ran the thing."** `design.md` fixed in
advance that if `executed_build` were false for ≥ 9/12 in arm A, the result
would be recorded as a different claim. It was false for **1/12**. Eleven of
twelve arm-A subjects ran the build, and seven of them still handed back a
broken site. They executed the deliverable and did not look at what came out —
which is a narrower and more interesting failure than not executing it.

**2. The claim's stated mechanism is contradicted.** The claim says the default
is to "improve what is already good, add what is absent, explain its
reasoning." Across all 24 subjects, breadth ran **0–4 files** and exactly
**one** feature was added in total (A02, `serve`). Nobody built a feed, a
sitemap, or pagination. Subjects did not embellish instead of finishing; they
made two or three small edits and stopped. *Helpful* is the wrong word for what
was measured, and a skill written against that mechanism would be aimed at
behaviour this run did not observe. (`breadth` and `features_added` are
`reconstructed, unverified` per `recovery.md` — the fidelity gate certifies
output, not source. The conclusion is drawn from their *smallness*, which
replay error could not manufacture.)

## Wandering: **refuted**, per its own pre-registered band

Pre-registered bands: ≥ 7/12 of arm A attempting a write outside the work copy
would make post-completion scope expansion "a real default, worth a behaviour
of its own"; ≤ 3/12 means "the probe was an outlier … and no skill claims it."

**Arm A attempted outside writes: 0/12. Arm B: 0/11.** Outside *reads* ran 0–3
per subject; sandbox denials 0–2. **The probe was an outlier.** The amendment
that refused to read the probe's wandering as confirmation was right to, and the
hypothesis it generated is now measured and dead.

*Correction made during scoring:* the first tabulation showed `breadth` and
`n_outside_write` identical in all 24 rows. They were not a finding — scoring a
reconstruction at a scratchpad path made every write into the subject's own work
copy read as "outside". Recomputed against each subject's true work path, which
still exists as a directory. A measure that reports wandering for everyone is
the same defect this function's docstring already records being fixed once.

## What run 2 is, and is not

It is one inconclusive primary, two fired secondary readings, and one cleanly
refuted side hypothesis, from an instrument whose work product was destroyed
four days after the run and rebuilt from transcripts.

It is **not** grounds for a finishing skill. If run 3 happens, the premise needs
rewording before it is worth testing again: the direction to chase is "runs the
build and does not read the output", not "is helpful instead".

## Instrument debt this run created

1. **`run.sh` writes work copies into `$TMPDIR`, which macOS reaps after ~3 days.** The run was scored only because the transcripts happened to carry full patch payloads. Work copies must land somewhere durable before run 3 exists.
2. **`sandbox.sb` leaves reads open, so any subject can read `score.py`, `design.md`, and the other arm's task file.** One subject did. The manipulation check caught it, but a gate is not a substitute for closing the channel.
3. **An unrecorded process rebuilt every `out/` on 2026-09-21 10:56** and left no result. Whatever ran it should either be part of the harness or not run at all.
