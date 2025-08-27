import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import RetryError
from urllib3.util.retry import Retry

retry_strategy = Retry(total=2, status_forcelist=[429, 500, 502, 503, 504])
github_adapter = HTTPAdapter(max_retries=retry_strategy)

with requests.Session() as session:
    session.mount("https://api.github.com", github_adapter)
    try:
        response = session.get("https://api.github.com/")
    except RetryError as err:
        print(f"Error: {err}")
