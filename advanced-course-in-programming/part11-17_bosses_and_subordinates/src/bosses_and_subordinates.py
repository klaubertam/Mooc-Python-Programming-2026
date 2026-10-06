# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)
def count_subordinates(employee: Employee):
    if employee is None:
        return 0

    total = len(employee.subordinates)

    for sub in employee.subordinates:
        total += count_subordinates(sub)

    return total