import unittest
from models.book import Book
from models.library import Library
from services import manager
from exceptions.errors import BookNotFoundError, BookAlreadyBorrowedError

class TestManagerWithExceptions(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book("Sample", "Author", "001")
        manager.add_book(self.book, self.library)

    def test_borrow_available_book(self):
        manager.borrow_book("001", self.library)
        self.assertFalse(self.book.available)

    def test_borrow_nonexistent_book_raises(self):
        with self.assertRaises(BookNotFoundError):
            manager.borrow_book("999", self.library)

    def test_borrow_already_borrowed_book_raises(self):
        self.book.available = False
        with self.assertRaises(BookAlreadyBorrowedError):
            manager.borrow_book("001", self.library)

    def test_return_book_success(self):
        self.book.available = False
        result = manager.return_book("001", self.library)
        self.assertTrue(result)
        self.assertTrue(self.book.available)

    def test_return_nonexistent_book_raises(self):
        with self.assertRaises(BookNotFoundError):
            manager.return_book("999", self.library)
