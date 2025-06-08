from app.repositories.employee_repository import EmployeeRepository
from app.models.employee import Employee


class EmployeeService:
    def __init__(self):
        self.repository = EmployeeRepository("./database/Employee.db")
        self.repository.create_table()

    def get_all_employees(self):
        return self.repository.fetch_all()

    def add_employee(self, employee: Employee):
        self.repository.insert(employee)

    def update_employee(self, employee: Employee):
        self.repository.update(employee)

    def delete_employee(self, employee_id):
        self.repository.delete(employee_id)