import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("flight_data_2024_sample.csv")
df["fl_date"] = pd.to_datetime(df["fl_date"])

profile = ProfileReport(
    df,
    title="Flight Delay Report",
    tsmode=True,
    sortby="fl_date",
)
profile.to_file("flight_timeseries_report.html")
