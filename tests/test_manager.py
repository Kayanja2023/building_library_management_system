import unittest
from models.book import Book
from models.library import Library
from services import manager

class TestManager(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book("Sample", "Author", "001")
        manager.add_book(self.book, self.library)

    def test_add_book(self):
        self.assertEqual(len(self.library.books), 1)

    def test_borrow_book(self):
        result = manager.borrow_book("001", self.library)
        self.assertTrue(result)
        self.assertFalse(self.book.available)

    def test_return_book(self):
        self.book.available = False
        result = manager.return_book("001", self.library)
        self.assertTrue(result)
        self.assertTrue(self.book.available)

    def test_remove_book(self):
        result = manager.remove_book("001", self.library)
        self.assertTrue(result)
        self.assertEqual(len(self.library.books), 0)

    def test_search_books(self):
        results = manager.search_books("sample", self.library)
        self.assertIn(self.book, results)
