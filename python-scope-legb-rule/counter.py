counter = 0  # A global name


def update_counter_v1():
    global counter  # Declares counter as global
    counter = counter + 1  # Successfully updates the counter


def update_counter_v2(counter):
    return counter + 1  # Relies on a local name
