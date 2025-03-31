import unittest
from models.author import Author
from models.book import Book

class TestAuthor(unittest.TestCase):
    def test_add_book(self):
        author = Author("Jane Doe")
        book = Book("Title", "Jane Doe", "123")
        author.add_book(book)
        self.assertIn(book, author.books)

    def test_str(self):
        author = Author("Jane Doe")
        self.assertIn("Jane Doe", str(author))
