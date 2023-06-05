from numpy.random import PCG64DXSM, Generator

pcg64dxsm_rng = Generator(PCG64DXSM())
print(pcg64dxsm_rng.random())

rng1 = Generator(PCG64DXSM(seed=100))
print(rng1.random())
print(rng1.random())

rng2 = Generator(PCG64DXSM(seed=100))
print(rng2.random())
print(rng2.random())
