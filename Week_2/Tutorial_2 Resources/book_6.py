class Book:
    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.current_page = 0


book_1 = Book("Atomic Habits", "James Clear", 234)
