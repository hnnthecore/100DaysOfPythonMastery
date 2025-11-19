import tkinter as tk
import requests
import time
from datetime import datetime
from threading import Thread


# ---------------------------------------------
# FocusFrame: Productivity Dashboard
# ---------------------------------------------
class FocusFrame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("FocusFrame – Productivity Dashboard")
        self.geometry("900x600")
        self.config(bg="#F5F5F5")

        self.create_layout()
        self.update_clock()
        self.fetch_quote()
        self.fetch_weather()

    # ---------------------------------------------
    # Layout Setup
    # ---------------------------------------------
    def create_layout(self):

        # Left Column (To-Do + Timer)
        left_frame = tk.Frame(self, bg="#FFFFFF", width=300, height=600)
        left_frame.pack(side="left", fill="y")

        # Right Column (Clock + Quotes + Weather)
        right_frame = tk.Frame(self, bg="#F5F5F5")
        right_frame.pack(side="right", expand=True, fill="both")

        # To-Do List Section
        todo_label = tk.Label(left_frame, text="To-Do List", font=("Arial", 16, "bold"), bg="#FFFFFF")
        todo_label.pack(pady=10)

        self.todo_box = tk.Listbox(left_frame, width=30, height=15, font=("Arial", 12))
        self.todo_box.pack(pady=5)

        self.todo_entry = tk.Entry(left_frame, width=25, font=("Arial", 12))
        self.todo_entry.pack(pady=5)

        add_btn = tk.Button(left_frame, text="Add Task", width=20, command=self.add_task)
        add_btn.pack(pady=2)

        del_btn = tk.Button(left_frame, text="Delete Selected", width=20, command=self.delete_task)
        del_btn.pack(pady=5)

        # Pomodoro Timer Section
        timer_label = tk.Label(left_frame, text="Pomodoro Timer", font=("Arial", 16, "bold"), bg="#FFFFFF")
        timer_label.pack(pady=20)

        self.timer_display = tk.Label(left_frame, text="25:00", font=("Arial", 28, "bold"), bg="#FFFFFF")
        self.timer_display.pack(pady=10)

        start_btn = tk.Button(left_frame, text="Start Timer", width=20, command=self.start_pomodoro)
        start_btn.pack(pady=2)

        reset_btn = tk.Button(left_frame, text="Reset Timer", width=20, command=self.reset_pomodoro)
        reset_btn.pack(pady=5)

        # Clock section (Right)
        self.clock_label = tk.Label(right_frame, text="", font=("Arial", 36, "bold"), bg="#F5F5F5")
        self.clock_label.pack(pady=20)

        # Quote Section
        quote_title = tk.Label(right_frame, text="Daily Inspiration", font=("Arial", 16, "bold"), bg="#F5F5F5")
        quote_title.pack()

        self.quote_text = tk.Label(right_frame, text="Fetching quote...", wraplength=500,
                                   font=("Arial", 14), bg="#F5F5F5", justify="center")
        self.quote_text.pack(pady=10)

        # Weather Section
        weather_title = tk.Label(right_frame, text="Weather", font=("Arial", 16, "bold"), bg="#F5F5F5")
        weather_title.pack(pady=10)

        self.weather_label = tk.Label(right_frame, text="Loading weather...",
                                      font=("Arial", 14), bg="#F5F5F5")
        self.weather_label.pack()

    # ---------------------------------------------
    # To-Do Methods
    # ---------------------------------------------
    def add_task(self):
        task = self.todo_entry.get().strip()
        if task:
            self.todo_box.insert("end", task)
            self.todo_entry.delete(0, "end")

    def delete_task(self):
        selected = self.todo_box.curselection()
        if selected:
            self.todo_box.delete(selected)

    # ---------------------------------------------
    # Pomodoro Timer
    # ---------------------------------------------
    pomodoro_time = 25 * 60
    timer_running = False

    def start_pomodoro(self):
        if not self.timer_running:
            self.timer_running = True
            Thread(target=self.run_timer, daemon=True).start()

    def run_timer(self):
        time_left = self.pomodoro_time
        while time_left >= 0 and self.timer_running:
            minutes = time_left // 60
            seconds = time_left % 60
            self.timer_display.config(text=f"{minutes:02d}:{seconds:02d}")
            time.sleep(1)
            time_left -= 1

        self.timer_running = False

    def reset_pomodoro(self):
        self.timer_running = False
        self.pomodoro_time = 25 * 60
        self.timer_display.config(text="25:00")

    # ---------------------------------------------
    # Live Clock
    # ---------------------------------------------
    def update_clock(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text=now)
        self.after(1000, self.update_clock)

    # ---------------------------------------------
    # Daily Quote (No API Key Required)
    # ---------------------------------------------
    def fetch_quote(self):
        def get_quote():
            try:
                response = requests.get("https://api.quotable.io/random", timeout=5)
                response.raise_for_status()
                data = response.json()
                quote = data["content"]
            except:
                quote = "Could not fetch quote."

            self.quote_text.config(text=quote)

        Thread(target=get_quote, daemon=True).start()

    # ---------------------------------------------
    # Weather Display (Public API without Key)
    # ---------------------------------------------
    def fetch_weather(self):
        def get_weather():
            url = "https://wttr.in/?format=j1"
            try:
                r = requests.get(url, timeout=5)
                r.raise_for_status()
                data = r.json()

                temp = data["current_condition"][0]["temp_C"]
                desc = data["current_condition"][0]["weatherDesc"][0]["value"]

                self.weather_label.config(
                    text=f"Temperature: {temp}°C\nCondition: {desc}"
                )

            except:
                self.weather_label.config(text="Weather unavailable.")

        Thread(target=get_weather, daemon=True).start()


# ---------------------------------------------
# Run App
# ---------------------------------------------
if __name__ == "__main__":
    app = FocusFrame()
    app.mainloop()
