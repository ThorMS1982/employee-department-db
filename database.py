import sqlite3

# 1. Połączenie z bazą danych
# Jeśli plik nie istnieje → SQLite go utworzy
connection = sqlite3.connect("company.db")

# 2. Obiekt do wykonywania poleceń SQL
cursor = connection.cursor()

# 3. Tabela departments
cursor.execute("""
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)
""")

# 4. Tabela employees
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    salary REAL NOT NULL,
    department_id INTEGER NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(id)
)
""")

# 5. Zapis zmian i zamknięcie połączenia
connection.commit()
connection.close()

print("Baza danych i tabele zostały utworzone poprawnie.")
