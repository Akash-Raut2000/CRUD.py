import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup
conn = sqlite3.connect("crud_app.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
conn.commit()

# CRUD functions
def refresh_list():
    listbox.delete(0, tk.END)
    for row in cursor.execute("SELECT * FROM users"):
        listbox.insert(tk.END, f"{row[0]} - {row[1]}")

def add_user():
    if entry_name.get():
        cursor.execute("INSERT INTO users (name) VALUES (?)", (entry_name.get(),))
        conn.commit()
        entry_name.delete(0, tk.END)
        refresh_list()

def update_user():
    if entry_id.get() and entry_name.get():
        cursor.execute("UPDATE users SET name = ? WHERE id = ?", (entry_name.get(), entry_id.get()))
        conn.commit()
        refresh_list()

def delete_user():
    if entry_id.get():
        cursor.execute("DELETE FROM users WHERE id = ?", (entry_id.get(),))
        conn.commit()
        refresh_list()

# GUI setup
app = tk.Tk()
app.title("CRUD App")

tk.Label(app, text="ID").grid(row=0, column=0)
entry_id = tk.Entry(app)
entry_id.grid(row=0, column=1)

tk.Label(app, text="Name").grid(row=1, column=0)
entry_name = tk.Entry(app)
entry_name.grid(row=1, column=1)

tk.Button(app, text="Add", command=add_user).grid(row=2, column=0)
tk.Button(app, text="Update", command=update_user).grid(row=2, column=1)
tk.Button(app, text="Delete", command=delete_user).grid(row=2, column=2)

listbox = tk.Listbox(app, width=40)
listbox.grid(row=3, column=0, columnspan=3)

refresh_list()
app.mainloop()
