import time

from alien_pet_care.pet import AlienPet


def main():
    print("--- Welcome to the Alien Pet Incubator ---")
    pet = AlienPet(name="Zorg")

    print(f"Initializing care routine for {pet.name}...")
    time.sleep(0.5)

    for i in range(12):
        pet.feed()
        pet.rest()
        beam = "=" * (i + 1)
        print(
            f"\r🛸 {beam}> 👾 Feeding & Resting... (Cycle {i + 1}/12)",
            end="",
            flush=True,
        )
        time.sleep(0.15)

    print("\n\n--- Final Stats ---")
    print(f"Pet Name: {pet.name}")
    print(f"Fed Level: {pet.fed_level} / 10")
    print(f"Rested Level: {pet.rested_level} / 10")
    print(f"Current Status: {pet.get_status()}")


if __name__ == "__main__":
    main()
