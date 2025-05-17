import tkinter as tk
from tkinter import ttk, messagebox
from db_connection import connect_to_db

def open_insert_evaluation_form():
    window = tk.Toplevel()
    window.title("Add Evaluation")
    window.geometry("500x450")
    window.configure(bg="#f5f5f7")

    def center(win):
        sw, sh = win.winfo_screenwidth(), win.winfo_screenheight()
        win.geometry(f"500x450+{(sw - 500)//2}+{(sh - 450)//2}")

    center(window)

    ttk.Style().configure("TLabel", background="#f5f5f7", font=("Segoe UI", 10))
    ttk.Style().configure("TButton", font=("Segoe UI", 10, "bold"))

    ttk.Label(window, text="📄 Report ID").pack(pady=5)
    report_combo = ttk.Combobox(window, width=40)
    report_combo.pack()

    ttk.Label(window, text="🧑‍🏫 Supervisor ID").pack(pady=5)
    supervisor_combo = ttk.Combobox(window, width=40)
    supervisor_combo.pack()

    ttk.Label(window, text="📅 Evaluation Date (YYYY-MM-DD)").pack(pady=5)
    date_entry = ttk.Entry(window, width=40)
    date_entry.pack()

    ttk.Label(window, text="📊 Score (0–100)").pack(pady=5)
    score_entry = ttk.Entry(window, width=40)
    score_entry.pack()

    ttk.Label(window, text="💬 Comments").pack(pady=5)
    comments = tk.Text(window, height=4, width=50)
    comments.pack()

    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT report_id FROM training_reports")
        report_combo['values'] = [row[0] for row in cursor.fetchall()]
        cursor.execute("SELECT supervisor_id FROM internal_supervisors")
        supervisor_combo['values'] = [row[0] for row in cursor.fetchall()]
        conn.close()
    except Exception as e:
        messagebox.showerror("DB Error", str(e))
        window.destroy()
        return

    def submit():
        try:
            conn = connect_to_db()
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(evaluation_id) FROM evaluations")
            new_id = (cursor.fetchone()[0] or 0) + 1

            cursor.execute("""
                INSERT INTO evaluations (evaluation_id, report_id, supervisor_id, evaluation_date, evaluation_score, evaluation_comments)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                new_id,
                int(report_combo.get()),
                int(supervisor_combo.get()),
                date_entry.get(),
                float(score_entry.get()),
                comments.get("1.0", tk.END).strip()
            ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Evaluation inserted.")
            window.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(window, text="Submit Evaluation", command=submit).pack(pady=20)
