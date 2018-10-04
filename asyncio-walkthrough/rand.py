#!/usr/bin/env python3
# rand.py

import asyncio
import random

# colors
c = {
    1:     '\033[36m',  # cyan
    2:     '\033[91m',  # red
    3:     '\033[35m',  # magenta
    'end': '\033[0m'    # end of color
}

async def randint(a, b):
    return random.randint(a, b)

async def makerandom(idx, threshold=6, seed=444):
    random.seed(seed)
    print(c[idx] + f'Initiated makerandom({idx}).')
    i = await randint(0, 10)
    while i <= threshold:
        print(c[idx] + f'makerandom({idx}) == {i} too low; retrying.')
        await asyncio.sleep(idx)
        i = await randint(0, 10)
    print(c[idx] + f'---> Finished: makerandom({idx}) == {i}' + c['end'])
    return i

async def main():
    res = await asyncio.gather(*(makerandom(i, 10-i) for i in range(1, 4)))
    return res

if __name__ == '__main__':
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f'r1: {r1}, r2: {r2}, r3: {r3}')
