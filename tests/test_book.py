import unittest
from models.book import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        """Create a sample book object for use in all tests."""
        self.book = Book("Clean Code", "Robert C. Martin", "1234567890")

    def test_book_initialization(self):
        """Test that a Book object is initialized with correct attributes."""
        self.assertEqual(self.book.title, "Clean Code")
        self.assertEqual(self.book.author, "Robert C. Martin")
        self.assertEqual(self.book.isbn, "1234567890")
        self.assertTrue(self.book.available)

    def test_book_availability_toggle(self):
        """Verify that the book's availability can be changed."""
        self.book.available = False
        self.assertFalse(self.book.available)
        self.book.available = True
        self.assertTrue(self.book.available)

    def test_to_dict_serialization(self):
        """Test that the book serializes correctly to a dictionary."""
        expected = {
            'title': "Clean Code",
            'author': "Robert C. Martin",
            'isbn': "1234567890",
            'available': True
        }
        self.assertEqual(self.book.to_dict(), expected)

    def test_from_dict_deserialization(self):
        """Test that a book can be recreated from a dictionary."""
        data = {
            'title': "The Pragmatic Programmer",
            'author': "Andrew Hunt",
            'isbn': "9876543210",
            'available': False
        }
        book_from_dict = Book.from_dict(data)
        self.assertEqual(book_from_dict.title, "The Pragmatic Programmer")
        self.assertEqual(book_from_dict.author, "Andrew Hunt")
        self.assertEqual(book_from_dict.isbn, "9876543210")
        self.assertFalse(book_from_dict.available)

    def test_str_representation(self):
        """Test the string output of the Book object."""
        output = str(self.book)
        self.assertIn("Clean Code", output)
        self.assertIn("Robert C. Martin", output)
        self.assertIn("1234567890", output)
        self.assertIn("Available", output)


if __name__ == "__main__":
    unittest.main()
