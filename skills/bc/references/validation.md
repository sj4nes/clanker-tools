# Validating `bc` calculations

Every nontrivial calculation must include at least one meaningful check.

## Identity check

For a percentage calculation, `final + discount = original`:

```sh
bc <<'BC'
scale = 12
original = 79.99
rate = 15 / 100
discount = original * rate
final = original - discount
original
discount + final
BC
```

The two values should agree to the selected precision.

## Reverse calculation

For a unit conversion, `miles = kilometers / 1.609344`:

```sh
bc <<'BC'
scale = 12
miles = 42.195
factor = 1.609344
km = miles * factor
round_trip_miles = km / factor
miles
round_trip_miles
BC
```

## Bounds check

Check whether the result lies within physically or logically possible limits:

- A percentage is between 0 and 100 when the domain requires it.
- A discount amount is no greater than the original price.
- A weighted average lies between the minimum and maximum inputs when all weights are nonnegative.
- A probability lies in [0, 1].
- A duration, count, quantity, distance, or balance is nonnegative when required.

## Alternate-formula check

Compute the same result from an equivalent staged expression and compare at a high scale:

```sh
bc -l <<'BC'
scale = 24
p = 10000
r = 0.0525
n = 12
t = 5

a1 = p * (1 + r / n) ^ (n * t)

period_rate = r / n
periods = n * t
factor = (1 + period_rate) ^ periods
a2 = p * factor

a1
a2
a1 - a2
BC
```

The difference should be zero or negligible at the selected precision.

## Known-case check

Use a case with an obvious answer before relying on a reused formula:

- 10% of 100 must equal 10.
- A 0% growth rate must preserve the principal.
- A 1:1 unit conversion must preserve the number.
- A zero discount must preserve the original price.
- A weight of 1 on one value must return that value.
