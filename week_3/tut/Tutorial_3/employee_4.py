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


employee = Employee("1", "Santa", "Clause", "Intruder", 1)
print(employee.get_first_name())
