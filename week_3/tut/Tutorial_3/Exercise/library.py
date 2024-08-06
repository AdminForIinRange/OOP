from book import Book


class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def display_books(self):
        if not self.__books:
            print("The library is empty...how gloomy.")
        else:
            print("---Book Collection---".upper())
            for book in self.__books:
                print(book)

    # def __str__(self):
    #     description = "The library is empty...how gloomy." if not self.__books else "---Book Collection---".upper() + "\n"

    #     for book in self.__books:
    #         description += book.__str__() + "\n"

    #     return description


library = Library()
library.add_book(Book("Atomic Habits", "James Clear", 234))
library.add_book(Book("Dune", "Frank Herbert", 896))
library.add_book(Book("A Tale Of Two Cities", "Charles Dickens", 399))
library.add_book(Book("The Outer Limits Of Reason", "Noson S. Yanofsky", 403))
# library.display_books()
print(library)
