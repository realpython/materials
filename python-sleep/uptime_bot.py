import time
import urllib.error
import urllib.request

CHECK_INTERVAL = 60  # Seconds between checks


def uptime_bot(url):
    while True:
        try:
            urllib.request.urlopen(url)
        except urllib.error.HTTPError as e:
            # Email admin or log
            print(f"HTTPError: {e.code} for {url}")
        except urllib.error.URLError as e:
            # Email admin or log
            print(f"URLError: {e.reason} for {url}")
        else:
            # Website is up
            print(f"{url} is up")
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    url = "https://www.google.com/py"
    uptime_bot(url)
