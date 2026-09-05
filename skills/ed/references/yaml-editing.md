# YAML editing rules for `ed`

YAML is indentation-sensitive and admits many syntactically valid but semantically unintended structures. Treat it as high-risk for line-oriented editing.

## Preserve indentation exactly

YAML nesting is controlled by whitespace. Before editing a block, inspect neighboring lines with line numbers and literal rendering:

```text
/target-key/
-3,+12n
-3,+12l
```

Use spaces, not tabs, unless the existing file demonstrably uses a nonstandard convention and the task explicitly requires preserving it.

When adding a nested mapping entry:

```yaml
service:
  image: example/service:1.0
```

the inserted key must align with `image`, not with `service`:

```text
/^  image: example\/service:1\.0$/
a
  replicas: 3
.
```

When adding an item to a sequence, match the surrounding indentation and dash placement:

```yaml
env:
  - name: LOG_LEVEL
    value: info
```

Do not insert:

```yaml
  - name: NEW_VALUE
  value: enabled
```

because `value` is incorrectly aligned and changes the structure.

## Quote carefully

Preserve the file's established quote style. Do not add or remove quotes casually. YAML can reinterpret unquoted text as booleans, nulls, numbers, timestamps, or special values.

Potentially risky unquoted values include:

```yaml
yes
no
on
off
null
123
01
2026-09-05
```

If the existing schema or local style requires a string, preserve or add quotes consistently:

```yaml
enabled: "true"
```

Do not "normalize" unrelated YAML values while implementing a focused change.

## Avoid duplicate keys

YAML parsers differ in their treatment of duplicate mapping keys. Before adding a key, search the containing mapping block and then inspect the relevant range.

For example, before adding `timeout` under a service entry:

```text
/^[[:space:]]*service:/
.,+30n
```

Do not add `timeout:` if it already exists in that mapping. Update the existing key instead.

## Preserve comments and anchors

Do not delete or move YAML comments, anchors, aliases, merge keys, block scalars, or document separators without understanding their role.

Pay special attention to:

```yaml
defaults: &defaults
  retries: 3

service:
  <<: *defaults
```

and block scalar syntax:

```yaml
script: |
  echo "hello"
  echo "world"
```

An edit within a block scalar must preserve its indentation. A line accidentally dedented out of the scalar changes the YAML structure.

## YAML safe-edit checklist

Before writing YAML changes, confirm:

- Mapping indentation is consistent.
- Sequence items align with peer items.
- Added keys do not duplicate existing keys at the same mapping level.
- Quoting preserves the intended scalar type.
- Block scalar content remains indented correctly.
- Comments and anchors still attach to the intended structure.
- The file parses with the project's expected YAML tool.

## Validation

```sh
python - <<'PY'
import pathlib
import yaml
yaml.safe_load(pathlib.Path("path/to/file.yml").read_text())
print("YAML is valid")
PY
```

Use this only when PyYAML is available and when loading the file will not execute untrusted behavior. Prefer a project-provided linter or parser if one exists.
