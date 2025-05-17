# 🎓 Training Management System (TMS)

*A complete desktop application for managing student training records, reports, evaluations, and performance analytics — built with Python (Tkinter) and MySQL.*

---

## 📖 **Project Overview**

The Training Management System (TMS) is designed to streamline the process of managing internship and training data in educational institutions. This system offers a secure login, user-friendly interface, Excel import/export functionality, and real-time evaluation insights — all through a modern Python-based GUI.

Built for administrators and coordinators, TMS handles every step of training documentation, from student onboarding to supervisor evaluations, providing transparency and data accuracy.

---

## 📌 **Key Features**

### **1. Student Management**

* Add new students manually or upload in bulk from Excel files.
* Validate student data fields (ID, name, CGPA, enrollment year).
* Clean UI forms for smooth data entry.

### **2. Report Submission**

* Link training reports to students and organizations.
* Record date-stamped reports using a guided input form.
* Store and manage text-based summaries from interns.

### **3. Evaluation Tracking**

* Add evaluation records with score, supervisor ID, date, and comments.
* Use dropdowns populated from the database for consistency.
* Automatically assign unique evaluation IDs.

### **4. Admin Dashboard**

* Centralized dashboard with navigation sidebar.
* Apply filters by organization and score range.
* Search functionality and sorting built-in.

### **5. Analytics & Export**

* Run stored procedures to calculate average student performance.
* Export full reports to Excel with one click.
* Visual feedback with dialogs and alerts.

### **6. Help & Manual**

* Embedded usage manual for uploading files.
* Simple instructions for new users.

---

## 🧩 **Tech Stack**

* **Frontend**: Python + Tkinter (GUI)
* **Backend**: MySQL (Relational Database)
* **Data Handling**: Pandas
* **File Operations**: Excel (xlsx/xls)
* **Visual Assets**: Pillow (Logo rendering)

---

## 🚀 **Getting Started**

### **1. Prerequisites**

* Python 3.8 or later
* MySQL Server (with database `training_mm`)
* pip (Python package manager)

### **2. Installation**

```bash
git clone https://github.com/yourusername/training-management-system.git
cd training-management-system
pip install -r requirements.txt
```

### **3. Database Setup**

* Create a database named `training_mm`
* Run your schema SQL file to create tables:

  * `students`, `organizations`, `internal_supervisors`, `external_supervisors`, `training_reports`, `evaluations`, `users`
* Create the stored procedure `GetStudentEvaluationAvg` for average score.

### **4. Run the App**

```bash
python main.py
```

---

## 📂 **Repository Structure**

```
training-management-system/
├── main.py
├── dashboard.py
├── admin_panel.py
├── insert_student_form.py
├── insert_report_form.py
├── insert_evaluation_form.py
├── upload_students_gui.py
├── call_procedure_avg.py
├── report_export.py
├── manual_use.py
├── db_connection.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📸 **Screenshots** *(Optional Section — add if available)*

You can include:

* Login screen
* Main dashboard
* Report form
* Admin panel with filters

---

## 🤝 **Contributing**

Contributions are welcome! You can:

* Report bugs or issues
* Suggest new features
* Submit pull requests with improvements

---

## 📜 **License**

MIT License – see `LICENSE` file for full text.

---

Would you like me to generate this as a downloadable `README.md` file for you right now?
