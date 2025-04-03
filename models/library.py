class Library:

    """ Initializes an empty library for books and authors """
    def __init__(self):
        self.books = []


    """Adding a book to the library's collection """
    def add_book(self, book):
        self.books.append(book)

    """ Searching for a book using ISBN"""
    def find_book(self, isbn):
        return next((b for b in self.books if b.isbn == isbn), None)

    """Retrieve all books currently in library """
    def get_all_books(self):
        return self.books