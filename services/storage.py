import json
from models.book import Book

def load_books(filepath):
    try:
        with open(filepath, 'r') as f:
            content = f.read().strip()
            if not content:
                return []
            return [Book.from_dict(entry) for entry in json.loads(content)]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_books(filepath, books):
    with open(filepath, 'w') as f:
        json.dump([b.to_dict() for b in books], f, indent=2)