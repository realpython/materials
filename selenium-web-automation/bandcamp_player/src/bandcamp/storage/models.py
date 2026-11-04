import hashlib
from dataclasses import astuple, dataclass


@dataclass(frozen=True)
class Track:
    title: str
    artist: str
    artist_url: str
    album: str | None = None
    album_url: str | None = None
    genre: str | None = None

    @property
    def id(self) -> str:
        data = "".join([str(x) for x in astuple(self)]).encode("utf-8")
        return hashlib.md5(data).hexdigest()
