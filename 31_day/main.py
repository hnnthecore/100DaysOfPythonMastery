# Day 31 – ParticleFlow: Interactive Particle Physics Simulator
# A dynamic particle field affected by gravity, drag, and mouse forces.

import pygame
import random
import math

WIDTH, HEIGHT = 900, 600
NUM_PARTICLES = 300

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ParticleFlow – Physics Simulator")
clock = pygame.time.Clock()


class Particle:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.color = self.random_color()
        self.size = random.randint(2, 4)

    def random_color(self):
        return (
            random.randint(150, 255),
            random.randint(80, 200),
            random.randint(150, 255)
        )

    def update(self, mx, my):
        # Gravity effect
        gravity = 0.05
        self.vy += gravity

        # Apply drag
        self.vx *= 0.99
        self.vy *= 0.99

        # Mouse repulsion force
        dist = math.hypot(self.x - mx, self.y - my)
        if dist < 120 and dist != 0:
            force = 2 / dist
            self.vx += (self.x - mx) * force
            self.vy += (self.y - my) * force

        # Update position
        self.x += self.vx
        self.y += self.vy

        # Bounce off edges
        if self.x <= 0 or self.x >= WIDTH:
            self.vx *= -0.8
        if self.y <= 0 or self.y >= HEIGHT:
            self.vy *= -0.8

        # Clamp positions within window
        self.x = max(0, min(WIDTH, self.x))
        self.y = max(0, min(HEIGHT, self.y))

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)


def main():
    particles = [Particle() for _ in range(NUM_PARTICLES)]
    running = True

    while running:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((15, 15, 25))

        for p in particles:
            p.update(mx, my)
            p.draw()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
