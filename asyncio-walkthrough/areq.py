#!/usr/bin/env python3
# areq.py

"""Asynchronously get links embedded in multiple pages' HMTL."""

import asyncio
import logging
import re
import urllib.error
import urllib.parse
import sys
from typing import List, Tuple

import aiofiles
import aiohttp
from aiohttp.helpers import sentinel

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.DEBUG,
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)
logger = logging.getLogger("areq")
logging.getLogger("chardet.charsetprober").disabled = True

HREF_RE = re.compile(r'href="(.*?)"')
DEFAULT_GET_TIMEOUT = aiohttp.ClientTimeout(total=10)  # seconds


class BadURLError(Exception):
    """Blanket exception for a bad page."""

    pass


async def get(
    url: str,
    session: aiohttp.ClientSession,
    timeout: aiohttp.ClientTimeout = DEFAULT_GET_TIMEOUT,
    **kwargs,
) -> aiohttp.ClientResponse:
    """GET request; return only valid responses.

    kwargs are passed to `session.request()`.
    """

    # We only want to return valid responses.  This means the request
    # itself was made successfully *and* status code is good.
    try:
        resp = await session.request(
            method="GET", url=url, timeout=timeout, **kwargs
        )
    except Exception as e:
        logger.exception("Problem getting response for URL: %s", url)
        raise BadURLError("Failed request") from e
    try:
        resp.raise_for_status()
    except Exception as e:
        logger.error("Bad status [%s] for URL: %s", resp.status, url)
        raise BadURLError("Bad status") from e
    else:
        logger.info("Got response [%s] for URL: %s", resp.status, url)
        # Dont close session; let caller decide when to do that.
        return resp


async def parse(
    url: str,
    session: aiohttp.ClientSession,
    timeout: aiohttp.ClientTimeout = DEFAULT_GET_TIMEOUT,
    **kwargs,
) -> Tuple[str, set]:
    # Pass through the URL so that the end caller knows which URLs map
    # to which.
    res = set()
    try:
        resp = await get(url=url, session=session, timeout=timeout, **kwargs)
    except BadURLError as e:
        return url, res
    try:
        # This effectively functions like a "try-except-else"
        html = await resp.text()
    except:  # noqa
        logger.exception("Problem getting text for URL: %s", url)
        return url, res
    else:
        if not html:
            return url, res

    # This portion is not really async, but it is the request/response
    # IO cycle that eats the largest portion of time.
    for link in HREF_RE.findall(html):
        try:
            # Ensure we return an absolute path.
            abslink = urllib.parse.urljoin(url, link)
        except (urllib.error.URLError, ValueError):
            logger.exception("Error parsing URL: %s", link)
            pass
        else:
            res.add(abslink)
    logger.info("Found %d links for %s", len(res), url)
    return url, res


async def write(file, url: str, **kwargs) -> None:
    _, res = await parse(url=url, **kwargs)
    async with aiofiles.open(file, "a") as f:
        for p in res:
            await f.write(f"{url}\t{p}\n")
        logger.info("Wrote results for source URL: %s", url)


async def bulk_get_and_write(
    file, urls: set, session_timeout=None, **kwargs
) -> List[Tuple[str, set]]:
    if session_timeout is not sentinel:
        # A conservative timeout estimate is 10 seconds per URL.
        session_timeout = aiohttp.ClientTimeout(total=10 * len(urls))
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        tasks = []
        for url in urls:
            tasks.append(write(file=file, url=url, session=session, **kwargs))
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    import pathlib

    here = pathlib.Path(__file__).parent

    urls = set()
    with open(here.joinpath("urls.txt")) as infile:
        for i in infile:
            urls.add(i.strip())

    # Header - just a single row-write
    outpath = here.joinpath("foundurls.txt")
    with open(outpath, "w") as outfile:
        outfile.write("source_url\tparsed_url\n")

    asyncio.run(bulk_get_and_write(file=outpath, urls=urls))
