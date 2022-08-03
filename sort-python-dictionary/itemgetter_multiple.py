from operator import itemgetter

scores = {
    "Jack": 14,
    "Jill": 14,
    "John": 15,
    "Jane": 15,
    "Jim": 14,
    "Jess": 14,
}

print(sorted(scores.items(), key=itemgetter(1, 0)))
