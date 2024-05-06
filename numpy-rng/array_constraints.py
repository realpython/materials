from numpy.random import PCG64DXSM, Generator

rng = Generator(PCG64DXSM())

print(rng.integers(size=(2, 2), low=1, high=5))
print(rng.uniform(size=(2, 2), low=1, high=5))
