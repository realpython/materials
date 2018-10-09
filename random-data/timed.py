import random
import timeit

_sysrand = random.SystemRandom()


def prng() -> None:
    random.randint(0, 95)


def csprng() -> None:
    _sysrand.randint(0, 95)


setup = "import random; from __main__ import prng, csprng"

if __name__ == "__main__":
    print("Best of 3 trials with 1,000,000 loops per trial:")

    for f in ("prng()", "csprng()"):
        best = min(timeit.repeat(f, setup=setup))
        print("\t{:8s} {:0.2f} seconds total time.".format(f, best))
