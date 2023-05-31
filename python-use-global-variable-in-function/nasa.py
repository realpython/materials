import webbrowser

import requests

API_KEY = "DEMO_KEY"
BASE_URL = "https://api.nasa.gov/planetary"
TIMEOUT = 3


def load_earth_image(date):
    endpoint = f"{BASE_URL}/apod"
    try:
        response = requests.get(
            endpoint,
            params={
                "api_key": API_KEY,
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
