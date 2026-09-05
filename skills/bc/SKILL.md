---
name: bc
description: >-
  Perform exact, reproducible, reviewable calculations with the Unix `bc`
  calculator language instead of shell arithmetic, `expr`, `awk`, or Python.
  Use for decimal arithmetic, percentages and rates, currency with explicit
  rounding, unit conversions, fixed-point financial formulas, large integers,
  base conversion, and parameterized or iterative calculations. Covers the
  precision policy, explicit rounding (bc truncates, it does not round), and
  validation each calculation needs.
version: 1.0.0
author: Simon Janes
tags: [calculation, bc, arithmetic, precision, rounding, finance, terminal]
---

# Using `bc` as a Serious Calculator

You are an autonomous terminal agent that must perform exact, reproducible, reviewable calculations using the Unix `bc` calculator language. Use `bc` for arithmetic, fixed-point decimal work, base conversions, formulas, iterative calculations, and shell-integrated numeric tasks instead of relying on Python for routine calculator work.

Your priorities are:

1. **Numerical correctness**
2. **Explicit precision and rounding behavior**
3. **Auditable formulas and inputs**
4. **Appropriate validation**
5. **Clear reporting of units and assumptions**

Treat every calculation as a small computational transaction:

    define inputs → set arithmetic policy → compute → verify → report

Do not produce a numerical conclusion until you have made the input values, units, formula, and precision policy explicit.

## Operating principles

- Use `bc` for calculations that can be expressed in its arbitrary-precision decimal arithmetic and programming language.
- Do not rely on shell integer arithmetic, `expr`, `awk`, ad hoc mental math, floating-point snippets, or Python when `bc` is sufficient.
- Distinguish exact arithmetic from truncated decimal arithmetic.
- Set `scale` deliberately before division, square roots, exponentiation involving fractional results, or other operations that can produce decimals.
- Never assume `bc` rounds decimal results. Standard `bc` division truncates according to `scale`; communicate that behavior and compensate deliberately when a specific rounding mode is required.
- Preserve full intermediate precision and round only once, at the final reporting boundary, unless a stated policy requires intermediate rounding.
- Include units in surrounding shell variables, comments, labels, or prose; `bc` values themselves are unitless.
- Validate nontrivial results through an independently rearranged formula, a bound check, an identity, a second `bc` expression, or a known test case.
- Make calculations repeatable: use a heredoc or a clearly quoted expression rather than an opaque interactive session for consequential work.
- Do not use `bc` to make unsupported assumptions about input data. Obtain and verify the inputs first.

## Tool selection

Use `bc` when the task involves:

- Addition, subtraction, multiplication, or decimal division.
- Percentages, rates, margins, markups, discounts, taxes, commissions, and proportions.
- Currency arithmetic where decimal behavior and explicit rounding are controlled.
- Unit conversions.
- Financial-style fixed-point formulas where the assumptions are supplied.
- Scientific notation after manually converting it to a decimal expression.
- Large integers beyond shell arithmetic limits.
- Arbitrary-base integer conversion.
- Repeated or parameterized calculations.
- Simple formulas, loops, conditions, functions, and table generation.
- Square roots, trigonometric/logarithmic functions, or exponentiation with the GNU/POSIX math library loaded when available.

Do not use `bc` as the only tool when the task needs:

- Symbolic algebra, advanced statistics, matrix operations, optimization, plotting, data-frame processing, or parsing structured data.
- IEEE floating-point behavior, binary floating-point compatibility, or exact rational-number algebra.
- Complex numbers.
- A domain-specific simulator, compiler, scientific package, or regulated financial calculation whose required rounding convention cannot be implemented and validated clearly in `bc`.
- External information, such as current exchange rates, market prices, tax rates, measurements, or business metrics. Retrieve or receive those inputs first, then calculate with `bc`.

## Startup and capability checks

Use a controlled noninteractive invocation for routine work (`bc`), and `bc -l` for the math library. Use a quoted heredoc for multi-step calculations:

```sh
bc <<'BC'
scale = 10
12.5 / 3
BC
```

Use `-l` when the calculation needs `sqrt`, `s`, `c`, `a`, `l`, `e`, or the math library's higher default scale:

```sh
bc -l <<'BC'
scale = 20
sqrt(2)
BC
```

Do not assume every `bc` implementation offers the same extensions. GNU `bc`, POSIX `bc`, BusyBox `bc`, and BSD-derived variants differ in flags, functions, extension behavior, and syntax. Before depending on a nonportable feature, check `bc --version` (or `bc -v`). If neither works, use only conservative POSIX-style arithmetic, assignments, `if`, `while`, `define`, `ibase`, `obase`, `scale`, `length`, and basic functions confirmed available in the active environment.

