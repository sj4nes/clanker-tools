# Handoff — experiment-design / claim-fixture thread

Written 2026-09-15, mid-task, to resume in a fresh context.
Last commit: `f06020b`. **Working tree is dirty — see §1.**

---

## 0. TL;DR of where this landed

`directed-verification` behaviour 1 has been fixtured **twice** and is **still
unmeasured** (run 1: buggy subject; run 2: control arm received the treatment).
That second failure produced the real work of this thread: a **pre-flight gate**
for experiment design, shipped as `claim-fixture` 2.0.0, plus an empirically
verified recipe for spawning genuinely blind subjects.

---

## 1. FIRST THING TO DO — a broken check, and dirty files

### 1a. `skills/claim-fixture/verification/run.sh` currently FAILS

`preflight-check.sh` section 3 asserts the b1 fixture is blocked **at G2a**.
That assertion is now stale: I added `fingerprints.txt` to the b1 fixture, so
G2a passes there and it blocks at **G2b** (design declares no manipulation
check) and **G4** (no positive control).

Fix: in `skills/claim-fixture/verification/preflight-check.sh`, section 3,
change the expected token from `G2a  BLOCKED` to `G2b  BLOCKED`, and reword the
success line — it should say the gate blocks the real failed fixture, naming
whichever gate is still unmet. Then `sh skills/claim-fixture/verification/run.sh`
must exit 0.

This is the harness correctly detecting that the world changed. Do not "fix" it
by deleting the assertion.

### 1b. Uncommitted, all wanted

```
 M skills/claim-fixture/references/pre-flight.md          # isolation recipe added
?? skills/claim-fixture/verification/check_isolation.sh   # new, works, chmod +x done
?? skills/directed-verification/verification/b1-fixture/fingerprints.txt
 M docs/refuted-premises/.DS_Store                        # junk, do not commit
```

`rsi/` stays **untracked** — standing instruction from the user.

Commit after fixing 1a, as one commit: the isolation probe + recipe + b1
fingerprints. Suggested subject: `claim-fixture: an isolation probe, and the
verified recipe for a blind subject`.

---

## 2. What was established this session

### The b1 run-2 failure (the finding that drove everything else)

Both arms scored 5/5 `CATCHES`, Δ = 0. First reported as *no headroom* under a
pre-registered ceiling rule. **That was wrong.** Every arm-A subject had
`test-writing` in context — a skill prescribing the exact discipline under test
— and their transcripts quote `test-writing/SKILL.md` lines 37 and 48 verbatim.
The arms were one condition; Δ = 0 was structural.

Two lessons, both now encoded:

1. **Naive about the hypothesis ≠ clean of the intervention.** `claim-fixture`
   behaviour 2 was satisfied and the run was still ruined.
2. **A pre-registered reading of a null result can conceal a broken
   experiment.** The ceiling rule fired first, returned something respectable,
   and stopped the search for the cause. Hence: the manipulation check is scored
   **before** the bands, and contamination **voids** rather than annotates.

The tell was missed in plain sight: five arm-A reports shared a near-identical
"Risky area and targeted mistake" heading. Five independent agents do not
converge on a section heading.

### The isolation recipe — MEASURED, not assumed

| Subject launched as | Skills visible | Verdict |
|---|---|---|
| Agent-tool subagent, cwd anywhere | all 52 project skills | **contaminated** (what run 2 did) |
| `claude -p`, cwd outside the repo | 5 user + plugins + built-ins incl. `code-review` | residual |
| `claude -p --disable-slash-commands`, cwd outside repo | **NONE** | **clean** |

**The isolation boundary is the SESSION, not the working directory.** Run 2's
subjects already ran in `/private/tmp/...` and were contaminated anyway, because
an Agent-tool subagent inherits the parent session's project skills.

So a run-3 subject is a **Bash-invoked separate process**:

```sh
cd "$SUBJECT_DIR" && claude -p --disable-slash-commands "$(cat task-A.md)" </dev/null
```

