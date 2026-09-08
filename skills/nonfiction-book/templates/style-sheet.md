# Style sheet

The consistency spine. Created before the line-edit pass, maintained through
copyedit and proofread. Every decision that could be made two ways lands here so
it is made once.

```yaml
style_sheet:
  base_style: ""                 # e.g. Chicago Manual of Style 18th ed., author-date
  dictionary: ""                 # e.g. Merriam-Webster; first spelling
  english_variant: ""            # US | UK | other

  citation_system: ""            # notes-bibliography | author-date
  citation_format_notes: ""      # ibid. policy, short-form rules, URL/access-date policy

  numbers:
    spell_out_threshold: ""      # e.g. "spell out zero through one hundred"
    percentages: ""              # "percent" vs "%"; digits always
    dates: ""                    # "3 September 2026" | "September 3, 2026"
    ranges: ""                   # en dash; "2019-2024"

  capitalization: []             # per-term decisions: "the internet" (lc), "Global South" (cap), ...
  hyphenation: []                # "decision-making" (n. open, adj. hyphenated), ...
  spelling_exceptions: []        # "adviser" not "advisor", "judgement" not "judgment", ...

  terms:                         # the controlled vocabulary — one term per concept
    - term: ""
      definition: ""             # plain-language, as it will first appear to the reader
      first_used_chapter: 0
      do_not_use: []             # rejected synonyms that would read as different concepts

  names_and_titles: []           # confirmed spellings, honorifics, first-mention full forms
  recurring_people: []           # name, role, first-mention description, on/off-record status

  formatting:
    headings: ""                 # sentence case | title case; informative not clever
    lists: ""                    # when a list vs prose; parallel structure rule
    sidebars_boxes: ""           # when used; label convention
    emphasis: ""                 # italics vs bold policy

  cross_reference_style: ""      # "see chapter 4" | "see page 00" (filled at proof)
```

## Use

- Pass 4 (line edit): terminology consistency is checked against `terms`.
- Pass 5 (copyedit): everything else here is the checklist.
- Post-layout proofread: `cross_reference_style` resolves to real page numbers;
  check nothing broke in typesetting.
