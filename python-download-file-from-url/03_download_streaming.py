import requests

filename = "WDI_CSV.zip"
url = f"https://databank.worldbank.org/data/download/{filename}"

print("Downloading...")

response = requests.get(url, stream=True)
with open(filename, mode="wb") as file:
    for chunk in response.iter_content(chunk_size=10 * 1024):
        file.write(chunk)
    print(f"Downloaded file {filename}")
