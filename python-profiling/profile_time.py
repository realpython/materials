import time


def sleeper():
    time.sleep(1.75)


def spinlock():
    for _ in range(100_000_000):
        pass


for function in sleeper, spinlock:
    t1 = time.perf_counter(), time.process_time()
    function()
    t2 = time.perf_counter(), time.process_time()
    print(f"{function.__name__}()")
    print(f" Real time: {t2[0] - t1[0]:.2f} seconds")
    print(f" CPU time: {t2[1] - t1[1]:.2f} seconds")
    print()
