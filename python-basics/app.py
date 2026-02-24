from tkinter import *

def hello():
    print("Hello from Michael")

root = Tk()
root.geometry("600x600")

frame_one = Frame(root)
frame_one.pack()

button_one = Button(frame_one, text= "Say Hello", command= hello)
button_one.pack()

root.mainloop()

import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

# ------------------ SAMPLE PRODUCTS ------------------
products = {
    "Sugar": 120,
    "Milk": 60,
    "Bread": 55,
    "Rice": 150,
    "Soap": 80
}

cart = {}

# ------------------ FUNCTIONS ------------------

def add_to_cart():
    product = product_var.get()
    quantity = quantity_entry.get()

    if product == "" or quantity == "":
        messagebox.showwarning("Warning", "Select product and enter quantity")
        return

    quantity = int(quantity)

    if product in cart:
        cart[product] += quantity
    else:
        cart[product] = quantity

    update_cart()


def update_cart():
    cart_list.delete(0, tk.END)
    total = 0

    for product, quantity in cart.items():
        price = products[product]
        subtotal = price * quantity
        total += subtotal
        cart_list.insert(tk.END, f"{product} x{quantity} = Ksh {subtotal}")

    total_label.config(text=f"Total: Ksh {total}")


def remove_item():
    selected = cart_list.curselection()
    if not selected:
        return

    item_text = cart_list.get(selected)
    product = item_text.split(" x")[0]

    del cart[product]
    update_cart()


def clear_cart():
    cart.clear()
    update_cart()


def checkout():
    if not cart:
        messagebox.showwarning("Warning", "Cart is empty")
        return

    total = 0
    receipt_text = "------ SUPERMARKET RECEIPT ------\n"
    receipt_text += f"Date: {datetime.now()}\n\n"

    for product, quantity in cart.items():
        price = products[product]
        subtotal = price * quantity
        total += subtotal
        receipt_text += f"{product} x{quantity} = Ksh {subtotal}\n"

    receipt_text += "\n------------------------------\n"
    receipt_text += f"TOTAL: Ksh {total}\n"
    receipt_text += "Thank you for shopping!\n"

    # Save to CSV
    with open("sales.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), total])

    receipt_window = tk.Toplevel(root)
    receipt_window.title("Receipt")

    receipt_label = tk.Text(receipt_window, width=40, height=20)
    receipt_label.pack()
    receipt_label.insert(tk.END, receipt_text)

    cart.clear()
    update_cart()


# ------------------ GUI ------------------

root = tk.Tk()
root.title("Supermarket POS System")
root.geometry("500x500")

tk.Label(root, text="Select Product").pack()

product_var = tk.StringVar()
product_menu = tk.OptionMenu(root, product_var, *products.keys())
product_menu.pack()

tk.Label(root, text="Quantity").pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

tk.Button(root, text="Add to Cart", command=add_to_cart).pack(pady=5)

cart_list = tk.Listbox(root, width=50)
cart_list.pack(pady=10)

total_label = tk.Label(root, text="Total: Ksh 0", font=("Arial", 14))
total_label.pack()

tk.Button(root, text="Remove Selected Item", command=remove_item).pack(pady=5)
tk.Button(root, text="Clear Cart", command=clear_cart).pack(pady=5)
tk.Button(root, text="Checkout", command=checkout, bg="green", fg="white").pack(pady=10)

root.mainloop()