# Day 30 - PianoPy: Keyboard Piano Simulator
# A simple musical keyboard that plays notes when you press keys.
# Uses pygame for real-time audio playback and keyboard event handling.

import pygame
import numpy as np

# ------------------------------------------------------------
# Sound Synthesis (Tone Generator)
# ------------------------------------------------------------
def generate_tone(freq, duration=0.4, sample_rate=44100):
    """
    Generate a sine wave tone for a given frequency.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(freq * t * 2 * np.pi)

    # Normalize to 16-bit audio
    audio = (tone * 32767).astype(np.int16)
    return audio


# ------------------------------------------------------------
# Note Frequency Mapping
# ------------------------------------------------------------
NOTE_MAP = {
    pygame.K_a: 261.63,   # C4
    pygame.K_s: 293.66,   # D4
    pygame.K_d: 329.63,   # E4
    pygame.K_f: 349.23,   # F4
    pygame.K_g: 392.00,   # G4
    pygame.K_h: 440.00,   # A4
    pygame.K_j: 493.88,   # B4
    pygame.K_k: 523.25,   # C5
}


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------
def main():
    pygame.init()
    pygame.display.set_caption("PianoPy – Keyboard Piano Simulator")

    # Basic display window
    screen = pygame.display.set_mode((500, 200))
    font = pygame.font.Font(None, 36)

    text_surface = font.render("Press A-S-D-F-G-H-J-K to play notes", True, (255, 255, 255))

    # Audio initialization
    pygame.mixer.init(frequency=44100, size=-16, channels=1)

    running = True
    while running:
        screen.fill((40, 40, 40))
        screen.blit(text_surface, (40, 80))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Key pressed
            if event.type == pygame.KEYDOWN:
                if event.key in NOTE_MAP:
                    freq = NOTE_MAP[event.key]
                    tone = generate_tone(freq)
                    sound = pygame.mixer.Sound(buffer=tone)
                    sound.play()

                # Exit via ESC
                if event.key == pygame.K_ESCAPE:
                    running = False

    pygame.quit()


if __name__ == "__main__":
    main()
