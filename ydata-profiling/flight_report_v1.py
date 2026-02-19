import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("flight_data_2024_sample.csv")

profile = ProfileReport(df)
profile.to_file("flight_report.html")
