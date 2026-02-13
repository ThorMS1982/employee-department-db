import sqlite3

# Połączenie z bazą
connection = sqlite3.connect("company.db")
cursor = connection.cursor()

# Wymuszamy obsługę kluczy obcych (dobra praktyka)
cursor.execute("PRAGMA foreign_keys = ON;")

# -------------------------
# 1️⃣ Dodajemy działy
# -------------------------
departments = [
    ("IT",),
    ("HR",),
    ("Sales",),
    ("Finance",)
]

cursor.executemany("""
INSERT OR IGNORE INTO departments (name)
VALUES (?)
""", departments)

# -------------------------
# 2️⃣ Pobieramy ID działów
# -------------------------
cursor.execute("SELECT id, name FROM departments")
department_ids = {name: dep_id for dep_id, name in cursor.fetchall()}

# -------------------------
# 3️⃣ Dodajemy pracowników
# -------------------------
employees = [
    ("Jan Kowalski", "jan.kowalski@firma.pl", 9000, department_ids["IT"]),
    ("Anna Nowak", "anna.nowak@firma.pl", 7500, department_ids["HR"]),
    ("Piotr Zielinski", "piotr.zielinski@firma.pl", 8200, department_ids["Sales"]),
    ("Katarzyna Mazur", "katarzyna.mazur@firma.pl", 10500, department_ids["IT"]),
    ("Marek Lewandowski", "marek.lewandowski@firma.pl", 6800, department_ids["Finance"]),
    ("Tomasz Wójcik", "tomasz.wojcik@firma.pl", 8800, department_ids["IT"]),
    ("Magdalena Kamińska", "magdalena.kaminska@firma.pl", 7200, department_ids["HR"]),
    ("Paweł Kaczmarek", "pawel.kaczmarek@firma.pl", 7900, department_ids["Sales"]),
    ("Agnieszka Piotrowska", "agnieszka.piotrowska@firma.pl", 11500, department_ids["IT"]),
    ("Łukasz Dąbrowski", "lukasz.dabrowski@firma.pl", 6400, department_ids["Finance"]),
    ("Natalia Król", "natalia.krol@firma.pl", 8300, department_ids["Sales"]),
    ("Karol Wieczorek", "karol.wieczorek@firma.pl", 9700, department_ids["IT"]),
    ("Barbara Zając", "barbara.zajac@firma.pl", 7100, department_ids["HR"]),
    ("Michał Pawlak", "michal.pawlak@firma.pl", 7600, department_ids["Finance"]),
    ("Joanna Michalska", "joanna.michalska@firma.pl", 9900, department_ids["IT"]),
    ("Rafał Nowicki", "rafal.nowicki@firma.pl", 8100, department_ids["Sales"]),
    ("Monika Wróbel", "monika.wrobel@firma.pl", 7300, department_ids["HR"]),
    ("Grzegorz Jankowski", "grzegorz.jankowski@firma.pl", 8700, department_ids["IT"]),
    ("Ewa Malinowska", "ewa.malinowska@firma.pl", 6500, department_ids["Finance"]),
    ("Damian Szymański", "damian.szymanski@firma.pl", 9200, department_ids["Sales"]),
]


cursor.executemany("""
INSERT OR IGNORE INTO employees (name, email, salary, department_id)
VALUES (?, ?, ?, ?)
""", employees)

# Zapisujemy zmiany
connection.commit()
connection.close()

print("Dane testowe zostały dodane do bazy.")
