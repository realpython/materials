WIDTH = 71

print(" Empty ".center(WIDTH, "="))
print(f"{bytearray() = }")
print(f"{bytearray(0) = }")
print(f"{bytearray([]) = }")
print(f"{bytearray(b"") = }\n")

print(" Zero-filled ".center(WIDTH, "="))
print(f"{bytearray(5) = }\n")

print(" From an iterable of integers ".center(WIDTH, "="))
print(f"{bytearray([65, 66, 67]) = }")
print(f"{bytearray(range(3)) = }\n")

print(" From a bytes-like object ".center(WIDTH, "="))
print(f"{bytearray(b"Espa\xc3\xb1ol") = }\n")

print(" From a string ".center(WIDTH, "="))
print(f"{bytearray("Español", "utf-8") = }")
print(f"{bytearray("Español", "ascii", errors="ignore") = }")
print(f"{bytearray("Español", "ascii", errors="replace") = }\n")

print(" From hexadecimal digits".center(WIDTH, "="))
print(f"{bytearray.fromhex("30 8C C9 FF") = }")
