# Acceptance checklist

Run before calling the book finished. Each item is a yes/no gate. A "yes"
requires the named evidence — not an opinion. Record any exception explicitly
with its justification.

```yaml
acceptance:
  - item: "The intended reader can identify themselves from the title, subtitle,
      introduction, or description."
    evidence: "≥3 target readers, shown only the cover copy + intro, described the
      book's reader in terms matching the positioning brief."
    status: ""            # yes | no | exception
    note: ""

  - item: "The book makes a clear, distinctive promise and fulfills it."
    evidence: "Promise-vs-delivery map from Pass 1: every promise element is
      delivered by a named chapter; no undelivered promise; no major content
      outside the promise."
    status: ""
    note: ""

  - item: "The strongest claims are supported by appropriate, checkable evidence."
    evidence: "Every claim-ledger row feeding a headline argument is `resolved`
      with a primary or high-quality-secondary source and a passing citation-check."
    status: ""
    note: ""

  - item: "The book distinguishes facts, interpretations, anecdotes, and
      recommendations."
    evidence: "Pass 2 audit found no claim where advice is stated as settled
      evidence or one interpretation as inevitable fact."
    status: ""
    note: ""

  - item: "The structure builds understanding or capability in a logical order."
    evidence: "`tsort` concept order has no cycle; Pass 3 found no term used
      before it is defined; governing structure pattern is followed."
    status: ""
    note: ""

  - item: "Every chapter changes what the reader knows, feels, or can do."
    evidence: "Chapter-function table from Pass 1: every chapter has a non-vague
      `reader_can_now` and a job distinct from its neighbours."
    status: ""
    note: ""

  - item: "There are enough concrete stories, examples, data, and demonstrations
      to make the ideas believable."
    evidence: "Every chapter's `ingredients_present` has story/case AND proof
      points AND actionable guidance (as its type requires)."
    status: ""
    note: ""

  - item: "The book acknowledges relevant uncertainty, limitations, exceptions,
      and counterarguments."
    evidence: "Every consequential claim-ledger row has non-empty `caveats`
      reflected in the prose; each chapter addresses its `likely_objection`."
    status: ""
    note: ""

  - item: "Outside readers from the target audience found it understandable and
      valuable."
    evidence: "≥5 beta readers from the target audience; feedback tracker shows
      no unresolved cluster (≥3 readers stumbling at one point)."
    status: ""
    note: ""

  - item: "A knowledgeable expert has reviewed content where accuracy matters."
    evidence: "Named subject-matter expert signed off on the technical / medical /
      legal / financial / historical substance; their notes are dispositioned."
    status: ""
    note: ""

  - item: "The book has undergone developmental editing, copyediting, and final
      proofreading."
    evidence: "Passes 1, 4, and 5 complete; post-layout proofread done on the
      typeset files, not the manuscript."
    status: ""
    note: ""

  - item: "Front matter, citations, permissions, illustrations, tables, and
      accessibility considerations are complete."
    evidence: "Project folder: permissions log closed; image/table inventory
      complete with alt text; citation database matches the endnotes; front and
      back matter assembled."
    status: ""
    note: ""
```

**The essential principle:** write the book readers need, not the book you happen
to know how to write today.
