# SPEC — duration strings

A **duration** is a whole number of seconds, at least 0 and less than 360000.

## Text form

A duration string is one to three *components* separated by single spaces. A
component is a decimal integer followed by one of the unit letters `h`, `m`, `s`.

A duration string is well-formed when all of the following hold:

- Units appear in the order `h`, `m`, `s`, and no unit appears more than once.
- At least one component is present.
- The integer part is one or more decimal digits with no leading zero, unless
  the integer is the single digit `0`.
- Only the first component present may exceed the range of its unit. A later
  component using `m` or `s` is less than 60.
- The total is less than 360000 seconds.

The value of a duration string is `3600·h + 60·m + s` over the components
present. Text that is not well-formed is not a duration string.

## `parse_duration(text) -> int`

Returns the value of a well-formed duration string. Raises `ValueError` for
anything that is not a well-formed duration string, including a `text` that is
not a `str`.

## `format_duration(seconds) -> str`

Returns the **canonical** duration string for a duration. The canonical string
omits components whose value is zero; the canonical string for a duration of
zero is the single component using `s`. Raises `ValueError` for an `int` outside
the duration range, and `TypeError` for a `seconds` that is not an `int`. A
`bool` is not an `int` for this purpose.

## Relationship

Every string `format_duration` returns is well-formed. `parse_duration` accepts
well-formed strings that `format_duration` never returns.

Example: `"1h 30m"` has the value 5400.
