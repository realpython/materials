import requests
from requests.auth import AuthBase


class TokenAuth(AuthBase):
    """Implements a token authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to the Authorization header."""
        r.headers["Authorization"] = f"Bearer {self.token}"
        return r


if __name__ == "__main__":
    token = "<YOUR_GITHUB_PA_TOKEN>"
    response = requests.get(
        "https://api.github.com/user", auth=TokenAuth(token)
    )
    print(response.status_code)
    print(response.text)
