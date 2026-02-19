import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("flight_data_2024_sample.csv")

profile = ProfileReport(
    df,
    variables={
        "descriptions": {
            "origin": "Airport code where the flight originated",
            "dest": "Airport code of flight destination",
            "crs_dep_time": "Scheduled departure time at origin (hhmm)",
        }
    },
)
profile.to_file("documented_report.html")
