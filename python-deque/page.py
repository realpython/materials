from collections import deque

doc_history = deque(maxlen=3)

urls = ("https://google.com", "https://yahoo.com", "https://www.bing.com")

for url in urls:
    doc_history.appendleft(url)

print(doc_history)

doc_history.appendleft("https://youtube.com")

print(doc_history)

doc_history.appendleft("https://facebook.com")

print(doc_history)
