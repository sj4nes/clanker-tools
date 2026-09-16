# Pre-flight: qualifying a design before you spend subjects

Four fixtures have run in this corpus. **Two produced results; two were
invalid.** Both invalid runs failed for reasons that were knowable before a
single subject was spawned, and in both cases the cost was the whole run.

This is the gate that would have caught them. Run it *before* recruiting, not
after scoring — the point is to spend judgement instead of subjects.

## The failure inventory this rubric is derived from

Nothing here is invented. Each gate below exists because of a specific run.

| # | Fixture | What went wrong | Knowable in advance? |
|---|---|---|---|
| F1 | `role-deck` premise | scorer and results landed in one commit; pre-registration unprovable | yes — mechanical |
| F2 | `role-deck` ordering | the second cause was visible in the subject's *output*, so the shortcut also found it | yes — judgement; caught by the author before running |
| F3 | `directed-verification` b1 run 1 | the subject function was itself buggy; good harnesses scored `BROKEN` | yes — mechanical |
| F4 | b1 run 1 | 4 of 5 arm-B subjects died on a session limit, leaving n=1 | partly — spawn order |
| F5 | b1 run 2 | **the control arm had the treatment** (`test-writing` in context) | yes — mechanical |
| F6 | b1 run 2 | a pre-registered ceiling rule supplied a respectable reading of Δ=0 that concealed F5 | yes — ordering of checks |
| F7 | all four | no positive control; the method has never detected an effect it knew was there | yes — by declaration |
| F8 | b1 runs 1 and 2 | neither result names the model or effort that produced its subjects; the runs are not reproducible and the claims have no stated scope | yes — by declaration |

Two of these (F2, F6) are the dangerous kind: the run completes, the numbers
look clean, and the design produces a confident wrong reading rather than an
obvious error.

## The gates, in dependency order

A gate that cannot be evaluated is **blocked**, not passed. Do not proceed past
a blocked gate by assuming it would have passed.

### G1 — Is there a contrast at all?

> *From F5. The single most expensive failure so far.*

- [ ] The arms are written down as separate artifacts, and they differ.
- [ ] The difference is **only** the treatment. Read both aloud; anything that
      differs and is not the intervention is a confound you chose.
- [ ] **The control does not already contain the treatment** — not in its
      prompt, and not in its *environment*.

That last clause is the one that failed. Arm A's prompt was clean; arm A's
**context** was not, because the corpus's own `test-writing` skill prescribes
the intervention under test.

**The isolation boundary is the SESSION, not the working directory.** Run 2's
subjects already ran outside the repo and were contaminated anyway. A subagent
spawned by the Agent tool inherits the parent session's project skills wherever
it does its work. Only a separate `claude` process, launched with a cwd outside
the project, drops them.

**A corpus of installed skills makes its own claims hard to test.** Any
behaviour your skills teach is contamination for any fixture asking whether
that behaviour needs teaching. Assume contamination and prove its absence;
never assume isolation and hope.

#### The isolation recipe, verified 2026-09-15

Three layers, each measured rather than assumed:

| Subject launched as | Skills visible | Verdict |
|---|---|---|
| Agent-tool subagent, cwd anywhere | all 52 project skills | **contaminated** — this is what run 2 did |
| `claude -p`, cwd outside the repo | 5 user + plugin + built-ins, incl. `code-review` | residual |
| `claude -p --disable-slash-commands`, cwd outside the repo | **NONE** | **clean** |

So a run-3 subject is a **Bash-invoked separate process**, not an Agent-tool
subagent:

```sh
cd "$SUBJECT_DIR" && claude -p --disable-slash-commands "$(cat task-A.md)"
```

This changes the harness shape, and in a useful direction: the subject's full
transcript is now a file you own, which makes the manipulation check a `grep`
rather than an inference.

Prove it before every run, with the flags the subjects will actually use:

```sh
sh verification/check_isolation.sh <subject-cwd> <fingerprints.txt> "--disable-slash-commands"
```

The probe refuses a cwd whose git root has a `.claude/skills` directory without
spending an API call, then launches a throwaway session and greps its skill list
against the fingerprints. It proves absence of the **named** contaminants only —
a fingerprint you did not think of is still unchecked, which is why the list is
a fixture artifact under review, not a constant.

### G2 — Can you prove the contrast held?

> *From F5 and F6. G1 is a plan; this is the evidence it was carried out.*

- [ ] A **fingerprint list** exists: concrete strings, file paths, or artifacts
      whose presence in a control subject's context or transcript means that
      subject received the treatment.
