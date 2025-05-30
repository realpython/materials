filename = "   Report_2025 FINAL.pdf  "

# Correctly chained methods
print(filename.strip().lower().replace(" ", "_"))

# Incorrect order
print(filename.lower().replace(" ", "_").strip())
