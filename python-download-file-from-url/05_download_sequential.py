import requests


def download_file(url):
    response = requests.get(url)
    if "content-disposition" in response.headers:
        content_disposition = response.headers["content-disposition"]
        filename = content_disposition.split("filename=")[1]
    else:
        filename = url.split("/")[-1]
    with open(filename, mode="wb") as file:
        file.write(response.content)
    print(f"Downloaded file {filename}")


template_url = (
    "https://api.worldbank.org/v2/en/indicator/"
    "{resource}?downloadformat=csv"
)

urls = [
    # Total population by country
    template_url.format(resource="SP.POP.TOTL"),
    # GDP by country
    template_url.format(resource="NY.GDP.MKTP.CD"),
    # Population density by country
    template_url.format(resource="EN.POP.DNST"),
]

for url in urls:
    download_file(url)
