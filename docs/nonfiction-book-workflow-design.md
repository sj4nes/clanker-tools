# Design note: a nonfiction-book production skill

**Status:** design draft (step 3 of a 3→1 plan). Working out how the pipeline
decomposes into human and agent turns, and where the existing skills plug in,
before committing to a `SKILL.md` structure.

**Date:** 2026-09-08

---

## 1. What kind of skill this is

The source workflow describes five linked systems — **positioning, research,
architecture, drafting, editorial production** — plus a revise-in-passes
discipline and a final acceptance checklist. That is the same shape as
`design-of-experiments`, `control-systems`, and `simulation`:

> charter up front → typed intermediate artifacts → staged passes each with one
> defined purpose → a decision/acceptance report at the end, with explicit
> non-claims.

So `nonfiction-book` is a **methodology meta-skill** in the house style. It is
*not* a "write my book" generator. Its deliverable is the **project system** —
four or five living artifacts plus a pass playbook — and its job is to keep the
five systems independently inspectable and to enforce the seams between them.

Like the other meta-skills (`math-theorem-tree`, `theorem-tree-tutorial`,
`formula-tree-tutorial`), it orchestrates lower skills rather than reimplementing
them.

## 2. The artifacts are the human/agent interface

The whole collaboration runs through a small set of documents. Each has a clear
owner, a clear contributor, and a clear "done enough to proceed" bar. This is the
core design claim: **the artifacts, not the chapters, are the unit of work.**

| Artifact | Primary owner | Agent's role | Gate to pass before next system |
|---|---|---|---|
| **Positioning brief** | human | drafts from reader-interview notes; pressure-tests the one-sentence promise; maintains the "will not cover" list | promise sentence answers all five questions; ≥3 comps named; exclusions written |
| **Comps table** | agent | builds and maintains; extracts recurring praise/complaints; drafts the differentiation sentence | ≥10 comps; each has promise + structure + gap; differentiation sentence approved by human |
| **Claim ledger** | agent | owns the row-by-row mechanics; flags every unresolved/low-confidence claim; runs the evidence pass | every drafting-blocking claim is `high` or explicitly flagged `draft-anyway` |
| **Fat outline** | co-owned | drafts chapter briefs from the brief + research; enforces "one distinct job per chapter" and the through-line sentences | every chapter has: entering question, central claim, evidence plan, running example, likely objection, "reader can now ___" |
| **Style sheet** | agent | creates and maintains; every term, spelling, capitalization, number style, citation style decision lands here | exists before line-edit pass |
| **Feedback tracker** | agent | logs every beta-reader / expert / editor note with location, theme, and disposition | — (runs continuously) |

The **positioning brief is the constitution.** Every later decision — a chapter,
an example, a cut — is checked against it. When the brief and a draft chapter
disagree, that is a flag to surface, not a thing to quietly resolve.

## 3. Division of labour, system by system

### System 1 — Positioning (human-led)

- **Human owns:** who the reader is, the transformation promised, the thesis, the
  book type (prescriptive / explanatory / narrative / argument / memoir /
  reference), the exclusions.
