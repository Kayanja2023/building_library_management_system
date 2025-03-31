import unittest
from models.library import Library
from models.book import Book

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book("Book1", "Author1", "111")
        self.library.add_book(self.book)

    def test_add_book(self):
        self.assertIn(self.book, self.library.books)

    def test_find_book(self):
        found = self.library.find_book("111")
        self.assertIsNotNone(found)

    def test_get_all_books(self):
        self.assertEqual(len(self.library.get_all_books()), 1)
