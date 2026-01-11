from collections import deque

page_history = deque(maxlen=3)

urls = ("https://google.com", "https://yahoo.com", "https://www.bing.com")

for url in urls:
    page_history.appendleft(url)

print(page_history)

page_history.appendleft("https://youtube.com")

print(page_history)

page_history.appendleft("https://facebook.com")

print(page_history)
