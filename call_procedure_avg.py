import tkinter as tk
from tkinter import messagebox
from db_connection import connect_to_db

def open_avg_score_form():  # <-- Make sure this is NOT indented
    window = tk.Toplevel()
    window.title("Get Student Average Score")
    window.geometry("300x200")

    tk.Label(window, text="Enter Student ID").pack(pady=10)
    student_id_entry = tk.Entry(window)
    student_id_entry.pack()

    def call_procedure():
        try:
            student_id = int(student_id_entry.get())

            conn = connect_to_db()
            cursor = conn.cursor()

            cursor.callproc('GetStudentEvaluationAvg', [student_id])

            for result in cursor.stored_results():
                row = result.fetchone()

            if row:
                name, avg_score = row
                messagebox.showinfo("Average Score", f"{name}'s average score: {avg_score:.2f}")
            else:
                messagebox.showwarning("No Data", "No evaluations found for this student.")

            conn.close()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch score: {e}")

    tk.Button(window, text="Get Average Score", command=call_procedure).pack(pady=20)
