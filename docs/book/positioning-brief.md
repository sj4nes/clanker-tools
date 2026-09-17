# Positioning brief — The Missing Manual

The constitution for this book. Every later choice — a chapter, an example, a
cut — is checked against this. When this brief and a draft chapter disagree,
that is surfaced, not quietly resolved.

Status: **Phase 1, one gate condition outstanding.** Promise, exclusions and
comps are written (comps from the author's own Amazon survey, 2026-09-15, in
[`comps-table.md`](comps-table.md)). Reader interviews are recorded as an
**accepted exception**, not an outstanding failure — see the end.

```yaml
positioning_brief:
  working_title: "The Missing Manual"
  working_subtitle: "Building skills for AI agents, with an AI agent, and knowing whether they work"

  one_sentence_promise: >-
    For someone building a corpus of skills for AI agents, this book shows how
    to work WITH an agent to produce skills that are known to work rather than
    merely written — by holding each to a standard that can fail, and by
    measuring the default behaviour it claims to displace.

  secondary_promise: >-                 # added 2026-09-17, see "Amendments"
    And that a corpus held to this standard yields teaching material nearly for
    free: the checks that make a body of knowledge falsifiable turn out to be
    the beats that teach it, so a verified capsule can be cut into a lesson
    rather than having one written beside it.

  promise_check:
    who_is_it_for: >-
      Someone who already writes skills for AI agents — SKILL.md files, system
      prompts, runbooks, tool contracts — and is accumulating a corpus. The
      direct comps have taught them the format; this reader is past that and
      has started to worry about whether the pile is an asset or a liability.
      They work alongside an agent daily and are comfortable having it do work,
      but have not thought of it as a collaborator in QUALITY.
    what_problem: >-
      Costly and quietly frustrating. You write a document, it reads well, it
      sounds right, and you have no way to know whether it helps, hurts, or
      does nothing. So you keep writing more, and each one inherits the
      uncertainty of the last.
    what_outcome: >-
      They can do four things they could not do before: name the default
      behaviour a skill displaces; build a harness that has been SEEN to fail;
      measure whether that default is real before building on it; and direct an
      agent to do most of that work, including the part where it disproves
      them.
    unique_angle: >-
      Two things together, and the pairing is the angle. First, EVIDENCE from a
      real corpus rather than a worked example: fifty skills held to the
      standard, four audits of what that found, and two premises measured and
      struck, including the author's own. Second, the COLLABORATION itself —
      every skill in the corpus was produced by a human and an agent working
      together, with the agent doing much of the verification work and
      repeatedly proving its own author wrong. The comps teach a person to
      write a SKILL.md. This is about a pair producing one that is known to
      work.
    why_a_book: >-
      The standard is a system, not a tip: the parts depend on each other and
      need sustained explanation. And the corpus itself has reference value
      once the reader wants to copy something.

  book_type: "prescriptive"
  secondary_modes: ["argument-driven", "reference"]
  mode_mixing_risk: >-
    The drafted Part III is currently pure argument — four audits and a
    synthesis, with nothing for the reader to DO. In a prescriptive book that
    reads as a war story. Mitigation: every audit chapter must land on a
    practice the reader applies to their own document, and the catalogue must
    be framed as worked examples rather than an inventory.

  target_reader:
    description: >-
      Writes instruction documents for agents. Has a handful to a few dozen.
      Technical enough to run a shell script; not necessarily a tester.
    starting_state: >-
      Believes document quality is essentially unmeasurable, and treats writing
      one as a craft judgement. Has probably never planted a defect to check
      whether a check can fail. May have a verification step that has never
      failed and reads that as good news.
    desired_end_state: >-
      Treats an instruction document as something with a falsifiable claim
      attached. Ships a harness only after seeing it fail. Asks what a document
      displaces before writing it, and whether that default is real before
      building on it.
  core_problem_and_stakes: >-
    An unverified instruction document is not neutral. It spends the agent's
    context and the author's confidence, and a corpus of them compounds both.
    The stakes rise with the corpus: fifty documents nobody can evaluate is
    worse than five.

  central_thesis_or_framework: >-
    An instruction document makes a claim — that it displaces some default
    behaviour with a better one — and that claim can be checked. Checking it
    has two halves that are usually both skipped: a harness that can fail, and
    a measurement of whether the default was ever real.

  comparable_titles:             # full table + limitations in comps-table.md
    - "Claude Code Skills — The SKILL.md Playbook (J Cook, Mar 2026)"
    - "AI Agent Skills: The Complete SKILL.md Standard Guide (\"Prompt Master\", Jun 2026)"
    - "AI Agent Skills for Claude, Codex, and Beyond (Erik Volkmann, Aug 2026)"
    - "AI Agent Skills: The New Standard… (Tung KnowYa, Feb 2026)"
    - "CLAUDE SKILLS: Master Prompt Engineering, AI Workflows… (Eslam Wahba, May 2026)"

  differentiation_sentence: >-
    Existing books teach the SKILL.md format and how to ship a first skill
    quickly; this book helps someone who already writes skills find out whether
    a specific skill does anything — by building verification that can fail,
    and by measuring the default behaviour the skill claims to displace —
    working with the agent as a collaborator rather than writing at it.

  author_credibility: >-
    Built and maintains the corpus the book is about, including the audits that
    found its own verification unable to fail and the experiments that refuted
    two of its own premises.

  will_not_cover:
    - "Prompt engineering technique — phrasing, few-shot, chain-of-thought."
    - "Model selection, fine-tuning, RAG, context-window management."
    - "Agent frameworks and orchestration — the harness that runs the agent."
    - "DEVELOPING the domain content of the capsules. Part VI catalogues
       what was cut from them and how; it does not teach the chemistry,
       and no reader should arrive at it to learn electrochemistry."
    - "Evaluation of model capability. This is about documents, not models."
    - "Marketing, distribution, and publishing."
    - "Monetisation. The adjacent shelf is full of make-money-with-AI titles;
       this book is defined against that genre and will not gesture at it."
    - "Getting started. The reader already writes skills. A beginner's on-ramp
       is what the direct comps already do well enough."
```

