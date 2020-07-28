from datetime import date, timedelta
import requests

today = date.today()
yesterday = today - timedelta(days=1)
country = "germany"
endpoint = "https://api.covid19api.com/country/%s/status/confirmed" % country
params = {"from": str(yesterday), "to": str(today)}

response = requests.get(endpoint, params=params).json()
total_confirmed = 0
for region in response:
    cases = region.get("Cases", 0)
    total_confirmed += cases

print("Total Confirmed COVID cases in %s: %s" % (country, total_confirmed))
