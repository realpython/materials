height = 6
sail_patterns = "*#-x+o"
for row in range(height):
    pattern = ""
    spacing = " " * (height - row)
    for symbol in sail_patterns:
        pattern += symbol * row + spacing

    print(pattern)
