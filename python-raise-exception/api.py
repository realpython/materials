import requests


class APIError(Exception):
    pass


def call_external_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as error:
        raise APIError(f"{error}") from None
    return data


print(call_external_api("https://api.github.com/events"))
