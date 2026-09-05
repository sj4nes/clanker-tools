# `bc` calculation patterns

Keep conversion constants and rates visible as named variables, and identify their units in comments or prose.

## Basic arithmetic

```sh
bc <<'BC'
scale = 10
a = 125.75
b = 18.25
a + b
a - b
a * b
a / b
BC
```

## Percentage of a value

`amount = base * percentage / 100`

```sh
bc <<'BC'
scale = 12
base = 240
pct = 17.5
amount = base * pct / 100
amount
BC
```

## Percentage change

`percent change = (new - old) / old * 100`

```sh
bc <<'BC'
scale = 12
old = 84.50
new = 92.25
change = (new - old) / old * 100
change
BC
```

Always handle `old = 0` before applying this formula. Percentage change from zero is undefined or requires a domain-specific definition.

## Unit conversion

`kilometers = miles * 1.609344`

```sh
bc <<'BC'
scale = 12
miles = 42.195
km_per_mile = 1.609344
km = miles * km_per_mile
km
BC
```

## Weighted average

`xbar = sum(w_i * x_i) / sum(w_i)`

```sh
bc <<'BC'
scale = 12
x1 = 88; w1 = 0.25
x2 = 93; w2 = 0.35
x3 = 79; w3 = 0.40
weighted_sum = x1 * w1 + x2 * w2 + x3 * w3
weight_total = w1 + w2 + w3
average = weighted_sum / weight_total
average
weight_total
BC
```

Validate that the total weight equals 1 when weights are intended as proportions.

## Compound growth

Nominal annual rate `r`, compounded `n` times per year over `t` years: `A = P(1 + r/n)^(nt)`.

```sh
bc -l <<'BC'
scale = 24
p = 5000
r = 0.06
n = 12
t = 10
period_rate = r / n
period_count = n * t
a = p * (1 + period_rate) ^ period_count
a
BC
```

Assumes the rate is nominal and compounding occurs at the supplied frequency. Do not apply it to an APY, a continuously compounded rate, or an irregular cash-flow stream without changing the formula.

## Continuous compounding

`A = P * e^(rt)` — requires `e(x)` from `bc -l`; confirm it is provided.

```sh
bc -l <<'BC'
scale = 24
p = 5000
r = 0.06
t = 10
a = p * e(r * t)
a
BC
```

## Square roots

```sh
bc -l <<'BC'
scale = 20
x = sqrt(2)
x
x * x
BC
```

Validate by squaring: `x * x` should agree with 2 to the expected precision, subject to truncation.

## Integer arithmetic and divisibility

`bc` handles arbitrarily large integers:

```sh
bc <<'BC'
123456789012345678901234567890 * 98765432109876543210
BC
```

Modulo for divisibility (`0` means divisible):

```sh
bc <<'BC'
n = 123456789
n % 9
BC
```

Quotient and remainder:

```sh
bc <<'BC'
n = 123
d = 10
q = n / d
r = n % d
q
r
BC
```

Keep operands integral when using `%`. Modulo has no intuitive meaning for decimal values.

## Base conversion

`bc` supports input/output bases via `ibase` and `obase`. The trap: **once `ibase` changes, every later numeric literal — including the one you assign to `obase` — is read in the new base.** After `ibase = 16`, writing `obase = 10` sets `obase` to sixteen (`10` base 16), so a hex-to-decimal conversion silently prints hex. Set `obase` *first*, or use the hex digit `A` for ten:

```sh
bc <<'BC'
obase = A
ibase = 16
FF
BC
```

Expected: `255`. Or keep it on one line with `obase` before `ibase`:

```sh
echo 'obase=10; ibase=16; FF' | bc     # => 255
```

Decimal to hex needs no such care (`ibase` stays 10):

```sh
bc <<'BC'
obase = 16
255
BC
```

Expected: `FF`. Prefer a fresh `bc` invocation per conversion to avoid leftover base state. Use base conversion for integer values only unless fractional-digit behavior has been confirmed on the installed implementation.

## Reusable `define` functions

Keep functions small and document assumptions.

Positive-value rounding (half away from zero). Drops to `scale = 0` only for the
truncating division so it works on both GNU `bc` and the macOS/FreeBSD `bc`, where
a bare `x / 1` does not truncate:

```bc
define roundpos(x, d) {
    auto os, r
    os = scale
    scale = 0
    r = (x * (10 ^ d) + 0.5) / 1
    scale = d
    return r / (10 ^ d)
}
```

Monthly payment for a fixed-rate, fully amortizing loan: `M = P * i(1+i)^N / ((1+i)^N - 1)`, where `P` is principal, `i` the periodic rate, `N` the number of payments.

```sh
bc -l <<'BC'
scale = 24

define payment(p, i, n) {
    auto f
    f = (1 + i) ^ n
    return p * (i * f) / (f - 1)
}

principal = 300000
annual_rate = 0.065
payments_per_year = 12
years = 30

periodic_rate = annual_rate / payments_per_year
payment_count = payments_per_year * years
monthly_payment = payment(principal, periodic_rate, payment_count)
monthly_payment
BC
```

Before using this formula, confirm: the rate is nominal annual interest, not APR with fees or APY; payments occur at regular intervals; the loan is fully amortizing; the periodic rate is nonzero. If the periodic rate is zero, use `M = P / N` instead of dividing by a zero denominator.
