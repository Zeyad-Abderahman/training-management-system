# insert_student_form.py

import tkinter as tk
from tkinter import messagebox
from db_connection import connect_to_db

def open_insert_student_form():
    window = tk.Toplevel()
    window.title("Add New Student")
    window.geometry("400x400")
    window.configure(bg="white")

    # UI Components
    tk.Label(window, text="Student ID", bg="white").pack(pady=5)
    id_entry = tk.Entry(window)
    id_entry.pack()

    tk.Label(window, text="Full Name", bg="white").pack(pady=5)
    name_entry = tk.Entry(window)
    name_entry.pack()

    tk.Label(window, text="Program", bg="white").pack(pady=5)
    program_entry = tk.Entry(window)
    program_entry.pack()

    tk.Label(window, text="Enrollment Year (2015-2025)", bg="white").pack(pady=5)
    year_entry = tk.Entry(window)
    year_entry.pack()

    tk.Label(window, text="CGPA (0.00 - 4.00)", bg="white").pack(pady=5)
    cgpa_entry = tk.Entry(window)
    cgpa_entry.pack()

    # Submit function
    def submit():
        try:
            student_id = int(id_entry.get())
            name = name_entry.get()
            program = program_entry.get()
            year = int(year_entry.get())
            cgpa = float(cgpa_entry.get())

            conn = connect_to_db()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO students (student_id, student_name, program, enrollment_year, cgpa)
                VALUES (%s, %s, %s, %s, %s)
            """, (student_id, name, program, year, cgpa))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Student added successfully!")
            window.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to insert student: {e}")

    # Submit Button
    tk.Button(window, text="Submit Student", command=submit, bg="#3498db", fg="white").pack(pady=20)

    window.mainloop()
