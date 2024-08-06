class Cat:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def walk(self):
        print("*evasively strolling*")


cat = Cat("Kora", 1, "Devon Rex")
cat.walk()
