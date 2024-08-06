class Book:
    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count


bookOne = Book("bookTitle", "bookAuthor", 1234)

print(bookOne.title)










"""
        n python, every instance of a class has its own copy of all the
        methods inside the class. The __init__ method is a special method that 
        gets called when a new object is created from a class. The self parameter
        is a reference to the current instance of the class and is used to 
        access variables that belong to the class.
        """
