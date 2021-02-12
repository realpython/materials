from browser import aio, document


def log(message):
    document["log"].value += f"{message} \n"


async def process_get(url):
    log("Before await aio.get")
    req = await aio.get(url)
    log(f"Retrieved data: '{req.data}'")


def aio_get(evt):
    log("Before aio.run")
    aio.run(process_get("/api.txt"))
    log("After aio.run")


document["get-btn"].bind("click", aio_get)
