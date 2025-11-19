import tkinter as tk
from tkinter import messagebox
import requests
from threading import Thread
from PIL import Image, ImageTk
from io import BytesIO


class PocketDex(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("PocketDex – Pokémon Viewer")
        self.geometry("700x550")
        self.config(bg="#F5F5F5")

        self.create_layout()

    # ---------------------------------------------------
    # UI Layout
    # ---------------------------------------------------
    def create_layout(self):
        title_label = tk.Label(self, text="PocketDex", font=("Arial", 26, "bold"), bg="#F5F5F5")
        title_label.pack(pady=10)

        search_frame = tk.Frame(self, bg="#F5F5F5")
        search_frame.pack(pady=10)

        self.search_entry = tk.Entry(search_frame, width=30, font=("Arial", 14))
        self.search_entry.grid(row=0, column=0, padx=10)

        search_btn = tk.Button(search_frame, text="Search", font=("Arial", 12), command=self.start_search)
        search_btn.grid(row=0, column=1)

        # Image Display
        self.image_label = tk.Label(self, bg="#F5F5F5")
        self.image_label.pack(pady=10)

        # Info Display
        self.info_text = tk.Label(self, text="", font=("Arial", 14), bg="#F5F5F5", justify="left")
        self.info_text.pack(pady=10)

    # ---------------------------------------------------
    # Start threaded search
    # ---------------------------------------------------
    def start_search(self):
        pokemon = self.search_entry.get().strip().lower()
        if pokemon == "":
            messagebox.showerror("Error", "Please enter a Pokémon name or ID.")
            return

        Thread(target=self.search_pokemon, args=(pokemon,), daemon=True).start()

    # ---------------------------------------------------
    # Fetch data from API
    # ---------------------------------------------------
    def search_pokemon(self, name):
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"

        self.info_text.config(text="Loading...")
        self.image_label.config(image="")

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            # Extract values
            p_name = data["name"].title()
            p_id = data["id"]
            types = ", ".join([t["type"]["name"].title() for t in data["types"]])
            abilities = ", ".join([a["ability"]["name"].title() for a in data["abilities"]])

            stats_lines = []
            for stat in data["stats"]:
                stat_name = stat["stat"]["name"].title()
                stat_value = stat["base_stat"]
                stats_lines.append(f"{stat_name}: {stat_value}")

            stats_text = "\n".join(stats_lines)

            info = (
                f"Name: {p_name}\n"
                f"ID: {p_id}\n"
                f"Types: {types}\n"
                f"Abilities: {abilities}\n\n"
                f"Stats:\n{stats_text}"
            )

            # Update Info
            self.info_text.config(text=info)

            # Load Image
            img_url = data["sprites"]["other"]["official-artwork"]["front_default"]
            if img_url:
                img_response = requests.get(img_url, timeout=10)
                img_data = Image.open(BytesIO(img_response.content))
                img_data = img_data.resize((250, 250))
                img = ImageTk.PhotoImage(img_data)

                self.image_label.config(image=img)
                self.image_label.image = img

        except Exception:
            self.info_text.config(text="Could not find Pokémon. Check the name or ID.")


# ---------------------------------------------------
# Run App
# ---------------------------------------------------
if __name__ == "__main__":
    app = PocketDex()
    app.mainloop()
