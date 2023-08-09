import numpy as np


def truncate(n, decimals=0):
    multiplier = 10**decimals
    return np.trunc(n * multiplier) / multiplier


def round_up(n, decimals=0):
    multiplier = 10**decimals
    return np.ceil(n * multiplier) / multiplier


def round_down(n, decimals=0):
    multiplier = 10**decimals
    return np.floor(n * multiplier) / multiplier


def round_half_up(n, decimals=0):
    multiplier = 10**decimals
    return np.floor(n * multiplier + 0.5) / multiplier


def round_half_down(n, decimals=0):
    multiplier = 10**decimals
    return np.ceil(n * multiplier - 0.5) / multiplier


def round_half_away_from_zero(n, decimals=0):
    rounded_abs = round_half_up(np.abs(n), decimals)
    return np.copysign(rounded_abs, n)


def round_half_to_even(n, decimals=0):
    return np.round(n, decimals=decimals)
