import time

# class time_execution:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args, **kwargs):
#         start = time.time()
#         result = self.func(*args, **kwargs)
#         end = time.time()
#         print(f"{self.func.__name__}() takes {(end - start) * 1000:.4f} ms")
#         return result


class time_execution:
    def __init__(self, repetitions=1):
        self.repetitions = repetitions

    def __call__(self, func):
        def _timer(*args, **kwargs):
            result = func(*args, **kwargs)
            total_time = 0
            print(f"Running {func.__name__}() {self.repetitions} times")
            for _ in range(self.repetitions):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                total_time += end - start
            average_time = total_time / self.repetitions
            print(
                f"{func.__name__}() takes "
                f"{average_time * 1000:.4f} ms on average"
            )
            return result

        return _timer
