# Generating alternatives and challenging the plan

The goal is to break a single narrative into a set of live possibilities and to
find the observations that would tell them apart.

## Premortem

Prompt: *It is 12–18 months later. The program failed materially. What happened?
What warning signs were ignored? Which assumption turned out false? Who was
harmed, surprised, or unable to act? What was the first recoverable moment?*

The premortem makes it socially acceptable to raise concerns before commitment.
Run it across **every** required lens and record a mechanism, an earliest
indicator, and an owner per failure story:

technical · operational · user / customer · financial · safety · cybersecurity /
adversarial · legal / regulatory · reputational / communications · equity and
accessibility · governance / ownership · dependency / vendor · data / model.

A premortem output with no earliest indicator per item is not finished — it is a
worry list.

## Red teaming and devil's advocacy

A red team is not "be negative". It is assigned a different hypothesis, a
different evidence standard, and a deliverable.

| Mode | Question |
|---|---|
| Devil's advocate | What is the strongest case that the preferred plan is wrong? |
| Competitive / adversarial | How would a competitor, attacker, or self-interested insider exploit this? |
| Outside view | What happened in comparable projects, industries, historical cases? |
| Alternative futures | What plausible future makes the current strategy fail? |
| Model challenger | What alternative causal / system model fits the same evidence? |
| Stakeholder inversion | How does this look to a non-user, an excluded group, a regulator, an operator, a maintainer, an affected community? |
| Boundary challenger | What sits just outside the stated system boundary but can affect the outcome? |
| Incentive challenger | What behaviour does this policy actually reward? |
| Failure analyst | What chain of small failures defeats the safeguards? |

## Outside view

Before estimating from the inside ("our plan, our steps, our timeline"), find
the reference class: comparable efforts and their base rates for cost overrun,
delay, adoption, failure. State the base rate first, then argue why this case
differs — not the reverse.

## Analysis of competing hypotheses

Do not ask "is our hypothesis correct?" Build a set `H = {H1, H2, …}` and an
evidence matrix. For each evidence item `Ej`, mark whether it is **expected**,
**unexpected**, **neutral**, or **missing** under each hypothesis.

| Evidence | H1: demand decline | H2: measurement outage | H3: checkout friction | Diagnostic next check |
|---|---|---|---|---|
| Web traffic stable | weakens | neutral | supports | Compare server logs vs analytics events |
| Purchase events down | supports | supports | supports | Audit event pipeline + payment logs |
| Cart abandonment up | weakens | neutral | **supports strongly** | Checkout errors by browser / version |
| Revenue stable in processor data | weakens | **supports strongly** | weakens | Reconcile orders vs processor |

Key moves:

- **Diagnosticity beats confirmation.** "Purchase events down" is consistent
  with every hypothesis — it barely updates anything. "Cart abandonment up" and
  "revenue stable in processor data" each separate the field. Spend the probe
  budget there.
- **Try to disprove the front-runner.** Look for the evidence that would break
  the currently favoured `H`, and check the sensitivity of the conclusion to
  the one or two most influential evidence items.
- **Report the set.** Give the ranked hypotheses, the evidence matrix, the
  diagnostic evidence still missing, and observable milestones that would
  indicate a different path — not just the winner.

### Evidence matrix schema

```yaml
competing_hypotheses:
  question: ""
  hypotheses:
    - id: "H1"
      statement: ""
      prior_rationale: ""
  evidence:
    - item: ""
      source_reliability: "low | medium | high"
      under:
        H1: "expected | unexpected | neutral | missing"
        H2: "..."
      diagnostic: true          # does it separate any pair of hypotheses?
  diagnostic_evidence_needed: []
  current_ranking: []           # with the caveat that it can change
  what_would_change_our_mind: []
```

## Keeping dissent alive

An operational plan usually needs a single "most likely" story. That story must
never delete the alternatives. Maintain the alternative-hypothesis register and
a "what would change our mind" section alongside the plan, and give both a
review date.
