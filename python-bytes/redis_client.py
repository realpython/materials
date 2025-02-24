import socket
from functools import partial
from typing import Callable, Self


class RedisClient:
    def __init__(self, address: str = "localhost", port: int = 6379) -> None:
        self._socket = socket.create_connection((address, port))

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self._socket.close()

    def flush(self) -> None:
        self._socket.sendall(flush_command())

    def ping(self) -> None:
        self._socket.sendall(ping_command())

    def echo(self, message: str) -> None:
        self._socket.sendall(echo_command(message))

    def last_save(self) -> None:
        self._socket.sendall(last_save_command())

    def keys(self, pattern: str = "*") -> None:
        self._socket.sendall(keys_command(pattern))

    def get(self, key: str) -> None:
        self._socket.sendall(get_command(key))

    def set(self, key: str, value: str, ex: int | None = None) -> None:
        self._socket.sendall(set_command(key, value, ex))

    def delete(self, *keys: str) -> None:
        self._socket.sendall(del_command(*keys))

    def get_response(self) -> str | int | None | list:
        line = bytearray()
        while not line.endswith(b"\r\n"):
            line.extend(self._socket.recv(1))
        match prefix := line[:1]:
            case b"+" | b"-":
                return line[1:-2].decode("ascii")
            case b":":
                return int(line[1:-2])
            case b"$":
                if (length := int(line[1:])) == -1:
                    return None
                else:
                    data = self._socket.recv(length + 2)
                    return data[:-2].decode("utf-8")
            case b"*":
                return [self.get_response() for _ in range(int(line[1:]))]
            case _:
                raise ValueError(f"Unsupported type: {prefix}")


def flush_command() -> bytes:
    return array(bulk_string("FLUSHDB"))


def ping_command() -> bytes:
    return array(bulk_string("PING"))


def echo_command(message: str) -> bytes:
    return array(bulk_string("ECHO"), bulk_string(message))


def keys_command(pattern: str) -> bytes:
    return array(bulk_string("KEYS"), bulk_string(pattern))


def set_command(key: str, value: str, ex: int | None) -> bytes:
    items = [
        bulk_string("SET"),
        bulk_string(key),
        bulk_string(value),
    ]
    if ex is not None:
        items.append(bulk_string("EX"))
        items.append(bulk_string(str(ex)))
    return array(*items)


def get_command(key: str) -> bytes:
    return array(bulk_string("GET"), bulk_string(key))


def del_command(*keys: str) -> bytes:
    return array(bulk_string("DEL"), *map(bulk_string, keys))


def last_save_command() -> bytes:
    return array(bulk_string("LASTSAVE"))


def array(*items: bytes) -> bytes:
    binary = bytearray(f"*{len(items)}\r\n".encode("ascii"))
    for item in items:
        binary.extend(item)
    return bytes(binary)


def bulk_string(value: str) -> bytes:
    binary = value.encode("utf-8")
    return f"${len(binary)}\r\n".encode("utf-8") + binary + b"\r\n"


def simple_string(value: str) -> bytes:
    return f"+{value}\r\n".encode("ascii", errors="strict")


def integer(value: int) -> bytes:
    return f":{value}\r\n".encode("ascii")


if __name__ == "__main__":
    with RedisClient() as redis:
        commands: list[Callable] = [
            redis.ping,
            partial(redis.echo, "Café"),
            redis.last_save,
            redis.flush,
            partial(redis.get, "key"),
            partial(redis.set, "key1", "value1"),
            partial(redis.set, "key2", "value2"),
            partial(redis.get, "key1"),
            redis.keys,
            partial(redis.delete, "key1", "key2"),
            partial(redis.set, "key3", "value3", 5),
        ]
        for command in commands:
            if isinstance(command, partial):
                args = " ".join([str(x) for x in command.args])
                print(f"{command.func.__name__.upper()} {args}")
            else:
                print(f"{command.__name__.upper()}")
            command()
            print(repr(redis.get_response()))
            print()
