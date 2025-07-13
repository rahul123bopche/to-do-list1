import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

CONTACTS_FILE = "contacts.json"


# Load contacts from file or initialize an empty list
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []


def save_contacts():
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


# Add contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not name or not phone:
        messagebox.showerror("Error", "Name and phone are required.")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts()
    refresh_list()
    clear_entries()


# View all contacts
def refresh_list():
    contact_list.delete(0, tk.END)
    for i, c in enumerate(contacts):
        contact_list.insert(tk.END, f"{i + 1}. {c['name']} - {c['phone']}")


# Search contacts
def search_contact():
    query = search_entry.get().lower()
    contact_list.delete(0, tk.END)
    for i, c in enumerate(contacts):
        if query in c['name'].lower() or query in c['phone']:
            contact_list.insert(tk.END, f"{i + 1}. {c['name']} - {c['phone']}")


# Select and fill entries
def select_contact(event):
    try:
        index = contact_list.curselection()[0]
        selected = contacts[index]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, selected["name"])
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, selected["phone"])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, selected["email"])
        address_entry.delete(0, tk.END)
        address_entry.insert(0, selected["address"])
    except IndexError:
        pass


# Update selected contact
def update_contact():
    try:
        index = contact_list.curselection()[0]
        contacts[index] = {
            "name": name_entry.get(),
            "phone": phone_entry.get(),
            "email": email_entry.get(),
            "address": address_entry.get()
        }
        save_contacts()
        refresh_list()
        clear_entries()
    except IndexError:
        messagebox.showwarning("Select Contact", "Please select a contact to update.")


# Delete contact
def delete_contact():
    try:
        index = contact_list.curselection()[0]
        del contacts[index]
        save_contacts()
        refresh_list()
        clear_entries()
    except IndexError:
        messagebox.showwarning("Select Contact", "Please select a contact to delete.")


def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


# GUI Setup
app = tk.Tk()
app.title("Contact Management System")
app.geometry("600x400")

contacts = load_contacts()

# Input Fields
tk.Label(app, text="Name").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1)

tk.Label(app, text="Phone").grid(row=1, column=0, padx=10, pady=5)
phone_entry = tk.Entry(app)
phone_entry.grid(row=1, column=1)

tk.Label(app, text="Email").grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(app)
email_entry.grid(row=2, column=1)

tk.Label(app, text="Address").grid(row=3, column=0, padx=10, pady=5)
address_entry = tk.Entry(app)
address_entry.grid(row=3, column=1)

# Buttons
tk.Button(app, text="Add", command=add_contact).grid(row=0, column=2, padx=10)
tk.Button(app, text="Update", command=update_contact).grid(row=1, column=2)
tk.Button(app, text="Delete", command=delete_contact).grid(row=2, column=2)

# Search
tk.Label(app, text="Search").grid(row=4, column=0, padx=10, pady=5)
search_entry = tk.Entry(app)
search_entry.grid(row=4, column=1)
tk.Button(app, text="Search", command=search_contact).grid(row=4, column=2)

# Contact List
contact_list = tk.Listbox(app, width=50)
contact_list.grid(row=5, column=0, columnspan=3, pady=10)
contact_list.bind("<<ListboxSelect>>", select_contact)

refresh_list()

app.mainloop()
