from world import World
from events import world_event

world = World()

print("🌍 A New World Has Been Born")
print("-" * 40)

while True:
    print("\n📖 World State:")
    for k, v in world.describe().items():
        print(f"{k}: {v}")

    choice = input("\nAdvance one year? (y/n): ").lower()

    if choice != "y":
        print("Simulation ended.")
        break

    world.age_world()

    event = world_event(world)
    if event:
        print("⚠️ Event:", event)

    # Collapse condition
    if world.danger_level >= 15:
        print("\n💥 The world collapsed due to extreme danger.")
        break
