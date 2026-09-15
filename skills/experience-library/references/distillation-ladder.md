# The distillation ladder and the library lifecycle

Reference material for behaviours 1 and 4 of [`../SKILL.md`](../SKILL.md).
Lookup, not guidance.

Source: Duan, Liu, Tang, Chen, Zhou et al., *The Last AI Built by Humans:
Toward Genuine Recursive Self-Improvement*, arXiv:2609.11873v1 (Sept 2026),
§3.5.1 (trajectory distillation) and §3.5.3 (selective retention and library
maintenance), which survey ~25 deployed systems along these axes.

---

## 1. The four rungs

Trajectory distillation converts interaction histories into artifacts that
persist across sessions. The **form** of the artifact determines its cost to
maintain, its cost to consult, and what gate it can be held to.

| Rung | What it is | Retrieved as | Promotion gate | Fails by |
|---|---|---|---|---|
| **Text note** | natural-language passages retrieved into the prompt — strategies, pitfalls, a curated evolving note | prose in context | none beyond behaviour 2 | growing unbounded; being superseded silently; compression losing the detail that mattered |
| **Structured record** | explicit records or graphs — milestone dependencies, per-user preference entries, tool-use critiques | fields, or a graph query | schema validity | the conditions for reuse being inspectable but wrong |
| **Procedure** | a reusable skill or standard operating procedure another agent follows directly, loaded as part of its instructions | read once, in full | **followable as written** by an executor that did not author it | being retrieved and not followed — behaviour 5's third factor |
| **Executable** | a callable tool or function compiled out of a repeatedly-reused plan | invoked | **compiles and runs in a sandbox**, and the plan has already recurred across tasks | being invoked on inputs the originating trajectory never saw |

Two rules from the surveyed systems:

- **Promote on recurrence, not on quality.** The Metis pattern: a text plan
  is rewritten as a callable tool *only after* it has already recurred across
  tasks and then passes dependency and compilation checks. Quality is what
  behaviour 2 measures; recurrence is what justifies paying the higher rung's
  maintenance cost.
- **Learn from failures, not only successes.** ReasoningBank distils judged
  trajectories of *both* kinds into short titled strategies; PRACTICE trains
  failure awareness by contrasting successful and failed trajectories from
  different executors on the same task. A library built only from wins
  encodes no information about where its entries stop applying.

## 2. Admission: the paired-execution gate

The HDSO design, and the reason behaviour 2 is a *pairing* and not a
comparison:

1. A curator observes compact executor traces and proposes a candidate
   artifact **with an explicit validation plan** — the hypothesis, written
   first.
2. The same tasks are executed **twice**: control with the current approved
   repository, treatment with the candidate added.
3. The candidate is admitted only when the difference between the two runs
   supports the stated hypothesis.
4. The comparison runs in **stages of increasing size**, and ends with
   confirmation on **independent tasks**.

What this prevents: a skill that encodes a spurious shortcut from a noisy
trajectory, or a rule the executor cannot actually follow. Both read well.

## 3. Maintenance: the Library Drift lifecycle

Skills that were once useful degrade as tasks and models change, and
**unbounded accumulation degrades retrieval quality and stalls progress
before the effect is visible in task scores**. Three parts:

| Part | Rule |
|---|---|
| **Evidence log** | append-only; tracks each entry's contribution to task outcomes over time |
| **Cap** | the number of active entries is bounded, so a new skill **competes with** the entries already present |
| **Authoring guide** | a stored meta-skill steering how future entries are written, so the library stays internally consistent as it turns over |

And the finding that bounds the policy: **retiring too aggressively performs
worse than leaving the library unguided.** The governance curve has an
interior optimum in both directions — see `../verification/checks.bc` §3,
where governed (0.390) > ungoverned (0.133) > aggressive (0.092).

A related analysis finds that **carefully filtering skill edits** improves
task performance, where **repeatedly rewriting skills from task outcomes**
does not. Edit volume is not progress.

## 4. The three factors

Retention, activation, and execution are separately measurable and separately
broken (§6, "Persistent-State Management and Reliable Reuse"):

```
realised benefit = retention x activation x execution
```

- **Retention** — was the artifact kept at all?
- **Activation** — was it retrieved when it was relevant? *(a relevant skill
  may never be retrieved)*
- **Execution** — once retrieved, was it followed correctly? *(an agent may
  retrieve it and not follow it)*

The surveyed analysis separates two further capabilities that are routinely
conflated: **producing** a useful persistent update, and **benefiting from**
one at solve time. They are largely independent of base model capability —
a small model's updates yielded gains comparable to a frontier model's —
which is why the paper's practical conclusion is that **capability investment
belongs in the task-solving agent rather than in the artifact generator**.
