from app.models.employee import Employee
import sqlite3


class EmployeeRepository:
    def __init__(self, db_path):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS employees(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age TEXT,
                    doj TEXT,
                    email TEXT,
                    gender TEXT,
                    contact TEXT,
                    address TEXT
                )
            """)
            conn.commit()

    def fetch_all(self):
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM employees")
            rows = cur.fetchall()
            return [Employee(*row) for row in rows]

    def insert(self, employee: Employee):
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO employees VALUES (NULL,?,?,?,?,?,?,?)",
                        (employee.name, employee.age, employee.doj, employee.email, employee.gender, employee.contact, employee.address))
            conn.commit()

    def delete(self, employee_id):
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM employees WHERE id=?", (employee_id,))
            conn.commit()

    def update(self, employee: Employee):
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                UPDATE employees SET name=?, age=?, doj=?, email=?, gender=?, contact=?, address=?
                WHERE id=?
            """, (employee.name, employee.age, employee.doj, employee.email, employee.gender, employee.contact, employee.address, employee.id))
            conn.commit()