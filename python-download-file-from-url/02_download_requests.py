import requests

url = "https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD"
query_parameters = {"downloadformat": "csv"}

response = requests.get(url, query_parameters)

print(f"{response.url = }")
print(f"{response.ok = }")
print(f"{response.status_code = }")

filename = "gdp_by_country.zip"
with open(filename, mode="wb") as file:
    file.write(response.content)

print(f"Downloaded file {filename}")
