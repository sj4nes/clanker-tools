# How a knap render goes wrong

Every statement here is pinned by a case in `verification/`. If the tool changes
one of them, `run.sh` fails and this file is what must be corrected.

## The one that matters: a missing variable is silent

```
template: A[{{ nope }}]B[{{ a.b.c }}]C
output:   A[]B[]C
exit:     0
```

Case `c04-missing-is-silent`. A variable absent from the data — a typo, a
renamed field, an API that stopped returning it — renders as the empty string
and the command **succeeds**. There is no strict mode.

So **exit 0 is not evidence the document is right.** A rendered file with a hole
in it is indistinguishable, by status code, from a correct one. Check the
output, not the return value: assert the rendered text contains what the data
said it should, or diff it against a snapshot.

This is the whole reason `run.sh` diffs output rather than checking `$?`.

## `knap validate` is a static check, and says so

```
$ knap validate -t '{% if a %}x'
error PARSE_ERROR: Missing {% endif %} to close {% if %}      exit 1

$ knap validate -t '{{ definitely_not_in_any_data }}'
Template is valid (static checks only; runtime values are not checked).   exit 0
```

It catches syntax. It cannot catch the failure above, because it never sees your
data. Both behaviours are asserted in `run.sh` section 2 — including the second
one, so that a future version which *did* start checking values would fail the
harness rather than silently making this page wrong.

## Errors that do fail loudly

| mistake | exit | message |
|---|---|---|
| unknown filter | 1 | `error UNKNOWN_FILTER: Unknown filter "nosuch"` |
| unclosed tag | 1 | `error PARSE_ERROR: Missing {% endif %} to close {% if %}` |

Both print `file:line:column` and a `Help:` line pointing at the relevant
`knap help` topic. Case `c06-unknown-filter`.

## `-t` cannot take a template starting with a dash

```
$ knap render -t '---
year: {{ year }}
---'
knap: Option '-t' argument is ambiguous.
```

Which bites exactly when you are doing the most common Markdown job there is,
writing YAML front matter. Three ways out, in order of preference:

1. **Put the template in a file** — `knap render page.knap -d data.json`. This
   is what the cases do, and what production use should do anyway.
2. `--template=---...` with an equals sign.
3. `-t-` immediately followed by the text, per the tool's own error message.

## Values render as their JSON type

A bare array interpolates as JSON, not as a list:

```
{{ directors }}  ->  ["Lana Wachowski","Lilly Wachowski"]
```

Use `list`, `join`, or `table` when you want Markdown. Conditions treat `false`,
`null`, `undefined`, `""`, `0`, and `[]` as false — so `{{ count ?? "none" }}`
falls back when `count` is `0`, which is rarely what a report wants.
