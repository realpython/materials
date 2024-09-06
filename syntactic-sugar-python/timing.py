import time


def timer(func):
    def _timer(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")
        return result

    return _timer


@timer
def delayed_mean(sample):
    time.sleep(1)
    return sum(sample) / len(sample)


delayed_mean([10, 2, 4, 7, 9, 3, 9, 8, 6, 7])
