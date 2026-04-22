import tkinter as tk

from tkinter import messagebox

import sqlite3

# ===============================

# Деректер базасы

# ===============================

conn = sqlite3.connect("library.db")

cursor = conn.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS books (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT NOT NULL

)

""")

conn.commit()

# ===============================

# Функциялар

# ===============================

def add_book():

    title = entry.get()

    if title == "":

        messagebox.showwarning("Ескерту", "Кітап атауын енгізіңіз!")

        return

    

    cursor.execute("INSERT INTO books (title) VALUES (?)", (title,))

    conn.commit()

    entry.delete(0, tk.END)

    show_books()

def delete_book():

    selected = listbox.curselection()

    if not selected:

        return

    

    book = listbox.get(selected[0])

    cursor.execute("DELETE FROM books WHERE title=?", (book,))

    conn.commit()

    show_books()

def show_books():

    listbox.delete(0, tk.END)

    cursor.execute("SELECT title FROM books")

    books = cursor.fetchall()

    

    for book in books:

        listbox.insert(tk.END, book[0])

def search_book():

    keyword = entry.get()

    listbox.delete(0, tk.END)

    

    cursor.execute("SELECT title FROM books WHERE title LIKE ?", ('%' + keyword + '%',))

    results = cursor.fetchall()

    

    for book in results:

        listbox.insert(tk.END, book[0])

# ===============================

# GUI

# ===============================

root = tk.Tk()

root.title("GUI Кітапхана Жүйесі")

root.geometry("400x400")

label = tk.Label(root, text="Кітап атауы:")

label.pack()

entry = tk.Entry(root, width=40)

entry.pack(pady=5)

btn_add = tk.Button(root, text="Кітап қосу", command=add_book)

btn_add.pack(pady=5)

btn_delete = tk.Button(root, text="Кітап өшіру", command=delete_book)

btn_delete.pack(pady=5)

btn_search = tk.Button(root, text="Іздеу", command=search_book)

btn_search.pack(pady=5)

btn_show = tk.Button(root, text="Барлығын көрсету", command=show_books)

btn_show.pack(pady=5)

listbox = tk.Listbox(root, width=50, height=10)

listbox.pack(pady=10)

show_books()

root.mainloop()
