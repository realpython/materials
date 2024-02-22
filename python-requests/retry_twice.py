import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import RetryError

github_adapter = HTTPAdapter(max_retries=2)

session = requests.Session()

session.mount("https://api.github.com", github_adapter)

try:
    response = session.get("https://api.github.com/")
except RetryError as err:
    print(f"Error: {err}")
finally:
    session.close()