total = 123456.99

# Formatting values
width = 30
align = ">"
fill = "."
precision = 2
sep = ","

print(f"Total{total:{fill}{align}{width}{sep}.{precision}f}")
