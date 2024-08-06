class clock:
    def __init__(self, hour, minute, second, is_am):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
        self.__is_am = is_am  # made it private

    def set_hour(self, hour):
        self.__hour = hour

    def set_minute(self, minute):  # more setter functions because its private
        self.__minute = minute

    def set_second(self, second):
        self.__second = second

    def display_time(self):

        suffix = "am" if self.__is_am else "pm"  # suffix is am if true, pm if false, its called a ternary operator
        result = f"{self.__hour}:{self.__minute}:{self.__second}{suffix}"
        print(result)


clock1 = clock(10, 38, 55, False)
# calling the setter and directy change its priv value as shown in the "def" above
clock1.set_hour(12)
clock1.set_minute(10)
clock1.set_second(30)
clock1.display_time()
