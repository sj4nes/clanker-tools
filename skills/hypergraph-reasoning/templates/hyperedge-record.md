# Hyperedge record

One typed, role-labelled, time-scoped, provenance-backed assertion. Copy per
edge.

```yaml
id: <type>_<date>_<seq>          # e.g. decision_2026_0912_014
type: Decision | Event | Action | ClaimSupport | CausalHypothesis | Requirement | Experiment | Dependency | Contradiction | Outcome

participants:                    # roles from the defined vocabulary, not free text
  - {node: "<ns>:<id>", role: subject}
  - {node: "<ns>:<id>", role: decision_maker}      # or actor / approver / ...
  - {node: "<ns>:<id>", role: selected_option}
  - {node: "<ns>:<id>", role: rejected_option}     # keep declined options
  - {node: "<ns>:<id>", role: constraint}
  - {node: "<ns>:<id>", role: scope}               # what the assertion is limited to
  - {node: "<ns>:<id>", role: budget}
  - {node: "<ns>:<id>", role: evidence}
  # a role the source does not fill is omitted or {node: unknown, role: X} — never guessed

valid_time: {start: "<ISO date>", end: null}       # end null = open interval
recorded_at: "<ISO datetime>"

provenance:
  - source_id: "<ns>:<id>"
    source_span: "<exact quoted text / table cell / tool-output line>"
    extractor: "agent" | "human"
    extraction_time: "<ISO datetime>"

epistemic_status: asserted | observed | inferred | proposed | superseded
confidence: 0.0-1.0
access_scope: "<who may see this edge>"
version: 1

# modality / negation captured explicitly where present:
modality: null | "may" | "must" | "must_not" | "considered" | "rejected"

# for superseded edges only:
superseded_by: "<edge id>"
```

## Checklist

- [ ] Type is set and matches the assertion (a rejected option is a
      `rejected_option` role, not a `Decision` to adopt).
- [ ] Every role value is either grounded in the source or omitted — none
      invented.
- [ ] `valid_time.start` reflects "effective <date>" / "as of" language.
- [ ] `provenance.source_span` is present and is verbatim.
- [ ] `epistemic_status` distinguishes what the source states from what you
      inferred or hypothesized.
- [ ] Scope / budget / region / segment qualifiers are roles *inside* this
      edge, not separate binary edges.