- **Agent does:** run the one-sentence test against the draft promise; check the
  chosen book type against the provisional TOC for mode-mixing ("a history with a
  self-help skeleton"); assemble the comps table; draft — never finalize — the
  differentiation sentence; turn raw reader-interview notes into a vocabulary /
  objection / desired-outcome list.
- **Agent must not:** invent an audience, fabricate comps or market data, or
  decide the thesis.
- **Blocking questions only.** If the reader or the promise is missing, ask. Do
  not proceed on an assumed audience.

### System 2 — Research (agent-heavy, human adjudicates)

- **Agent owns:** the claim ledger mechanics — one row per assertion, typed
  (fact / statistic / interpretation / recommendation / quote / anecdote /
  prediction), with evidence-needed, source, **date checked**, confidence,
  caveats, chapter, citation status.
- **Agent does:** enforce the source hierarchy (primary → high-quality secondary
  → tertiary → discovery); refuse to let a discovery source carry a load-bearing
  claim; keep fact, interpretation, and recommendation in separate rows even when
  they will sit in one paragraph; maintain the permissions log and the
  interview-consent register.
- **Human owns:** what the evidence actually supports, which interpretations to
  advance, and all on/off-record judgement calls.
- **Plugs into [`citation-check`](../skills/citation-check/SKILL.md):** the
  ledger's "does this source support the precise wording" field *is*
  citation-check's job. Any claim at `high` confidence with a formal citation
  should have passed citation-check.

### System 3 — Architecture (co-owned)

- **Agent does:** draft the fat outline from the brief + ledger; for every
  chapter force the sentence "After reading this chapter, the reader will
  understand or be able to ___" and reject "know more about X"; check each
  chapter has a job distinct from its neighbours; write the end-of-chapter
  through-line transition sentences; pick the governing structure pattern
  (problem→solution, beginner→advanced, myth→evidence→action, case→principle,
  chronology) and flag chapters that fight it.
- **Human owns:** the argument arc, what to cut, chapter order when the logic is
  genuinely ambiguous.
- **Plugs into the tutorial skills' premise:** "the reader experiences a sequence
  of capabilities, not a warehouse of information" is the same principle
  `theorem-tree-tutorial` and `formula-tree-tutorial` run on.

### System 4 — Drafting (human-led, agent supports)

The draft's one job is to produce revisable material. The agent's default is
**not to ghostwrite** — voice is the human's. Agent support:

- Assemble the per-chapter working set (only the ledger rows and sources that
  chapter needs) so the human is not drafting with the whole library open.
- Check altitude: flag runs of prose that stay abstract with no zoom-in (person,
  number, scene, quote, object) or that bury the idea under detail with no
  zoom-out.
- Flag the quality traps from the source: research dumping, framework inflation
  ("every observation is a System"), unsupported certainty, generic examples,
  premature advice, repetition-as-emphasis, unexamined bias, quotation overload.
- Maintain a "unresolved research" list so the human flags and moves on instead
  of stalling.
- **If** the human asks for drafted prose: produce it clearly marked as a draft
  to be rewritten in the human's voice, and log which ledger rows it leans on.

### System 5 — Editorial production (agent-heavy on mechanics, human on voice)

Five passes, each a separate read with one purpose. The agent runs the
mechanical passes and prepares the others; the human owns developmental judgement
and voice.

| Pass | Purpose | Owner | Agent contribution |
|---|---|---|---|
| **1. Developmental** | premise fulfilled? structure builds? every chapter a distinct job? conclusion synthesizes not repeats? | human | produce the chapter-function table, the promise-vs-delivery map, the repetition report |
| **2. Argument & evidence** | every meaningful assertion audited against its best source at the stated wording; limitations disclosed | agent + human adjudication | run [`citation-check`](../skills/citation-check/SKILL.md) over flagged rows; produce the "skeptical informed reader" objection list; check quote exactness and attribution |
| **3. Reader usability** | concept introduced before use? instructions actionable? terms defined in plain language? examples representative? skimmable? | agent drafts, human confirms | dependency-check concept order; audit every imperative for actionability; check every term against the style sheet; use [`visualization-design`](../skills/visualization-design/SKILL.md) for any figure, table, or diagram that would reduce confusion |
| **4. Line edit** | sentences, rhythm, voice; cut throat-clearing; active verbs; consistent terminology | human | flag candidates only; `simple-technical-english` applies **only** to genuinely instructional passages (checklists, procedures, how-to steps) — not to narrative or argument, where controlled English would strip useful nuance |
| **5. Copyedit & proofread** | grammar, punctuation, consistency, citations, cross-refs, tables; then post-layout proof | agent (copyedit mechanics) + human | run the style-sheet consistency check; verify every cross-reference resolves; check citation format uniformity; the post-layout proof is a **separate** pass because typesetting introduces new errors |

**Rule carried from the source:** do not demand polished prose and comprehensive
fact-checking in the same moment — different cognitive tasks, different passes.

### Outside readers (human-coordinated, agent-tracked)

Agent maintains the feedback tracker and does the pattern analysis: "three
readers stumbled at the same point → investigate the manuscript; one reader
dislikes the premise → do not rebuild the book." Agent does not contact readers
or decide who to recruit.

## 4. Where each existing skill plugs in

| Skill | Used in | For |
|---|---|---|
| [`citation-check`](../skills/citation-check/SKILL.md) | System 2, Pass 2 | verifying any load-bearing citation as record-linkage + evidence; the calibrated status feeds the ledger's confidence field |
| [`visualization-design`](../skills/visualization-design/SKILL.md) | System 3, Pass 3 | deciding whether a chart / table / diagram earns its place, then building it with integrity + accessibility |
| [`simple-technical-english`](../skills/simple-technical-english/SKILL.md) | Pass 4, **instructional passages only** | tightening checklists, procedures, and how-to steps so a literal reader performs the intended action |
| [`unknown-discovery`](../skills/unknown-discovery/SKILL.md) | optional, System 1–2 | premortem on the premise; assumption register for the thesis; "what would make a reader skeptical" as disconfirming-signal work |
| [`csplit`](../skills/csplit/SKILL.md) / [`ed`](../skills/ed/SKILL.md) | Systems 4–5 | splitting the manuscript into per-chapter working files; minimal reviewable edits to structured front/back matter |
| [`tsort`](../skills/tsort/SKILL.md) | System 3, Pass 3 | ordering concept introductions so no term is used before it is defined (the "fat outline" as a small dependency graph) |
| [`bc`](../skills/bc/SKILL.md) | System 2 | any arithmetic in the book's own claims (rates, percentages, conversions) done exactly and reviewably |

The `tsort` use is worth calling out: a nonfiction book *is* a dependency-ordered
sequence of concepts, exactly like a formula tree or a theorem tree. The fat
outline can be linearized the same way — every prerequisite concept before the
chapter that uses it.

## 5. Skill artifacts to ship (templates/)

Following the `design-of-experiments` pattern (`charter.md`,
`analysis-plan.md`, `decision-report.md`):

1. `positioning-brief.md` — the 10-field brief, one page, promise sentence at top.
2. `claim-ledger.md` — the row schema + a filled example row + the source
   hierarchy + the fact/interpretation/recommendation separation rule.
3. `fat-outline.md` — the per-chapter brief template + the "reader can now ___"
   forcing sentence + the through-line transition slot.
4. `style-sheet.md` — term list, number style, citation style, capitalization,
   spelling decisions.
5. `acceptance-checklist.md` — the 12-point quality standard from the source,
   as a yes/no gate with evidence required for each yes.

## 6. references/ to write

- `positioning.md` — the one-sentence test, the five book types and mode-mixing
  failures, the comps method, the reader-interview question set.
- `research-system.md` — claim ledger fields in full, source hierarchy, fact vs
  interpretation vs recommendation, interview practice and on/off-record rules.
- `architecture.md` — fat-outline ingredients, "every chapter earns its place",
  the structure-pattern table, the through-line practice.
- `drafting.md` — the chapter-drafting sequence, the three altitudes with the
  worked onboarding example, the eight quality traps.
- `editorial-passes.md` — the five passes in detail, what each does and does not
  touch, the outside-reader matrix, beta-reader question set.
- `production.md` — traditional proposal contents vs self-publishing production
  chain, manuscript hygiene, the project-folder inventory.

## 7. Guardrails — the skill refuses or escalates when

- There is no concrete primary reader, or the promise is topic-led ("a book
  about X") with no reader and no outcome.
- The agent is asked to invent an audience, fabricate comps, endorsements,
  platform, or market data, or manufacture a proposal's marketing claims.
- A load-bearing claim rests only on a discovery source (social media, blog,
  search snippet, AI summary), or a claim is stated at `high` confidence with no
  entry in the ledger.
- Advice is being presented as settled evidence, or one interpretation as
  inevitable fact — especially on medical, legal, financial, or political
  subjects, where scope and competing views must be stated.
- A quote is being "cleaned up" in a way that changes meaning, or interview
  material is used without the on/off-record basis established first.
- Polishing prose in a chapter that the developmental pass has flagged for
  possible cutting.
- Controlled-English rewriting (`simple-technical-english`) is being applied to
  narrative or argument rather than to instructional passages.
- The book makes a claim the ledger cannot trace to a source that supports the
  precise wording.
- A technical / scientific / health / legal / financial book is heading to
  production with no subject-matter-expert review of substance (an editor checks
  expression, not facts).

## 8. Open questions for the SKILL.md pass

1. **One skill or two?** Positioning + research + architecture is a "should I
   write this, and what is it" phase that stands alone. Drafting + editorial is
   execution. Split like `math-theorem-tree` (build) vs `theorem-tree-tutorial`
   (teach), or keep as one workflow with clear phase gates? *Leaning: one skill,
   phase-gated — the artifacts already enforce the seams.*
2. **How far into production?** Stop at "production-ready manuscript + project
   folder", or include proposal-drafting and self-publishing production-chain
   guidance? *Leaning: include as a `references/production.md` but keep the
   skill's spine at manuscript quality — marketing and distribution are a
   different discipline.*
3. **Verification.** The other methodology skills each have a
   `verification/run.sh` exercising the workflow on a tractable case with a known
   answer. What is the tractable case here? Candidate: a short (~3-chapter)
   worked mini-"book" on a bounded topic, carried through positioning → ledger →
   outline → one drafted chapter → the five passes, with the acceptance checklist
   as the pass/fail. Needs thought — quality here is less numeric than a power
   calculation.
4. **Does `unknown-discovery` belong in the spine or stay optional?** The
   premortem-on-the-premise and assumption-register-for-the-thesis moves are
   genuinely valuable at System 1. *Leaning: reference it in System 1 as a
   recommended-not-required step.*
5. **Naming.** `nonfiction-book` / `book-production` / `nonfiction-production`?
