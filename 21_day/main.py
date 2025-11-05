# Day 21 - BioSim: The Life Simulation
# A simple console-based ecosystem simulation with creatures and food.

import random
import time
import os

# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------
GRID_SIZE = 10
NUM_CREATURES = 5
NUM_FOOD = 10
ENERGY_GAIN = 5
ENERGY_LOSS = 1
MAX_ENERGY = 20
TICKS = 30  # number of time steps

# --------------------------------------------------
# ENTITY CLASSES
# --------------------------------------------------
class Creature:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.energy = random.randint(10, MAX_ENERGY)

    def move(self):
        """Move randomly on the grid."""
        dx, dy = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        self.x = (self.x + dx) % GRID_SIZE
        self.y = (self.y + dy) % GRID_SIZE
        self.energy -= ENERGY_LOSS

    def eat(self):
        """Increase energy when food is eaten."""
        self.energy = min(self.energy + ENERGY_GAIN, MAX_ENERGY)

    def is_alive(self):
        return self.energy > 0


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# --------------------------------------------------
# WORLD SIMULATION
# --------------------------------------------------
class World:
    def __init__(self):
        self.creatures = []
        self.food = []

    def populate(self):
        """Create initial creatures and food."""
        for i in range(NUM_CREATURES):
            x, y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
            self.creatures.append(Creature(f"C{i+1}", x, y))

        for _ in range(NUM_FOOD):
            x, y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
            self.food.append(Food(x, y))

    def step(self):
        """Perform one simulation step."""
        for creature in self.creatures:
            if not creature.is_alive():
                continue
            creature.move()
            for food in self.food:
                if creature.x == food.x and creature.y == food.y:
                    creature.eat()
                    self.food.remove(food)
                    break

        # Respawn some food randomly
        if random.random() < 0.3:
            self.food.append(Food(random.randint(0, GRID_SIZE-1),
                                  random.randint(0, GRID_SIZE-1)))

    def display(self, tick):
        """Render the world grid."""
        os.system('cls' if os.name == 'nt' else 'clear')
        grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

        for food in self.food:
            grid[food.y][food.x] = "*"

        for creature in self.creatures:
            if creature.is_alive():
                grid[creature.y][creature.x] = "C"

        print(f"=== BioSim – Life Simulation | Tick {tick} ===")
        for row in grid:
            print(" ".join(row))
        alive = [c for c in self.creatures if c.is_alive()]
        print(f"\nAlive: {len(alive)} / {len(self.creatures)}")
        for c in alive:
            print(f"{c.name}: Energy {c.energy}")
        time.sleep(0.5)


# --------------------------------------------------
# MAIN LOOP
# --------------------------------------------------
def main():
    world = World()
    world.populate()

    for tick in range(1, TICKS + 1):
        world.display(tick)
        world.step()

    print("\nSimulation complete.")


if __name__ == "__main__":
    main()
