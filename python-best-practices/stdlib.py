# Avoid this:
# words = ["python", "pep8", "python", "testing"]
# counts = {}
# for word in words:
#     if word in counts:
#         counts[word] += 1
#     else:
#         counts[word] = 1


# Favor this:
from collections import Counter

words = ["python", "pep8", "python", "testing"]
counts = Counter(words)
print(counts)
