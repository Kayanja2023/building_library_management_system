from utils.validations import validate_isbn, validate_non_empty


class Book:
    def __init__(self, title, author, isbn, available=True):
        validate_non_empty(title, "Title")
        validate_non_empty(author, "Author")
        validate_isbn(isbn)

        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }

    @staticmethod
    def from_dict(data):
        return Book(
            title=data["title"],
            author=data["author"],
            isbn=data["isbn"],
            available=data.get("available", True)
        )

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"

