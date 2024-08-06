class Clock:
    def __init__(self, hour, minute, second, is_am):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
        self.__is_am = is_am
        self.__display_time()

    def __display_time(self):
        suffix = "am"
        if not self.__is_am:
            suffix = "pm"

        print(f"{self.__hour}:{self.__minute}:{self.__second}{suffix}")

    # def display_time(self):
    #     # Checks go here.
    #     self.__display_time()


clock = Clock(10, 38, 55, False)
# clock.display_time()
