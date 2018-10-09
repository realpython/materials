"""Companion code to https://realpython.com/fast-flexible-pandas.

'Fast, Flexible, Easy and Intuitive: How to Speed Up Your Pandas Projects'

Note: most of the functions here modify a Pandas DataFrame in-place,
which is generally not great practice but used with caution here.
"""

import numpy as np
import pandas as pd

from .timer import timeit


# Two functions for conversion of object dtype to datetime
# Note that you could also specify `parse_dates` within `pd.read_csv()`
@timeit(repeat=3, number=10)
def convert(df, column_name):
    return pd.to_datetime(df[column_name])


@timeit(repeat=3, number=100)
def convert_with_format(df, column_name):
    return pd.to_datetime(df[column_name], format="%d/%m/%y %H:%M")


def apply_tariff(kwh, hour):
    """Calculates cost of electricity for given hour."""
    if 0 <= hour < 7:
        rate = 12
    elif 7 <= hour < 17:
        rate = 20
    elif 17 <= hour < 24:
        rate = 28
    else:
        raise ValueError(f"Invalid hour: {hour}")
    return rate * kwh


# NOTE: Don't do this!
@timeit(repeat=2, number=10)
def apply_tariff_loop(df):
    """Calculate costs in loop.  Modifies `df` inplace."""
    energy_cost_list = []
    for i in range(len(df)):
        # Get electricity used and hour of day
        energy_used = df.iloc[i]["energy_kwh"]
        # This is an example of chained indexing, which can create
        # hard-to-track bugs
        hour = df.iloc[i]["date_time"].hour
        energy_cost = apply_tariff(energy_used, hour)
        energy_cost_list.append(energy_cost)
    df["cost_cents"] = energy_cost_list


@timeit(repeat=3, number=50)
def apply_tariff_iterrows(df):
    energy_cost_list = []
    for index, row in df.iterrows():
        # Get electricity used and hour of day
        energy_used = row["energy_kwh"]
        hour = row["date_time"].hour
        # Append cost list
        energy_cost = apply_tariff(energy_used, hour)
        energy_cost_list.append(energy_cost)
    df["cost_cents"] = energy_cost_list


@timeit(repeat=3, number=100)
def apply_tariff_withapply(df):
    df["cost_cents"] = df.apply(
        lambda row: apply_tariff(
            kwh=row["energy_kwh"], hour=row["date_time"].hour
        ),
        axis=1,
    )


@timeit(repeat=3, number=1000)
def apply_tariff_isin(df):
    # Define hour range Boolean arrays
    peak_hours = df.index.hour.isin(range(17, 24))
    shoulder_hours = df.index.hour.isin(range(7, 17))
    off_peak_hours = df.index.hour.isin(range(0, 7))

    # Apply tariffs to hour ranges
    df.loc[peak_hours, "cost_cents"] = df.loc[peak_hours, "energy_kwh"] * 28
    df.loc[shoulder_hours, "cost_cents"] = (
        df.loc[shoulder_hours, "energy_kwh"] * 20
    )  # noqa
    df.loc[off_peak_hours, "cost_cents"] = (
        df.loc[off_peak_hours, "energy_kwh"] * 12
    )  # noqa


@timeit(repeat=3, number=1000)
def apply_tariff_cut(df):
    cents_per_kwh = pd.cut(
        x=df.index.hour,
        bins=[0, 7, 17, 24],
        include_lowest=True,
        labels=[12, 20, 28],
    ).astype(int)
    df["cost_cents"] = cents_per_kwh * df["energy_kwh"]


@timeit(repeat=3, number=1000)
def apply_tariff_digitize(df):
    prices = np.array([12, 20, 28])
    bins = np.digitize(df.index.hour.values, bins=[7, 17, 24])
    df["cost_cents"] = prices[bins] * df["energy_kwh"].values


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(here, "demand_profile.csv")
    df = pd.read_csv(file)

    convert(df, "date_time")
    df["date_time"] = convert_with_format(df, "date_time")

    apply_tariff_loop(df)
    apply_tariff_iterrows(df)
    apply_tariff_withapply(df)

    df.set_index("date_time", inplace=True)

    apply_tariff_isin(df)
    apply_tariff_cut(df)
    apply_tariff_digitize(df)


if __name__ == "__main__":
    # To run as a script, you will need to be cd'd outside of this
    # package and use the -m flag.  In other words, unless you append
    # to sys.path, make sure your current working directory is
    # outside of this package, then run:
    # $ python3 -m tutorial

    import os.path
    import platform
    import sys

    pd.set_option("mode.chained_assignment", None)
    pd.set_option("compute.use_bottleneck", True)
    pd.set_option("compute.use_numexpr", True)

    print(__doc__)
    print("Python version:", platform.python_version())
    print("Pandas version:", pd.__version__, end="\n\n")
    print("Timing code ...", end="\n\n")

    sys.exit(main())
