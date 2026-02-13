import sqlite3
import pandas as pd

# Połączenie z bazą
connection = sqlite3.connect("company.db")

# Raport: pracownicy per dział
query_departments = """
SELECT
    d.name AS department,
    COUNT(e.id) AS employee_count
FROM departments d
LEFT JOIN employees e ON d.id = e.department_id
GROUP BY d.id, d.name
ORDER BY employee_count DESC
"""
df_departments = pd.read_sql_query(query_departments, connection)

# Zapis do CSV
df_departments.to_csv("employees_per_department.csv", index=False)

# Raport: wynagrodzenia per dział
query_salaries = """
SELECT
    d.name AS department,
    ROUND(AVG(e.salary), 2) AS avg_salary,
    SUM(e.salary) AS total_salary
FROM departments d
LEFT JOIN employees e ON d.id = e.department_id
GROUP BY d.id, d.name
"""
df_salaries = pd.read_sql_query(query_salaries, connection)

# Zapis do CSV
df_salaries.to_csv("salary_report.csv", index=False)

# Eksport do jednego pliku Excel z dwoma arkuszami
with pd.ExcelWriter("company_reports.xlsx", engine="openpyxl") as writer:
    df_departments.to_excel(writer, sheet_name="Employees per Department", index=False)
    df_salaries.to_excel(writer, sheet_name="Salary Summary", index=False)

connection.close()

print("Raporty CSV i Excel zostały wygenerowane ")
