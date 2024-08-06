

def square(number, power=2):
    return number ** power

print(square(2))




def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 != 0


print(is_odd(5))
print(is_even(5))



def calculate_average(numbers):
    return sum(numbers) / len(numbers)


print(calculate_average([1, 2, 3, 4, 5]))


class Number: 
    def ReSquare(self, number):
        return number ** 2

print(Number().ReSquare(5))