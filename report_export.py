# report_export.py

import pandas as pd
from tkinter import messagebox
from db_connection import connect_to_db  # ✅ Corrected import

def export_reports():
    try:
        conn = connect_to_db()  # ✅ Corrected function name
        cursor = conn.cursor()
        query = """
            SELECT s.student_name, o.organization_name, tr.report_text, e.evaluation_score, e.evaluation_comments
            FROM students s
            JOIN training_reports tr ON s.student_id = tr.student_id
            JOIN organizations o ON tr.organization_id = o.organization_id
            JOIN evaluations e ON tr.report_id = e.report_id
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = ['Student Name', 'Organization', 'Report', 'Score', 'Comments']
        df = pd.DataFrame(rows, columns=columns)
        df.to_excel("exported_reports.xlsx", index=False)
        messagebox.showinfo("Export Complete", "Report saved as exported_reports.xlsx")
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to export reports: {e}")
