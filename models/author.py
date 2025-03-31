class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        return f"{self.name} ({len(self.books)} books)"