import json
from collections import Counter

words = "the cat and the hat and the bat".split()
counts = Counter(words)

print(counts.most_common(2))
print(json.dumps(counts.most_common(1)))
