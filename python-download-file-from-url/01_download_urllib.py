from urllib.request import urlretrieve

url = (
    "https://api.worldbank.org/v2/en/indicator/"
    "NY.GDP.MKTP.CD?downloadformat=csv"
)
filename = "gdp_by_country.zip"

path, headers = urlretrieve(url, filename)
for name, value in headers.items():
    print(name, value)

print(f"Downloaded file {path}")
