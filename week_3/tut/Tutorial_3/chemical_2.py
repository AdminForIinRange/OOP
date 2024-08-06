class Chemical:
    def __init__(self, name, formula):
        self.__name = name
        self.__formula = formula

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"{self.__name} is made of {self.__formula}"


class Chemist:
    def __init__(self, name):
        self.__name = name

    def use_chemical(self, chemical):
        print(f"{self.__name} is working with {chemical.get_name()}")


chemical = Chemical("Aqua Regia", "HNO3 + 3 HCl")
chemist = Chemist("John Chemist")
chemist.use_chemical(chemical)
