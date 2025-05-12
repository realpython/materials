crew_ids = [1, 2, 8, 4, 5, 6, 7, 8, 9, 10]
detected = set()
for id in crew_ids:
    if id in detected:
        print(f"Clone found: id {id} is a duplicate.")
    else:
        detected.add(id)
