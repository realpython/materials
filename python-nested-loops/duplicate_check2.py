crew_ids = [1, 2, 8, 4, 5, 6, 7, 8, 9, 10]
detected = set()
for crew_id in crew_ids:
    if crew_id in detected:
        print(f"Clone found: id={crew_id} is a duplicate.")
    else:
        detected.add(crew_id)
