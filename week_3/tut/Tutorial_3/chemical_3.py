class Chemical:
    def __init__(self, name):
        self.__name = name
        self.__formula = ""
        self.__compounds = []

    def add_compound(self, compound):
        self.__compounds.append(compound)

    def generate_formula(self):
        for compound in self.__compounds:
            if compound.get_count() == 1:
                self.__formula += f"{compound.get_name()} "
            else:
                self.__formula += f"{compound.get_name()}+{compound.get_count()} "
        return self.__formula

    def __str__(self):
        return f"{self.__name} is made of {self.__formula}"


class Compound:
    def __init__(self, name, count):
        self.__name = name
        self.__count = count

    def get_name(self):
        return self.__name

    def get_count(self):
        return self.__count


aqua_regia = Chemical("Aqua Regia")
aqua_regia.add_compound(Compound("HNO\u00b3", 3))
aqua_regia.add_compound(Compound("HCl", 1))
aqua_regia.generate_formula()
print(aqua_regia)
