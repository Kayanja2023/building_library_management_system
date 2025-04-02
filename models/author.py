from utils.validations import validate_non_empty

class Author:
    def __init__(self, name):
        validate_non_empty(name, "Author name")
        self.name = name
        self.books = []


    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        return f"{self.name} ({len(self.books)} books)"