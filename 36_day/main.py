import tkinter as tk
from tkinter import ttk
import requests
from threading import Thread
import xml.etree.ElementTree as ET
import webbrowser


RSS_FEEDS = {
    "BBC News": "https://feeds.bbci.co.uk/news/rss.xml",
    "Reuters World": "https://feeds.reuters.com/reuters/worldNews",
    "ABC Top Stories": "https://abcnews.go.com/abcnews/topstories"
}


class NewsFlash(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("NewsFlash – Live Headlines Reader")
        self.geometry("900x600")
        self.config(bg="#F5F5F5")

        self.create_layout()

    # ---------------------------------------------------
    # Layout Setup
    # ---------------------------------------------------
    def create_layout(self):

        title = tk.Label(self, text="NewsFlash – Live News Reader",
                         font=("Arial", 24, "bold"), bg="#F5F5F5")
        title.pack(pady=15)

        # Feed Selection
        feed_frame = tk.Frame(self, bg="#F5F5F5")
        feed_frame.pack(pady=10)

        tk.Label(feed_frame, text="Select News Source:",
                 font=("Arial", 14), bg="#F5F5F5").grid(row=0, column=0, padx=10)

        self.feed_select = ttk.Combobox(
            feed_frame, width=30, font=("Arial", 12),
            values=list(RSS_FEEDS.keys()),
            state="readonly"
        )
        self.feed_select.grid(row=0, column=1, padx=10)
        self.feed_select.set("BBC News")

        load_btn = tk.Button(feed_frame, text="Load Headlines",
                             font=("Arial", 12), command=self.start_fetch)
        load_btn.grid(row=0, column=2, padx=10)

        # News Display
        self.news_frame = tk.Frame(self, bg="#F5F5F5")
        self.news_frame.pack(pady=20, fill="both", expand=True)

        self.status_label = tk.Label(self, text="", font=("Arial", 12), bg="#F5F5F5")
        self.status_label.pack(pady=5)

    # ---------------------------------------------------
    # Threaded Fetch
    # ---------------------------------------------------
    def start_fetch(self):
        Thread(target=self.fetch_news, daemon=True).start()

    # ---------------------------------------------------
    # Fetch and Parse RSS
    # ---------------------------------------------------
    def fetch_news(self):
        feed_name = self.feed_select.get()
        feed_url = RSS_FEEDS[feed_name]

        self.status_label.config(text="Loading news...")
        self.clear_news()

        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(feed_url, headers=headers, timeout=10)
            response.raise_for_status()

            root = ET.fromstring(response.content)
            items = root.findall(".//item")

            if not items:
                self.status_label.config(text="No news found.")
                return

            for item in items[:10]:  # Show top 10
                title = item.find("title").text if item.find("title") is not None else "No title"
                link = item.find("link").text if item.find("link") is not None else ""

                self.add_news_card(title, link)

            self.status_label.config(text="Loaded successfully.")

        except Exception:
            self.status_label.config(text="Failed to load news.")

    # ---------------------------------------------------
    # Add clickable news card
    # ---------------------------------------------------
    def add_news_card(self, title, link):
        frame = tk.Frame(self.news_frame, bg="#FFFFFF", bd=1, relief="solid")
        frame.pack(fill="x", padx=20, pady=8)

        lbl = tk.Label(frame, text=title, font=("Arial", 14, "bold"),
                       bg="#FFFFFF", wraplength=750, justify="left", anchor="w")
        lbl.pack(padx=10, pady=5)

        if link:
            btn = tk.Button(frame, text="Open Link", font=("Arial", 12),
                            command=lambda url=link: webbrowser.open(url))
            btn.pack(pady=5)

    # ---------------------------------------------------
    # Utility: Clear old headlines
    # ---------------------------------------------------
    def clear_news(self):
        for widget in self.news_frame.winfo_children():
            widget.destroy()


# ---------------------------------------------------
# Run App
# ---------------------------------------------------
if __name__ == "__main__":
    app = NewsFlash()
    app.mainloop()
