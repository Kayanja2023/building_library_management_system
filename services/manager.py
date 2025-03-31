from exceptions.errors import BookNotFoundError, BookAlreadyBorrowedError
from models.book import Book

def add_book(book, library):
    library.add_book(book)

def borrow_book(isbn, library):
    book = library.find_book(isbn)
    if not book:
        raise BookNotFoundError(isbn)
    if not book.available:
        raise BookAlreadyBorrowedError(book.title)
    book.available = False
    return True

def return_book(isbn, library):
    book = library.find_book(isbn)
    if book:
        book.available = True
        return True
    return False

def search_books(keyword, library):
    return [b for b in library.books if keyword.lower() in b.title.lower() or keyword.lower() in b.author.lower()]

def remove_book(isbn, library):
    book = library.find_book(isbn)
    if book:
        library.books.remove(book)
        return True
    return False