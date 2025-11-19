import tkinter as tk
from tkinter import ttk, messagebox
import requests
from threading import Thread


class FXDesk(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("FXDesk – Real-Time Currency Converter")
        self.geometry("600x400")
        self.config(bg="#F5F5F5")

        self.rates = {}
        self.base_currency = "USD"

        self.create_layout()
        self.load_rates()

    # ---------------------------------------------------
    # Layout
    # ---------------------------------------------------
    def create_layout(self):
        title = tk.Label(
            self,
            text="FXDesk – Currency Converter",
            font=("Arial", 22, "bold"),
            bg="#F5F5F5"
        )
        title.pack(pady=15)

        form_frame = tk.Frame(self, bg="#F5F5F5")
        form_frame.pack(pady=20)

        tk.Label(form_frame, text="From", font=("Arial", 14), bg="#F5F5F5").grid(row=0, column=0, padx=10)
        tk.Label(form_frame, text="Amount", font=("Arial", 14), bg="#F5F5F5").grid(row=0, column=1, padx=10)
        tk.Label(form_frame, text="To", font=("Arial", 14), bg="#F5F5F5").grid(row=0, column=2, padx=10)

        self.from_currency = ttk.Combobox(form_frame, width=10, font=("Arial", 12), state="readonly")
        self.from_currency.grid(row=1, column=0, padx=10)

        self.amount_entry = tk.Entry(form_frame, width=10, font=("Arial", 12))
        self.amount_entry.grid(row=1, column=1, padx=10)

        self.to_currency = ttk.Combobox(form_frame, width=10, font=("Arial", 12), state="readonly")
        self.to_currency.grid(row=1, column=2, padx=10)

        convert_btn = tk.Button(
            self,
            text="Convert",
            width=20,
            font=("Arial", 14),
            command=self.start_conversion
        )
        convert_btn.pack(pady=10)

        self.result_label = tk.Label(self, text="", font=("Arial", 18, "bold"), bg="#F5F5F5")
        self.result_label.pack(pady=20)

        self.status_label = tk.Label(
            self,
            text="Loading exchange rates...",
            font=("Arial", 12),
            bg="#F5F5F5"
        )
        self.status_label.pack(pady=5)

    # ---------------------------------------------------
    # Load exchange rates
    # ---------------------------------------------------
    def load_rates(self):
        Thread(target=self.fetch_rates, daemon=True).start()

    def fetch_rates(self):
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            url = f"https://open.er-api.com/v6/latest/{self.base_currency}"

            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            data = response.json()

            if data["result"] != "success":
                raise ValueError("API error")

            self.rates = data["rates"]
            currency_list = sorted(self.rates.keys())

            self.from_currency["values"] = currency_list
            self.to_currency["values"] = currency_list

            self.from_currency.set("USD")
            self.to_currency.set("INR")

            self.status_label.config(text="Exchange rates loaded.")
        except:
            self.status_label.config(text="Failed to load exchange rates.")

    # ---------------------------------------------------
    # Conversion logic
    # ---------------------------------------------------
    def start_conversion(self):
        Thread(target=self.convert_currency, daemon=True).start()

    def convert_currency(self):
        try:
            amount = float(self.amount_entry.get())
            from_cur = self.from_currency.get()
            to_cur = self.to_currency.get()

            if not from_cur or not to_cur:
                messagebox.showerror("Error", "Select currencies before converting.")
                return

            if from_cur not in self.rates or to_cur not in self.rates:
                messagebox.showerror("Error", "Invalid currency.")
                return

            # Convert amount to USD base
            usd_value = amount / self.rates[from_cur]
            converted = usd_value * self.rates[to_cur]

            result_text = f"{amount} {from_cur} = {converted:.2f} {to_cur}"
            self.result_label.config(text=result_text)

        except ValueError:
            messagebox.showerror("Error", "Enter a valid number.")
        except Exception:
            messagebox.showerror("Error", "Conversion failed.")


# ---------------------------------------------------
# Run App
# ---------------------------------------------------
if __name__ == "__main__":
    app = FXDesk()
    app.mainloop()
