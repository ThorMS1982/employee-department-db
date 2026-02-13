import sqlite3

# Połączenie z bazą
connection = sqlite3.connect("company.db")
cursor = connection.cursor()

# -----------------------------------
# 1️⃣ Raport: liczba pracowników per dział
# -----------------------------------
cursor.execute("""
SELECT
    d.name AS department,
    COUNT(e.id) AS employee_count
FROM departments d
LEFT JOIN employees e ON d.id = e.department_id
GROUP BY d.name
ORDER BY employee_count DESC
""")

department_summary = cursor.fetchall()

print("Liczba pracowników per dział:")
for department, count in department_summary:
    print(f"{department}: {count}")

# -----------------------------------
# 2️⃣ Raport: statystyki wynagrodzeń per dział
# -----------------------------------
cursor.execute("""
SELECT
    d.name AS department,
    ROUND(AVG(e.salary), 2) AS avg_salary,
    SUM(e.salary) AS total_salary
FROM departments d
LEFT JOIN employees e ON d.id = e.department_id
GROUP BY d.name
""")

salary_summary = cursor.fetchall()

print("\nStatystyki wynagrodzeń per dział:")
for department, avg_salary, total_salary in salary_summary:
    print(
        f"{department}: "
        f"średnia = {avg_salary}, "
        f"suma = {total_salary}"
    )

# Zamykamy połączenie
connection.close()
