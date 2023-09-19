import time

# class ExecutionTimer:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args, **kwargs):
#         start = time.perf_counter()
#         result = self.func(*args, **kwargs)
#         end = time.perf_counter()
#         print(f"{self.func.__name__}() took {(end - start) * 1000:.4f} ms")
#         return result


class ExecutionTimer:
    def __init__(self, repetitions=1):
        self.repetitions = repetitions

    def __call__(self, func):
        def timer(*args, **kwargs):
            result = None
            total_time = 0
            print(f"Running {func.__name__}() {self.repetitions} times")
            for _ in range(self.repetitions):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                end = time.perf_counter()
                total_time += end - start
            average_time = total_time / self.repetitions
            print(
                f"{func.__name__}() takes "
                f"{average_time * 1000:.4f} ms on average"
            )
            return result

        return timer
