import math


def truncate(n, decimals=0):
    multiplier = 10**decimals
    return int(n * multiplier) / multiplier


def round_up(n, decimals=0):
    multiplier = 10**decimals
    return math.ceil(n * multiplier) / multiplier


def round_down(n, decimals=0):
    multiplier = 10**decimals
    return math.floor(n * multiplier) / multiplier


def round_half_up(n, decimals=0):
    multiplier = 10**decimals
    return math.floor(n * multiplier + 0.5) / multiplier


def round_half_down(n, decimals=0):
    multiplier = 10**decimals
    return math.ceil(n * multiplier - 0.5) / multiplier


def round_half_away_from_zero(n, decimals=0):
    rounded_abs = round_half_up(abs(n), decimals)
    return math.copysign(rounded_abs, n)


def round_half_to_even(n, decimals=0):
    return round(n, ndigits=decimals)
