from concurrent.futures import ThreadPoolExecutor


def find_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


def slow_function():
    print("Slow thread started")
    try:
        return find_divisors(100_000_000)
    finally:
        print("Slow thread ended")


def fast_function():
    print("Fast thread started")
    try:
        return find_divisors(50_000_000)
    finally:
        print("Fast thread ended")


def main():
    with ThreadPoolExecutor(max_workers=2) as pool:
        pool.submit(slow_function)
        pool.submit(fast_function)

    print("Main thread ended")


if __name__ == "__main__":
    main()
