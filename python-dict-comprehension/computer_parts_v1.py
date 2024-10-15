parts = [
    "CPU",
    "GPU",
    "Motherboard",
    "RAM",
    "SSD",
    "Power Supply",
    "Case",
    "Cooling Fan",
]
stocks = [15, 8, 12, 30, 25, 10, 5, 20]
print({part: stock for part, stock in zip(parts, stocks)})
