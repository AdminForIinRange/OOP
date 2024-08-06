class Clock:
    def __init__(self, hour, minute, second, is_am):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
        self.__is_am = is_am

    def display_time(self):
        suffix = "am"
        if not self.__is_am:
            suffix = "pm"

        print(f"{self.__hour}:{self.__minute}:{self.__second}{suffix}")

    def set_hour(self, hour):
        self.__hour = hour

    def set_minute(self, minute):
        self.__minute = minute

    def set_second(self, second):
        self.__second = second


clock = Clock(10, 38, 55, False)

clock.display_time()
clock.set_hour(12)
clock.set_minute(10)
clock.set_second(30)
clock.display_time()
