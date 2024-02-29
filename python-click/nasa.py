import webbrowser

import click
import requests

BASE_URL = "https://api.nasa.gov/planetary"
TIMEOUT = 3


@click.command()
@click.option("--date", default="2021-10-01")
@click.option("--api-key", envvar="NASA_API_KEY")
def cli(date, api_key):
    endpoint = f"{BASE_URL}/apod"
    try:
        response = requests.get(
            endpoint,
            params={
                "api_key": api_key,
                "date": date,
            },
            timeout=TIMEOUT,
        )
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to API: {e}")
        return

    try:
        url = response.json()["url"]
    except KeyError:
        print(f"No image available on {date}")
        return

    webbrowser.open(url)


if __name__ == "__main__":
    cli()
