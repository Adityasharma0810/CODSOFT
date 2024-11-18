import tkinter as tk
from tkinter import messagebox

# Functions
def clear_fields():
    name_var.set("")
    phone_var.set("")
    email_var.set("")
    address_var.set("")

def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()
    address = address_var.get()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone are required!")
        return

    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
    clear_fields()
    refresh_contact_list()

def refresh_contact_list():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details['Phone']}")

def view_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "No contact selected!")
        return

    name = list(contacts.keys())[selected[0]]
    details = contacts[name]
    name_var.set(name)
    phone_var.set(details["Phone"])
    email_var.set(details["Email"])
    address_var.set(details["Address"])

def update_contact():
    name = name_var.get()

    if name not in contacts:
        messagebox.showerror("Update Error", "Contact not found!")
        return

    contacts[name] = {
        "Phone": phone_var.get(),
        "Email": email_var.get(),
        "Address": address_var.get(),
    }
    messagebox.showinfo("Success", f"Contact '{name}' updated successfully!")
    clear_fields()
    refresh_contact_list()

def delete_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "No contact selected!")
        return

    name = list(contacts.keys())[selected[0]]
    del contacts[name]
    messagebox.showinfo("Success", f"Contact '{name}' deleted successfully!")
    clear_fields()
    refresh_contact_list()

def search_contact():
    query = search_var.get().lower()
    results = {name: details for name, details in contacts.items() if query in name.lower() or query in details["Phone"]}

    contact_list.delete(0, tk.END)
    for name, details in results.items():
        contact_list.insert(tk.END, f"{name} - {details['Phone']}")

# Data
contacts = {}

# GUI
root = tk.Tk()
root.title("Contact Manager")
root.geometry("600x400")

# Input fields
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
name_var = tk.StringVar()
tk.Entry(frame, textvariable=name_var).grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
phone_var = tk.StringVar()
tk.Entry(frame, textvariable=phone_var).grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Email:").grid(row=2, column=0, padx=5, pady=5)
email_var = tk.StringVar()
tk.Entry(frame, textvariable=email_var).grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="Address:").grid(row=3, column=0, padx=5, pady=5)
address_var = tk.StringVar()
tk.Entry(frame, textvariable=address_var).grid(row=3, column=1, padx=5, pady=5)

# Buttons
tk.Button(frame, text="Add Contact", command=add_contact).grid(row=4, column=0, pady=10)
tk.Button(frame, text="Update Contact", command=update_contact).grid(row=4, column=1, pady=10)

# Contact list and actions
list_frame = tk.Frame(root)
list_frame.pack(pady=10)

contact_list = tk.Listbox(list_frame, width=50, height=10)
contact_list.pack(side=tk.LEFT, padx=5)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

contact_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=contact_list.yview)

tk.Button(root, text="View Contact", command=view_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

# Search functionality
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

tk.Label(search_frame, text="Search:").pack(side=tk.LEFT, padx=5)
search_var = tk.StringVar()
tk.Entry(search_frame, textvariable=search_var).pack(side=tk.LEFT, padx=5)
tk.Button(search_frame, text="Search", command=search_contact).pack(side=tk.LEFT, padx=5)

refresh_contact_list()
root.mainloop()
