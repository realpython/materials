"""Download and decode textures concurrently with asyncio."""

import asyncio

CATALOG = {
    "bakery-dawn": 0.35,
    "bakery-noon": 0.15,
    "bakery-dusk": 0.25,
}


async def download_texture(name: str, latency: float) -> bytes:
    await asyncio.sleep(latency)
    return name.encode() * 100_000


async def decode_texture(payload: bytes) -> int:
    checksum = 0
    for byte in payload:
        checksum = (checksum * 31 + byte) % 1_000_003
    return checksum


async def main() -> None:
    async with asyncio.TaskGroup() as group:
        downloads = {
            name: group.create_task(
                download_texture(name, latency), name=f"download-{name}"
            )
            for name, latency in CATALOG.items()
        }
    for name, download in downloads.items():
        checksum = await decode_texture(download.result())
        print(f"{name}: {checksum}")


if __name__ == "__main__":
    asyncio.run(main())
