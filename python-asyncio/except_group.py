import asyncio


async def main():
    results = await asyncio.gather(
        coro_a(), coro_b(), coro_c(), return_exceptions=True
    )
    exceptions = [e for e in results if isinstance(e, Exception)]
    if exceptions:
        raise ExceptionGroup("Errors", exceptions)


async def coro_a():
    await asyncio.sleep(1)
    raise ValueError("Error in coro A")


async def coro_b():
    await asyncio.sleep(2)
    raise TypeError("Error in coro B")


async def coro_c():
    await asyncio.sleep(0.5)
    raise IndexError("Error in coro C")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except* ValueError as ve_group:
        print(f"[ValueError handled] {ve_group.exceptions}")
    except* TypeError as te_group:
        print(f"[TypeError handled] {te_group.exceptions}")
    except* IndexError as ie_group:
        print(f"[IndexError handled] {ie_group.exceptions}")
