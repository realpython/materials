from collections import deque


def slice_deque(deck, *, start, stop):
    slice = deque()
    temp = deque()
    for i in range(stop, start, -1):
        deck.rotate(i)
        item = deck.popleft()
        slice.appendleft(item)
        temp.append(item)
    deck.extend(temp)
    # for i in range(start, stop):
    #     deck.rotate(-i)

    return slice


d = deque([1, 2, 3, 4, 5])
print(slice_deque(d, start=0, stop=3))
print(d)
