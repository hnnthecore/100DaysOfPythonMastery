# Day 27 - GenePy: DNA Pattern Visualizer
# Generates and mutates DNA sequences directly in terminal.
# No files are written; this is a pure runtime visual simulation.

import random
import time
import os

BASES = ["A", "T", "G", "C"]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def generate_dna(length=60):
    """Generate a random DNA sequence."""
    return "".join(random.choice(BASES) for _ in range(length))


def mutate_dna(seq, mutation_rate=0.05):
    """Mutate sequence by changing bases randomly."""
    seq_list = list(seq)
    for i in range(len(seq_list)):
        if random.random() < mutation_rate:
            current = seq_list[i]
            seq_list[i] = random.choice([b for b in BASES if b != current])
    return "".join(seq_list)


def get_complement(base):
    """Return complementary DNA base."""
    mapping = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return mapping.get(base, "N")


def chunk_sequence(seq, chunk_size=30):
    """Split DNA sequence into chunks for display."""
    return [seq[i:i + chunk_size] for i in range(0, len(seq), chunk_size)]


def visualize(seq, generation):
    """Print the DNA and its complement."""
    clear_screen()
    print("=" * 60)
    print(f"GENEPY – DNA PATTERN VISUALIZER | Generation {generation}")
    print("=" * 60)
    for line in chunk_sequence(seq):
        comp = "".join(get_complement(b) for b in line)
        print(f"DNA : {line}")
        print(f"Comp: {comp}")
        print("-" * 40)
    print("\nPress Ctrl+C to stop simulation.")


def run_simulation(length=60, generations=5, mutation_rate=0.05, delay=1.0):
    """Run multiple generations of DNA mutation and visualization."""
    dna = generate_dna(length)
    for gen in range(1, generations + 1):
        visualize(dna, gen)
        time.sleep(delay)
        dna = mutate_dna(dna, mutation_rate)


def main():
    print("GenePy – DNA Pattern Visualizer")
    try:
        length = int(input("Enter DNA length (default 60): ") or 60)
        generations = int(input("Enter generations (default 5): ") or 5)
        mutation_rate = float(input("Enter mutation rate (default 0.05): ") or 0.05)
    except ValueError:
        print("Invalid input. Using defaults.")
        length, generations, mutation_rate = 60, 5, 0.05

    run_simulation(length, generations, mutation_rate)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSimulation stopped.")
