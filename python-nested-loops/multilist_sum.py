resource_donators = [[8, 6, 3], [9, 2, 7], [4, 1, 5]]
total_resources = 0
for planet in resource_donators:
    for resource in planet:
        total_resources += resource

print(f"All resources gathered for interstellar travels: {total_resources}")
