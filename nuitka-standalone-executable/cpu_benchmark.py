import time


def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


def main():
    start = time.perf_counter()

    count = 0
    for number in range(2, 100_000):
        if is_prime(number):
            count += 1

    elapsed = time.perf_counter() - start

    print(f"Primes found: {count}")
    print(f"Time: {elapsed:.3f}s")


if __name__ == "__main__":
    main()
