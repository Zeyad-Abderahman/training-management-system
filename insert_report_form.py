import tkinter as tk
from tkinter import ttk, messagebox
from db_connection import connect_to_db

def open_insert_report_form():
    window = tk.Toplevel()
    window.title("Add Training Report")
    window.geometry("500x450")
    window.configure(bg="#f5f5f7")

    def center(win):
        sw, sh = win.winfo_screenwidth(), win.winfo_screenheight()
        ww, wh = 500, 450
        win.geometry(f"{ww}x{wh}+{(sw - ww) // 2}+{(sh - wh) // 2}")

    center(window)

    ttk.Style().configure("TLabel", background="#f5f5f7", font=("Segoe UI", 10))
    ttk.Style().configure("TButton", font=("Segoe UI", 10, "bold"))

    ttk.Label(window, text="👨‍🎓 Student ID").pack(pady=5)
    student_combo = ttk.Combobox(window, width=40)
    student_combo.pack()

    ttk.Label(window, text="🏢 Organization ID").pack(pady=5)
    org_combo = ttk.Combobox(window, width=40)
    org_combo.pack()

    ttk.Label(window, text="📅 Report Date (YYYY-MM-DD)").pack(pady=5)
    date_entry = ttk.Entry(window, width=40)
    date_entry.pack()

    ttk.Label(window, text="📝 Report Text").pack(pady=5)
    text_entry = tk.Text(window, height=5, width=50)
    text_entry.pack()

    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT student_id FROM students")
        student_combo['values'] = [row[0] for row in cursor.fetchall()]
        cursor.execute("SELECT organization_id FROM organizations")
        org_combo['values'] = [row[0] for row in cursor.fetchall()]
        conn.close()
    except Exception as e:
        messagebox.showerror("DB Error", str(e))
        window.destroy()
        return

    def submit():
        try:
            conn = connect_to_db()
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(report_id) FROM training_reports")
            new_id = (cursor.fetchone()[0] or 0) + 1

            cursor.execute("""
                INSERT INTO training_reports (report_id, student_id, organization_id, report_date, report_text)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                new_id,
                int(student_combo.get()),
                int(org_combo.get()),
                date_entry.get(),
                text_entry.get("1.0", tk.END).strip()
            ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Report added.")
            window.destroy()
        except Exception as e:
            messagebox.showerror("Insert Failed", str(e))

    ttk.Button(window, text="Submit Report", command=submit).pack(pady=20)
