# %%
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

PROJECT_ROOT = Path.cwd()
DATA_PATH = PROJECT_ROOT / "data" / "bike_share_trips.csv"

trips = pd.read_csv(DATA_PATH, parse_dates=["started_at", "ended_at"])

# %%
trips_by_hour = (
    trips.assign(hour=trips["started_at"].dt.hour)
    .groupby("hour", as_index=False)
    .size()
    .rename(columns={"size": "trip_count"})
)

ax = trips_by_hour.plot(
    x="hour",
    y="trip_count",
    kind="line",
    marker="o",
    legend=False,
    title="Bike Share Trips by Hour",
)
ax.set(xlabel="Hour of Day", ylabel="Trip Count")
ax.set_xticks(range(24))
plt.tight_layout()
plt.show()