import asyncio

import aiohttp


async def download_file(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if "content-disposition" in response.headers:
                header = response.headers["content-disposition"]
                filename = header.split("filename=")[1]
            else:
                filename = url.split("/")[-1]
            with open(filename, mode="wb") as file:
                while True:
                    chunk = await response.content.read()
                    if not chunk:
                        break
                    file.write(chunk)
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


async def main():
    tasks = [download_file(url) for url in urls]
    await asyncio.gather(*tasks)


asyncio.run(main())
