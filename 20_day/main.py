# Day 20 - CodeCanvas: Python Drawing Pad
# A creative Python project for generating geometric art interactively.

import turtle
import random

# --------------------------------------------------
# Setup the canvas
# --------------------------------------------------
screen = turtle.Screen()
screen.title("CodeCanvas - Python Drawing Pad")
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# --------------------------------------------------
# Utility functions
# --------------------------------------------------
def random_color():
    """Generate a random RGB color."""
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

def draw_square(size):
    """Draw a square of given size."""
    pen.color(random_color())
    for _ in range(4):
        pen.forward(size)
        pen.right(90)

def draw_circle(radius):
    """Draw a circle with given radius."""
    pen.color(random_color())
    pen.circle(radius)

def draw_polygon(sides, length):
    """Draw a polygon with N sides."""
    pen.color(random_color())
    angle = 360 / sides
    for _ in range(sides):
        pen.forward(length)
        pen.right(angle)

def draw_spiral(turns, step):
    """Draw a colorful spiral."""
    pen.color(random_color())
    for i in range(turns):
        pen.forward(i * step / 10)
        pen.right(45)

# --------------------------------------------------
# Interactive menu
# --------------------------------------------------
def draw_menu():
    print("=" * 60)
    print(" CODECANVAS – PYTHON DRAWING PAD ".center(60))
    print("=" * 60)
    print("Select a shape to draw:")
    print("1. Square")
    print("2. Circle")
    print("3. Polygon")
    print("4. Spiral")
    print("5. Random Art")
    print("6. Clear Canvas")
    print("7. Exit")
    print("-" * 60)

def main():
    while True:
        draw_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            size = int(input("Enter square size: "))
            draw_square(size)

        elif choice == "2":
            radius = int(input("Enter circle radius: "))
            draw_circle(radius)

        elif choice == "3":
            sides = int(input("Enter number of sides: "))
            length = int(input("Enter side length: "))
            draw_polygon(sides, length)

        elif choice == "4":
            turns = int(input("Enter number of turns: "))
            step = int(input("Enter step size: "))
            draw_spiral(turns, step)

        elif choice == "5":
            print("Generating random art...")
            for _ in range(20):
                pen.penup()
                pen.goto(random.randint(-200, 200), random.randint(-200, 200))
                pen.pendown()
                shape = random.choice(["square", "circle", "polygon"])
                if shape == "square":
                    draw_square(random.randint(20, 100))
                elif shape == "circle":
                    draw_circle(random.randint(20, 80))
                else:
                    draw_polygon(random.randint(3, 8), random.randint(20, 70))

        elif choice == "6":
            pen.clear()

        elif choice == "7":
            print("Exiting CodeCanvas. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

    turtle.done()


if __name__ == "__main__":
    main()
