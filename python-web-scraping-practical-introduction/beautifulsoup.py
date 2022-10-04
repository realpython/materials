from urllib.request import urlopen

from bs4 import BeautifulSoup

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
image1, image2 = soup.find_all("img")

print(image1.name)
print(image2.name)
print(soup.title.string)
