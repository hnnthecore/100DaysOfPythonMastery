import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
import os

FILE_NAME = "passwords.json"


def load_data():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


def add_password():
    site = site_entry.get().strip()
    username = user_entry.get().strip()
    password = pass_entry.get().strip()

    if not site or not username or not password:
        messagebox.showerror("Error", "All fields are required")
        return

    data = load_data()
    data[site] = {
        "username": username,
        "password": password
    }
    save_data(data)
    refresh_list()
    site_entry.delete(0, tk.END)
    user_entry.delete(0, tk.END)
    pass_entry.delete(0, tk.END)


def show_password():
    selected = listbox.get(tk.ACTIVE)
    if not selected:
        return

    data = load_data()
    creds = data[selected]
    messagebox.showinfo(
        "Saved Credentials",
        f"Site: {selected}\nUsername: {creds['username']}\nPassword: {creds['password']}"
    )


def refresh_list():
    listbox.delete(0, tk.END)
    data = load_data()
    for site in sorted(data.keys()):
        listbox.insert(tk.END, site)


root = tk.Tk()
root.title("Password Manager")
root.geometry("400x420")
root.resizable(False, False)

frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Website").pack(anchor="w")
site_entry = ttk.Entry(frame)
site_entry.pack(fill="x", pady=5)

ttk.Label(frame, text="Username").pack(anchor="w")
user_entry = ttk.Entry(frame)
user_entry.pack(fill="x", pady=5)

ttk.Label(frame, text="Password").pack(anchor="w")
pass_entry = ttk.Entry(frame, show="*")
pass_entry.pack(fill="x", pady=5)

ttk.Button(frame, text="Save Password", command=add_password).pack(pady=10)

ttk.Label(frame, text="Saved Sites").pack(anchor="w", pady=(10, 0))
listbox = tk.Listbox(frame, height=8)
listbox.pack(fill="both", expand=True, pady=5)

ttk.Button(frame, text="View Selected", command=show_password).pack(pady=5)

refresh_list()
root.mainloop()
