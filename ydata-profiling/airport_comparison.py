import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("flight_data_2024_sample.csv")

# Split into flights originating from LAX and ATL
df_lax = df[df["origin"] == "LAX"]
df_atl = df[df["origin"] == "ATL"]

lax_profile = ProfileReport(df_lax, title="LAX Flights")
atl_profile = ProfileReport(df_atl, title="ATL Flights")

comparison = lax_profile.compare(atl_profile)
comparison.to_file("airport_comparison.html")
