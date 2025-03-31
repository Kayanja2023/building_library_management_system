import unittest
from models.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("Test Title", "Test Author", "123456")

    def test_to_dict(self):
        self.assertEqual(self.book.to_dict(), {
            "title": "Test Title",
            "author": "Test Author",
            "isbn": "123456",
            "available": True
        })

    def test_from_dict(self):
        data = {
            "title": "Python",
            "author": "Someone",
            "isbn": "999",
            "available": False
        }
        book = Book.from_dict(data)
        self.assertEqual(book.title, "Python")
        self.assertFalse(book.available)

    def test_str(self):
        self.assertIn("Test Title", str(self.book))