- [ ] A **manipulation check** is written and runs against those fingerprints.
- [ ] The manipulation check is scored **before** the outcome is interpreted,
      and a failure **invalidates the run** rather than annotating it.

The ordering is not bureaucratic. In run 2 the pre-registered interpretation
fired first, returned "no headroom", and that respectable reading is exactly
what stopped the author looking for the cause. **Pre-registering how to read a
null result is not the same as checking the experiment ran.** A design that can
report "no headroom" needs a prior check that the arms differed at all.

Cheapest form: one `grep` per subject transcript. It costs seconds and it
invalidates a broken run before you build a story on it.

### G3 — Is the instrument readable?

> *From F3.*

- [ ] The subject is **verified correct by an independent oracle** before any
      subject sees it — not assumed, not eyeballed.
- [ ] The scorer re-asserts that as a **precondition** and refuses to score if
      it ever fails.
- [ ] If a defect is planted, its blast radius is enumerated: which inputs
      distinguish planted from clean, and how many.

Run 1 skipped this and inverted its own measurement — the better the harness,
the worse it scored. Run 2 did it properly (28,824 cases, zero mismatches) and
the precondition held. This gate works.

### G4 — Could the design detect a real effect?

> *From F7. The gap the whole method still has.*

- [ ] A **positive control** is named: a manipulation whose effect you already
      know, which this design would detect.
- [ ] If you cannot construct one, say so in the writeup and treat every null
      result as uninterpretable.

A method with no demonstrated sensitivity cannot distinguish *no effect* from
*no instrument*. `claim-fixture` has produced two refutations and two invalid
runs and has **never once returned a positive**, so its ability to detect one
is itself untested. Refutations from an instrument of unknown sensitivity are
weaker evidence than they look.

### G5 — Does the shortcut pass its own check?

> *From F2.*

- [ ] A subject taking the lazy path reaches an answer that **looks right to
      them**.
- [ ] The evidence distinguishing lazy from thorough is **not present in what
      the subject is handed** — not in the output, the docstring, or the error
      message.
- [ ] If a null result and "the answer was visible" are indistinguishable, the
      fixture is not ready.

F2 was caught in time: the second cause was visible in the subject's output, so
it moved into the code before the run. That is this gate working manually.

**Note the tension with G1.** A task small enough to fixture cleanly is often
small enough that the treatment has nothing to buy — every b1 subject aimed
correctly. Headroom in the *defect* is not headroom in the *population*; the
gate is only satisfied when a competent control would plausibly miss.

### G6 — Will the run survive to completion?

> *From F4.*

- [ ] Arms are **interleaved** in spawn order, so truncation costs both arms
      equally rather than destroying one.
- [ ] A minimum n per arm is declared, below which the run is void.
- [ ] Attrition is reported as a number, not silently dropped.

### G7 — Is the interpretation committed and provable?

> *From F1.*

- [ ] Bands are written for **every** outcome, including the ones that refute
      you.
- [ ] Scorer and bands are in a commit that **strictly precedes** the first
      result.
- [ ] The bands say what gets **struck**, not what gets reworded.

Subject to G2's ordering: bands are read only after the manipulation check
passes.

### G8 — What population is this a claim about?

> *From F8.*

An agent subject is a **model at an effort level**. A score that does not name
its configuration is a claim about nothing in particular, and cannot be
reproduced or contradicted.

- [ ] The design declares a line `Primary configuration: <what a subject is>`.
- [ ] That configuration is recorded **per subject, at spawn time**, not
      reconstructed afterwards from memory.
- [ ] If more than one configuration will be run, the design says which one is
      **primary** and which are labelled replications.

The third box is the one with teeth. Configuration is cheap to vary and
expensive to vary honestly: *k* models × *m* effort levels is *k·m* chances to
find the band you wanted at n=5. Behaviour 5 pre-commits the bands; it does not
by itself pre-commit **which cell counts**. Block, do not cross.

A fixture whose subjects are not model-driven still declares the line — it just
declares people, or a fixed program. The gate asks you to name your subjects,
not to be running an LLM.

If a configuration is varied deliberately, prefer a **directional prediction
registered in advance** ("the effect is larger at low effort") to an
after-the-fact comparison of cells. An interaction chosen once the cells are
visible is a description of noise.

## The pre-flight is not a guarantee

- It cannot tell you the claim is worth measuring.
- It cannot tell you the task shape generalises — one task, one population,
  one day.
- It cannot supply a positive control you do not have; G4 can only make its
  absence explicit.
- **It is itself unmeasured.** This rubric is derived from four runs by one
  author. It is a checklist against known failures, not a theory of
  experimental design, and a fifth run will probably add a gate.
