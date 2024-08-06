class Book:
    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count

    def __str__(self):
        return self.title + " was written by " + self.author + \
            " and is " + str(self.page_count) + " pages long."


book_collection = []
book_collection.append(Book("Atomic Habits", "James Clear", 234))
book_collection.append(Book("Dune", "Frank Herbert", 896))
book_collection.append(Book("A Tale Of Two Cities", "Charles Dickens", 399))
book_collection.append(Book("The Outer Limits Of Reason", "Noson S. Yanofsky", 403))

for book in book_collection:
    print(book)