## Core arithmetic model

`bc` evaluates expressions in a decimal, arbitrary-precision environment. It is not a conventional floating-point calculator.

The most important control variable is `scale = N`. For division, `scale` controls the number of digits after the decimal point in the quotient, and **the result is truncated, not rounded**:

```sh
bc <<'BC'
scale = 2
10 / 3
BC
```

returns `3.33`, not `3.34`. Do not write an expression involving division without first deciding the required output precision.

### Decimal literals

Use decimal literals directly (`12.50`, `0.075`, `1000`). Prefer a leading zero (`0.333333`, not `.333333`) even though many implementations accept the latter.

Avoid scientific notation in raw `bc` input: `1e-6` is not portable `bc` syntax. Rewrite it as `0.000001`, or `1 / 1000000` with a sufficiently high `scale`.

### Operator precedence

Use parentheses for every nontrivial expression. Do not rely on remembered precedence when a formula affects a meaningful result:

```bc
(annual_rate / periods_per_year) * principal
```

not `annual_rate / periods_per_year * principal`. Parentheses make the intended structure auditable.

## Required calculation workflow

### 1. State the question and units

Before computing, identify: the requested output; every input value; each input's unit; any unit conversions needed; whether the result is exact, truncated, rounded, bounded, or approximate; the number of decimal places required for the final result; and whether the answer has a required convention (currency to cents, percentage to two decimals).

Convert percentage inputs to decimal form explicitly: `15% = 15/100 = 0.15`. Do not silently use `15` where the formula needs `0.15`.

### 2. Choose precision policy

Set a working scale higher than the final reporting scale whenever a calculation includes division, roots, logarithms, exponentials, trigonometric functions, or repeated arithmetic. A reasonable starting policy:

    working scale = final decimal places + 6

Increase the guard digits when: the formula has many sequential operations; the calculation involves compounding or repeated multiplication; inputs are very large or very small; two nearly equal values are subtracted; the result feeds later calculations; or a validation check requires tighter agreement.

| Output requirement | Typical working scale |
|---|---:|
| Whole-number result | 6 |
| Currency to cents | 8 to 12 |
| Percentage to 2 decimals | 8 to 12 |
| Engineering conversion to 6 decimals | 12 to 16 |
| High-precision scientific result | Final digits + 10 or more |

Write the precision policy into the script (`scale = 12`). If the final answer must display two decimal places, calculate at a higher scale and apply an explicit final rounding method.

### 3. Enter inputs once

Assign values to named variables instead of duplicating literals:

```sh
bc <<'BC'
scale = 12

price = 79.99
discount_rate = 15 / 100

discount = price * discount_rate
final_price = price - discount

discount
final_price
BC
```

In portable `bc`, names are conventionally limited to lowercase letters and may be implementation-dependent. For widest compatibility use short lowercase names (`p`, `r`, `d`, `f`) with explanatory comments. Do not reuse a variable for different units or concepts.

### 4. Compute in named stages

Break complex formulas into understandable intermediate quantities. For compound growth `A = P(1 + r/n)^(nt)`:

```sh
bc -l <<'BC'
scale = 20

p = 10000
r = 0.0525
n = 12
t = 5

period_rate = r / n
periods = n * t
growth_factor = (1 + period_rate) ^ periods
future_value = p * growth_factor
interest = future_value - p

future_value
interest
BC
```

Do not compress a significant formula into one line if that makes it hard to inspect or validate.

### 5. Apply final rounding explicitly

Standard `bc` truncates; it does not automatically apply "round half up" or banker's rounding. To round a positive `x` to `d` places: `round(x,d) = floor(x * 10^d + 0.5) / 10^d`.

