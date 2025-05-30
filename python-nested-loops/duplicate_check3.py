from collections import Counter

crew_ids = [1, 2, 8, 4, 5, 6, 7, 8, 9, 10]
detected = Counter(crew_ids)
for key, value in detected.items():
    if value > 1:
        print(f"Clone found: id={key} is a duplicate.")