## Comps: written, with a limitation that must travel with them

Six direct comps and four adjacent ones are in
[`comps-table.md`](comps-table.md), from the author's Amazon survey.

**None of them have been read.** Their positioning is inferred from titles,
subtitles and series placement. That supports a claim about *the shelf* — every
direct comp is dated February to August 2026, and all promise production rather
than evaluation — and it does not support any claim about a specific book's
content.

The differentiation sentence therefore rests on a **hypothesis about the
category**, not a finding about competitors. Before that sentence appears in
the manuscript it needs either the two or three closest comps read, or
rephrasing as a characterisation of the genre rather than an assertion about
titles. Recorded here so it cannot be forgotten at draft time.

## Reader interviews: accepted exception

The skill asks for 10–20. There will be none, and the reason is not neglect:
**the corpus is ten days old.** The category itself is younger than a year —
every direct comp is dated February to August 2026. There is no population of
people maintaining a corpus of agent skills to interview, because the practice
barely exists yet.

The skill's acceptance checklist admits exactly this case: an item may be an
evidenced yes **or an explicitly recorded exception**. This is the exception,
recorded here so it travels with the brief rather than being quietly forgotten
at draft time.

### What this costs, stated plainly

Every claim in this brief about what the reader believes, wants, or already
knows is **one person's assumption about people he has not spoken to** — the
same shape as the two premises this book's own Part III reports measuring and
striking. The brief should be read with that in mind, and the irony is not lost
on its author.

### The mitigation available

Two, neither a substitute for a reader:

+ **The author is a genuine instance of the reader**, having built fifty skills
  and hit the problem the book describes. An n of one that is not invented is
  worth more than a fabricated ten.
+ **The claims are testable with the book's own method.** `claim-fixture`
  exists to measure a behavioural claim cheaply, and "skill authors cannot tell
  whether their documents work" is such a claim. Running it would be the
  method's first use outside the repository that produced it, and is the
  obvious thing to do the moment a second adopter exists.


## Amendments

### 2026-09-17 — Part VI, and the promise it needed

Part VI (*What the Checks Turned Into*) was built on 2026-09-17 from a
conversation rather than from the fat outline, and the drift check
([`drift-check.md`](drift-check.md) §1) found it outside this brief: its 24
entries describe capsule domain content, which the `will_not_cover` list
excluded, and they serve a reader who wants to learn chemistry rather than one
auditing a corpus of agent skills.

Resolved by amending the brief, not by trimming the part. Two changes above: a
`secondary_promise`, and the exclusion narrowed from the capsules' *content* to
*developing* that content.

**Why this way.** The part's argument — that a check which can fail and a lesson
which teaches are the same event, so the tutorials were cut from the harnesses
rather than written beside them — is a claim about the standard, and it is one
of the few places the book shows the method paying a return that was not the
return it was built for. Cutting the catalogue would have kept the brief intact
and removed the evidence for its own new clause.

**What it costs.** The book is now a little more reference-shaped, which this
brief lists as a secondary mode and flags as the mode-mixing risk. Part VI has
one practice and 24 entries; if a developmental pass finds the close weakened by
following Part V's open problems with a catalogue, the appendix option is still
open and is the obvious fix.

**What it does not license.** Teaching the domain. If a future part explains
electrochemistry rather than cataloguing what was cut from it, this amendment
does not cover it and the brief should stop it.
