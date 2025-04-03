from exceptions.errors import BookNotFoundError, BookAlreadyBorrowedError


""" adding a book to the library """
def add_book(book, library):
    library.add_book(book)

""" Borrowing a book by marking it as unavailable"""
def borrow_book(isbn, library):
    book = library.find_book(isbn)
    if not book:
        raise BookNotFoundError(isbn)
    if not book.available:
        raise BookAlreadyBorrowedError(book.title)
    book.available = False
    return True                                                # returns True if the operation is successfull

""" Returns a borrowed book by marking it as available"""
def return_book(isbn, library):
    book = library.find_book(isbn)
    if not book:
        raise BookNotFoundError(f"Book with ISBN {isbn} not found.")
    book.available = True
    return True

""" Searching for books by keyword in title or author """
def search_books(keyword, library):
    return [b for b in library.books if keyword.lower() in b.title.lower() or keyword.lower() in b.author.lower()]

""" Remove a book from the library using ISBN """
def remove_book(isbn, library):
    book = library.find_book(isbn)
    if book:
        library.books.remove(book)
        return True                                                # bool: True if the book was removed, False if not found.
    return False