from numpy.random import Generator, PCG64DXSM

rng1 = Generator(PCG64DXSM())
print(rng1.random())

rng2 = Generator(PCG64DXSM(100))
print(rng2.random())
print(rng2.random())

rng3 = Generator(PCG64DXSM(100))
print(rng3.random())
print(rng3.random())
