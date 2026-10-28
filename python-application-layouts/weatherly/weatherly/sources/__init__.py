from weatherly.sources.fake import FakeSource

SOURCES = {"fake": FakeSource}


def get_source(name):
    """Return an API client for the named weather provider."""
    try:
        return SOURCES[name]()
    except KeyError:
        raise LookupError(f"unknown weather source: {name}") from None
