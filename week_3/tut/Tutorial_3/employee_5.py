class Employee:
    def __init__(self, id, first_name, last_name, position, salary):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__position = position
        self.__salary = salary
        self.full_name = self.__first_name + " " + self.__last_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_position(self, position):
        self.__position = position

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
