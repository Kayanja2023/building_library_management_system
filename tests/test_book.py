import unittest
from models.book import Book
from exceptions.errors import InvalidISBNError

class TestBook(unittest.TestCase):
    def setUp(self):
        """Initialize a reusable Book instance for testing."""
        self.book = Book("Clean Code", "Robert C. Martin", "1234567890123")  # 13-digit ISBN

    def test_book_initialization(self):
        """Ensure a Book is initialized correctly with availability True."""
        self.assertEqual(self.book.title, "Clean Code")
        self.assertEqual(self.book.author, "Robert C. Martin")
        self.assertEqual(self.book.isbn, "1234567890123")
        self.assertTrue(self.book.available)

    def test_book_availability_toggle(self):
        """Check toggling the 'available' status on a Book."""
        self.book.available = False
        self.assertFalse(self.book.available)

        self.book.available = True
        self.assertTrue(self.book.available)

    def test_to_dict_serialization(self):
        """Verify Book serializes correctly to a dictionary."""
        expected = {
            'title': "Clean Code",
            'author': "Robert C. Martin",
            'isbn': "1234567890123",
            'available': True
        }
        self.assertEqual(self.book.to_dict(), expected)

    def test_from_dict_deserialization(self):
        """Ensure Book can be reconstructed from a dictionary."""
        data = {
            'title': "The Pragmatic Programmer",
            'author': "Andrew Hunt",
            'isbn': "9876543210987",
            'available': False
        }
        book_from_dict = Book.from_dict(data)
        self.assertIsInstance(book_from_dict, Book)
        self.assertEqual(book_from_dict.title, "The Pragmatic Programmer")
        self.assertEqual(book_from_dict.author, "Andrew Hunt")
        self.assertEqual(book_from_dict.isbn, "9876543210987")
        self.assertFalse(book_from_dict.available)

    def test_str_representation(self):
        """Test __str__ returns readable output including all fields."""
        output = str(self.book)
        self.assertIn("Clean Code", output)
        self.assertIn("Robert C. Martin", output)
        self.assertIn("1234567890123", output)
        self.assertIn("Available", output)

    #  Validation tests
    def test_invalid_isbn_length_raises(self):
        """Test that an ISBN with incorrect length raises an exception."""
        with self.assertRaises(InvalidISBNError):
            Book("Bad Length", "Author", "12345")  # too short

    def test_invalid_isbn_non_digit_raises(self):
        """Test that an ISBN with non-digit characters raises an exception."""
        with self.assertRaises(InvalidISBNError):
            Book("Bad Format", "Author", "12345abc90123")  # not all digits

    def test_valid_13_digit_isbn_passes(self):
        """Test that a valid 13-digit ISBN does not raise an error."""
        try:
            book = Book("Valid Book", "Author", "1111111111111")
            self.assertEqual(book.isbn, "1111111111111")
        except InvalidISBNError:
            self.fail("Valid 13-digit ISBN incorrectly raised InvalidISBNError.")

    def test_valid_15_digit_isbn_passes(self):
        """Test that a valid 15-digit ISBN does not raise an error."""
        try:
            book = Book("Valid Book", "Author", "123456789012345")
            self.assertEqual(book.isbn, "123456789012345")
        except InvalidISBNError:
            self.fail("Valid 15-digit ISBN incorrectly raised InvalidISBNError.")


if __name__ == "__main__":
    unittest.main()
