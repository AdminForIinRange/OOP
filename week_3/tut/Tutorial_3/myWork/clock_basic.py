class clock:
    def __init__(self, hour, minute, second, is_am):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
        self.__is_am = is_am # made it private

    def display_time(self):

        suffix = "am" if self.__is_am else "pm" # suffix is am if true, pm if fals, its called a ternary operator
        result = f"{self.__hour}:{self.__minute}:{self.__second}{suffix}"
        print(result)


    def set_hour(self, hour): # i have to put "hour" as a arugment becuasse hour in private, normally i dont.
        self.__hour = hour # now i can change the hour value, can be conssiderec a setter function


clock1 = clock(10, 38, 55, False)
clock1.display_time()

