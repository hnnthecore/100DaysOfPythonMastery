import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
from threading import Thread

OMDB_API_KEY = "YOUR_OMDB_API_KEY"
OMDB_URL = "https://www.omdbapi.com/"


class MovieQuestApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("MovieQuest – Movie Search Explorer")
        self.geometry("900x600")
        self.config(bg="#F5F5F5")

        self.poster_label = None
        self.poster_image = None

        self.build_layout()

    # -------------------------------------------------
    # UI LAYOUT
    # -------------------------------------------------
    def build_layout(self):
        header = tk.Label(
            self,
            text="MovieQuest",
            font=("Arial", 26, "bold"),
            bg="#F5F5F5"
        )
        header.pack(pady=15)

        search_frame = tk.Frame(self, bg="#F5F5F5")
        search_frame.pack(pady=10)

        tk.Label(
            search_frame,
            text="Movie Title:",
            font=("Arial", 14),
            bg="#F5F5F5"
        ).grid(row=0, column=0, padx=5)

        self.search_entry = tk.Entry(search_frame, font=("Arial", 14), width=40)
        self.search_entry.grid(row=0, column=1, padx=5)

        search_btn = tk.Button(
            search_frame,
            text="Search",
            font=("Arial", 12),
            command=self.start_search
        )
        search_btn.grid(row=0, column=2, padx=5)

        # Main content frame
        content_frame = tk.Frame(self, bg="#F5F5F5")
        content_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Poster on the left
        self.poster_label = tk.Label(content_frame, bg="#F5F5F5")
        self.poster_label.pack(side="left", padx=20, pady=10)

        # Info panel on the right
        self.info_text = tk.Text(
            content_frame,
            font=("Arial", 12),
            wrap="word",
            state="disabled",
            width=60,
            height=25
        )
        self.info_text.pack(side="right", fill="both", expand=True)

        # Status bar
        self.status_label = tk.Label(
            self,
            text="Enter a movie title and click Search.",
            font=("Arial", 11),
            bg="#F5F5F5"
        )
        self.status_label.pack(pady=5)

    # -------------------------------------------------
    # SEARCH HANDLER
    # -------------------------------------------------
    def start_search(self):
        title = self.search_entry.get().strip()
        if not title:
            messagebox.showwarning("Warning", "Please enter a movie title.")
            return

        self.status_label.config(text="Searching...")
        self.clear_display()

        thread = Thread(target=self.fetch_movie, args=(title,), daemon=True)
        thread.start()

    # -------------------------------------------------
    # API CALL
    # -------------------------------------------------
    def fetch_movie(self, title):
        try:
            params = {
                "t": title,
                "apikey": OMDB_API_KEY
            }
            response = requests.get(OMDB_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            if data.get("Response") == "False":
                self.status_label.config(text="Movie not found.")
                self.set_info_text("Movie not found. Check the title and try again.")
                return

            self.display_movie(data)
            self.status_label.config(text="Loaded successfully.")

        except Exception as e:
            self.status_label.config(text="Failed to fetch movie data.")
            self.set_info_text("An error occurred while fetching movie data.")
            print("Error:", e)

    # -------------------------------------------------
    # DISPLAY HELPERS
    # -------------------------------------------------
    def clear_display(self):
        self.poster_label.config(image="", text="")
        self.poster_image = None
        self.set_info_text("")

    def set_info_text(self, text):
        self.info_text.config(state="normal")
        self.info_text.delete("1.0", tk.END)
        self.info_text.insert("1.0", text)
        self.info_text.config(state="disabled")

    def display_movie(self, data):
        # Text info
        title = data.get("Title", "N/A")
        year = data.get("Year", "N/A")
        rated = data.get("Rated", "N/A")
        runtime = data.get("Runtime", "N/A")
        genre = data.get("Genre", "N/A")
        director = data.get("Director", "N/A")
        actors = data.get("Actors", "N/A")
        plot = data.get("Plot", "N/A")
        imdb_rating = data.get("imdbRating", "N/A")
        language = data.get("Language", "N/A")
        country = data.get("Country", "N/A")

        info = []
        info.append(f"Title: {title}")
        info.append(f"Year: {year}")
        info.append(f"Rated: {rated}")
        info.append(f"Runtime: {runtime}")
        info.append(f"Genre: {genre}")
        info.append(f"Director: {director}")
        info.append(f"Actors: {actors}")
        info.append(f"Language: {language}")
        info.append(f"Country: {country}")
        info.append(f"IMDb Rating: {imdb_rating}")
        info.append("")
        info.append("Plot:")
        info.append(plot)

        self.set_info_text("\n".join(info))

        # Poster
        poster_url = data.get("Poster")
        if poster_url and poster_url != "N/A":
            try:
                img_response = requests.get(poster_url, timeout=10)
                img_response.raise_for_status()
                img_data = Image.open(BytesIO(img_response.content))
                img_data = img_data.resize((300, 450))
                self.poster_image = ImageTk.PhotoImage(img_data)
                self.poster_label.config(image=self.poster_image)
            except Exception as e:
                print("Poster load error:", e)
                self.poster_label.config(text="No poster available.")
        else:
            self.poster_label.config(text="No poster available.")


if __name__ == "__main__":
    app = MovieQuestApp()
    app.mainloop()
