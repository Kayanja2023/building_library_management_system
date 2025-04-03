from utils.validations import validate_non_empty

class Author:
    """ Initializes an Author instance."""
    def __init__(self, name):
        validate_non_empty(name, "Author name")
        self.name = name
        self.books = []

    """Adds a book to the author's collection"""
    def add_book(self, book):
        self.books.append(book)

    """ Returns a string representation of the author,
        including their name and the number of books they've authored."""
    def __str__(self):
        return f"{self.name} ({len(self.books)} books)"