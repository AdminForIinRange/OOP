class Book:
    def __init__(self):
        self.title = "Atomic Habits"
        self.author = "James Clear"
        self.page_count = 234


book_1 = Book()
book_2 = Book()
book_3 = Book()

print(book_1.title)
book_1.title = "Arry' Poh ah"
print(book_1.title)
print(book_1.author)
print(book_1.page_count)
