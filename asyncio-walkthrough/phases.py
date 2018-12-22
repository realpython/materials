#!/usr/env/bin python3
# phases.py

import asyncio


async def phase1(callerid: str):
    print(f"phase 1 called from {callerid}")
    await asyncio.sleep(2)
    return "result1"


async def phase2(callerid: str, arg: str):
    print(f"phase 2 called from {callerid}")
    await asyncio.sleep(2)
    # No await needed here - arg is passed from caller.
    return f"result2 derived from {arg}"


async def outer(callerid: str):
    """A wrapper for parameterizing a full coroutine."""
    print(f"outer called from {callerid}")
    r1 = await phase1(callerid)
    r2 = await phase2(callerid, r1)
    return r1, r2


async def main():
    """Wrap the coroutines into tasks and execute."""
    results = await asyncio.gather(*(outer(i) for i in "ABC"))
    return results


if __name__ == "__main__":
    asyncio.run(main())
