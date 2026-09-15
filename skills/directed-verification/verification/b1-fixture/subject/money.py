"""Money rounding for the billing module."""


def round_half_up(amount_cents, rate):
    """Apply `rate` to `amount_cents` and round the result half-up.

    Half-up means a result of exactly .5 rounds AWAY from zero: 2.5 -> 3.
    This is what the billing spec requires and is not what Python's built-in
    round() does.
    """
    scaled = amount_cents * rate
    floor = int(scaled)
    remainder = scaled - floor
    if remainder > 0.5:
        return floor + 1
    if remainder < 0.5:
        return floor
    return floor + 1          # exactly .5 rounds up
