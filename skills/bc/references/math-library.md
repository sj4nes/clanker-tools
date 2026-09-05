# `bc` math library (`bc -l`)

Use `bc -l` for the standard math library when available. Common functions:

| Function | Typical meaning |
|---|---|
| `s(x)` | Sine, with `x` in radians |
| `c(x)` | Cosine, with `x` in radians |
| `a(x)` | Arctangent, returning radians |
| `l(x)` | Natural logarithm |
| `e(x)` | Exponential `e^x` |
| `j(n, x)` | Bessel function of integer order `n` |
| `sqrt(x)` | Square root |

The math library commonly sets a larger default `scale`, but set `scale` explicitly anyway.

## Radians and degrees

Trigonometric functions use radians. Convert degrees explicitly: `radians = degrees * pi / 180`.

A portable way to derive pi in `bc -l` is `pi = 4 * a(1)` (that is, `4 * arctan(1)`):

```sh
bc -l <<'BC'
scale = 30
pi = 4 * a(1)
degrees = 30
radians = degrees * pi / 180
s(radians)
BC
```

## Caveats

- Confirm `e()`, `l()`, `s()`, `c()`, `a()` are provided by the installed implementation before relying on them.
- Do not claim exact trigonometric or transcendental outputs. They are numerical approximations affected by the library implementation and the selected scale.
