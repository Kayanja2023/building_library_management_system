import unittest
from models.book import Book
from models.library import Library
from services import manager
from exceptions.errors import BookNotFoundError, BookAlreadyBorrowedError


class TestManager(unittest.TestCase):
    def setUp(self):
        """ Initialize a Library and sample books for use in tests."""
        self.library = Library()
        self.book1 = Book("Python Crash Course", "Eric Matthes", "001001001001001")
        self.book2 = Book("Fluent Python", "Luciano Ramalho", "002002002002002")

        manager.add_book(self.book1, self.library)
        manager.add_book(self.book2, self.library)

    def test_add_book_to_library(self):
        """ testing adding a book to the library."""
        book3 = Book("Effective Python", "Brett Slatkin", "003003003003003")
        manager.add_book(book3, self.library)
        self.assertIn(book3, self.library.books)

    def test_borrow_available_book(self):
        """testing borrowing a book that is currently available."""
        manager.borrow_book("001001001001001", self.library)
        self.assertFalse(self.book1.available)

    def test_borrow_nonexistent_book_raises(self):
        """ testing that borrowing a non-existent book raises BookNotFoundError."""
        with self.assertRaises(BookNotFoundError):
            manager.borrow_book("999999999999999", self.library)

    def test_borrow_already_borrowed_book_raises(self):
        """ testing that borrowing an unavailable book raises BookAlreadyBorrowedError."""
        self.book1.available = False
        with self.assertRaises(BookAlreadyBorrowedError):
            manager.borrow_book("001001001001001", self.library)

    def test_return_borrowed_book(self):
        """ testing returning a borrowed book makes it available again."""
        manager.borrow_book("002002002002002", self.library)
        manager.return_book("002002002002002", self.library)
        self.assertTrue(self.book2.available)

    def test_return_nonexistent_book_raises(self):
        """ testing that returning a book with an invalid ISBN raises BookNotFoundError."""
        with self.assertRaises(BookNotFoundError):
            manager.return_book("404404404404404", self.library)

    def test_remove_existing_book(self):
        """ testing that a book with a valid ISBN is removed from the library."""
        result = manager.remove_book("001001001001001", self.library)
        self.assertTrue(result)
        self.assertNotIn(self.book1, self.library.books)

    def test_remove_nonexistent_book_returns_false(self):
        """ testing that removing a non-existent book returns False."""
        result = manager.remove_book("404404404404404", self.library)
        self.assertFalse(result)

    def test_search_books_by_title(self):
        """ testing that search returns books that match a title keyword."""
        results = manager.search_books("Crash", self.library)
        self.assertIn(self.book1, results)

    def test_search_books_by_author(self):
        """ testing that search returns books that match an author keyword."""
        results = manager.search_books("Luciano", self.library)
        self.assertIn(self.book2, results)

    def test_search_books_no_match_returns_empty_list(self):
        """ testing that a search with no matches returns an empty list."""
        results = manager.search_books("Nonexistent", self.library)
        self.assertEqual(results, [])


if __name__ == "__main__":
    unittest.main()
