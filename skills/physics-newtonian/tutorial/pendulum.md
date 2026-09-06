# Why a Pendulum Keeps Time

> Generated from the `physics-newtonian` capsule (Release 0.1) with the
> `formula-tree-tutorial` skill. The physics, the prerequisite order, and every
> calculation come from that capsule.

## How to run this

Install [upmd](https://upmd.dev), then from the repository root run
`upmd skills/physics-newtonian/tutorial/pendulum.md` for the interactive walk, or
`upmd --ci --all skills/physics-newtonian/tutorial/pendulum.md` to run every
calculation top to bottom.

Each section ends with a calculation you run yourself. Blocks depend on earlier
ones, so `upmd --ci -b capstone skills/physics-newtonian/tutorial/pendulum.md`
runs the whole chain up to the capstone.

## What you need first

Single-variable calculus (a derivative), SI units, and vectors as directed
quantities. Everything else is built below, in the order the capsule's
dependency graph requires: `newton_second_law` → `hookes_law` →
`simple_harmonic_motion` → `angular_frequency_shm` → `shm_period`, with
`small_angle_approximation`, ending at `simple_pendulum`.

The checks track dimensions on the `[M, L, T]` basis: each quantity is three
exponents, and a consistent formula prints `0 0 0` for (left side − right side).

---

## 0. Setup

These constants feed every calculation below: standard gravity, and the pendulum
we will predict at the end.

```bash [name:setup]
export G=9.81            # m/s^2, standard gravity (uniform_gravity)
export PEND_L=1.00       # m, the worked-example pendulum length
export PEND_MEASURED=2.006  # s, a "stopwatch" period to check against
echo "constants loaded: g=$G m/s^2, L=$PEND_L m"
```

## 1. Newton's second law

`F_net = m a` relates the net force on a point mass to its acceleration in an
inertial frame. `F` is in newtons (`M L T^-2`), `m` in kilograms (`M`), `a` in
`m/s^2` (`L T^-2`). This is the *nonrelativistic*, *constant-mass* form — it
breaks if you leave a force out of the sum, or at speeds near light.

Formula: **`F = m a`**

```bash [name:chk_newton_second_law, deps:setup]
# [F] = [m][a] on the (M, L, T) exponent basis
# m: (1,0,0)   a: (0,1,-2)   F should be (1,1,-2)
awk 'BEGIN{ m0=1;m1=0;m2=0; a0=0;a1=1;a2=-2; f0=1;f1=1;f2=-2;
  print (f0-(m0+a0)), (f1-(m1+a1)), (f2-(m2+a2)), " (want 0 0 0)" }'
```

A consistent second law: force dimensions equal mass times acceleration.

## 2. Hooke's law

A spring (or any linear restoring element) pulls back in proportion to how far
it is displaced from equilibrium: `F = -k x`. The stiffness `k` is in `N/m`
(`M T^-2`), `x` in metres. The minus sign is what makes it *restoring* — force
opposes displacement. It fails past the elastic limit and for soft or plastic
materials.

Formula: **`F = -k x`**

```bash [name:chk_hookes_law, deps:chk_newton_second_law]
# [k x] must be a force: k:(1,0,-2)  x:(0,1,0)  ->  (1,1,-2) = [F]
awk 'BEGIN{ k0=1;k1=0;k2=-2; x0=0;x1=1;x2=0; f0=1;f1=1;f2=-2;
  print (f0-(k0+x0)), (f1-(k1+x1)), (f2-(k2+x2)), " (want 0 0 0)" }'
x=0; echo "F at x=0 is $(echo "-1 * 3.5 * $x" | bc)  (want 0)"
```

Restoring force, zero at equilibrium, linear in displacement — the ingredient
that produces oscillation.

## 3. Simple harmonic motion

Put Hooke's law into the second law, `m x'' = -k x`, and the solution is a
sinusoid: `x(t) = A cos(w t + phi)`. `A` is the amplitude (m), `w` the angular
frequency (`rad/s`, dimension `T^-1`), `phi` the starting phase. This is the
*small-oscillation*, *undamped* motion; a nonlinear restoring force or damping
changes it.

Formula: **`x(t) = A cos(w t + phi)`**

```bash [name:chk_simple_harmonic_motion, deps:chk_hookes_law]
# x(t) = amp*cos(w t) must satisfy  m x'' + k x = 0.
# with x'' = -w^2 x, the left side is  amp*cos(w t) * (k - m w^2),
# which is exactly zero when w^2 = k/m.  Evaluate the residual at t = 0.3.
echo "scale=10
amp = 1; m = 0.25; k = 40; t = 0.3
w2 = k / m
x  = amp * c(sqrt(w2) * t)
m * (-w2 * x) + k * x
" | bc -l
echo "  ^ residual of  m x'' + k x  (want 0)"
```

The acceleration always points back toward equilibrium, scaled by `w^2 = k/m` —
so the sinusoid is an exact solution.

## 4. Angular frequency of a mass-spring

Substituting the sinusoid into `m x'' = -k x` gives `m w^2 = k`, so
`w = sqrt(k/m)`. Stiffer spring or lighter mass means faster oscillation; `w` has
dimension `T^-1`. (The capsule machine-checks the algebra `m w^2 = k` as Lean
instance check 4.)

Formula: **`w = sqrt(k / m)`**

```bash [name:chk_angular_frequency_shm, deps:chk_simple_harmonic_motion]
# dimensions: 2*[w] = [k] - [m]  ->  2*(0,0,-1) = (1,0,-2) - (1,0,0)
awk 'BEGIN{ w0=0;w1=0;w2=-1; k0=1;k1=0;k2=-2; m0=1;m1=0;m2=0;
  print (2*w0-(k0-m0)), (2*w1-(k1-m1)), (2*w2-(k2-m2)), " (want 0 0 0)" }'
echo "numeric: w = sqrt(40/0.25) = $(echo "scale=4; sqrt(40/0.25)" | bc -l) rad/s"
```

## 5. Period of the oscillation

The period is the time for one full cycle: `T = 2 pi / w`. For the mass-spring
that is `T = 2 pi sqrt(m/k)`. Crucially `T` does not depend on the amplitude —
that is *isochronism*, and it is why oscillators make clocks.

Formula: **`T = 2 pi / w`**

```bash [name:chk_shm_period, deps:chk_angular_frequency_shm]
# T for the k=40, m=0.25 oscillator, two ways, must agree
w=$(echo "scale=8; sqrt(40/0.25)" | bc -l)
t1=$(echo "scale=6; 8*a(1) / $w" | bc -l)             # 2*pi/w, pi = 4*atan(1)
t2=$(echo "scale=6; 8*a(1) * sqrt(0.25/40)" | bc -l)  # 2*pi*sqrt(m/k)
echo "2pi/w         = $t1 s"
echo "2pi sqrt(m/k) = $t2 s   (want equal)"
```

## 6. The small-angle approximation

For a pendulum the restoring "spring" is gravity, and it is only *linear* for
small swings: `sin(theta) ~ theta` when `theta` is in radians and small. The
leading error is `-theta^3/6`. Use degrees, or swing wide, and this breaks — the
real period grows.

Formula: **`sin(theta) ~ theta`**  (theta in radians, |theta| << 1)

```bash [name:chk_small_angle_approximation, deps:setup]
echo "scale=8; s(0.1) - 0.1" | bc -l
echo "  ^ sin(0.1) - 0.1   (want about -1.667e-4 = -0.1^3/6)"
echo "scale=8; s(0.5) - 0.5" | bc -l
echo "  ^ sin(0.5) - 0.5   (already -0.02: 0.5 rad ~ 29 deg is NOT small)"
```

## 7. The simple pendulum

A point bob on a massless rod of length `L`, swinging a small angle under uniform
gravity `g`, is a simple harmonic oscillator with effective `w^2 = g/L` (the
`(m g L)/(m L^2) = g/L` reduction — Lean instance check 5, mass cancels). So the
period is `T = 2 pi sqrt(L/g)`: `T` in seconds, `L` in metres, `g` in `m/s^2`.
Assumptions: small amplitude, rigid massless rod, point bob, uniform `g`, no
damping. It fails for large swings (elliptic-integral correction), an extended
physical pendulum, or varying `g`.

Formula: **`T = 2 pi sqrt(L / g)`**

```bash [name:chk_simple_pendulum, deps:"chk_shm_period | chk_small_angle_approximation"]
# dimensions: 2*[T] = [L] - [g]  ->  2*(0,0,1) = (0,1,0) - (0,1,-2)
awk 'BEGIN{ t0=0;t1=0;t2=1; l0=0;l1=1;l2=0; g0=0;g1=1;g2=-2;
  print (2*t0-(l0-g0)), (2*t1-(l1-g1)), (2*t2-(l2-g2)), " (want 0 0 0)" }'
```

Length over gravity, square-rooted, times `2 pi` — the units land on seconds.

---

## Capstone: predict a real pendulum

You now have the whole chain. Predict the period of the `L = 1.00 m` pendulum
from Setup, compare it to the "stopwatch" value, and see how far a 30-degree
swing would push it.

```bash [name:capstone, deps:chk_simple_pendulum]
pi=$(echo "scale=10; 4*a(1)" | bc -l)
T=$(echo "scale=6; 2*$pi*sqrt($PEND_L/$G)" | bc -l)
echo "predicted T = 2*pi*sqrt($PEND_L/$G) = $T s"
echo "measured  T = $PEND_MEASURED s"
d=$(echo "scale=6; d = $T - $PEND_MEASURED; if (d < 0) d = -d; d" | bc -l)
echo "difference  = $d s"
awk -v d="$d" 'BEGIN{ if (d < 0.01) print "PASS: small-angle prediction within 10 ms"; else { print "FAIL"; exit 1 } }'

# large-angle correction: T_true ~ T * (1 + theta0^2/16) for amplitude theta0
theta0=$(echo "scale=6; 30 * $pi / 180" | bc -l)   # 30 degrees in radians
corr=$(echo "scale=6; $T * (1 + ($theta0*$theta0)/16)" | bc -l)
echo
echo "at 30-degree amplitude the true period is about $corr s"
echo "  -> the small-angle formula is ~$(echo "scale=2; 100*($corr-$T)/$T" | bc)% low there"
```

If the capstone prints `PASS`, every link from Newton's second law to the
pendulum period held together — dimensionally and numerically.

## Where to go next

- The full [`physics-newtonian`](../SKILL.md) capsule: work/energy and its
  conservation, momentum and impulse, gravitation — all with regimes and checks.
- Concepts past this path in the capsule's `tsort` order:
  `conservation_of_mechanical_energy`, `conservation_of_momentum`,
  `newton_gravitation`, `gravitational_pe_general`.
- The damped and driven oscillator, and the physical (extended) pendulum, are
  out of scope for Release 0.1 — see `scope.md`.
