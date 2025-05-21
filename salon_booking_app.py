import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime
import sqlite3

# Database setup
conn = sqlite3.connect("salon_bookings.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        service TEXT NOT NULL,
        stylist TEXT NOT NULL
    )
''')
conn.commit()

# Theme colors
PRIMARY_COLOR = "#9461b6"
DARKER_PRIMARY = "#7a4ca0"
LIGHT_BG = "#f3e9f9"
TEXT_COLOR = "#ffffff"
ENTRY_BG = "#e5d4f3"
ENTRY_FG = "#000000"

# Save booking
def save_booking():
    name = name_entry.get()
    date = date_entry.get()
    time = time_entry.get()
    service = service_combobox.get()
    stylist = stylist_combobox.get()

    if not name or not date or not time or not service or not stylist:
        messagebox.showerror("Input Error", "All fields must be filled.")
        return

    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        datetime.datetime.strptime(time, "%H:%M")
    except ValueError:
        messagebox.showerror("Format Error", "Use date YYYY-MM-DD and time HH:MM format.")
        return

    cursor.execute('''
        INSERT INTO bookings (name, date, time, service, stylist)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, date, time, service, stylist))
    conn.commit()

    clear_fields()
    load_bookings()

# Load and display bookings
def load_bookings():
    bookings_listbox.delete(0, tk.END)
    cursor.execute("SELECT name, date, time, service, stylist FROM bookings ORDER BY date, time")
    for row in cursor.fetchall():
        display = f"{row[1]} {row[2]} | {row[0]} | {row[3]} with {row[4]}"
        bookings_listbox.insert(tk.END, display)

# Clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    service_combobox.set("")
    stylist_combobox.set("")

# GUI setup
root = tk.Tk()
root.title("Smart Beauty Booking")
root.geometry("450x550")
root.configure(bg=LIGHT_BG)

# Styling
style = ttk.Style()
style.theme_use("default")
style.configure("TCombobox", fieldbackground=ENTRY_BG, background="white", foreground=ENTRY_FG)
style.map("TCombobox", fieldbackground=[('readonly', ENTRY_BG)])

# Title
tk.Label(root, text="Smart Beauty Booking", font=("Arial", 18, "bold"),
         bg=PRIMARY_COLOR, fg=TEXT_COLOR, pady=10).pack(fill=tk.X)

# UI Components
def add_label(text):
    return tk.Label(root, text=text, bg=LIGHT_BG, fg="#333", font=("Arial", 11))

def create_entry():
    return tk.Entry(root, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground="#333", relief="flat", font=("Arial", 11), bd=2)

add_label("Customer Name").pack(pady=(10, 0))
name_entry = create_entry()
name_entry.pack()

add_label("Date (YYYY-MM-DD)").pack(pady=(10, 0))
date_entry = create_entry()
date_entry.pack()

add_label("Time (HH:MM)").pack(pady=(10, 0))
time_entry = create_entry()
time_entry.pack()

add_label("Service").pack(pady=(10, 0))
service_combobox = ttk.Combobox(root, values=[
    "Haircut", "Hair Coloring", "Facial", "Manicure", "Pedicure", "Massage"
], font=("Arial", 11))
service_combobox.pack()

add_label("Stylist").pack(pady=(10, 0))
stylist_combobox = ttk.Combobox(root, values=[
    "Alex", "Jamie", "Taylor", "Sam"
], font=("Arial", 11))
stylist_combobox.pack()

# Book Button
book_btn = tk.Button(root, text="Book Appointment", command=save_booking,
                      font=("Arial", 12, "bold"),
                     
                     relief="flat", bd=0, padx=10, pady=8)
# book_btn = tk.Button(root, text="Book Appointment", command=save_booking,
#                      bg=PRIMARY_COLOR, fg=TEXT_COLOR, font=("Arial", 12, "bold"),
#                      activebackground=DARKER_PRIMARY, activeforeground=TEXT_COLOR,
#                      relief="flat", bd=0, padx=10, pady=8)
book_btn.pack(pady=20)

# Bookings List
add_label("Upcoming Bookings").pack(pady=(5, 0))
bookings_listbox = tk.Listbox(root, width=60, height=10, bg=ENTRY_BG, fg="#333", font=("Arial", 10))
bookings_listbox.pack(pady=(0, 10))

# Initial load
load_bookings()

# Run the app
root.mainloop()