Truncation itself is not portable as a bare `x / 1`: on GNU `bc` `x / 1` truncates, but on the `bc` that ships with macOS and FreeBSD (Gavin Howard's `bc`) it keeps the ambient `scale`, so `1235.06 / 1` is `1235.060000…`, not `1235`. The portable idiom is to drop to `scale = 0` only for the division and restore it:

```sh
bc <<'BC'
scale = 12

define roundpos(x, d) {
    auto os, r
    os = scale
    scale = 0
    r = (x * (10 ^ d) + 0.5) / 1
    scale = d
    return r / (10 ^ d)
}

roundpos(12.3456, 2)
roundpos(67.9915, 2)
BC
```

produces `12.35` and `67.99`. The multiplication `x * (10 ^ d)` is exact regardless of `scale`; only the `/ 1` needs `scale = 0` to truncate; `scale = d` before the final division makes the printed result carry exactly `d` places. For values that may be negative, use a sign-aware definition:

```sh
bc <<'BC'
scale = 12

define roundhalfaway(x, d) {
    auto os, r
    os = scale
    scale = 0
    if (x >= 0) r = (x * (10 ^ d) + 0.5) / 1
    if (x < 0)  r = (x * (10 ^ d) - 0.5) / 1
    scale = d
    return r / (10 ^ d)
}

roundhalfaway(12.3456, 2)
roundhalfaway(-12.3456, 2)
BC
```

produces `12.35` and `-12.35`. Use this only when "half away from zero" is the required convention. Do not claim it is banker's rounding or a jurisdiction-specific standard.

For currency or regulated financial work, determine the required rounding rule first: truncation; half away from zero; half up; half to even (banker's rounding); round at each line item; or round only after aggregation. These produce different results — state the one used.

### 6. Format output deliberately

`bc` may omit leading zeros (`.5` instead of `0.5`). Do not rely on raw `bc` output alone when presentation matters. Format the final value with a controlled shell formatter *after* the arithmetic and rounding policy are established:

```sh
result=$(
  bc <<'BC'
scale = 12
x = 79.99 * (1 - 15 / 100)
define roundpos(x, d) { auto os, r; os = scale; scale = 0; r = (x * (10 ^ d) + 0.5) / 1; scale = d; return r / (10 ^ d) }
roundpos(x, 2)
BC
)
printf 'Discounted price: $%.2f\n' "$result"
```

Do not use shell formatting as a hidden substitute for deciding how arithmetic should be rounded. For exact integer outputs, print directly from `bc`.

## References

- [`references/patterns.md`](references/patterns.md) — worked patterns: basic arithmetic, percentage of a value, percentage change, unit conversion, weighted average, compound and continuous growth, square roots, integer arithmetic and divisibility, base conversion, `define` functions, loan amortization.
- [`references/math-library.md`](references/math-library.md) — `bc -l` functions, radians vs degrees, deriving pi, caveats on transcendental output.
- [`references/validation.md`](references/validation.md) — identity, reverse-calculation, bounds, alternate-formula, and known-case checks. Every nontrivial calculation needs at least one.

## Error handling

If `bc` reports a syntax error: check unmatched parentheses/braces/quotes in the surrounding shell command; check for scientific notation, unsupported function names, nonportable variable names, or unsupported comments; check whether a variable name collides with an implementation keyword or function; reduce to a small reproducible case; then correct and rerun the full calculation.

If the result has too few decimal places: increase `scale`, then **recompute from the original inputs**. You cannot recover missing digits after low-precision division by raising `scale` later:

```bc
scale = 2
x = 1 / 3      /* x is now 0.33 */
scale = 20
x              /* still 0.33 — the precision is already lost */
```

Correct: set `scale = 20` *before* `x = 1 / 3`.

If the result is surprising: print intermediate variables; check units; verify percentage conversion; confirm parentheses; check whether an integer-looking expression triggered truncating division; check the active `scale`; recompute using an alternate form; compare against a simple magnitude estimate.

If an input is invalid, missing, ambiguous, nonnumeric, or dimensionally incompatible, do not invent a value or silently coerce it. Report the problem and request the correct input.

## Shell-integration rules

Use a quoted heredoc (`<<'BC'`) to prevent shell expansion and preserve the `bc` program exactly. Use `$(...)` only when capturing a single unambiguous final result.

Do not embed untrusted values directly in a `bc` program — interpolated text can alter the program rather than merely provide a number. Validate inputs before interpolation against a strict grammar, such as:

    optional minus sign + digits + optional decimal point and digits

Reject unexpected characters, blank values, locale-specific separators, thousands separators, exponent notation (unless intentionally supported), and arbitrary text. Do not use unquoted shell expansion inside `bc` code unless the value has been validated and controlled.

## Calculation reporting format

For consequential calculations, report enough detail for a reviewer to reproduce the result:

```text
Goal:
- Calculate [requested quantity].

Inputs:
- [Name] = [value] [unit].

Method:
- Formula: [formula].
- Working precision: [scale] decimal places.
- Final rounding: [policy and decimal places].

Result:
- [value] [unit].

Validation:
- [identity, reverse computation, bound check, or known-case result].

Assumptions:
- [Only assumptions actually used.]
```

## Completion requirements

Before declaring a calculation complete, confirm that:

- All inputs were identified and their units are clear.
- The formula matches the requested quantity.
- Percentage and rate units were converted correctly.
- `scale` was set before precision-sensitive operations.
- Intermediate precision was adequate.
- Any final rounding policy was explicitly implemented.
- The final result has an appropriate number of decimal places.
- At least one meaningful validation was performed for nontrivial calculations.
- Any tool, implementation, input, or domain limitation is disclosed.
- The reported result distinguishes calculated values from assumptions or externally sourced inputs.
