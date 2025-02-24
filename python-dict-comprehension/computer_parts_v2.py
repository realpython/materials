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
part_costs = [250, 500, 150, 80, 100, 120, 70, 25]
print(
    {
        part: stock * cost
        for part, stock, cost in zip(parts, stocks, part_costs)
    }
)
