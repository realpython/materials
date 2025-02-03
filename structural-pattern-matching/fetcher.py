from http.client import HTTPConnection, HTTPResponse, HTTPSConnection
from sys import stderr
from urllib.parse import ParseResult, urlparse


def fetch(url):
    print(f"Fetching URL: {url}", file=stderr)
    connection = make_connection(url)
    try:
        connection.request("GET", "/")
        match connection.getresponse():
            case HTTPResponse(status=code) if code >= 400:
                raise ValueError("Failed to fetch URL")
            case HTTPResponse(status=code) as resp if (
                code >= 300 and (redirect := resp.getheader("Location"))
            ):
                return fetch(redirect)
            case HTTPResponse(status=code) as resp if code >= 200:
                return resp.read()
            case _:
                raise ValueError("Unexpected response")
    finally:
        connection.close()


def make_connection(url):
    match urlparse(url):
        case ParseResult("http", netloc=host):
            return HTTPConnection(host)
        case ParseResult("https", netloc=host):
            return HTTPSConnection(host)
        case _:
            raise ValueError("Unsupported URL scheme")


if __name__ == "__main__":
    fetch("http://realpython.com/")
