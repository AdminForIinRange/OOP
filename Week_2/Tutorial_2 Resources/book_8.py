class Book:
    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count

    def display_information(self):
        print(self.title, "was written by", self.author,
              "and is", self.page_count, "pages long.")


book_1 = Book("Atomic Habits", "James Clear", 234)
book_2 = Book("Dune", "Frank Herbert", 896)
book_3 = Book("A Tale Of Two Cities", "Charles Dickens", 399)
book_4 = Book("The Outer Limits Of Reason", "Noson S. Yanofsky", 403)

book_1.display_information()
book_2.display_information()
book_3.display_information()
book_4.display_information()
