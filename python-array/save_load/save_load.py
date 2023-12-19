from array import array
from struct import pack, unpack


def save(filename, numbers):
    with open(filename, mode="wb") as file:
        file.write(numbers.typecode.encode("ascii"))
        file.write(pack("<I", len(numbers)))
        numbers.tofile(file)


def load(filename):
    with open(filename, mode="rb") as file:
        typecode = file.read(1).decode("ascii")
        (length,) = unpack("<I", file.read(4))
        numbers = array(typecode)
        numbers.fromfile(file, length)
        return numbers


save("binary.data", array("H", [12, 42, 7, 15, 42, 38, 21]))
print("Saved array as: 'binary.data'")
print(load("binary.data"))
