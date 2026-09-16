# Filters

`knap help filter <name>` is authoritative — it ships with the binary, gives
exact whitespace, and cannot drift from the tool. **Read it before using a
filter you have not used before.**

This file is the part that help output cannot give you: which filter to reach
for, what the result actually looks like, and where the surprises are. Every
output below is copied from a verification case, not from memory.

## Two things that will bite you first

**Parameter syntax is not uniform.** Some filters take a parenthesised tuple,
some take repeated colons, some take a bare number:

```knap
{{ title | truncate:(10, "...") }}     tuple
{{ title | replace:"matrix":"MATRIX" }}  repeated colon
{{ nums  | nth:2 }}                     bare number, unquoted
```

Guessing gives `INVALID_FILTER_ARGUMENTS` with the accepted forms in the message
— which is the fastest way to learn one. knap reports **every** bad filter in
the template at once, with `line:column`, not just the first.

**Several filters emit Obsidian-flavoured Markdown, not portable Markdown.**
`highlight` → `==x==`, `comment` → `%%x%%`, `callout` → `> [!warning]`,
`wikilink` → `[[x]]`, `embed` → `![[x]]`. None of those render on GitHub or in
a standard CommonMark pipeline. Check your destination before reaching for them.

## By the shape of the job

| you have | you want | reach for |
|---|---|---|
| array of same-shaped objects | a table | `table`, `table_pretty` for padded |
| array of objects | one column | `map:"Prop"` |
| array of objects | a subset of rows | `where:"Prop","value"` |
| array of objects | a total | `sum:"Prop"` |
| array | ordered | `sort`, `sort:"Prop"` for objects |
| array | a sentence | `join:", "` |
| array | a bullet list | `list` |
| array with blanks | no blanks | `compact` |
| array with repeats | no repeats | `unique` |
| a value | a front-matter line | `yaml_property:"name"` |
| text for a filename | a safe filename | `safe_name` |
| text that must render literally | escaped punctuation | `escape_md` |
| text with markup to strip | plain text | `strip_md`, `strip_tags` |

## Text — case `c08-text`

```
upper          | THE MATRIX RELOADED
title          | The Matrix Reloaded
capitalize     | The matrix reloaded
kebab          | the-matrix-reloaded
snake          | the_matrix_reloaded
camel          | theMatrixReloaded
pascal         | TheMatrixReloaded
uncamel        | some value here
trim           | [Padded Text]
truncate       | the mat...
truncatewords  | the matrix…
length         | 19
replace        | the MATRIX reloaded
slice          | matrix
split          | ["the","matrix","reloaded"]
safe_name      | notes2024 recap
escape_md      | a\*b\_c\[d\]
strip_md       | bold and em and a link
```

Watch: `capitalize` **lowercases the rest** — it is not title case. `truncate`
counts the suffix inside its limit (`truncate:(10,"...")` gives 10 characters
total), while `truncatewords` appends a Unicode `…` you did not ask for.
`safe_name` strips `/` `:` `?` but **keeps spaces**, so filenames can still
contain them. `split` returns a JSON array, not text.

## Collections — case `c09-collections`

```
sort           | [1,2,3]
sort:prop      | Bo,Cy,Ada
reverse        | [2,1,3]
first/last     | beta / 2
unique         | ["beta","alpha","",null,"gamma"]
compact        | ["beta","alpha","beta","gamma"]
join           | 3 + 1 + 2
length(arr)    | 3
map            | eng,ops
where          | Ada,Cy
nth            | 1
merge          | [3,1,2,"4"]
sum            | 6
sum:prop       | 240
slice(arr)     | [3,1]
object         | [["a",1],["b",2]]
template       | Ada (eng)
               |
               | Bo (ops)
               |
               | Cy (eng)
list           | - 3
               | - 1
               | - 2
```

Watch, in order of how much time it will cost you:

- **`compact` and `unique` are complementary, not overlapping.** `compact`
  removes `null` and `""` and **keeps duplicates**; `unique` removes duplicates
  and **keeps `null` and `""`**. For both, chain them: `| compact | unique`.
- **`merge:4` produced the string `"4"`, not the number `4`.** A merged literal
  is not typed like the array it joins, so a later `sum` or comparison may not
  do what you expect.
- **`template` returns text, not an array.** It joins its items with blank
  lines, so a following `join` has nothing to join and silently does nothing —
  which is what the blank lines above are.
- `reverse` reverses order; it does not sort. `nth` is 1-indexed.
- Bare arrays interpolate as JSON. Reach for `list`, `join`, or `table` when you
  want Markdown.

## Markdown structure, links and YAML — case `c10-markdown`

```
h2             | ## the matrix reloaded
bold/italic    | **x** *y* ~~z~~ ==h==
code           | `a=1`
code_block     | ```python
               | a=1
               | ```
blockquote     | > First line.
               | > Second line.
callout        | > [!warning]
               | > careful
hr             | mid
               |
               | ---
indent         |   First line.
               |   Second line.
hard_break     | First line.··
               | Second line.
comment        | %%hidden%%
link           | [Example](https://example.com/a%20b?q=1&r=2)
image          | ![Alt](https://example.com/a%20b?q=1&r=2)
wikilink       | [[Page|Alias]]
embed          | ![[Page]]
yaml           | a: 1
               | b: 2
yaml_property  | tags:
               |   - "beta"
               |   - "alpha"
               |   - "beta"
               |   - "gamma"
```

(`··` marks the two trailing spaces `hard_break` emits.)

`blockquote`, `indent` and `hard_break` apply to **every** line, so
multi-paragraph text stays intact. `link` and `image` percent-encode the URL for
you — do not also run `encode_uri`, or you will double-encode. `yaml` and
`yaml_property` quote strings and leave numbers, booleans and `null` unquoted;
`yaml_property` emits **no delimiters**, so the `---` fence is yours to write.

## Numbers, dates, HTML — case `c10-markdown`

```
number_format  | 1,234,567.89
round          | 1234567.9
calc           | 1234.567891
duration       | 01:02:05
date           | 2026-09-16
date_modify    | 2026-09-17
encode_uri     | https%3A%2F%2Fexample.com%2Fa%20b%3Fq%3D1%26r%3D2
strip_tags     | hi there
strip_attr     | <p>hi <b>there</b></p>
remove_tags    | <p class="x">hi there</p>
```

`number_format` adds separators and is for display only. `duration` renders
seconds as `HH:MM:SS`. `strip_tags` removes tags **and** keeps text;
`strip_attr` keeps tags and drops attributes; `remove_tags:"b"` drops the named
tag and keeps its content. All three take allowlists — see their help.

## Not available in the CLI

`knap help filters` names these at the end, and it is worth knowing before you
design around one:

- `html_to_json` and `remove_html` are DOM-dependent and need the library API.
- Host integrations — markdown conversion, browser selectors, prompts — are not
  in the CLI at all.

If a task needs those, the CLI is the wrong entry point. Say so rather than
composing a template around a filter that will not resolve.
