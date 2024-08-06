
from book import Book

class Library:
    def __init__(self):
        self.__books = []
    def append_book(self, book):
        self.__books.append(book)

    def display_books(self):
        if not self.__books:
            print("The library is empty...how gloomy.")
        else:
            print("---Book Collection---".upper())
            for book in self.__books:
                print(book)
    
library = Library()
library.append_book(Book("Atomic Habits", "James Clear", 234)
library.add_book(Book("Dune", "Frank Herbert", 896))