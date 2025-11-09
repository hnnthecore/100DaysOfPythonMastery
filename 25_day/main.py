# Day 25 - StarGen: Procedural Universe Simulator
# Generates a fictional galaxy with star systems, planets, and moons.
# Outputs both a console catalog and a JSON file.

import random
import json
import time

OUTPUT_FILE = "stargen_universe.json"


# ------------------------------------------------------------
# Procedural name generators
# ------------------------------------------------------------
SYLLABLES = [
    "al", "kor", "ve", "dra", "ion", "ser", "tal", "xor", "un",
    "lyr", "pha", "zen", "mar", "quar", "ris", "the", "vex", "sol"
]

PLANET_PREFIX = ["A", "B", "C", "D", "E", "F", "G"]


def generate_name():
    """Generate a star/system name by stitching together syllables."""
    return "".join(random.choices(SYLLABLES, k=random.randint(2, 3))).title()


# ------------------------------------------------------------
# Generators for planets, moons, and systems
# ------------------------------------------------------------
def generate_moon(idx):
    return {
        "name": f"Moon-{idx}",
        "radius_km": random.randint(500, 3500),
        "has_ice": random.choice([True, False])
    }


def generate_planet(idx):
    planet_types = [
        "terrestrial",
        "gas giant",
        "ice world",
        "lava world",
        "ocean world",
        "desert world"
    ]
    p_type = random.choice(planet_types)
    planet = {
        "name": f"Planet-{PLANET_PREFIX[idx % len(PLANET_PREFIX)]}{idx}",
        "type": p_type,
        "radius_km": random.randint(2500, 70000) if p_type != "terrestrial" else random.randint(2500, 15000),
        "orbital_distance_au": round(random.uniform(0.2, 30.0), 2),
        "has_atmosphere": p_type in ["terrestrial", "ocean world", "desert world"],
        "temperature_k": random.randint(50, 1200),
        "moons": []
    }

    # Some planets get moons
    if p_type in ["gas giant", "ice world", "terrestrial"]:
        moon_count = random.randint(0, 3)
        planet["moons"] = [generate_moon(i + 1) for i in range(moon_count)]

    return planet


def generate_star():
    star_classes = ["O", "B", "A", "F", "G", "K", "M"]
    cls = random.choice(star_classes)
    return {
        "class": cls,
        "temperature_k": random.randint(2500, 30000),
        "mass_solar": round(random.uniform(0.2, 10.0), 2)
    }


def generate_system(system_id):
    system_name = generate_name()
    num_stars = random.choice([1, 1, 1, 2])  # mostly single, sometimes binary
    num_planets = random.randint(0, 8)

    system = {
        "id": system_id,
        "name": system_name,
        "stars": [generate_star() for _ in range(num_stars)],
        "planets": []
    }

    for i in range(num_planets):
        system["planets"].append(generate_planet(i + 1))

    return system


def generate_galaxy(num_systems=10):
    galaxy = {
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "galaxy_name": generate_name() + " Sector",
        "system_count": num_systems,
        "systems": []
    }

    for i in range(1, num_systems + 1):
        galaxy["systems"].append(generate_system(i))

    return galaxy


# ------------------------------------------------------------
# Rendering to console
# ------------------------------------------------------------
def print_catalog(galaxy):
    print("=" * 70)
    print(f"STAR GEN – PROCEDURAL UNIVERSE SIMULATOR".center(70))
    print("=" * 70)
    print(f"Galaxy: {galaxy['galaxy_name']}")
    print(f"Systems generated: {galaxy['system_count']}")
    print(f"Generated at: {galaxy['generated_at']}")
    print("-" * 70)

    for system in galaxy["systems"]:
        print(f"[System {system['id']}] {system['name']}")
        print(f"  Stars: {len(system['stars'])}")
        for idx, star in enumerate(system["stars"], start=1):
            print(f"    Star {idx}: Class {star['class']} | Temp {star['temperature_k']}K | Mass {star['mass_solar']} Msun")

        if not system["planets"]:
            print("  Planets: None")
        else:
            print(f"  Planets: {len(system['planets'])}")
            for p in system["planets"]:
                moon_str = f" | Moons: {len(p['moons'])}" if p["moons"] else ""
                print(
                    f"    - {p['name']} ({p['type']}) at {p['orbital_distance_au']} AU"
                    f" | Temp: {p['temperature_k']}K{moon_str}"
                )
        print("-" * 70)


# ------------------------------------------------------------
# Save to JSON
# ------------------------------------------------------------
def save_to_json(galaxy, filename=OUTPUT_FILE):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(galaxy, f, indent=4)
    print(f"Universe saved to {filename}")


# ------------------------------------------------------------
# Main entry
# ------------------------------------------------------------
def main():
    try:
        count = input("How many star systems to generate? (default 10): ").strip()
        num = int(count) if count else 10
    except ValueError:
        num = 10

    galaxy = generate_galaxy(num_systems=num)
    print_catalog(galaxy)
    save_to_json(galaxy)


if __name__ == "__main__":
    main()
