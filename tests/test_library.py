import unittest
from models.library import Library
from models.book import Book
from services import manager

class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Set up a fresh Library instance with two sample books."""
        self.library = Library()
        self.book1 = Book("The Pragmatic Programmer", "Andy Hunt", "1234567890123")
        self.book2 = Book("Refactoring", "Martin Fowler", "9876543210987")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_add_book_to_library(self):
        """Verify that adding a new book increases the library's book count."""
        book3 = Book("Clean Architecture", "Robert C. Martin", "3213213213213")
        self.library.add_book(book3)
        self.assertIn(book3, self.library.books)
        self.assertEqual(len(self.library.books), 3)

    def test_get_all_books_returns_correct_list(self):
        """Check that get_all_books returns all added books."""
        all_books = self.library.get_all_books()
        self.assertEqual(len(all_books), 2)
        self.assertIn(self.book1, all_books)
        self.assertIn(self.book2, all_books)

    def test_find_book_success(self):
        """Ensure find_book returns the correct book object by ISBN."""
        result = self.library.find_book("1234567890123")
        self.assertEqual(result, self.book1)

    def test_find_book_not_found(self):
        """Ensure find_book returns None when ISBN is not found."""
        result = self.library.find_book("0000000000000")
        self.assertIsNone(result)

    def test_remove_book_successfully(self):
        """Test that an existing book is removed correctly via manager."""
        removed = manager.remove_book("9876543210987", self.library)
        self.assertTrue(removed)
        self.assertNotIn(self.book2, self.library.books)

    def test_remove_nonexistent_book(self):
        """Attempting to remove a non-existent book should return False."""
        removed = manager.remove_book("0000000000000", self.library)
        self.assertFalse(removed)


if __name__ == "__main__":
    unittest.main()
