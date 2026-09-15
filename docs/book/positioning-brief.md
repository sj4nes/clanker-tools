# Positioning brief — The Missing Manual

The constitution for this book. Every later choice — a chapter, an example, a
cut — is checked against this. When this brief and a draft chapter disagree,
that is surfaced, not quietly resolved.

Status: **Phase 1, gate not yet passed.** The promise and exclusions are
written; the comps table is thin and unverified (see below), and no reader
interviews have been run.

```yaml
positioning_brief:
  working_title: "The Missing Manual"
  working_subtitle: "Writing instructions an agent follows, and knowing whether they work"

  one_sentence_promise: >-
    For someone who writes instruction documents an LLM agent will follow — a
    skill, a system prompt, a runbook, a tool contract — this book shows how to
    tell whether the document changes anything, by holding it to a standard
    that can fail and by measuring its premise before building on it.

  promise_check:
    who_is_it_for: >-
      A person who writes and maintains agent-facing instruction documents, and
      increasingly a corpus of them. Not "prompt engineers" in general: this
      reader has more than one document, expects to keep them, and has started
      to worry about whether the pile is an asset.
    what_problem: >-
      Costly and quietly frustrating. You write a document, it reads well, it
      sounds right, and you have no way to know whether it helps, hurts, or
      does nothing. So you keep writing more, and each one inherits the
      uncertainty of the last.
    what_outcome: >-
      They can do three things they could not do before: name the default
      behaviour their document displaces; build a harness that has been SEEN to
      fail; and test the premise a document rests on before building on it.
    unique_angle: >-
      Evidence and experience, from a real corpus rather than a worked example.
      Fifty instruction documents held to the standard, four audits of what
      that found, and two premises measured and struck — including the
      author's own.
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

  comparable_titles: []          # SEE BELOW — deliberately empty, not yet earned

  differentiation_sentence: >-
    Existing books teach how to write prompts and how to test software; this
    book helps someone who writes agent instruction documents find out whether
    a specific document does anything, using a standard applied to a real
    corpus and a method for measuring the premise underneath it.

  author_credibility: >-
    Built and maintains the corpus the book is about, including the audits that
    found its own verification unable to fail and the experiments that refuted
    two of its own premises.

  will_not_cover:
    - "Prompt engineering technique — phrasing, few-shot, chain-of-thought."
    - "Model selection, fine-tuning, RAG, context-window management."
    - "Agent frameworks and orchestration — the harness that runs the agent."
    - "The domain content of the corpus's knowledge capsules."
    - "Evaluation of model capability. This is about documents, not models."
    - "Marketing, distribution, and publishing."
```

## The comps table is not written, and should not be faked

The skill's gate asks for at least three comparable titles, and the guardrails
forbid fabricating them. Both apply here, in tension.

The honest position: **this reader's attention is not currently competed for by
books.** It is competed for by vendor documentation, blog posts, and framework
READMEs. The adjacent book shelf — testing discipline, measurement under
uncertainty, evidence-based engineering practice — is real but addresses a
different reader.

Naming specific titles, editions and publishers from memory is exactly the
failure mode `citation-check` exists to catch, and a positioning brief that
rests on remembered bibliography is a brief resting on a discovery source.

**Action required before this gate passes:** the author names the three to five
things this reader currently reads instead, from their own experience, and each
is verified before it enters the table.

## Reader interviews: none run

The skill asks for 10–20. The corpus has one adopter, who is the author. That
is worth stating rather than working around: every claim in this brief about
what the reader believes and wants is an assumption held by one person about
people he has not spoken to.

It is also directly testable with the method the book itself teaches, which is
the obvious first application of `claim-fixture` outside its own repository.
