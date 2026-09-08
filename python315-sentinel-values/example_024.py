STOP = sentinel("STOP")


def producer():
    words = ["ready", "done", "pending"]
    for word in words:
        yield word
    yield STOP


words_stream = producer()
for word in words_stream:
    if word == STOP:
        break
    print(f"Processing '{word}'...")
