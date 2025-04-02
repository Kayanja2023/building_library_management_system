# utils/validations.py

from exceptions.errors import InvalidISBNError

def validate_isbn(isbn: str):
    if not isbn.isdigit():
        raise InvalidISBNError("ISBN must contain only digits.")
    if len(isbn) not in (13, 15):
        raise InvalidISBNError("ISBN must be 13 or 15 digits long.")

def validate_non_empty(field_value: str, field_name: str):
    if not field_value.strip():
        raise ValueError(f"{field_name} cannot be empty.")
