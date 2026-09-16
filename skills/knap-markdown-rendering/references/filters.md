# Choosing a filter

`knap help filters` lists all 80 with one-line descriptions, and
`knap help filter <name>` gives syntax, parameters, notes and worked examples
with exact whitespace. **That output is authoritative and this file is not** —
it ships with the binary, so it cannot drift from it. Duplicating it here would
create a second copy that can.

What the tool's help does not give you is *which one to reach for*. That is this
file.

## By the shape of the job

| you have | you want | reach for |
|---|---|---|
| array of same-shaped objects | a table | `table`, or `table_pretty` for padded columns |
| array of objects | one column of it | `map:"Prop"` |
| array of objects | a subset of rows | `where:"Prop","value"` |
| array | ordered output | `sort`, or `sort:"Prop"` for objects |
| array | a sentence | `join:", "` |
| array with holes | no holes | `compact` |
| a value | a YAML front-matter line | `yaml_property:"name"` |
| a note name | an Obsidian link | `wikilink`, `wikilink:"Alias"` |
| prose | a quoted block | `blockquote` |
| text going into a filename | a safe filename | `safe_name` |
| text that must render literally | escaped punctuation | `escape_md` |

Filters chain left to right and parameters follow a colon:
`{{ cast | where:"Role","Neo" | map:"Actor" | join:", " }}` →
`Keanu Reeves` (case `c05-where-map`).

## Not available in the CLI

`knap help filters` ends by naming these, and the skill repeats it because it is
the kind of thing an agent discovers at the worst moment:

- `html_to_json` and `remove_html` are DOM-dependent and need the library API.
- Host integrations — markdown conversion, browser selectors, prompts — are not
  supplied by the CLI at all.

If a task needs those, the CLI is the wrong entry point; say so rather than
composing a template around a filter that will not resolve.
