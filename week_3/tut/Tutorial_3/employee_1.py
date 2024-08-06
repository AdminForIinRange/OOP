class Employee:
    def __init__(self, id, first_name, last_name, position, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.salary = salary

    def assign_task(self, task):
        print(f"{self.first_name} {self.last_name} has been assigned the task: {task}.")


employee = Employee("1", "Santa", "Clause", "Intruder", 1)
employee.assign_task("Give Gift")
