import logging

import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import RetryError
from urllib3.util import Retry

logging.basicConfig(level=logging.DEBUG)

retry_strategy = Retry(total=3, status_forcelist=[404])
github_adapter = HTTPAdapter(max_retries=retry_strategy)

with requests.Session() as session:
    session.mount("https://api.github.com", github_adapter)
    try:
        response = session.get("https://api.github.com/")
        print(response.status_code)
        response = session.get("https://api.github.com/invalid")
        print(response.status_code)
    except RetryError as err:
        print(f"Error: {err}")
