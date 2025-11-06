# Day 22 - AlgoVision: Sorting Algorithm Visualizer
# Visualize common sorting algorithms step by step in the terminal.

import random
import time
import os

# --------------------------------------------------
# Configuration
# --------------------------------------------------
ARRAY_SIZE = 15
SLEEP_TIME = 0.3  # time delay between visualization steps


# --------------------------------------------------
# Visualization Utilities
# --------------------------------------------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_array(arr, highlight_index=None):
    """Render array as vertical bars."""
    clear_screen()
    print("AlgoVision – Sorting Algorithm Visualizer\n")
    max_val = max(arr)
    for i, value in enumerate(arr):
        bar = "|" * int((value / max_val) * 50)
        marker = " <" if highlight_index == i else ""
        print(f"{value:3}: {bar}{marker}")
    print("\n" + "-" * 60)
    time.sleep(SLEEP_TIME)


# --------------------------------------------------
# Sorting Algorithms (with Visualization)
# --------------------------------------------------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            display_array(arr, highlight_index=j)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    display_array(arr)
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            display_array(arr, highlight_index=j)
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    display_array(arr)
    return arr


def quick_sort_visual(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        display_array(arr, highlight_index=pi)
        quick_sort_visual(arr, low, pi - 1)
        quick_sort_visual(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        display_array(arr, highlight_index=j)
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# --------------------------------------------------
# Main Menu and CLI Logic
# --------------------------------------------------
def main():
    while True:
        clear_screen()
        print("=" * 60)
        print(" ALGOVISION – SORTING ALGORITHM VISUALIZER ".center(60))
        print("=" * 60)
        print("Select an algorithm:")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Quick Sort")
        print("4. Exit")
        print("-" * 60)

        choice = input("Enter your choice: ").strip()

        if choice == "4":
            print("Exiting AlgoVision. Goodbye!")
            break

        if choice not in ["1", "2", "3"]:
            print("Invalid choice. Please try again.")
            time.sleep(1)
            continue

        arr = [random.randint(1, 50) for _ in range(ARRAY_SIZE)]
        display_array(arr)

        if choice == "1":
            bubble_sort(arr)
        elif choice == "2":
            insertion_sort(arr)
        elif choice == "3":
            quick_sort_visual(arr, 0, len(arr) - 1)

        print("\nSorting complete!")
        input("\nPress Enter to return to menu...")


if __name__ == "__main__":
    main()
