# Fat outline

More than chapter titles. One brief per chapter, plus a book-level structure
decision. Readers experience nonfiction as a sequence of answers, discoveries, or
capabilities — not a warehouse of information.

## Book-level

```yaml
outline:
  governing_structure: ""        # problem->solution | beginner->advanced |
                                 #   past->present->future | myth->evidence->action |
                                 #   case-study->principle | journey/chronology
  structure_rationale: ""        # why this pattern fits the book type and reader
  concept_dependency_order: []   # from tsort: every prerequisite concept before the
                                 #   chapter that first uses it
  chapters_that_fight_the_pattern: []   # flagged for reorder / cut / rework
```

## Per chapter

```yaml
chapter:
  number: 0
  working_title: ""
  entering_question: ""          # the question the reader has when the chapter opens
  central_claim_or_skill: ""     # the ONE thing this chapter establishes
  why_it_matters_now: ""
  key_evidence: []               # claim-ledger row ids
  running_example_or_scene: ""   # a person, case, decision, failure — not a generic example
  framework_or_process: ""       # the explanation / method / model
  likely_objection: ""           # the credible misconception or pushback, and the answer
  practical_takeaway: ""
  reader_can_now: ""             # "After reading this chapter, the reader will understand
                                 #  or be able to ___."  NOT "know more about the topic".
  distinct_from_neighbours: ""   # how this chapter's job differs from the ones before/after
  through_line_transition: ""    # closing sentence that makes the next chapter necessary
  ingredients_present:           # a useful chapter usually has all five
    idea_or_framework: false
    story_or_case: false
    reasoning: false
    proof_points: false          # data, citations
    actionable_guidance: false
```

## Structure patterns

| Pattern | Best for | Progression |
|---|---|---|
| Problem → solution | practical books | diagnose → principles → method → implementation |
| Beginner → advanced | skill-building | foundations → practice → edge cases → mastery |
| Past → present → future | history, ideas | origins → turning points → current implications |
| Myth → evidence → action | corrective books | common belief → what evidence shows → what to do |
| Case study → principle | business, applied | story → lesson → tool → next case |
| Journey / chronology | narrative nonfiction | inciting event → escalation → resolution → meaning |

## Gate to Phase 4

- [ ] Every chapter has a non-vague `reader_can_now` (not "know more about X").
- [ ] Every chapter's `distinct_from_neighbours` is filled — no chapter repeats
      another in new words.
- [ ] `governing_structure` is chosen; chapters that fight it are flagged.
- [ ] `concept_dependency_order` from `tsort` has no cycle and no term used
      before it is introduced.
- [ ] Every chapter has a `through_line_transition`.
