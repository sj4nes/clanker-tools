"""Second-order mass-spring-damper plant + PID / state-feedback, stdlib only.

Continuous plant (normalised):

    xdot = [ 0            1        ] x + [ 0        ] u
           [ -wn^2   -2 zeta wn    ]     [ wn^2 * g ]
    y = x1

wn = 1.0, zeta = 0.2 (underdamped), g = actuator/plant gain (nominal 1.0).
Known closed forms are used by checks.bc and by the assertions in run.sh.
"""

WN = 1.0
ZETA = 0.2


def deriv(x, u, g):
    x1, x2 = x
    return (x2, -WN * WN * x1 - 2.0 * ZETA * WN * x2 + WN * WN * g * u)


def rk4_step(x, u, g, dt):
    k1 = deriv(x, u, g)
    k2 = deriv((x[0] + 0.5 * dt * k1[0], x[1] + 0.5 * dt * k1[1]), u, g)
    k3 = deriv((x[0] + 0.5 * dt * k2[0], x[1] + 0.5 * dt * k2[1]), u, g)
    k4 = deriv((x[0] + dt * k3[0], x[1] + dt * k3[1]), u, g)
    return (
        x[0] + dt / 6.0 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]),
        x[1] + dt / 6.0 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]),
    )


def controllability_2x2(g=1.0):
    """det[ B  A B ] ; nonzero => controllable (n = 2)."""
    b = (0.0, WN * WN * g)
    ab = (b[1], -2.0 * ZETA * WN * b[1])          # A @ b
    return b[0] * ab[1] - b[1] * ab[0]


def observability_2x2():
    """det[ C ; C A ] with C = [1 0] ; nonzero => observable."""
    c = (1.0, 0.0)
    ca = (0.0, 1.0)                                # C @ A = second row selector
    return c[0] * ca[1] - c[1] * ca[0]


def closed_loop_poles_state_fb(k1, k2, g=1.0):
    """Poles of A - B K, K = [k1 k2].  s^2 + a1 s + a0."""
    bg = WN * WN * g
    a1 = 2.0 * ZETA * WN + bg * k2
    a0 = WN * WN + bg * k1
    disc = a1 * a1 - 4.0 * a0
    if disc >= 0:
        r = disc ** 0.5
        return [(-a1 + r) / 2.0, (-a1 - r) / 2.0], [0.0, 0.0]
    r = (-disc) ** 0.5
    return [-a1 / 2.0, -a1 / 2.0], [r / 2.0, -r / 2.0]


def simulate_pid(setpoint=1.0, kp=4.0, ki=3.0, kd=1.5, ts=0.05, t_end=30.0,
                 g=1.0, u_min=None, u_max=None, anti_windup=True, x0=(0.0, 0.0)):
    """Discrete PID (derivative on measurement, back-calculation anti-windup)
    wrapped around the RK4-integrated continuous plant. Returns a time/output
    trace and summary metrics."""
    sub = 20
    dt = ts / sub
    x = tuple(x0)
    integ = 0.0
    y_prev = x[0]
    ts_series, ys = [], []
    n = int(round(t_end / ts))
    for k in range(n):
        y = x[0]
        e = setpoint - y
        d = -(y - y_prev) / ts
        u_unsat = kp * e + ki * integ + kd * d
        u = u_unsat
        if u_max is not None and u > u_max:
            u = u_max
        if u_min is not None and u < u_min:
            u = u_min
        # integrate error, with anti-windup back-calculation on saturation
        integ += e * ts
        if anti_windup and ki != 0.0 and u != u_unsat:
            integ += (u - u_unsat) / ki
        y_prev = y
        for _ in range(sub):
            x = rk4_step(x, u, g, dt)
        ts_series.append((k + 1) * ts)
        ys.append(x[0])
    return ts_series, ys, _metrics(ts_series, ys, setpoint)


def _metrics(t, y, sp):
    peak = max(y) if y else 0.0
    overshoot = max(0.0, (peak - sp) / sp * 100.0) if sp else 0.0
    final = y[-1] if y else 0.0
    sse = abs(sp - final)
    diverged = any(abs(v) > 1e3 for v in y) or (y and abs(y[-1]) > 10 * abs(sp) + 10)
    # settling time to +/-2%
    band = 0.02 * abs(sp)
    settle = t[-1] if t else 0.0
    for i in range(len(y) - 1, -1, -1):
        if abs(y[i] - sp) > band:
            settle = t[i] if i + 1 >= len(t) else t[i + 1]
            break
    else:
        settle = 0.0
    return {
        "overshoot_pct": overshoot,
        "steady_state_error": sse,
        "settling_time": settle,
        "final": final,
        "diverged": diverged,
    }
