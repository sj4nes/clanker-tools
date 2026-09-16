# Verified patterns

Every template here is a case in `verification/cases/`, rendered by the real
`knap` and diffed against captured output. The case name is given so you can
read the exact expected bytes.

## YAML front matter — the fence is `---`

`c03-frontmatter`:

```knap
---
year: {{ year }}
{{ directors | wikilink | yaml_property:"directors" }}
---

# {{ title }}
```

```markdown
---
year: 1999
directors:
  - "[[Lana Wachowski]]"
  - "[[Lilly Wachowski]]"
---

# The Matrix
```

`yaml_property` emits the key and its value with correct block indentation —
no separate `yaml` or `indent` filter is needed, and it deliberately emits **no
delimiters**. The fence is yours to write, and it must be `---`: version 1.0.0
of this skill used `***`, which renders perfectly and parses as front matter
nowhere. `run.sh` asserts the rendered document matches `\A---\n.*?\n---\n`,
which is a check `***` cannot pass and a diff cannot make.

Apply transformations such as `wikilink` **before** `yaml_property`.

## A section that disappears when its data is empty

`c02-table`:

```knap
{% if cast %}## Cast

{{ cast | sort:"Actor" | table }}
{% endif %}
```

```markdown
## Cast

| Actor | Role |
| - | - |
| Carrie-Anne Moss | Trinity |
| Keanu Reeves | Neo |
```

`table` takes column names from the objects' keys, so the array must be
consistently shaped. Guarding with `{% if %}` is what stops an empty array
leaving a heading with nothing under it — and `[]` is false, so the guard fires
on an explicitly empty collection as well as an absent one.

## Prose into a quote

`c01-blockquote`:

```knap
# {{ title }}

{{ plot | blockquote }}
```

`blockquote` prefixes **every** line, so multi-paragraph text stays inside the
quote.

## Filtering a collection down to a sentence

`c05-where-map`:

```knap
{{ cast | where:"Role","Neo" | map:"Actor" | join:", " }}
```

→ `Keanu Reeves`

## One file per record

```sh
knap batch row.knap --data-json '[{"Actor":"Neo"},{"Actor":"Trinity"}]' \
     --output-dir out --filename '{{ Actor | safe_name }}.md'
```

`--data` also takes a CSV file, a JSON array file, or a folder of JSON objects.
`--dry-run` lists the paths without writing. `--overwrite` is required to
replace existing files, and duplicate filenames within one batch are an error
rather than a silent last-write-wins — so `safe_name` on a field that is not
unique will fail the batch, which is the desired direction.

## Where knap is the wrong tool

Compose prose that needs reasoning, voice, or editorial judgement **first**, as
prose, and pass it in as a data value. Use the template for the repeatable
structure around it. A template is not a place to think.
