class Book:
    def __init__(self):
        self.title = "Atomic Habits"
        self.author = "James Clear"
        self.page_count = 234

    def display_information(self):
        print(self.title, "was written by", self.author,
              "and is", self.page_count, "pages long.")


book_1 = Book()
book_1.display_information()
