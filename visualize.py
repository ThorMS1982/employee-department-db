import sqlite3
import matplotlib.pyplot as plt

# Połączenie z bazą
connection = sqlite3.connect("company.db")
cursor = connection.cursor()

# -----------------------------
# 1️⃣ Pobieramy dane: liczba pracowników per dział
# -----------------------------
query_employee_count = """
SELECT
    d.name AS department,
    COUNT(e.id) AS employee_count
FROM departments d
LEFT JOIN employees e ON d.id = e.department_id
GROUP BY d.id, d.name
ORDER BY employee_count DESC
"""
cursor.execute(query_employee_count)
employee_data = cursor.fetchall()

departments = [row[0] for row in employee_data]
employee_counts = [row[1] for row in employee_data]

# -----------------------------
# 2️⃣ Pobieramy dane: suma wynagrodzeń per dział
# -----------------------------
query_salary_sum = """
SELECT
    d.name AS department,
    SUM(e.salary) AS total_salary
FROM departments d
LEFT JOIN employees e ON d.id = e.department_id
GROUP BY d.id, d.name
ORDER BY total_salary DESC
"""
cursor.execute(query_salary_sum)
salary_data = cursor.fetchall()

salary_departments = [row[0] for row in salary_data]
total_salaries = [row[1] if row[1] is not None else 0 for row in salary_data]  # obsługa działów bez pracowników

# Zamykamy połączenie
connection.close()

# -----------------------------
# 3️⃣ Wykres liczby pracowników
# -----------------------------
plt.figure(figsize=(10,6))
bars1 = plt.bar(departments, employee_counts, color='skyblue')
for bar in bars1:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.1, str(height), ha='center', va='bottom')

plt.title("Liczba pracowników per dział")
plt.xlabel("Dział")
plt.ylabel("Liczba pracowników")
plt.ylim(0, max(employee_counts)*1.2)
plt.tight_layout()
plt.savefig("employees_per_department.png")
plt.show()

# -----------------------------
# 4️⃣ Wykres sumy wynagrodzeń
# -----------------------------
plt.figure(figsize=(10,6))
bars2 = plt.bar(salary_departments, total_salaries, color='lightgreen')
for bar in bars2:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + max(total_salaries)*0.01, f"{int(height)}", ha='center', va='bottom')

plt.title("Suma wynagrodzeń per dział")
plt.xlabel("Dział")
plt.ylabel("Suma wynagrodzeń")
plt.ylim(0, max(total_salaries)*1.2)
plt.tight_layout()
plt.savefig("salary_per_department.png")
plt.show()

print("Wykresy zostały wygenerowane i zapisane jako 'employees_per_department.png' oraz 'salary_per_department.png' ✅")
