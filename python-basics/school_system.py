import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from datetime import datetime

FILE_NAME = "students.csv"

# Create CSV file if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Course", "Phone", "Grade"])


# ---------------- FUNCTIONS ---------------- #

def register_student():
    student_id = entry_id.get()
    name = entry_name.get()
    course = entry_course.get()
    phone = entry_phone.get()

    if student_id == "" or name == "":
        messagebox.showerror("Error", "ID and Name are required!")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == student_id:
                messagebox.showerror("Error", "Student already exists!")
                return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, course, phone, ""])

    messagebox.showinfo("Success", "Student Registered!")
    clear_fields()
    display_students()


def display_students():
    for row in tree.get_children():
        tree.delete(row)

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            tree.insert("", tk.END, values=row)


def update_course():
    update_column(2, entry_course.get(), "Course Updated!")


def assign_grade():
    update_column(4, entry_grade.get(), "Grade Assigned!")


def update_column(column_index, new_value, success_message):
    student_id = entry_id.get()
    rows = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == student_id:
                row[column_index] = new_value
                found = True
            rows.append(row)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        messagebox.showinfo("Success", success_message)
        display_students()
    else:
        messagebox.showerror("Error", "Student Not Found!")


def delete_student():
    student_id = entry_id.get()
    rows = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] != student_id:
                rows.append(row)
            else:
                found = True

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        messagebox.showinfo("Success", "Student Deleted!")
        clear_fields()
        display_students()
    else:
        messagebox.showerror("Error", "Student Not Found!")


def search_student():
    search_id = entry_id.get()

    for row in tree.get_children():
        tree.delete(row)

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] == search_id:
                tree.insert("", tk.END, values=row)


def export_to_text():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

        if len(rows) <= 1:
            messagebox.showwarning("Warning", "No data to export!")
            return

        filename = f"students_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        with open(filename, "w") as txt_file:
            txt_file.write("SCHOOL MANAGEMENT SYSTEM REPORT\n")
            txt_file.write("=" * 60 + "\n")
            txt_file.write(f"Generated: {datetime.now()}\n\n")

            headers = rows[0]
            txt_file.write("{:<10} {:<15} {:<15} {:<15} {:<10}\n".format(*headers))
            txt_file.write("-" * 70 + "\n")

            for row in rows[1:]:
                txt_file.write("{:<10} {:<15} {:<15} {:<15} {:<10}\n".format(*row))

        messagebox.showinfo("Success", f"Exported successfully as {filename}")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def clear_fields():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_course.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_grade.delete(0, tk.END)


def select_row(event):
    selected = tree.focus()
    values = tree.item(selected, "values")

    if values:
        clear_fields()
        entry_id.insert(0, values[0])
        entry_name.insert(0, values[1])
        entry_course.insert(0, values[2])
        entry_phone.insert(0, values[3])
        entry_grade.insert(0, values[4])


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("School Management System")
root.geometry("1000x600")

title = tk.Label(root, text="School Management System",
                 font=("Arial", 18, "bold"))
title.pack(pady=10)

form_frame = tk.Frame(root)
form_frame.pack(pady=10)

tk.Label(form_frame, text="Student ID").grid(row=0, column=0)
entry_id = tk.Entry(form_frame)
entry_id.grid(row=0, column=1)

tk.Label(form_frame, text="Name").grid(row=1, column=0)
entry_name = tk.Entry(form_frame)
entry_name.grid(row=1, column=1)

tk.Label(form_frame, text="Course").grid(row=2, column=0)
entry_course = tk.Entry(form_frame)
entry_course.grid(row=2, column=1)

tk.Label(form_frame, text="Phone").grid(row=3, column=0)
entry_phone = tk.Entry(form_frame)
entry_phone.grid(row=3, column=1)

tk.Label(form_frame, text="Grade").grid(row=4, column=0)
entry_grade = tk.Entry(form_frame)
entry_grade.grid(row=4, column=1)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Register", command=register_student).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Update Course", command=update_course).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Assign Grade", command=assign_grade).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Delete", command=delete_student).grid(row=0, column=3, padx=5)
tk.Button(button_frame, text="Search", command=search_student).grid(row=0, column=4, padx=5)
tk.Button(button_frame, text="Export to Text", command=export_to_text).grid(row=0, column=5, padx=5)
tk.Button(button_frame, text="Refresh", command=display_students).grid(row=0, column=6, padx=5)

# -------- TABLE -------- #

columns = ("ID", "Name", "Course", "Phone", "Grade")

tree_frame = tk.Frame(root)
tree_frame.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(tree_frame)
scrollbar.pack(side="right", fill="y")

tree = ttk.Treeview(tree_frame, columns=columns, show="headings",
                    yscrollcommand=scrollbar.set)

scrollbar.config(command=tree.yview)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack(fill="both", expand=True)

tree.bind("<ButtonRelease-1>", select_row)

display_students()

root.mainloop()