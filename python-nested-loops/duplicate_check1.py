crew_ids = [1, 2, 8, 4, 5, 6, 7, 8, 9, 10]
for i, first_id in enumerate(crew_ids):
    for second_id in crew_ids[i + 1 :]:
        if first_id == second_id:
            print(f"Clone found: id={first_id} is a duplicate.")
