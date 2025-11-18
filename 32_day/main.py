import tkinter as tk
import random
import time

# ---------------------------------------------
# DATA (Swiss German → English)
# ---------------------------------------------
WORD_PAIRS = [
    ("Grüezi", "Hello"),
    ("Chatz", "Cat"),
    ("Hund", "Dog"),
    ("Merci vilmal", "Thank you"),
    ("Öpfel", "Apple"),
    ("Buech", "Book"),
    ("Chäs", "Cheese"),
    ("Rot", "Red"),
]

# ---------------------------------------------
# GAME SETTINGS
# ---------------------------------------------
GRID_ROWS = 4
GRID_COLS = 4
CARD_WIDTH = 14
CARD_HEIGHT = 4
FLIP_DELAY = 900  # ms


class LinguaMatch:
    def __init__(self, root):
        self.root = root
        self.root.title("LinguaMatch – Swiss Language Memory Game")
        self.root.config(bg="#E8F8F5")

        self.card_values = []
        self.buttons = []
        self.first_card = None
        self.second_card = None
        self.matches = 0
        self.locked = False

        self.header_label = tk.Label(
            root,
            text="Match the Swiss German word with its English meaning!",
            font=("Arial", 16, "bold"),
            bg="#E8F8F5"
        )
        self.header_label.pack(pady=10)

        self.status_label = tk.Label(root, text="Matches: 0", font=("Arial", 14), bg="#E8F8F5")
        self.status_label.pack(pady=5)

        self.reset_button = tk.Button(
            root, text="Restart Game", font=("Arial", 12, "bold"),
            command=self.reset_game, bg="#D5F5E3", activebackground="#ABEBC6"
        )
        self.reset_button.pack(pady=5)

        self.game_frame = tk.Frame(root, bg="#E8F8F5")
        self.game_frame.pack()

        self.create_cards()
        self.render_board()

    def create_cards(self):
        self.card_values = []
        for swiss, english in WORD_PAIRS:
            self.card_values.append((swiss, "CH"))
            self.card_values.append((english, "EN"))
        random.shuffle(self.card_values)

    def render_board(self):
        for btn in self.buttons:
            btn.destroy()
        self.buttons = []

        idx = 0
        for r in range(GRID_ROWS):
            for c in range(GRID_COLS):
                btn = tk.Button(
                    self.game_frame,
                    text="❓",
                    width=CARD_WIDTH,
                    height=CARD_HEIGHT,
                    font=("Arial", 12, "bold"),
                    bg="#F2F3F4",
                    command=lambda i=idx: self.flip_card(i)
                )
                btn.grid(row=r, column=c, padx=8, pady=8)
                self.buttons.append(btn)
                idx += 1

    def flip_card(self, index):
        if self.locked:
            return
        if self.buttons[index]["text"] != "❓":
            return

        text, lang = self.card_values[index]
        self.buttons[index].config(text=text, bg="#FDEDEC")

        if not self.first_card:
            self.first_card = index
        else:
            self.second_card = index
            self.check_match()

    def check_match(self):
        idx1, idx2 = self.first_card, self.second_card
        word1, lang1 = self.card_values[idx1]
        word2, lang2 = self.card_values[idx2]

        pair_found = False
        for ch, en in WORD_PAIRS:
            if (word1 == ch and word2 == en) or (word1 == en and word2 == ch):
                pair_found = True
                break

        if pair_found:
            self.buttons[idx1].config(bg="#ABEBC6", state="disabled")
            self.buttons[idx2].config(bg="#ABEBC6", state="disabled")
            self.matches += 1
            self.status_label.config(text=f"Matches: {self.matches}")

            if self.matches == len(WORD_PAIRS):
                self.status_label.config(text="🎉 You matched ALL pairs! 🎉")

            self.first_card = None
            self.second_card = None

        else:
            self.locked = True
            self.root.after(FLIP_DELAY, self.hide_cards)

    def hide_cards(self):
        self.buttons[self.first_card].config(text="❓", bg="#F2F3F4")
        self.buttons[self.second_card].config(text="❓", bg="#F2F3F4")

        self.first_card = None
        self.second_card = None
        self.locked = False

    def reset_game(self):
        self.first_card = None
        self.second_card = None
        self.matches = 0
        self.status_label.config(text="Matches: 0")
        self.create_cards()
        self.render_board()


if __name__ == "__main__":
    root = tk.Tk()
    app = LinguaMatch(root)
    root.mainloop()
