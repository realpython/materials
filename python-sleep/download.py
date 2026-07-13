import urllib.error
import urllib.request

from utils import retry


@retry(delay=3)
def download_file(url):
    try:
        response = urllib.request.urlopen(url)
        print(f"Downloaded {url} ({response.length} bytes)")
    except urllib.error.URLError as e:
        print(f"Download failed: {e.reason}")
        raise


if __name__ == "__main__":
    download_file("http://www.example.com/data.csv")
