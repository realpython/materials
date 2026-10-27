from collections import Counter

stats = Counter()


def record_event(**labels):
    stats[frozendict(labels)] += 1


record_event(endpoint="/login", outcome="failure", reason="bad_password")
record_event(reason="bad_password", endpoint="/login", outcome="failure")
record_event(endpoint="/login", outcome="success")
record_event(outcome="success", endpoint="/checkout")

num_failures = sum(
    count
    for labels, count in stats.items()
    if labels.get("outcome") == "failure"
)

print("Number of failed outcomes:", num_failures)
