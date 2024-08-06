class Book:
    def __init__(self, title, author, page_count):
        self.__title = title
        self.__author = author
        self.__page_count = page_count

    def __str__(self):
        return f"{self.__title} was written by {self.__author} and is {self.__page_count} pages long."
