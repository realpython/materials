# Literal syntax (ASCII only)
print(b"Hello")
# From an iterable of integers (0 to 255)
print(bytes([72, 101, 108, 108, 111]))
# By encoding a string
print("café".encode("utf-8"))

data = b"caf\xc3\xa9"
data.decode("utf-8")
print(data)

packet = b"ABCDEF"
print(len(packet))
print(packet[0])
print(packet[1:4])

buffer = bytearray(b"ABC")
buffer[0] = 97
print(buffer)
print(bytes(buffer))

print(b"Hello".hex())
print(bytes.fromhex("48656c6c6f"))
