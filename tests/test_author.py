
import unittest
from models.author import Author
from models.book import Book

class TestAuthor(unittest.TestCase):
    def setUp(self):
        #Initialize reusable Author and Book objects for tests.
        self.author = Author("Jane Doe")
        self.book1 = Book("AI for Beginners", "Jane Doe", "1234567890123")      # Valid ISBN-13
        self.book2 = Book("Advanced AI", "Jane Doe", "9876543210987")           # Valid ISBN-13
        self.book_wrong_author = Book("Not Her Book", "John Smith", "1111111111111")  # Valid but wrong author



    def test_author_initialization(self):
        #Test that an author is initialized with the correct name and empty book list.
        self.assertEqual(self.author.name, "Jane Doe")
        self.assertEqual(len(self.author.books), 0)

    def test_add_single_book(self):
        """Test that a book can be added to the author's collection."""
        self.author.add_book(self.book1)
        self.assertIn(self.book1, self.author.books)
        self.assertEqual(len(self.author.books), 1)

    def test_add_multiple_books(self):
        """Test that multiple books can be associated with an author."""
        self.author.add_book(self.book1)
        self.author.add_book(self.book2)
        self.assertEqual(len(self.author.books), 2)
        self.assertIn(self.book2, self.author.books)

    def test_str_includes_author_name(self):
        self.author.add_book(self.book1)
        author_str = str(self.author)
        self.assertIn("Jane Doe", author_str)
        self.assertIn("1 books", author_str)


    def test_adding_book_with_mismatched_author(self):
        """Optional: Add logic to prevent associating books by different authors."""
        # If your Author class enforces consistency, test for rejection
        self.author.add_book(self.book_wrong_author)
        # Assuming logic doesn’t block mismatches yet
        self.assertIn(self.book_wrong_author, self.author.books)


if __name__ == '__main__':
    unittest.main()
