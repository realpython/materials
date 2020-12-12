import requests

# The datetime package is useful to manipulate dates.
from datetime import date, timedelta

# To fetch the latest total confirmed cases number you need to pass a 24h
# window to the API. That's why you need to pass both yesterday's date
# and today's.
today = date.today()
yesterday = today - timedelta(days=1)

# Pick a country slug from the list: https://api.covid19api.com/countries
country = "germany"

endpoint = f"https://api.covid19api.com/country/{country}/status/confirmed"
params = {"from": str(yesterday), "to": str(today)}

# The response will be a list of results per day, in your case only 1 result.
response = requests.get(endpoint, params=params).json()

# Finally, you need to traverse through the response and increment the
# `total_confirmed` variable with the total number of confirmed cases
# available that day, which is in the field `Cases`.
total_confirmed = 0
for day in response:
    cases = day.get("Cases", 0)
    total_confirmed += cases

print(f"Total Confirmed Covid-19 cases in {country}: {total_confirmed}")
