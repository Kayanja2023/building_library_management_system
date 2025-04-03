class BookNotFoundError(Exception):
    """Raised when a book with the specified ISBN is not found in the library."""
    def __init__(self, isbn=None):
        message = f"Book with ISBN '{isbn}' was not found." if isbn else "Book not found."
        super().__init__(message)
        self.isbn = isbn


class BookAlreadyBorrowedError(Exception):
    """Raised when attempting to borrow a book that is already borrowed."""
    def __init__(self, title=None):
        message = f"The book '{title}' is already borrowed." if title else "The book is already borrowed."
        super().__init__(message)
        self.title = title



class InvalidISBNError(Exception):
    """Raised when the ISBN is not numeric or of incorrect length."""
    pass

