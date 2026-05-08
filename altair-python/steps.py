import altair as alt
import pandas as pd

steps = pd.DataFrame(
    {
        "Day": ["1-Mon", "2-Tue", "3-Wed", "4-Thu", "5-Fri", "6-Sat", "7-Sun"],
        "Steps": [6200, 8400, 7100, 9800, 5500, 9870, 3769],
    }
)

weekly_steps = (
    alt.Chart(steps)
    .mark_bar()
    .encode(
        x="Day",
        y="Steps",
    )
)
weekly_steps
