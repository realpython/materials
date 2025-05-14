living_quarters = 3
sections = 2
floors = 3

for floor in range(floors):
    for section in range(sections):
        for living_quarter in range(living_quarters):
            print(
                f"Scanning quarter {living_quarter} in section {section}"
                f" on floor {floor} for the intruder..."
            )
