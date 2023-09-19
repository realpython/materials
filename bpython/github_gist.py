#!/usr/bin/env python

import json
import os
import sys
from urllib.request import Request, urlopen


def main() -> None:
    """Print the URL of a GitHub gist created from the standard input."""
    print(create_gist(sys.stdin.read()))


def create_gist(content: str) -> str:
    """Return the URL of the created GitHub gist."""
    response = post_json(
        url="https://api.github.com/gists",
        data={
            "description": "bpython REPL",
            "public": False,
            "files": {"repl.py": {"content": content}},
        },
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
            "Content-Type": "application/json",
        },
    )
    return response["html_url"]


def post_json(url: str, data: dict, headers: dict = None) -> dict:
    """Return the JSON response from the server."""
    payload = json.dumps(data).encode("utf-8")
    with urlopen(Request(url, payload, headers or {})) as response:
        return json.loads(response.read().decode("utf-8"))


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(ex)
