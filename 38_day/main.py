import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
from threading import Thread


GOOGLE_BOOKS_URL = "https://www.googleapis.com/books/v1/volumes"


class BookFinderApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("BookFinder – Book Search & Details Explorer")
        self.geometry("1000x600")
        self.config(bg="#F5F5F5")

        self.books = []
        self.current_cover = None

        self.build_layout()

    # -------------------------------------------------
    # UI LAYOUT
    # -------------------------------------------------
    def build_layout(self):
        header = tk.Label(
            self,
            text="BookFinder",
            font=("Arial", 26, "bold"),
            bg="#F5F5F5",
        )
        header.pack(pady=10)

        search_frame = tk.Frame(self, bg="#F5F5F5")
        search_frame.pack(pady=5)

        tk.Label(
            search_frame,
            text="Search:",
            font=("Arial", 14),
            bg="#F5F5F5",
        ).grid(row=0, column=0, padx=5)

        self.search_entry = tk.Entry(search_frame, font=("Arial", 14), width=40)
        self.search_entry.grid(row=0, column=1, padx=5)

        search_btn = tk.Button(
            search_frame,
            text="Search Books",
            font=("Arial", 12),
            command=self.start_search,
        )
        search_btn.grid(row=0, column=2, padx=5)

        # Main content frame
        main_frame = tk.Frame(self, bg="#F5F5F5")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Left: results list
        left_frame = tk.Frame(main_frame, bg="#F5F5F5", width=350)
        left_frame.pack(side="left", fill="y", padx=5)

        tk.Label(
            left_frame,
            text="Results",
            font=("Arial", 16, "bold"),
            bg="#F5F5F5",
        ).pack(pady=5)

        self.results_list = tk.Listbox(
            left_frame,
            font=("Arial", 12),
            width=45,
            height=25,
        )
        self.results_list.pack(fill="y", padx=5, pady=5)
        self.results_list.bind("<<ListboxSelect>>", self.on_book_select)

        # Right: cover + info
        right_frame = tk.Frame(main_frame, bg="#F5F5F5")
        right_frame.pack(side="right", fill="both", expand=True, padx=5)

        self.cover_label = tk.Label(right_frame, bg="#F5F5F5")
        self.cover_label.pack(pady=10)

        self.info_text = tk.Text(
            right_frame,
            font=("Arial", 12),
            wrap="word",
            state="disabled",
        )
        self.info_text.pack(fill="both", expand=True, padx=10, pady=5)

        # Status bar
        self.status_label = tk.Label(
            self,
            text="Enter a keyword or book title and click Search.",
            font=("Arial", 11),
            bg="#F5F5F5",
        )
        self.status_label.pack(pady=5)

    # -------------------------------------------------
    # SEARCH HANDLER
    # -------------------------------------------------
    def start_search(self):
        query = self.search_entry.get().strip()
        if not query:
            messagebox.showwarning("Warning", "Please enter a search term.")
            return

        self.status_label.config(text="Searching...")
        self.clear_results()
        thread = Thread(target=self.fetch_books, args=(query,), daemon=True)
        thread.start()

    # -------------------------------------------------
    # API CALL
    # -------------------------------------------------
    def fetch_books(self, query):
        try:
            params = {
                "q": query,
                "maxResults": 20,
            }
            response = requests.get(GOOGLE_BOOKS_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            items = data.get("items", [])
            if not items:
                self.status_label.config(text="No books found.")
                return

            self.books = items
            self.populate_results()
            self.status_label.config(text=f"Found {len(items)} result(s).")

        except Exception as e:
            self.status_label.config(text="Failed to fetch books.")
            messagebox.showerror("Error", "An error occurred while fetching books.")
            print("Error:", e)

    # -------------------------------------------------
    # RESULTS HANDLING
    # -------------------------------------------------
    def clear_results(self):
        self.results_list.delete(0, tk.END)
        self.books = []
        self.clear_display()

    def populate_results(self):
        self.results_list.delete(0, tk.END)
        for item in self.books:
            volume = item.get("volumeInfo", {})
            title = volume.get("title", "Unknown Title")
            authors = volume.get("authors", [])
            authors_str = ", ".join(authors) if authors else "Unknown Author"
            self.results_list.insert(tk.END, f"{title} — {authors_str}")

    def on_book_select(self, event):
        if not self.results_list.curselection():
            return

        index = self.results_list.curselection()[0]
        if index >= len(self.books):
            return

        book_data = self.books[index]
        self.display_book(book_data)

    # -------------------------------------------------
    # DISPLAY HELPERS
    # -------------------------------------------------
    def clear_display(self):
        self.cover_label.config(image="", text="")
        self.current_cover = None
        self.set_info_text("")

    def set_info_text(self, text):
        self.info_text.config(state="normal")
        self.info_text.delete("1.0", tk.END)
        self.info_text.insert("1.0", text)
        self.info_text.config(state="disabled")

    def display_book(self, book_data):
        volume = book_data.get("volumeInfo", {})

        title = volume.get("title", "N/A")
        subtitle = volume.get("subtitle", "")
        authors = volume.get("authors", [])
        authors_str = ", ".join(authors) if authors else "N/A"
        published = volume.get("publishedDate", "N/A")
        categories = volume.get("categories", [])
        categories_str = ", ".join(categories) if categories else "N/A"
        page_count = volume.get("pageCount", "N/A")
        language = volume.get("language", "N/A")
        description = volume.get("description", "No description available.")
        publisher = volume.get("publisher", "N/A")
        rating = volume.get("averageRating", "N/A")
        ratings_count = volume.get("ratingsCount", 0)

        lines = []
        lines.append(f"Title: {title}")
        if subtitle:
            lines.append(f"Subtitle: {subtitle}")
        lines.append(f"Authors: {authors_str}")
        lines.append(f"Publisher: {publisher}")
        lines.append(f"Published: {published}")
        lines.append(f"Categories: {categories_str}")
        lines.append(f"Pages: {page_count}")
        lines.append(f"Language: {language}")
        lines.append(f"Average Rating: {rating} ({ratings_count} rating(s))")
        lines.append("")
        lines.append("Description:")
        lines.append(description)

        self.set_info_text("\n".join(lines))

        # Cover image
        image_links = volume.get("imageLinks", {})
        thumbnail = (
            image_links.get("thumbnail")
            or image_links.get("smallThumbnail")
        )

        if thumbnail:
            try:
                img_response = requests.get(thumbnail, timeout=10)
                img_response.raise_for_status()
                img_data = Image.open(BytesIO(img_response.content))
                img_data = img_data.resize((260, 360))
                self.current_cover = ImageTk.PhotoImage(img_data)
                self.cover_label.config(image=self.current_cover, text="")
            except Exception as e:
                print("Cover load error:", e)
                self.cover_label.config(text="No cover available.", image="")
                self.current_cover = None
        else:
            self.cover_label.config(text="No cover available.", image="")
            self.current_cover = None


if __name__ == "__main__":
    app = BookFinderApp()
    app.mainloop()
