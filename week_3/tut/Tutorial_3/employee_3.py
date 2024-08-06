class Employee:
    def __init__(self, id, first_name, last_name, position, salary):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__position = position
        self.__salary = salary
        self.full_name = self.__first_name + " " + self.__last_name

    def __assign_task(self, task):
        print(f"{self.full_name} has been assigned the task: {task}.")

    def assign_task(self, task):
        if task != None:
            return self.__assign_task(task)


employee_1 = Employee("1854327", "Ratchet", "", "Mechanic", 101000.0)
employee_2 = Employee("XJ-0461", "and", "Clank", "Glorified Backpack", 1500000.0)
employee_1.assign_task("Capture Dr. Nefarious")
employee_2.assign_task("Store Item")
