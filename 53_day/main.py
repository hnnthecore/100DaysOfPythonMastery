import tkinter as tk
from tkinter import messagebox
import requests
import json
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


API_URL = "https://wttr.in/{}?format=j1"
CACHE_FILE = "day53_cache.json"


class WeatherSphere:
    def __init__(self, root):
        self.root = root
        self.root.title("Day 53 - WeatherSphere: Weather Dashboard")
        self.root.geometry("900x600")
        self.root.config(bg="#eef2f3")

        self.build_ui()
        self.load_cached_weather()

    def build_ui(self):
        top = tk.Frame(self.root, bg="#eef2f3")
        top.pack(pady=10)

        tk.Label(top, text="Enter City:", font=("Arial", 14), bg="#eef2f3").pack(side="left", padx=10)

        self.city_entry = tk.Entry(top, font=("Arial", 14), width=25)
        self.city_entry.pack(side="left")

        tk.Button(top, text="Get Weather", font=("Arial", 12),
                  command=self.get_weather).pack(side="left", padx=10)

        self.info_label = tk.Label(self.root, text="", font=("Arial", 16, "bold"), bg="#eef2f3")
        self.info_label.pack(pady=10)

        self.fig, self.ax = plt.subplots(figsize=(6, 3))
        self.chart_canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.chart_canvas.get_tk_widget().pack(pady=10)

    def load_cached_weather(self):
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "r") as f:
                data = json.load(f)
            self.display_weather(data, cached=True)

    def get_weather(self):
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showerror("Error", "Enter a city name.")
            return

        try:
            response = requests.get(API_URL.format(city))
            data = response.json()

            with open(CACHE_FILE, "w") as f:
                json.dump(data, f, indent=4)

            self.display_weather(data)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch weather.\n{e}")

    def display_weather(self, data, cached=False):
        current = data["current_condition"][0]
        temp = current["temp_C"]
        humidity = current["humidity"]
        wind = current["windspeedKmph"]

        status = "CACHED RESULT" if cached else "LIVE DATA"

        self.info_label.config(
            text=f"{status} | Temp: {temp}°C  | Humidity: {humidity}%  | Wind: {wind} km/h"
        )

        forecast = data["weather"]
        days = ["Today", "Tomorrow", "Day 3"]
        temps = [int(f["avgtempC"]) for f in forecast[:3]]

        self.ax.clear()
        self.ax.bar(days, temps, color=["#ffab91", "#81d4fa", "#a5d6a7"])
        self.ax.set_title("3-Day Temperature Forecast")
        self.ax.set_ylabel("°C")

        self.chart_canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    WeatherSphere(root)
    root.mainloop()
