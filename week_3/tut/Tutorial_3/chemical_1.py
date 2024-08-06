class Chemical:
    def __init__(self, name, formula):
        self.__name = name
        self.__formula = formula

    def __str__(self):
        return f"{self.__name} is made of {self.__formula}"


aqua_regia = Chemical("Aqua Regia", "HNO3 + 3 HCl")
print(aqua_regia)
