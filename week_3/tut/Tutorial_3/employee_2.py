class Employee:
    def __init__(self, id, first_name, last_name, position, salary):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__position = position
        self.__salary = salary

    def __assign_task(self, task):
        print(f"{self.__first_name} {self.__last_name} has been assigned the task: {task}.")


employee = Employee("1", "Santa", "Clause", "Intruder", 1)
print(employee.__first_name)
