import unittest
from models.library import Library
from models.book import Book
from services import manager


class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Set up a fresh Library instance and sample books for each test."""
        self.library = Library()
        self.book1 = Book("The Pragmatic Programmer", "Andy Hunt", "001")
        self.book2 = Book("Refactoring", "Martin Fowler", "002")

    def test_add_book_to_library(self):
        """Ensure that a book can be added and retrieved from the library."""
        self.library.add_book(self.book1)
        self.assertIn(self.book1, self.library.books)
        self.assertEqual(len(self.library.books), 1)

    def test_get_all_books_returns_correct_list(self):
        """Verify get_all_books returns the correct collection."""
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        all_books = self.library.get_all_books()
        self.assertEqual(len(all_books), 2)
        self.assertIn(self.book2, all_books)

    def test_find_book_success(self):
        """Test successful book lookup by ISBN."""
        self.library.add_book(self.book1)
        result = self.library.find_book("001")
        self.assertEqual(result, self.book1)

    def test_find_book_not_found(self):
        """Ensure None is returned if ISBN is not found."""
        result = self.library.find_book("999")
        self.assertIsNone(result)

    def test_remove_book_successfully(self):
        """Test that a book can be removed from the library."""
        self.library.add_book(self.book1)
        removed = manager.remove_book("001",self.library)
        self.assertTrue(removed)
        self.assertNotIn(self.book1, self.library.books)

    def test_remove_nonexistent_book(self):
        """Attempting to remove a book that doesn't exist should return False."""
        removed = manager.remove_book("999",self.library)
        self.assertFalse(removed)


if __name__ == "__main__":
    unittest.main()
