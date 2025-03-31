class Library:
    def __init__(self):
        self.books = []
        self.authors = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, isbn):
        return next((b for b in self.books if b.isbn == isbn), None)

    def get_all_books(self):
        return self.books