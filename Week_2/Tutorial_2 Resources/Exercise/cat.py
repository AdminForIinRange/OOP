class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.age = 1 
        self.breed = breed

    def walk(self):
        print("*evasively strolling*")

cat_new = Cat("Kora","Devon Rex")
cat_new.walk()
