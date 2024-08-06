def greet(name):
    if name is None:
        print("Welcome, guest!")
    else:
        print("Welcome,", name)


# A hypothetical case where a name has not yet been assigned in your program.
user = None
greet(user)

user = "Tam"
greet(user)
