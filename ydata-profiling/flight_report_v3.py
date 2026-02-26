import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("flight_data_2024_sample.csv")

# Option 1: Generate a minimal report
profile = ProfileReport(df, minimal=True)
profile.to_file("minimal_report.html")

# Option 2: Sample your data before profiling
df_sample = df.sample(n=10000, random_state=42)
profile = ProfileReport(df_sample)
profile.to_file("sampled_report.html")
