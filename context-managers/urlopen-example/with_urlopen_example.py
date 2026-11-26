
"""
Using the 'with' statement to open a URL

This example demonstrates how Python's 'with' statement can be used
to manage resources like HTTP connections when working with URLS
"""

from urllib.request import urlopen

url = "https://www.python.org"

# 'with' ensures that the connection automatically closes
with urlopen(url) as response:
    html = response.read()
    print(html[:200]) # prints first 200 bytes