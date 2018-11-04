#!/usr/bin/env python3
# areq.py

"""Asynchronously get links embedded in multiple pages' HMTL."""

import asyncio
import logging
import re
import sys
from typing import BinaryIO, Union
import urllib.error
import urllib.parse

import aiofiles
import aiohttp
from aiohttp import ClientSession, ClientTimeout
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

# You can specify timeouts for both the session as a whole and
# for individual requests.
#
# https://aiohttp.readthedocs.io/en/stable/client_quickstart.html#timeouts
DEFAULT_GET_TIMEOUT = ClientTimeout(total=8)  # seconds


async def fetch_html(
    url: str, session: ClientSession, timeout: ClientTimeout, **kwargs
) -> str:
    """GET request wrapper to fetch page HTML.

    kwargs are passed to `session.request()`.
    """

    # Don't do any try/except here.  If either the request or reading
    # of bytes raises, let that be handled by caller.
    resp = await session.request(
        method="GET", url=url, timeout=timeout, **kwargs
    )
    resp.raise_for_status()  # raise if status >= 400
    logger.info("Got response [%s] for URL: %s", resp.status, url)
    html = await resp.text()  # For bytes: resp.read()

    # Dont close session; let caller decide when to do that.
    return html


async def parse(
    url: str,
    session: ClientSession,
    timeout: ClientTimeout = DEFAULT_GET_TIMEOUT,
    **kwargs
) -> set:
    """Find HREFs in the HTML of `url`."""
    found = set()
    try:
        html = await fetch_html(
            url=url, session=session, timeout=timeout, **kwargs
        )
    except (
        aiohttp.ClientError,
        aiohttp.http_exceptions.HttpProcessingError,
    ) as e:
        logger.error(
            "aiohttp exception for %s [%s]: %s",
            url,
            getattr(e, "status", None),
            getattr(e, "message", None),
        )
        return found
    except Exception as e:
        # May be raised from other libraries, such as chardet or yarl.
        # logger.exception will show the full traceback.
        logger.exception(
            "Non-aiohttp exception occured:  %s", getattr(e, "__dict__", {})
        )
        return found
    else:
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
                found.add(abslink)
        logger.info("Found %d links for %s", len(found), url)
        return found


async def write_one(file: BinaryIO, url: str, **kwargs) -> None:
    """Write the found HREFs from `url` to `file`."""
    res = await parse(url=url, **kwargs)
    if not res:
        return None
    async with aiofiles.open(file, "a") as f:
        for p in res:
            await f.write(f"{url}\t{p}\n")
        logger.info("Wrote results for source URL: %s", url)


async def bulk_crawl_and_write(
    file: BinaryIO,
    urls: set,
    timeout: Union[object, ClientTimeout] = sentinel,
    **kwargs,
) -> None:
    """Crawl & write concurrently to `file` for multiple `urls`."""
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(
                write_one(file=file, url=url, session=session, **kwargs)
            )
        await asyncio.gather(*tasks)  # see also: return_exceptions=True


if __name__ == "__main__":
    import pathlib
    import sys

    assert sys.version_info >= (3, 7), "Script requires Python 3.7+."
    here = pathlib.Path(__file__).parent

    with open(here.joinpath("urls.txt")) as infile:
        urls = set(map(str.strip, infile))

    # Header - just a single, initial row-write
    outpath = here.joinpath("foundurls.txt")
    with open(outpath, "w") as outfile:
        outfile.write("source_url\tparsed_url\n")

    asyncio.run(bulk_crawl_and_write(file=outpath, urls=urls))
