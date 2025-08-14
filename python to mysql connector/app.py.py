# Employee Management System with Gradio
# Run this in Google Colab - will provide a public link

!pip install gradio pandas sqlite3

import gradio as gr
import sqlite3
import pandas as pd

# Initialize database
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        emp_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        mobile TEXT,
        salary REAL,
        department TEXT,
        join_date TEXT
    )
''')
conn.commit()

# Sample data
sample_data = [
    ('EMP001', 'Alex Johnson', '555-0101', 75000, 'Engineering', '2023-01-15'),
    ('EMP002', 'Maria Garcia', '555-0102', 68000, 'Marketing', '2023-02-20')
]
cursor.executemany("INSERT OR IGNORE INTO employees VALUES (?, ?, ?, ?, ?, ?)", sample_data)
conn.commit()

# Database functions
def get_employees():
    return pd.read_sql_query("SELECT * FROM employees", conn)

def add_employee(emp_id, name, mobile, salary, department, join_date):
    try:
        cursor.execute(
            "INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?)",
            (emp_id, name, mobile, float(salary), department, join_date)
        conn.commit()
        return True, get_employees()
    except sqlite3.IntegrityError:
        return False, "Employee ID already exists!"

def update_employee(emp_id, name, mobile, salary, department, join_date):
    cursor.execute(
        """UPDATE employees 
        SET name=?, mobile=?, salary=?, department=?, join_date=? 
        WHERE emp_id=?""",
        (name, mobile, float(salary), department, join_date, emp_id))
    conn.commit()
    return get_employees()

def delete_employee(emp_id):
    cursor.execute("DELETE FROM employees WHERE emp_id=?", (emp_id,))
    conn.commit()
    return get_employees()

# Gradio UI
with gr.Blocks(theme=gr.themes.Soft(), title="Employee Management System") as app:
    gr.Markdown("# 🏢 Employee Management System")
    gr.Markdown("Manage your organization's employee records with this interactive dashboard")
    
    with gr.Tab("📋 View Employees"):
        dataframe = gr.Dataframe(
            value=get_employees(),
            interactive=False,
            height=500
        )
        refresh_btn = gr.Button("🔄 Refresh Data")
    
    with gr.Tab("➕ Add Employee"):
        with gr.Row():
            with gr.Column():
                emp_id = gr.Textbox(label="Employee ID", placeholder="EMP001")
                name = gr.Textbox(label="Full Name", placeholder="Alex Johnson")
                mobile = gr.Textbox(label="Mobile Number", placeholder="555-0100")
            with gr.Column():
                salary = gr.Number(label="Salary", value=50000)
                department = gr.Dropdown(
                    ["Engineering", "Marketing", "HR", "Finance", "Operations"],
                    label="Department"
                )
                join_date = gr.Date(label="Join Date")
        
        submit_btn = gr.Button("💾 Save Employee", variant="primary")
        result = gr.Textbox(label="Operation Result", interactive=False)
    
    with gr.Tab("✏ Edit Employee"):
        emp_id_edit = gr.Dropdown(
            label="Select Employee ID",
            choices=list(get_employees()['emp_id'])
        )
        with gr.Row():
            with gr.Column():
                name_edit = gr.Textbox(label="Full Name")
                mobile_edit = gr.Textbox(label="Mobile Number")
            with gr.Column():
                salary_edit = gr.Number(label="Salary")
                department_edit = gr.Dropdown(
                    ["Engineering", "Marketing", "HR", "Finance", "Operations"],
                    label="Department"
                )
                join_date_edit = gr.Date(label="Join Date")
        
        update_btn = gr.Button("🔄 Update Record", variant="primary")
        delete_btn = gr.Button("🗑 Delete Employee", variant="stop")
    
    # Event handlers
    refresh_btn.click(
        fn=get_employees,
        outputs=dataframe
    )
    
    submit_btn.click(
        fn=add_employee,
        inputs=[emp_id, name, mobile, salary, department, join_date],
        outputs=[result, dataframe]
    )
    
    emp_id_edit.change(
        fn=lambda x: get_employees()[get_employees()['emp_id'] == x].iloc[0][1:].tolist(),
        inputs=emp_id_edit,
        outputs=[name_edit, mobile_edit, salary_edit, department_edit, join_date_edit]
    )
    
    update_btn.click(
        fn=update_employee,
        inputs=[emp_id_edit, name_edit, mobile_edit, salary_edit, department_edit, join_date_edit],
        outputs=dataframe
    )
    
    delete_btn.click(
        fn=delete_employee,
        inputs=emp_id_edit,
        outputs=dataframe
    )

# Launch the app
app.launch(share=True)