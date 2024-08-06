class Employee:
    def __init__(self, id, first_name, last_name, position, salary):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__position = position
        self.__salary = salary
        self.full_name = self.__first_name + " " + self.__last_name

    def get_id(self):
        return self.__id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_position(self):
        return self.__position

    def get_salary(self):
        return self.__salary

    def set_first_name(self, first_name):
        if isinstance(first_name, str):
            self.__first_name = first_name

    def set_last_name(self, last_name):
        if isinstance(last_name, str):
            self.__last_name = last_name

    def set_position(self, position):
        self.__position = position

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary

    def __assign_task(self, task):
        print(f"{self.full_name} has been assigned the task: {task}.")

    def assign_task(self, task):
        if task != None:
            return self.__assign_task(task)

    def __str__(self):
        return f"Employee ID: {self.__id} \
            \nName: {self.full_name} \
            \nPosition: {self.__position} \
            \nSalary: ${self.__salary} per anum.\n"


employee_1 = Employee("1854327", "Ratchet", "", "Mechanic", 101000.0)
employee_2 = Employee("XJ-0461", "and", "Clank", "Glorified Backpack", 1500000.0)
employee_1.assign_task("asdouhado")

# Invoke the __str__ method.
print(employee_1)
print(employee_2)

employee_1.set_position("Intergalactic Hero")
print(employee_1.get_position())
employee_1.assign_task("Capture Dr. Nefarious")

# Does not access private attribute but instead creates a new one.
employee_1.__salary = 188000.0

# Both salaries are printed and we can see no change ocurred in employee_1.
print(employee_1.__salary)
print(employee_1.get_salary())

# Setter is called to ensure the salary attribute is correctly updated.
employee_1.set_salary(188000.0)
print(employee_1.get_salary())
