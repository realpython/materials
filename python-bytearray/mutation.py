WIDTH = 71

print(">>> pixels = bytearray([48, 140, 201, 252, 186, 3, 37, 186, 52])")
print(">>> list(pixels)")
pixels = bytearray([48, 140, 201, 252, 186, 3, 37, 186, 52])
print(list(pixels))

print("\n" + " Item assignment ".center(WIDTH, "="))
print(
    """\
>>> for i in range(len(pixels)):
...     pixels[i] = 255 - pixels[i]
..."""
)
for i in range(len(pixels)):
    pixels[i] = 255 - pixels[i]
print(">>> list(pixels)")
print(list(pixels))

print("\n" + " Slice assignment ".center(WIDTH, "="))
print(">>> pixels[3:6] = (0, 0, 0)")
pixels[3:6] = (0, 0, 0)
print(">>> list(pixels)")
print(list(pixels))

print("\n" + " Slice deletion ".center(WIDTH, "="))
del pixels[3:6]
print(">>> del pixels[3:6]")
print(">>> list(pixels)")
print(list(pixels))

print("\n" + " Item deletion ".center(WIDTH, "="))
del pixels[3]
print(">>> del pixels[3]")
print(">>> list(pixels)")
print(list(pixels))

print("\n" + " Item popping ".center(WIDTH, "="))
print(">>> fourth_byte = pixels.pop(3)")
print(">>> last_byte = pixels.pop()")
fourth_byte = pixels.pop(3)
last_byte = pixels.pop()
print(">>> list(pixels)")
print(list(pixels))

print("\n" + " Value removal ".center(WIDTH, "="))
print(">>> pixels.remove(115)")
pixels.remove(115)
print(">>> list(pixels)")
print(list(pixels))

print("\n" + " Clearing all items ".center(WIDTH, "="))
print(">>> pixels.clear()")
pixels.clear()
print(">>> list(pixels)")
print(list(pixels))

print("\n" + " Appending an item ".center(WIDTH, "="))
print(">>> pixels.append(65)")
print(">>> pixels.append(67)")
pixels.append(65)
pixels.append(67)
print(">>> list(pixels)")
print(list(pixels))

print("\n" + " Inserting an item ".center(WIDTH, "="))
print(">>> pixels.insert(1, 66)")
pixels.insert(1, 66)
print(">>> list(pixels)")
print(list(pixels))

print("\n" + " Extending the bytearray ".center(WIDTH, "="))
print(">>> pixels.extend((1, 2, 3))")
pixels.extend((1, 2, 3))
print(">>> list(pixels)")
print(list(pixels))

print("\n" + " Reversal ".center(WIDTH, "="))
print(">>> pixels.reverse()")
pixels.reverse()
print(">>> list(pixels)")
print(list(pixels))

print("\n" + " Making a copy ".center(WIDTH, "="))
print(">>> pixels_copy = pixels.copy()")
pixels_copy = pixels.copy()
print(">>> list(pixels)")
print(list(pixels))
