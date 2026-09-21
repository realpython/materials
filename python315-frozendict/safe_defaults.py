"""Show the mutable default argument bug, then fix it with a frozendict.

The buggy version keeps one dict alive across every call, so an auth token
supplied to one host leaks into an unrelated request. The frozendict version
builds a fresh mapping each time.

Run with Python 3.15 or later:

    python safe_defaults.py
"""


def fetch_buggy(url, headers={}, token=None):
    headers.setdefault("User-Agent", "acme/1.0")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    print(f"GET {url}")
    print(f"    {headers}")


def fetch(url, headers=frozendict(), token=None):
    headers = frozendict({"User-Agent": "acme/1.0"}) | headers
    if token:
        headers |= {"Authorization": f"Bearer {token}"}
    print(f"GET {url}")
    print(f"    {headers}")


def main():
    print("With a mutable default argument:")
    fetch_buggy("https://acme.test/me", token="admin-key")
    fetch_buggy("https://partner.example/ping")

    print()
    print("With a frozendict default argument:")
    fetch("https://acme.test/me", token="admin-key")
    fetch("https://partner.example/ping")


if __name__ == "__main__":
    main()