Useful side effect: the subject's transcript becomes a file you own, so the
manipulation check is a `grep` rather than an inference.

---

## 3. What shipped (committed, green except 1a)

- **`claim-fixture` 2.0.0** (`e9f5753`) — MAJOR. New **behaviour 3**: prove the
  control did not already receive the treatment, before reading any outcome.
  Old behaviours 3–6 renumbered to 4–7; cross-references updated repo-wide.
- **`references/pre-flight.md`** — 7 gates (G1–G7), each tagged to a named
  failure F1–F7 from this corpus's four runs. Nothing invented.
- **`verification/preflight.sh`** — scores a design *before* subjects are
  spawned; **blocks on any gate it cannot evaluate**.
- **`verification/preflight-check.sh`** — clears a compliant fixture, breaks one
  gate at a time, asserts the *specific* gate fires. (Stale in §1a.)
- **`verification/check_isolation.sh`** *(uncommitted)* — refuses a cwd whose git
  root has `.claude/skills` without spending an API call, then launches a
  throwaway session and greps its skill list against the fingerprints. Verified
  in all three directions: rejects the repo, rejects a bare `/tmp` session
  (`code-review`), accepts `/tmp` + `--disable-slash-commands`.
- **`directed-verification` 1.2.0** (`3cf2da3`) — run 2 recorded as INVALID, with
  the superseded "no headroom" reading kept in the file rather than rewritten.

---

## 4. Run 3 — blocked, and on what

**Do not spawn subjects until `preflight.sh` exits 0 on the fixture.** Currently
G2b and G4 are unmet. In order:

1. **G2b — write `design3.md`** with a manipulation check declared *and ordered
   before interpretation*. Must state that contamination voids the run.
2. **G4 — name a positive control.** A manipulation with a known effect that
   this design would detect.
3. **G5 (judgement, no gate) — the plant.** This is the hard one and it is
   *unsolved*. The run-2 plant had headroom in the *defect* (differed from
   correct code only at negative ties) but not in the *population* — every
   undirected agent aimed correctly anyway. A task small enough to fixture
   cleanly is often small enough that the treatment has nothing to buy.
   Candidates: a defect in an interaction between modules; one reachable only
   through a state sequence; one in code whose intended behaviour is **not
   recoverable from the code under test** (this is probably the key property —
   run 2's docstring stated the rounding rule outright).
4. Then rebuild the harness around Bash-invoked subjects (§2), interleaved,
   n≥5 per arm.

---

## 5. Open backlog (in `BACKLOG.md`)

- **`claim-fixture` owes a positive control of itself.** Four runs: two
  refutations, two invalid, **zero positives**. The method has never detected an
  effect it knew was there, so its sensitivity is untested and both refutations
  are weaker than they look. Until then every refutation reads as *"no effect
  detected by an instrument of unknown sensitivity."*
- `directed-verification` b1 run 3, gated as in §4.
- Pre-existing, untouched this session: `role-deck` improve deck; source-authority
  skill; 34 archetype failures (skill-authoring ratchet baseline = 34); book
  Parts I, II, IV, V.

---

## 6. Standing context worth not relearning

- **`rsi/` stays untracked.**
- Repo standard: a check that cannot fail is not a check. Every claim traces to
  a harness; displacement tables report `covered / judgement / gaps` honestly.
- `sh skills/skill-authoring/verification/run.sh` is the repo-wide authoring
  ratchet — baseline 34, must not rise.
- Recurring self-inflicted bug this session: **Python `str.replace()` silently
  no-ops on an anchor mismatch.** Two edits appeared applied and were not.
  Assert every anchor, and verify the result, when editing this way.
- Structural point worth keeping: **a corpus of installed skills cannot easily
  test its own premises** — any behaviour the skills teach contaminates any
  fixture asking whether that behaviour needs teaching. This will recur for
  every behavioural claim in this repo.
