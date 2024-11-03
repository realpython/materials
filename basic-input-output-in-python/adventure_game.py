import random

health = 5
enemy_health = 3

while health > 0 and enemy_health > 0:
    if input("Attack or Run? ").lower() == "attack":
        enemy_health -= 1
        print("You hit the enemy!")
        # Implement a 50% chance that the enemy strikes back.
        enemy_attacks = random.choice([True, False])
        if enemy_attacks:
            health -= 2
            print("The enemy strikes back!")
    else:
        print("You ran away!")
        break
    print(f"Your health: {health}, Enemy health: {enemy_health}")

print("Victory!" if enemy_health <= 0 else "Game Over")
