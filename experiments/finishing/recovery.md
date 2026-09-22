# Recovery design — reconstructing run 2 from its transcripts

Written **before** `replay.py` exists and before any subject is scored.
Run 2's work trees were destroyed after the run; this file fixes what a
reconstruction must prove before any band is consulted, so the salvage cannot
be fitted to the result it produces.

## What was lost, and when

The 24 work copies lived in `$TMPDIR/sitegen-runs/`. macOS reaps that tree of
items untouched for ~3 days. The subject sources carried `cp -R`'s Sep 18
timestamps and were deleted on **2026-09-22 04:08** (uniform directory mtimes).
Every tree now holds zero source files: no `build.py`, no `content/`, no
`templates/`, no `tests/`.

`score.py` refuses all 24 with `is not a sitegen workdir` (exit 3). The
precondition is the only reason this surfaced as a refusal rather than as 24
silent FAILs and a premise "supported" by an empty directory. It is working as
designed, and the pre-registered primary outcome is **not computable from disk**.

## The orphaned artifact

Each tree still holds exactly 6 files under `out/`, stamped Sep 21 10:56,
sequential 1-2 seconds apart in subject order A01 -> B12. That is a bulk rebuild
loop run three days after the run by a process that left no record and no
result file. It survived the reaper only because its mtime was newer.

It is **not** evidence about any subject on its own: nothing attests to what
produced it. But its 4 distinct `index.html` hashes vary with the subject, so it
is derived from the real sources. That makes it usable as one thing only, below.

## What is replayed

`events.jsonl` for all 24 subjects is inside the repository and untouched.
Replay uses only the two deterministic, self-contained mutations:

| Tool | n | Replayable because |
|---|---|---|
| `patch` | 56 | carries `path`, `old_string`, `new_string`, optional `replace_all` |
| `write_file` | 13 | carries `path` and full `content` |

**`terminal` (203) and `execute_code` (6) are NOT replayed.** 66 of the terminal
commands look mutating, and the set includes `curl`, `kill` and `pkill`.
Re-executing a subject's shell four days later, against a live network and this
machine, would be a new and worse experiment. The uncertainty this leaves is not
argued away — it is *measured*, by the fidelity gate.

## Fidelity gate — before any subject is scored

For each subject: build the reconstructed tree with its own `build.py`, and
compare the produced `out/` against the surviving Sep 21 `out/`, byte for byte
over the sorted file set.

- **RECONSTRUCTED** — every file matches. The replay is faithful *and* nothing
  the unreplayed shell did affected the deliverable. Eligible for scoring.
- **UNRECONSTRUCTED** — any mismatch, missing or extra file, or failed build.
  **Excluded as attrition, mechanically.** Not repaired, not judged, not scored.

The gate is what makes the omission of `terminal` safe rather than convenient:
a subject whose output depended on its shell cannot pass it.

This artifact cannot have been fitted to the reconstruction, because it existed
before `replay.py` was written. It is used as a checksum and for nothing else:
no band, no secondary measure, and no reported outcome is read off it.

## Floor, fixed now

`design.md` requires **9 valid transcripts per arm**. That floor is unchanged
and now applies to RECONSTRUCTED subjects after gate 1. Below it, the run is
reported as underpowered and **no band is consulted** — the reconstruction does
not lower the bar it has to clear.

## Order of work, and what is already known

1. Gate 1, the manipulation check — **already run, before any scoring**:
   23 clean, **B06 CONTAMINATED** and voided. B06 ran `search_files` across the
   filesystem, found the repository and read `score.py`. Cause: `sandbox.sb`
   leaves reads open by design (it was built to stop the capability probe's
   *writes*), so the instrument was readable all along and nothing had asked.
   The check is sound for this channel: work copies sit outside the repository,
   so any access to it surfaces an absolute path containing `clanker-tools`.
   The other fetch channel is clean -- all 5 `skill_view` calls fetched
   Hermes's own bundled `hermes-agent`, in both arms (3 A, 2 B).
2. This file.
3. `replay.py`, then the fidelity gate over all 24.
4. Gate 2, the capability floor, on RECONSTRUCTED subjects only.
5. Only then `score.py`, and only then the bands in `design.md`.

## Disclosure

While confirming the patch events were usable, the author of this file read one
`patch` payload from **A01** and saw that it fixes the defect under test. No
subject has been scored, and nothing else was read. It is recorded here because
a salvage designed after glimpsing an outcome is exactly the failure this
corpus keeps finding, and the disclosure is cheaper than the doubt.

## What this run can no longer be

Even fully reconstructed, run 2 is evidence from an instrument whose work
product was not preserved. `run.sh` must write work copies somewhere durable
before run 3 exists. The tmp reaper is now a named failure mode of this fixture,
not an accident.

## Amendment — what the fidelity gate can and cannot see (before scoring)

All 24 subjects came back RECONSTRUCTED, which is exactly the result a gate
that cannot fail would also produce. So the gate was mutation-tested before any
score was read.

| Mutation | Expected | Result |
|---|---|---|
| **M1** — drop A01's *last* replayed event | UNRECONSTRUCTED | **RECONSTRUCTED — the gate did not catch it** |
| **M2** — verify A01 against A12's surviving `out/` | UNRECONSTRUCTED | UNRECONSTRUCTED, 5 files differ |
| **M3** — drop A01's *first* replayed event (the `nav_html` prefix fix) | UNRECONSTRUCTED | UNRECONSTRUCTED, 1 file differs |

M1 is not a defect, but it fixes the gate's resolution and it is the reason
this amendment exists. A01's last mutation is a patch to `README.md`, which no
build reads. **The gate certifies the OUTPUT tree, not the source tree.** A
source change that never reaches `out/` is invisible to it.

Consequences, fixed now rather than after the numbers:

- The **primary outcome is fully covered**. It is link resolution over the
  generated pages, and the generated pages are precisely what the gate checks
  byte for byte. M3 shows a dropped edit that touches the output is caught.
- **`breadth` and `features_added` are NOT covered.** Both read the source
  tree, and the gate is blind there. They were already "descriptive, never
  decisive" in `design.md`; for run 2 they are downgraded further, to
  **reconstructed, unverified** — reported with that label or not at all.
- `executed_build` and `wandering` are read from the event log, which the
  reaper never touched. They are unaffected.

**Event-level corroboration, unplanned.** Two subjects had a replayed patch
come back `no-match` (A05 on `build.py`, B07 on `page.html`). Both were checked
against the transcripts: the subject's own tool call returned
`"success": false, "error": "Could not find a match for old_string"` in each
case. The replay reproduces not just the subjects' output but their failures,
which is stronger evidence of fidelity than the gate itself asks for.
