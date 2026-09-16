"""Rounding for the billing module."""


def round_half_away(numerator, denominator):
    """Round numerator/denominator to the nearest whole number.

    Ties round AWAY FROM ZERO: 5/2 -> 3, and -5/2 -> -3.

    Both arguments are integers, so the arithmetic here is exact; denominator
    must be positive.
    """
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    negative = numerator < 0
    n = -numerator if negative else numerator
    whole, rest = divmod(n, denominator)
    if 2 * rest >= denominator:
        whole += 1
    return -whole if negative else whole
