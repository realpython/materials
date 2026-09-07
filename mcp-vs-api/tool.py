import json
import urllib.request


def get_package_info(package_name: str) -> dict:
    """
    Look up a package on PyPI
    and return its latest version and summary.
    """
    url = f"https://pypi.org/pypi/{package_name}/json"
    with urllib.request.urlopen(url) as response:
        data = json.load(response)
    info = data["info"]
    return {
        "name": info["name"],
        "version": info["version"],
        "summary": info["summary"],
    }
